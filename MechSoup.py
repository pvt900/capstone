import mechanicalsoup
from bs4 import BeautifulSoup

browser = mechanicalsoup.StatefulBrowser()
winnet = "http://winnet.wartburg.edu/coursefinder/"
browser.open(winnet)
Searchform = browser.select_form()
Searchform.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
response1 = browser.submit_selected()# Cant progress to second form. Grabs None Object? Second form Summary is infinite gibberish locks up Python.
table = browser.get_current_page().find('table')
print(type(table))
rows = table.get_text().split('\n') # List of all Class Rows split by \n. 


print(type(rows))
# 
# Methods for Error-Checking Submission
# return list of options and set by index?
# Return NExt Week with Concrete API Proposal for Live & Historic
    # Ensure all Queries are Valid.
# Work w/ Setting Form Fields via Script 
# 2 Very Different Pieces (Historic Data & "Hot" Queries)
# Flag that when object is created. Do you want to update Records?
# Function to check Terms in the Historic Data
    # Save Old Data Somehow?? - Backup File. Backup Sheet?
    # CSV's rather than using Openpyxl look at Pandas
    # Don't Foresee using Excel, Presenting Info using Excel/OpenOffice
    # Is there a Panda's file for multiple versions of a dataset
    # Take a look if there is something Panda-y we can use to store data present next time.