import requests
from bs4 import BeautifulSoup as bs
import pandas

#parse the Election id.csv to find the years and its corresponding id
# the csv has to be converted into a list first using "".values.tolist()""
for line in pandas.read_csv("ELECTION_ID.csv").values.tolist():
    link=("http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(line[1]))
    #save data from link into resp
    resp = requests.get(link)

    #Create the desired name for csv file and print data from each link as CSV
    name = "president_general_"+str(line[0]) +".csv"
    with open(name, "w") as out:
      out.write(resp.text)
