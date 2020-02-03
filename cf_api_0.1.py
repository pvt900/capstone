#API functions for Wartburg Winnet Course Finder
#By: Will Goettl & Rob Farmer
import mechanicalsoup
from bs4 import BeautifulSoup

#Sets StatefulBrowser Object to winnet then it it grabs form
browser = mechanicalsoup.StatefulBrowser()
winnet = "http://winnet.wartburg.edu/coursefinder/"
browser.open(winnet)
Searchform = browser.select_form()
#browser.select_form('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword')
#browser.get_current_form().print_summary()



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
       
    def by_keyword(keyword):
        #inputs keyword into course finder
        #gets user imput for keyword
        print("Enter keyword to search calss titles: ")
        keyword = input('')
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', keyword)

    def get_deptartments():
        #pulls current list of departments
        #and their corresponding codes from winnet
        select.form(selector = 'ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department')
        print(get_current_form())

    def by_department():
        #selects department for course finder
        print("Type in department code follwed by 3 spaces")
        dept = input('')
        Searchform.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", dept)

    #def get_terms():
        #pulls list of current available terms to query
        #pull each option, append to list
        
    def by_term(term):
        #selects term from course finder
        print("Enter Term Name e.g. 2020 Winter Term: ")
        term = input('')
        Searchform.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Term", term)


    #def get_times():
        #pulls list of class meeting times
        #pull each option, append to list
        
    def by_time(time):
        #selects class meeting time in course finder
        print("Enter class meeting time e.g. 12:00PM/MWF: ")
        time = input('')
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_MeetingTime', time)

    #def get_ee_reqs():
        #pulls list of essential es class types
        #pull each option, append to list

    def by_ee_req(ee_req):
        #selects essential ed class type
        print("Essenital Ed Course? Y/N: ")
        ee = input('')
        if ee == 'Y':
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', 'all')
        elif ee == 'N':
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', 'none')
        else:
            print("Invalid input, function only accepts 'Y' or 'N'")
            
        


   # def get_cult_div_reqs():
        #pulls list of 
        #pull each option, append to list

   def is_cult_div():
        print("If this is a Cultural course type C")
        print("If this is a Diversity course type D")
        print("If you want borth Cultural and Diversity courses type BOTH: ")
        cd = input('')
        if cd == 'C':
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'C')
        elif cd == 'D':
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'D')
        elif cd == "BOTH":
            Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'all')
        else:
            print("Please enter C, D, or BOTH. If you do not want to select an option, do not use this function.")

    def is_writing(write):
        #selects Writing Intensive option
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'WI')

    def is_pass_fail(pass_fail):
        #selects Pass/Fail classes
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail', 'PF')

    #def get_instructors():
        #gets list of all current instructors
        #pull each option, append to list

    def by_instructor(instructor):
        #selects instructor in dropdown menue
        print("Enter Instructors Wartburg ID#: ")
        instructor = input('')
        Searchform.set'ctl00$ContentPlaceHolder1$FormView1$DropDownList_Instructor', instructor)

    def couse_open(is_course_open):
        #selects checkbox
        Searchform.set('ctl00$ContentPlaceHolder1$FormView1$CheckBox_OpenCourses', True)



