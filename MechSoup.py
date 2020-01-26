import mechanicalsoup
from bs4 import BeautifulSoup

browser = mechanicalsoup.StatefulBrowser()
winnet = "http://winnet.wartburg.edu/coursefinder/"
browser.open(winnet)
Searchform = browser.select_form()

#Searchform.print_summary()
Searchform.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
response1 = browser.submit_selected()# Cant progress to second form. Grabs None Object? Second form Summary is infinite gibberish locks up Python.
#browser.launch_browser()
table = browser.get_current_page().find_all('table')
print(type(table))
#print(table().get_text())
#soup = BeautifulSoup(table(),'lxml')
first_data = table[0]
print(first_data.th.a.text)
