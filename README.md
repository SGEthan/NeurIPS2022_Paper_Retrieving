# NeurIPS2022_Paper_Retrieving
A crawler to retrieve the accepted paper list of NeurIPS 2022

### Files

```
crawl.py
```

this script is used to crawl the original data of the accepted papers, and will create a `nips2022.txt` containing all paper info.

```
data_analyze.py
```

this script is used to do some data analysis based on the above file `nips2022.txt`. It will count the papers of each affiliation, and the papers of each affiliation to which the first author belongs.

### How to run

Run the following

```
python crawl.py
```

then can get the accepted paper list.

Then run 

```
python data_analyze.py
```

to analyze the data.

We generate the following figure. 

![first_affiliations](\\first_affiliations.png)
