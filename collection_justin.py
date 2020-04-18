from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import fileinput

a = []
data = []
j = 1

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
    username.send_keys("/////////////////") #enter Username
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys("/////////////////") #enter password
    driver.find_element_by_xpath('//*[@id="siteNavBar_btnLogin"]').click()
    driver.get('https://my.wartburg.edu/ICS/Academics/Student.jnz?portlet=Registration&screen='
               'Advanced+Course+Search&screenType=next')
    select = Select(driver.find_element_by_xpath('//*[@id="pg0_V_ddlTerm"]'))
    index = 0
    select.select_by_index(index)
    select = Select(driver.find_element_by_xpath('//*[@id="pg0_V_ddlTerm"]'))
    selected = select.all_selected_options[0].text.split()

    
    while selected[:2] != ['2006', 'Winter']:
        index += 1
        driver.find_element_by_xpath('//*[@id="pg0_V_btnSearch"]').click()
        
        
        #//*[@id="pg0_V_dgCourses"]/tbody/tr[1]/td[3]
        #//*[@id="pg0_V_dgCourses"]/tbody/tr[3]/td[3]
        while True:
            for i in driver.find_elements_by_xpath('//*[@id="pg0_V_dgCourses"]/tbody/tr'):
                a=[]
                #course id
                #print(j)
                try:
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[3]').text == "":
                         a.append("ID NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[3]').text)
                        
                    #course title
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[4]').text == "":
                        a.append("TITLE NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[4]').text)
                        
                    #teacher name
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[5]/span').text == "":
                        a.append("NAME NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[5]/span').text)
                        
                    #seats
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[6]').text == "":
                        a.append("SEATS NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[6]').text)

                    #status    
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[7]').text == "":
                        a.append("STATUS NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[7]').text)

                    #meeting time
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[8]/ul/li').text == "":
                        a.append("MEETING TIME NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[8]/ul/li').text)

                    #credits
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[9]').text == "":
                        a.append("CREDITS NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[9]').text)

                    #begin date
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[10]').text == "":
                        a.append("BEGIN-DATE NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[10]').text)

                    #end date
                    if driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[11]').text == "":
                        a.append("END-DATE NULL")
                    else:
                        a.append(driver.find_element_by_xpath(f'//*[@id="pg0_V_dgCourses"]/tbody/tr[{j}]/td[11]').text)
                    data.append(a)
                    j += 2
                except:
                    j = 1
                    break
                
            if not Find(driver):
                j = 1
                break
        
        driver.get('https://my.wartburg.edu/ICS/Academics/Student.jnz?portlet=Registration&screen='
                   'Advanced+Course+Search&screenType=next')
        select = Select(driver.find_element_by_xpath('//*[@id="pg0_V_ddlTerm"]'))
        select.select_by_index(index)
        select = Select(driver.find_element_by_xpath('//*[@id="pg0_V_ddlTerm"]'))
        selected = select.all_selected_options[0].text.split()

driver.close()
print(data)
def chunk(lst, n): #class that partitions our lists neatly
    print("chunking...")
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

n = 9
#uberlist = list(chunk(data, n))
with open('historical_data.txt', 'w') as file: #output of scraped data
    print("writing file...")
    #for j in range(len(a)):
    #    a[j] = a[j].split('\n')
    for listitem in data:
        file.write('%s\n' % listitem)
        
with fileinput.FileInput('historical_data.txt', inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("['']", ""), end='')

