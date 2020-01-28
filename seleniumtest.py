from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


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

table_id = driver.find_element_by_id("ctl00_ContentPlaceHolder1_GridView1")
rows = table_id.find_elements_by_tag_name("tr")
for row in rows:
    col = row.find_elements_by_tag_name("td")
    for data in col:
        column_lst.append(data.text)

driver.close()
#RESULTS TABLE ID = id="ctl00_ContentPlaceHolder1_GridView1"
