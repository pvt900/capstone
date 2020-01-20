from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep

a = []

def Find(browser):
    try:
        next_page = browser.find_elements_by_xpath('//*[@id="pg0_V_divMain"]/div[3]/div/div/a')
        print(next_page[len(next_page)-1].text=="Next page -->")
        if next_page[len(next_page)-1].text == "Next page -->":
            next_page[len(next_page)-1].click()
            sleep(2)
            return True
        return False
    except NoSuchElementException:
        return False
    except IndexError:
        return False

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://my.wartburg.edu/ICS/')
    username = driver.find_element_by_id("userName")
    username.send_keys("") #enter Username
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys("") #enter password
    driver.find_element_by_xpath('//*[@id="siteNavBar_btnLogin"]').click()
    driver.get('https://my.wartburg.edu/ICS/Academics/Student.jnz?portlet=Registration&screen='
               'Advanced+Course+Search&screenType=next')
    select = Select(driver.find_element_by_xpath('//*[@id="pg0_V_ddlTerm"]'))
    index = 6
    select.select_by_index(index)
    select = Select(driver.find_element_by_xpath('//*[@id="pg0_V_ddlTerm"]'))
    selected = select.all_selected_options[0].text.split()

    while selected[:2] != ['2019', 'Fall']:
        index += 1
        driver.find_element_by_xpath('//*[@id="pg0_V_btnSearch"]').click()
        while True:
            for i in driver.find_elements_by_xpath('//*[@id="pg0_V_dgCourses"]/tbody/tr'):
                a.append(i.text)
            if not Find(driver):
                break
        #for j in range(len(a)):
        #    a[j] = a[j].split('\n')
        #print(a)
        driver.get('https://my.wartburg.edu/ICS/Academics/Student.jnz?portlet=Registration&screen='
                   'Advanced+Course+Search&screenType=next')
        select = Select(driver.find_element_by_xpath('//*[@id="pg0_V_ddlTerm"]'))
        select.select_by_index(index)
        select = Select(driver.find_element_by_xpath('//*[@id="pg0_V_ddlTerm"]'))
        selected = select.all_selected_options[0].text.split()

driver.close()

with open('historical_data.txt', 'w') as handler: #output of scraped data
    print("writing file...")
    for listitem in a:
        handler.write('%s\n' % listitem)
