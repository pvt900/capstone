#API functions for Wartburg Winnet Course Finder
#By: Will Goettl & Rob Farmer
import mechanicalsoup
from bs4 import BeautifulSoup as soup

#values = self.browser.get_current_page().findAll('option')
#for item in values:
#    valuetext = str(item).split('"')
#    option = valuetext[1] + ' ' + item.get_text()
#    print(option)

class search:    #uses helper functions to query and pull results

    def __init__(self):
        #Sets Statefulself.browser Object to winnet then it it grabs form
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.open("http://winnet.wartburg.edu/coursefinder/")
        self.page = self.browser.select_form()
        #Form Variables
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
       
    def by_keyword(self,key):
        #inputs user keyword into course finder
        keyword = key
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', keyword)

    def get_deptartments(self):
        #pulls current list of departments
        #and their corresponding codes from winnet
        select.form(selector = 'ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department')
        print(get_current_form())

    def by_department(self,department):
        #selects department for course finder
        dept = department
        self.page.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", dept)

    #def get_terms():
        #pulls list of current available terms to query
        #pull each option, append to list
        
    def by_term(self,term):
        #selects term from course finder
        self.page.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Term", term)

    #def get_times():
        #pulls list of class meeting times
        #pull each option, append to list
        
    def by_time(self,time):
        #selects class meeting time in course finder
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_MeetingTime', time)

    #def get_ee_reqs():
        #pulls list of essential es class types
        #pull each option, append to list

    def by_ee_req(self,ee):
        #selects essential ed class type
        if ee == 'Y':
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', 'all')
        elif ee == 'N':
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', 'none')
        else:
            print("Invalid input, function only accepts 'Y' or 'N'")
        
   # def get_cult_div_reqs():
        #pulls list of 
        #pull each option, append to list

    def is_cult_div(self,option):
        if option == 'C':
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'C')
        elif option == 'D':
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'D')
        elif option == "BOTH":
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'all')
        else:
            print("Please enter C, D, or BOTH. If you do not want to select an option, do not use this function.")

    def is_writing(self):
        #selects Writing Intensive option
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'WI')

    def is_pass_fail(self):
        #selects Pass/Fail classes
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail', 'PF')

    #def get_instructors():
        #gets list of all current instructors
        #pull each option, append to list

    def by_instructor(self,id_number):
        #selects instructor in dropdown menue
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_Instructor', id_number)

    def couse_open(self):
        #selects checkbox
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$CheckBox_OpenCourses', True)
    def search_form(self):
        #Submits Course Search
        self.page.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
        self.browser.submit_selected()# Submits Form. Retrieves Results.
        
    def display_browser(self):
        #Displays self.browser Windows of Current Page
        self.browser.launch_browser()

    def save_file(self):
        table_of_data = self.browser.get_current_page().find('table')
        data = table_of_data.get_text().split('\n')

        with open('test_data.txt', 'w') as handler: #output of scraped data
            print("writing file...")
            for listitem in data:
                handler.write('%s\n' % listitem)           
