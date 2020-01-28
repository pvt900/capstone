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
