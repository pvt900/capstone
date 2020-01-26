from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

lst = []
column_lst = []
chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://winnet.wartburg.edu/coursefinder/")

#department = driver.find_element_by_name("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department")
#print(department.text)
select = Select(driver.find_element_by_name("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Term"))
select.select_by_visible_text("2017 Fall Term")

#If Selecting Element and using dotText it will retrieve the text of the various inputs
#Search button Name: ctl00$ContentPlaceHolder1$FormView1$Button_FindNow

SearchNow = driver.find_element_by_name("ctl00$ContentPlaceHolder1$FormView1$Button_FindNow")
SearchNow.click()


#table_id = driver.find_element_by_id("ctl00_ContentPlaceHolder1_GridView1")
#rows = table_id.find_elements_by_tag_name("tr")
#for row in rows:
#    col = row.find_elements_by_tag_name("td")
#    for data in col:
#        column_lst.append(data.text)

        

#print(lst)
#This is theResult of the Above Nested For-Loops       
#View Details <- Ask Zelle if View Details is a requested feature.
#ART 480 01
#K-12 Art Methods
#Maynard, L
#M W 6:30PM-9:00PM
#18/3/0
#FAC 114G
#2019-20
#WI
#
#1.50


driver.close()




#RESULTS TABLE ID = id="ctl00_ContentPlaceHolder1_GridView1"
