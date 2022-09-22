import requests
import re
import json
from multiprocessing import Pool
url = 'https://nips.cc/Conferences/2022/Schedule?type=Poster'


def get_author_info(author):
    author_url = f'https://nips.cc/Conferences/2022/Schedule?showSpeaker={author}'

    while True:
        try:
            r = requests.get(author_url)
            break
        except:
            print('retrying')
            continue

    text = r.text.encode('unicode_escape').decode('utf-8')
    author_info = {}
    author_info['name'] = re.search(r'<h3>.*?</h3>', text, re.DOTALL).group(0).split('>')[1].split('<')[0]
    author_info['affiliation'] = re.search(r'<h4>.*?</h4>', text, re.DOTALL).group(0).split('>')[1].split('<')[0]
    author_info['no'] = author.split('-')[0]
    return author_info


def paper_retriever(paper_index):
    paper = {}
    paper_url = f'https://nips.cc/Conferences/2022/Schedule?showEvent={paper_index}'
    while True:
        try:
            r = requests.get(paper_url)
            break
        except:
            print('retrying')
            continue
    text = r.text.encode('unicode_escape').decode('utf-8')
    paper['title'] = re.search(r'<div class=\"maincardBody\">.*?</div>', text, re.DOTALL).group(0).split('>')[1].split('<')[0]

    author_info_list = re.findall(r'showSpeaker\(\'.*?\'\)', text, re.DOTALL)

    paper_authors = []

    for author in author_info_list:
        author_no = author.split('\'')[1]
        author_info = get_author_info(author_no)
        paper_authors.append(author_info)

    paper['authors'] = paper_authors

    print(paper['title'])
    return paper


def main():
    r = requests.get(url)
    text = r.text.encode('unicode_escape').decode('utf-8')

    with open('nips2022.txt', 'w') as f:
        f.write(text)

    with open('nips2022.txt', 'r') as f:
        text = f.read()

    # find all the poster sessions
    paper_list = re.findall(r'id=\"maincard_.*?\"', text, re.DOTALL)
    paper_index_list = []
    for paper in paper_list:
        paper_index_list.append(paper.split('_')[1].split('"')[0])

    # use multiprocessing to boost
    pool = Pool(20)
    papers = []

    # paper info retrieving
    for paper_index in paper_index_list:
        paper = pool.apply_async(paper_retriever, args=(paper_index,))
        papers.append(paper)

    # write to json file
    with open('nips2022.json', 'w') as f:
        for paper in papers:
            f.write(json.dumps(paper.get()) + '\n')

    print('done')


if __name__ == '__main__':
    main()
