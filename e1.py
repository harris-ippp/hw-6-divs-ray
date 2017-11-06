import requests
from bs4 import BeautifulSoup as bs
import pandas

# Sets address of the election site to grab IDs, gets HTML and parses it
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(addr)
html = resp.content
soup = bs(html, "html.parser")

#soup contains the parsed HTML file from the page.
#Then we find all instances of <tr> with class name election_item
all=soup.find_all("tr", "election_item")

#parsing "all" to find election ids and years
#then append (year, ID) tuples into a list
ELECTION_ID=[]
for i in range(0,len(all)):
    id=(all[i].get("id").split(sep="-")[2])
    year=(all[i].find("td", "year first").contents[0])
    year_id=year,id
    ELECTION_ID.append(year_id)

#save the list as csv for use in e2 and e3
data = pandas.DataFrame(ELECTION_ID)
data.to_csv("ELECTION_ID.csv", sep=',',index=False)
