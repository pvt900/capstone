#API functions for Wartburg Winnet Course Finder
#By: Will Goettl & Rob Farmer
import mechanicalsoup
from bs4 import BeautifulSoup as soup

#Sets StatefulBrowser Object to winnet then it it grabs form
browser = mechanicalsoup.StatefulBrowser()
winnet = "http://winnet.wartburg.edu/coursefinder/"
browser.open(winnet)
values = browser.get_current_page().findAll('option')
for item in values:
    valuetext = str(item).split('"')
    option = valuetext[1] + ' ' + item.get_text()
    print(option)





class search:    #uses helper functions to query and pull results

    def __init__(self):
        self.keyword = None
        self.dept = None
        self.term = None
        self.ee_req = None
        self.time = None
        self.is_cult_div = None
        self.ee_req = None
        self.write = False
        self.pass_fail = False
        self.instructor = None
        self.course_open = None
       
    def by_keyword(key):
        #inputs user keyword into course finder
        keyword = key
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', keyword)

    def get_deptartments():
        #pulls current list of departments
        #and their corresponding codes from winnet
        select.form(selector = 'ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department')
        print(get_current_form())

    def by_department(department):
        #selects department for course finder
        dept = department
        Searchform.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", dept)

    #def get_terms():
        #pulls list of current available terms to query
        #pull each option, append to list
        
    def by_term(term):
        #selects term from course finder
        Searchform.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Term", term)


    #def get_times():
        #pulls list of class meeting times
        #pull each option, append to list
        
    def by_time(time):
        #selects class meeting time in course finder
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_MeetingTime', time)

    #def get_ee_reqs():
        #pulls list of essential es class types
        #pull each option, append to list

    def by_ee_req(ee):
        #selects essential ed class type
        if ee == 'Y':
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', 'all')
        elif ee == 'N':
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', 'none')
        else:
            print("Invalid input, function only accepts 'Y' or 'N'")
            
        


   # def get_cult_div_reqs():
        #pulls list of 
        #pull each option, append to list

    def is_cult_div(option):
        if option == 'C':
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'C')
        elif option == 'D':
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'D')
        elif option == "BOTH":
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'all')
        else:
            print("Please enter C, D, or BOTH. If you do not want to select an option, do not use this function.")

    def is_writing():
        #selects Writing Intensive option
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'WI')

    def is_pass_fail():
        #selects Pass/Fail classes
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail', 'PF')

    #def get_instructors():
        #gets list of all current instructors
        #pull each option, append to list

    def by_instructor(id_number):
        #selects instructor in dropdown menue
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_Instructor', instructor)

    def couse_open():
        #selects checkbox
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$CheckBox_OpenCourses', True)



#browser.submit_selected()# Submits Form. Retrieves Results.
#table = browser.get_current_page().find('table') #Finds Result Table
#print(type(table))
#rows = table.get_text().split('\n') # List of all Class Rows split by \n. 
#print(type(rows))
#browser.launch_browser()
