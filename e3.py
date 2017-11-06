import requests
from bs4 import BeautifulSoup as bs
import pandas
from matplotlib import pyplot as plt
#%matplotlib inline

elec=pandas.DataFrame()
for line in pandas.read_csv("ELECTION_ID.csv").values.tolist():
    file=("president_general_{}.csv".format(line[0]))
    test=pandas.read_csv(file)
    #change the column names to : County','Year','Democratic','Republican','Total
    colnames=test.iloc[[0]].values[0]
    colnames[0]="County"
    colnames[1]="Year"
    colnames[test.shape[1]-1]="Total"
    colnames.tolist()
    test.columns=colnames

    #drop the first row as it only contains party and keep only relevant colummns
    test.drop(test.index[0], inplace=True)
    test['Year']=line[0]
    test=test[['County','Year','Democratic','Republican','Total']]

    #elec will contain all the data for all counties for all elections 1924-2016
    elec=elec.append(test,ignore_index=True)

#Strip "," out of each string
#The code "replace \D" only keeps digit values and removes any non digit values
elec['Republican'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
elec['Total'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')

#Convert the strings into floats
elec['Republican']=elec['Republican'].astype('float64')
elec['Total']=elec['Total'].astype('float64')

#Calculate the share of Rep votes in Total:
elec['Rep_sh']=elec['Republican']/elec['Total']*100

#Plot and save charts for the four counties
names=("Accomack County","Albemarle County","Alexandria City","Alleghany County")
fnames=("accomack_county","albemarle_county","alexandria_city","alleghany_county")
fn=0
for n in names:
    a=elec[elec['County'] == n].sort_values(by = 'Year', ascending = True)
    plt.plot(a['Year'],a['Rep_sh'])
    #set title of the chart
    plt.suptitle('{}: Republican party % in total votes 1924-2016'.format(n), fontsize=12)
    #set x-axis label
    plt.xlabel('Year', fontsize=12)
    #set y-axis label
    plt.ylabel('% share in total votes', fontsize=12)
    #save the file
    fname=fnames[fn]+".pdf"
    fn=fn+1
    plt.savefig(fname)
    #Clear the fig
    plt.clf()
