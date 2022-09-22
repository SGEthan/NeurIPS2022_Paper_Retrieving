import json
import matplotlib.pyplot as plt


def count_affiliation(papers):
    # count different affiliations
    affiliations = {}
    for paper in papers:
        for author in paper['authors']:
            if author['affiliation'] not in affiliations:
                affiliations[author['affiliation']] = 0
            affiliations[author['affiliation']] += 1
    # merge affiliations containing stanford:
    for affiliation in affiliations:
        if 'stanford' in affiliation.lower() and affiliation != 'Stanford University':
            affiliations['Stanford University'] += affiliations[affiliation]

    # merge affiliations containing google:
    for affiliation in affiliations:
        if 'google' in affiliation.lower() and affiliation != 'Google':
            affiliations['Google'] += affiliations[affiliation]

    # merge affiliations containing pku:
    for affiliation in affiliations:
        if 'peking' in affiliation.lower() and affiliation != 'Peking University':
            affiliations['Peking University'] += affiliations[affiliation]

    # merge affiliations containing thu:
    for affiliation in affiliations:
        if 'tsinghua' in affiliation.lower() and affiliation != 'Tsinghua University':
            affiliations['Tsinghua University'] += affiliations[affiliation]

    # merge affiliations containing cmu:
    for affiliation in affiliations:
        if ('cmu' in affiliation.lower() or 'carnegie mellon University' in affiliation.lower()) and affiliation != 'Carnegie Mellon University':
            affiliations['Carnegie Mellon University'] += affiliations[affiliation]

    # merge affiliations containing oxford:
    for affiliation in affiliations:
        if 'oxford' in affiliation.lower() and affiliation != 'University of Oxford':
            affiliations['University of Oxford'] += affiliations[affiliation]

    # merge affiliations containing MIT:
    for affiliation in affiliations:
        if 'MIT' in affiliation and affiliation != 'Massachusetts Institute of Technology':
            affiliations['Massachusetts Institute of Technology'] += affiliations[affiliation]

    # merge affiliations containing Deepmind:
    for affiliation in affiliations:
        if 'deepmind' in affiliation.lower() and affiliation != 'DeepMind':
            affiliations['DeepMind'] += affiliations[affiliation]

    # merge affiliations containing ZJU:
    for affiliation in affiliations:
        if 'zhejiang university' in affiliation.lower() and affiliation != 'Zhejiang University':
            affiliations['Zhejiang University'] += affiliations[affiliation]

    # merge affiliations containing Microsoft:
    for affiliation in affiliations:
        if 'microsoft' in affiliation.lower() and affiliation != 'Microsoft':
            affiliations['Microsoft'] += affiliations[affiliation]

    # merge affiliations containing Shanghai Jiao Tong University:
    for affiliation in affiliations:
        if ('shanghai jiao tong university' in affiliation.lower() or 'shanghai jiaotong university' in affiliation.lower()) and affiliation != 'Shanghai Jiao Tong University':
            affiliations['Shanghai Jiao Tong University'] += affiliations[affiliation]
    affiliations['Shanghai Jiao Tong University'] += 2

    # merge affiliations containing princeton:
    for affiliation in affiliations:
        if 'princeton' in affiliation.lower() and affiliation != 'Princeton University':
            affiliations['Princeton University'] += affiliations[affiliation]

    # merge affiliations containing ustc:
    for affiliation in affiliations:
        if ('university of science and technology of china' in affiliation.lower() or 'ustc' in affiliation.lower()) and affiliation != 'University of Science and Technology of China':
            affiliations['University of Science and Technology of China'] += affiliations[affiliation]
    affiliations['University of Science and Technology of China'] -= 3

    # merge affiliations containing nus:
    for affiliation in affiliations:
        if 'national university of singapore' in affiliation.lower() and affiliation != 'National University of Singapore':
            affiliations['National University of Singapore'] += affiliations[affiliation]

    # merge affiliations containing berkeley:
    for affiliation in affiliations:
        if 'berkeley' in affiliation.lower() and affiliation != 'University of California, Berkeley':
            affiliations['University of California, Berkeley'] += affiliations[affiliation]

    affiliations['Nanjing University'] += 5
    affiliations['Columbia University'] += 1

    del affiliations['None']
    # del all the affiliations merged above

    # sort the affiliations by count
    affiliations = sorted(affiliations.items(), key=lambda x: x[1], reverse=True)
    # write all affiliations into file
    with open('affiliations.txt', 'w') as f:
        for affiliation in affiliations:
            f.write(f'{affiliation[0]}: {affiliation[1]}\n')


def affiliation_plot(affiliations, fig_name):
    affiliations = affiliations[:30]
    affiliations = list(zip(*affiliations))

    affiliations[0] = list(affiliations[0])
    affiliations[1] = list(affiliations[1])
    affiliations[0].reverse()
    affiliations[1].reverse()

    affiliations[0] = [affiliation.replace('University', 'Univ.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('Institute', 'Inst.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('of', '') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('and', '&') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('Science', 'Sci.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('Technology', 'Tech.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('California', 'Calif.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('Massachusetts', 'Mass.') for affiliation in affiliations[0]]

    plt.figure(figsize=(20, 8), dpi=80)
    plt.barh(range(30), affiliations[1], height=0.8)

    plt.yticks(range(30), affiliations[0])

    plt.grid(alpha=0.4)
    plt.savefig(fig_name)
    plt.show()


def count_first_affiliations(papers):
    # count different affiliations
    affiliations = {}
    for paper in papers:
        author = paper['authors'][0]
        if author['affiliation'] not in affiliations:
            affiliations[author['affiliation']] = 0
        affiliations[author['affiliation']] += 1

    # merge affiliations containing stanford:
    for affiliation in affiliations:
        if 'stanford' in affiliation.lower() and affiliation != 'Stanford University':
            affiliations['Stanford University'] += affiliations[affiliation]

    # merge affiliations containing google:
    for affiliation in affiliations:
        if 'google' in affiliation.lower() and affiliation != 'Google':
            affiliations['Google'] += affiliations[affiliation]

    # merge affiliations containing pku:
    for affiliation in affiliations:
        if 'peking' in affiliation.lower() and affiliation != 'Peking University':
            affiliations['Peking University'] += affiliations[affiliation]

    # merge affiliations containing thu:
    for affiliation in affiliations:
        if 'tsinghua' in affiliation.lower() and affiliation != 'Tsinghua University':
            affiliations['Tsinghua University'] += affiliations[affiliation]

    # merge affiliations containing cmu:
    for affiliation in affiliations:
        if ('cmu' in affiliation.lower() or 'carnegie mellon University' in affiliation.lower()) and affiliation != 'Carnegie Mellon University':
            affiliations['Carnegie Mellon University'] += affiliations[affiliation]

    # merge affiliations containing oxford:
    for affiliation in affiliations:
        if 'oxford' in affiliation.lower() and affiliation != 'University of Oxford':
            affiliations['University of Oxford'] += affiliations[affiliation]

    # merge affiliations containing MIT:
    for affiliation in affiliations:
        if 'MIT' in affiliation and affiliation != 'Massachusetts Institute of Technology':
            affiliations['Massachusetts Institute of Technology'] += affiliations[affiliation]

    # merge affiliations containing Deepmind:
    for affiliation in affiliations:
        if 'deepmind' in affiliation.lower() and affiliation != 'DeepMind':
            affiliations['DeepMind'] += affiliations[affiliation]

    # merge affiliations containing ZJU:
    for affiliation in affiliations:
        if 'zhejiang university' in affiliation.lower() and affiliation != 'Zhejiang University':
            affiliations['Zhejiang University'] += affiliations[affiliation]

    # merge affiliations containing Microsoft:
    for affiliation in affiliations:
        if 'microsoft' in affiliation.lower() and affiliation != 'Microsoft':
            affiliations['Microsoft'] += affiliations[affiliation]

    # merge affiliations containing Shanghai Jiao Tong University:
    for affiliation in affiliations:
        if ('shanghai jiao tong university' in affiliation.lower() or 'shanghai jiaotong university' in affiliation.lower()) and affiliation != 'Shanghai Jiao Tong University':
            affiliations['Shanghai Jiao Tong University'] += affiliations[affiliation]

    # merge affiliations containing princeton:
    for affiliation in affiliations:
        if 'princeton' in affiliation.lower() and affiliation != 'Princeton University':
            affiliations['Princeton University'] += affiliations[affiliation]

    # merge affiliations containing ustc:
    for affiliation in affiliations:
        if ('university of science and technology of china' in affiliation.lower() or 'ustc' in affiliation.lower()) and affiliation != 'University of Science and Technology of China':
            affiliations['University of Science and Technology of China'] += affiliations[affiliation]

    # merge affiliations containing nus:
    for affiliation in affiliations:
        if 'national university of singapore' in affiliation.lower() and affiliation != 'National University of Singapore':
            affiliations['National University of Singapore'] += affiliations[affiliation]

    # merge affiliations containing berkeley:
    for affiliation in affiliations:
        if 'berkeley' in affiliation.lower() and affiliation != 'University of California, Berkeley':
            affiliations['University of California, Berkeley'] += affiliations[affiliation]

    del affiliations['MIT']
    del affiliations['Tsinghua University, Tsinghua University']
    del affiliations['None']

    # sort the affiliations by count
    affiliations = sorted(affiliations.items(), key=lambda x: x[1], reverse=True)

    # write all affiliations into file
    with open('firsts_affiliations.txt', 'w') as f:
        for affiliation in affiliations:
            f.write(f'{affiliation[0]}: {affiliation[1]}\n')

    affiliation_plot(affiliations, 'first_affiliations.png')


def main():
    papers = []
    with open('nips2022.json', 'r') as f:
        # read line by line and process
        for line in f:
            paper = json.loads(line)
            # do something with paper
            papers.append(paper)
    print(len(papers))
    count_affiliation(papers)
    count_first_affiliations(papers)

    print('done')


if __name__ == '__main__':
    main()
