#cf_api.py
#Written for CS460 01 Capstone at Wartburg College
#Instructor/Client - Dr.John Zelle
#By: Will Goettl & Rob Farmer

import mechanicalsoup
import pandas as pd
import os,time
from bs4 import BeautifulSoup as soup
from datetime import datetime

class CourseSearch:
    def __init__(self):
        '''
        Initializes Variables & StatefulBrowser for use within the CourseSearch class
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
        self.course_list = []
        self.changes = []
        self.data = []
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
        
    def update_historic(self):
        '''
        Opens file containing historical course data
        Takes search results and indexes them into a hashtable
        It then compares the courses in winnet to the historic courses and appends
        courses that are new and overwrites courses that are pre-existing.
        '''
        historic = pd.read_csv('course_history.txt', header=None, sep='"', encoding = 'ISO-8859-1',
                               names=['Course_ID', 'Course_Title', 'Professor_Name','Meeting_Time','Enrollment','Room','Year','Term','Credit'])
        winnet = pd.DataFrame(self.data,
                              columns=['Course_ID', 'Course_Title', 'Professor_Name','Meeting_Time','Enrollment','Room','Year','Term','Credit'])
        cols = ['Course_ID','Year','Term']
        combined = pd.concat([historic,winnet])
        combined = combined.drop_duplicates(subset=cols, keep='last')
        combined.set_index(['Course_ID','Year','Term'], inplace=True)
        combined.to_csv(r'course_history.txt',header=['Course_Title', 'Professor_Name','Meeting_Time','Enrollment','Room','Credit'],index=['Course_ID','Year','Term'],sep='"',mode='w')
        winnet.to_csv(r'Changelog.txt',header=['Course_ID', 'Course_Title', 'Professor_Name','Meeting_Time','Enrollment','Room','Year','Term','Credit'],index=['Course_ID','Year','Term'],sep='"',mode='w')
        historic.to_csv(r'historic_legacy.txt',header=['Course_ID', 'Course_Title', 'Professor_Name','Meeting_Time','Enrollment','Room','Year','Term','Credit'],index=['Course_ID','Year','Term'],sep='"',mode='w')
        
        timestr = time.strftime("%Y-%m-%d")
        changelog = "Changelog"+timestr+".txt"
        historic_V = 'historic_legacy'+timestr+'.txt'
        #os.rename is to append the Current Date as d.dataFrame.to_csv can't take a variable str w/ Datetime
        #os.rename will not change filename if the filename already exists
        os.rename('Changelog.txt',changelog)
        os.rename('historic_legacy.txt',historic_V)
        
    def set_keyword(self,key):
        '''
        Takes a String to be passed into the Keyword search parameter
        '''
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', key)

    def get_departments(self):
        '''
        Returns current lists of departments in an array
        '''
        departs = []
        for key,value in self.Departments.items():
            departs.append(value)
        return departs   

    def set_department(self,department):
        '''
        Takes a department as a string and passes corresponding department code to form
        '''
        dept = [k for k,v in self.Departments.items() if v.casefold() == department.casefold()]
        self.page.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", dept[0])
        
    def get_years(self):
        '''
        Compares current date to end of May Term. 
        If date is before june 1st, it will return an array of the past 2 years and future year
        if date is past, it will return last year and future 2 years. (Used for Determining Valid Years for Terms)
        '''
        dt = datetime.now()
        current_year = int('{:%Y}'.format(dt))
        end_of_term = datetime(current_year, 6, 1)
        if dt < end_of_term:
            return [current_year-2, current_year-1, current_year, current_year+1]
        else:
            return [current_year-1, current_year, current_year+1, current_year+2]
    
    def get_terms(self):    
        '''
        Returns array of current terms.
        '''
        return self.Terms

    def set_term(self,year,semester):
        '''
        Takes year (int) and semester (str)
        passes parameters to form as concatencated str
        '''
        term = str(year)+' '+semester
        self.page.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Term", term)

    def get_times(self):
        '''
        Returns array of available class times
        '''
        times = []
        for key,value in self.Times.items():
                times.append(value)
        return times 

    def set_time(self,period):
        '''
        Takes time as parameter and passes the proper form value to search form
        '''
        for k,v in self.Times.items():
            if period in v:
                self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_MeetingTime', k)

    def get_ed(self):
        '''
        Returns array of possible essential ed requirements
        '''
        eds = []
        for key,value in self.ED.items():
                eds.append(value)
        return eds

    def set_ed(self,ed):
        '''
        Takes 'ed' as string and passes to form for Essential Ed.
        '''
        for k,v in self.Times.items():
            if ed in v:
                self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', k)
    
    def get_cd(self):
        '''
        Returns list of Cultural-Diversity Requirment Options
        '''
        cd = []
        for key,value in self.CD.items():
            cd.append(value)
        return cd

    def set_cd(self,option):
        '''
        Takes option as a str, evaluates that self.CD contains the parameter
        If so, passes it to form to set Culural Diversity field.
        '''
        cdo = [k for k,v in self.CD.items() if v.casefold() == option.casefold()]
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', cdo[0])

    def set_wi(self, wi):
        '''
        Takes 'wi' as bool and sets fields with boolean.
        '''
        if wi == True:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'WI')
        else:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'none')

    def is_pf(self,pf):
        '''
        Takes parameter 'pf' as bool
        passes corresponding T/F to Pass/Fail Field
        '''
        if pf == True:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail', 'PF')
        elif pf == False:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail','none')

    def get_instructors(self):
        '''
        Determines instructors from Search form HTML,
        Creates a dictionary based on their ID:Names
        Returns an array all names.
        '''
        for item in self.option_list:
            value = str(item).split('"') #used " as delimeter due to , and ' being used in the course data
            if value[1].isdigit():
                self.Instructor[value[1]] = item.get_text()
        proflist = []
        for key,value in self.Instructor.items():
            proflist.append(value)
        return proflist

    def set_instructor(self, name):
        '''
        Takes parameter name as a str, cross-references instructor dictionary
        passes Instructor ID to instructor field.
        '''
        #transform name to id_num
        for k,v in self.Instructor.items():
            if name in v:
                self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_Instructor', k)

    def couse_open(self, option):
        '''
        Takes parameter option as bool, passes bool to field
        '''
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$CheckBox_OpenCourses', option)
    
    def search_form(self):
        '''
        Identifies form submission button, submits form and
        extracts the courses found in the results.
        Returns the courses in the form of a Tuple containing Tuples.
        '''
        self.course_list = []
        course = []
        counter = 0
        self.page.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
        self.browser.submit_selected()
        table_of_data = self.browser.get_current_page().find('table')
        data = table_of_data.get_text('td').replace('\n', '').replace('td', '|')
        data2 = data.split('|')
        for index in data2[18:]:
            if counter < 15:
                if index == '':
                    continue
                else:
                    if index == '\xa0' or index == ' ':
                        index = 'Null'
                    course.append(index)
                    counter +=1
            else:
                if index == '\xa0' or index == ' ':
                    index = 'Null'
                course.append(index)
                self.course_list.append(tuple(course))
                course = []
                counter = 0
        for item in self.course_list:
           self.data.append([item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[14]])
        
        return self.data

    def display_browser(self):
        '''
        Displays cached copy of webpage
        '''
        self.browser.launch_browser()
    
    def save_file(self):
        '''
        Saves the results of the search to a .csv file
        '''
        
        with open('test_data.txt', 'w') as handler: #output of scraped data
            print("writing file...")
            
            for course in self.course_list:
                handler.write('%s\n' % list(course))           
