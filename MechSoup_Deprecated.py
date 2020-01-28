import mechanicalsoup
import requests
from lxml import html
import pandas as pd

#This Will Use Mechanical Soup to grab the Form, Subit it and find the Data Table
browser = mechanicalsoup.StatefulBrowser()
winnet = "http://winnet.wartburg.edu/coursefinder/"
browser.open(winnet)
Searchform = browser.select_form()
Searchform.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
browser.submit_selected() #This Progresses to Second Form, this returns a 200 Response.
print('Page Submitted')
dataURL = browser.get_current_page()#Get URL of Results Form. 
#dataURL2 = 'https://winnet.wartburg.edu/coursefinder/Results.aspx' Results URL

pageContent=requests.get(dataURL) 
print('Requests Fulfilled')
tree = html.fromstring(pageContent.content)
print('Tree Set')
dataTable = tree.xpath('//*[@id="ctl00_ContentPlaceHolder1_GridView1"]')
print('XPath Set')
#print(dataTable)
print(type(dataTable))
rows = [] #initialize a collection of rows
print('')
for row in dataTable[0].xpath(".//tr"): #add new rows to the collection
    rows.append([cell.text_content().strip() for cell in row.xpath(".//td")])

df = pd.DataFrame(rows) #load the collection to a dataframe
print(df)
#XPath to Table
#//*[@id="ctl00_ContentPlaceHolder1_GridView1"]
#//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody