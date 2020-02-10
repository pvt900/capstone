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
        #DropDownDictionaries
        self.Departments = {'All':'None Selected','AC   ':'Accounting', 'ART  ':'Art','BI   ':'Biology','BA   ':'Business Administration','CH   ':'Chemistry', 'CS   ':'Computer Science',
               'CCJ  ':'Criminology/Criminal Justice','EC   ':'Economics', 'ED   ':'Education', 'ES   ':'Engineering Science', 'EN   ':'English','EI   ':'English International Students',
               'ENV  ':'Environmental Science', 'EXS  ':'Exercise Science', 'FL   ':'Foreign Language','FR   ':'French','SCI  ':'General Science',
               'GER  ':'German','GM   ':'Global Multicultural','GR   ':'Greek','HE   ':'Health','HB   ':'Hebrew','HI   ':'History','IS   ':'Inquiry Studies',
               'ID   ':'Interdisciplinary','COM  ':'Journalism and Communication','LS   ':'Liberal Studies','MA   ':'Mathematics', 'MU   ':'Music',
               'NSC  ':'Neuroscience','PJ   ':'Peace and Justice Studies','PH   ':'Philiosophy','PE   ':'Physical Education','PHY  ':'Physics','PS   ':'Political Science',
               'NUR  ':'Pre-Professional Nursing Prog', 'PSY  ':'Psychology', 'PBH  ':'Public Health','RE   ':'Religion','SCH  ':'Scholars Program',
               'SW   ':'Social Work','SO   ':'Sociology','SP   ':'Spanish','TH   ':'Theatre','VE   ':'Venture Ed','WW   ':'Wartburg West','WS   ':"Womens Studies"} # Automate to add rest to Dictionary

        self.Terms = ['May Term', 'Summer Session', 'Winter Term', 'Fall Term'] #Maybe Automate to Provide Year Options Instead of All?

        self.Times = {'all':'Show all', 'od':'Other Evening', 'oe':'Other Evening', '7:45AM/MWF':'7:45AM MWF', '9:00AM/MWF':'9:00AM MWF', '10:45AM/MWF':'10:45AM MWF',
                        '12:00PM/MWF':'12:00PM MWF', '1:15PM/MWF':'1:15PM MWF', '2:30PM/MWF':'2:30PM MWF', '3:50PM/MWF':'3:50PM MWF', '7:45AM/THX':'7:45AM TH',
                        '7:45AM/THX':'7:45AM TH', '9:35AM/THX':'9:35AM TH','11:30AM/THX':'11:30AM TH', '1:00PM/THX':'1:00PM TH', '2:50PM/THX':'2:50PM TH', '3:50PM/THX':'3:50PM TH'}

        self.ED = {'all':'Show all EE courses', 'CP':'CP - Capstone', 'FL':'FL- Foreign Language', 'FR':'FR - Faith & Reflection',
                    'HF':'HF - Humanities/Fine Arts Interconnected','MR':'MR - Mathematical Reasoning','NS':'NS - Natural Science Interconnected',
                    'SR':'SR - Scientific Reasoning','SS':'SS - Social Science Interconnected'}

        self.CD = {'none':'Not selected','C':'C - Cultural Immersion', 'D': 'D - Diversity Across Curriculum Course'}
        self.WI = {'none':'Not selected', 'WI':'Writing Intensive'}
        self.PF = {'none':'Not selected', 'PF':'Pass/D/F basis'}
        self.Instructor = {'0':'Not Selected'}

       
    def by_keyword(self,key):
        #inputs user keyword into course finder
        keyword = key
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', keyword)

    def get_deptartments(self):
        #pulls current list of departments
        #and their corresponding codes from winnet
        #select.form(selector = 'ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department')
        print('Possible Departments')
        print('_____________________')
        for key,value in self.Departments.items():
            print(value)
            
    def by_department(self,department):
        #selects department for course finder
        dept = [k for k,v in self.Departments.items() if v.casefold() == department.casefold()]
        self.page.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", dept[0])

    def get_terms(self):    
        #pulls list of current available terms to query
        #pull each option, append to list
        print('Term Terminology')
        print('_____________________')
        for term in self.Terms:
            print(term)

    def by_term(self,year,semester):
        #selects term from course finder
        term = str(year)+' '+semester
        print(term)
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
