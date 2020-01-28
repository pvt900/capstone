#Wartburg Course Finder Data Scraper
#By: Rob Farmer & Will Goettl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

Chrome_Options = Options()
Chrome_Options.add_argument("--headless") #allows program to run without opening a chrome window

driver = webdriver.Chrome() 
driver.get("https://winnet.wartburg.edu/coursefinder/") #sets the Silenium driver

select = Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_FormView1_DropDownList_Term"))
term_options = select.options
#for index in range(0, len(term_options) - 1):
#    select.select_by_index(index)

    
lst = []

DeptSelect = Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_FormView1_DropDownList_Department")) 
DeptSelect.select_by_visible_text("History") #finds the desiered department

search = driver.find_element_by_name("ctl00$ContentPlaceHolder1$FormView1$Button_FindNow")
search.click() #sends query

table_id = driver.find_element_by_id("ctl00_ContentPlaceHolder1_GridView1")
rows = table_id.find_elements_by_tag_name("tr")
for row in rows: #creates a list of lists containing our data
    col_lst = []
    col = row.find_elements_by_tag_name("td")
    for data in col:
        lst.append(data.text)

def chunk(l, n): #class that partitions our lists neatly
    print("chunking...")
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 16 #each list contains 16 items regardless of contents or search
uberlist = list(chunk(lst, n)) #call chunk fn to partion list

with open('class_data.txt', 'w') as handler: #output of scraped data
    print("writing file...")
    for listitem in uberlist:
        handler.write('%s\n' % listitem)

driver.close #ends and closes Silenium control over brower
