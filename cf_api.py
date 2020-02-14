#API functions for Wartburg Winnet Course Finder
#By: Will Goettl & Rob Farmer
import mechanicalsoup
from bs4 import BeautifulSoup as soup

class search:    #uses helper functions to query and pull results

    def __init__(self):
        '''
        Initializes Variables & StatefulBrowser for use within the Search class
        '''
        #Sets Statefulself.browser Object to winnet then it it grabs form
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.open("http://winnet.wartburg.edu/coursefinder/")
        self.page = self.browser.select_form()
        self.option_list = self.browser.get_current_page().findAll('option')
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
               'SW   ':'Social Work','SO   ':'Sociology','SP   ':'Spanish','TH   ':'Theatre','VE   ':'Venture Ed','WW   ':'Wartburg West','WS   ':"Womens Studies"} 
        self.Terms = ['May Term', 'Summer Session', 'Winter Term', 'Fall Term'] 
        self.Times = {'all':'Show all', 'od':'Other Evening', 'oe':'Other Evening', '7:45AM/MWF':'7:45AM MWF', '9:00AM/MWF':'9:00AM MWF', '10:45AM/MWF':'10:45AM MWF',
                    '12:00PM/MWF':'12:00PM MWF', '1:15PM/MWF':'1:15PM MWF', '2:30PM/MWF':'2:30PM MWF', '3:50PM/MWF':'3:50PM MWF', '7:45AM/THX':'7:45AM TH',
                    '7:45AM/THX':'7:45AM TH', '9:35AM/THX':'9:35AM TH','11:30AM/THX':'11:30AM TH', '1:00PM/THX':'1:00PM TH', '2:50PM/THX':'2:50PM TH', '3:50PM/THX':'3:50PM TH'}
        self.ED = {'all':'Show all EE courses', 'CP':'CP - Capstone', 'FL':'FL- Foreign Language', 'FR':'FR - Faith & Reflection',
                    'HF':'HF - Humanities/Fine Arts Interconnected','MR':'MR - Mathematical Reasoning','NS':'NS - Natural Science Interconnected',
                    'SR':'SR - Scientific Reasoning','SS':'SS - Social Science Interconnected'}
        self.CD = {'none':'Not selected','C':'C - Cultural Immersion', 'D': 'D - Diversity Across Curriculum Course','all':'Show both'}
        self.WI = {'none':'Not selected', 'WI':'Writing Intensive'}
        self.PF = {'none':'Not selected', 'PF':'Pass/D/F basis'}
        self.Instructor = {'0':'Not Selected'}

       
    def by_keyword(self,key):
        '''
        Takes parameter to be passed into the Course Finder Keyword Search
        '''
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', key)

    def get_deptartments(self):
        '''
        Pulls current lists of departments for Department drop down
        '''
        print('Possible Departments')
        print('_____________________')
        for key,value in self.Departments.items():
            print(value)
            
    def by_department(self,department):
        '''
        Takes department as a parameter and passes corresponding department code to form
        '''
        dept = [k for k,v in self.Departments.items() if v.casefold() == department.casefold()]
        self.page.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", dept[0])

    def get_terms(self):    
        '''
        Pulls list of current terms, terms are case-sensitive
        '''
        print('Term Terminology')
        print('_____________________')
        for term in self.Terms:
            print(term)

    def by_term(self,year,semester):
        '''
        Takes year and semester as parameters
        year is the school year
        semester is the calendar semester
        passes parameters to form as one string
        '''
        term = str(year)+' '+semester
        self.page.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Term", term)

    def get_times():
        '''
        Returns array of available class times
        '''
        print('unfinished')
    def by_time(self,time):
        '''
        Takes time as parameter and passes the proper form value to search form
        '''
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_MeetingTime', time)

    def get_ee(self):
        '''
        Returns array of possible essential ed requirements
        '''
        print('unfinished')
    def by_ee(self,ee):
        '''
        Takes ee as essential ed variable and passes to form
        '''
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', ee)
    def get_culdiv(self):
        '''
        Returns list of Cult-Diversity Options
        '''
        print('Cultural Diversity Options')
        print('_____________________')
        for key,value in self.CD.items():
            print(value)
    def is_culdiv(self,option):
        
        '''
        Takes option as a parameter and passes it to form
        option is the case-sensitive variables from get_culdiv()
        '''
        cdo = [k for k,v in self.CD.items() if v.casefold() == option.casefold()]
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', cdo[0])

    def is_writing(self, wi):
        '''
        Takes wi as a parameter and passes it to form
        wi is either True or False
        '''
        if wi == True:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'WI')
        elif wi == False:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'none')

    def is_pass_fail(self,pf):
        '''
        Takes pf as parameter passes to form
        pf is either TRUE or FALSE
        '''
        if pf == True:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail', 'PF')
        elif pf == False:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail','none')

    def get_instructors(self):
        '''
        Returns a list of Instructor names
        Names are case-sensitive
        '''
        for item in self.option_list:
            value = str(item).split('"')

            if value[1].isdigit():
                self.Instructor[value[1]] = item.get_text()
        print('Case Sensitive Instructor List')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        for key,value in self.Instructor.items():
            print(value)
        #Get Instructors from Historical data How can we do thatdatetime A combination of a date and a time. Attributes: ()
    def by_instructor(self,id_num):
        '''
        Takes name as parameter (Instructor's Name) and examines dictionary
        of ID numbers to pass their ID Num to the form.
        '''
        #transform name to id_num
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_Instructor', id_num)

    def couse_open(self, option):
        
        '''
        Takes option as a parameter
        parameter is True or False and passes that to a checkbock in form
        '''
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$CheckBox_OpenCourses', option)
    def search_form(self):
        '''
        selects and submits the form's search button
        '''
        self.page.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
        self.browser.submit_selected()
        
    def display_browser(self):
        '''
        Displays cached copy of webpage
        '''
        self.browser.launch_browser()

    def save_file(self):
        '''
        Saves the Results to a .csv file
        '''
        table_of_data = self.browser.get_current_page().find('table')
        data = table_of_data.get_text().split('\n')
        with open('test_data.txt', 'w') as handler: #output of scraped data
            print("writing file...")
            for listitem in data:
                handler.write('%s\n' % listitem)           
