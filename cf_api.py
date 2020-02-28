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

       
    def set_keyword(self,key):
        '''
        Takes parameter to be passed into the Course Finder Keyword Search
        '''
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', key)

    def get_deptartments(self):
        '''
        Pulls current lists of departments for Department drop down
        '''
        departs = []
        #print('Possible Departments')
        #print('_____________________')
        for key,value in self.Departments.items():
            departs.append(value)
        return departs   
    def set_department(self,department):
        '''
        Takes department as a parameter and passes corresponding department code to form
        '''
        dept = [k for k,v in self.Departments.items() if v.casefold() == department.casefold()]
        self.page.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", dept[0])

    def get_terms(self):    
        '''
        Pulls list of current terms, terms are case-sensitive
        '''
        term_list = []
        #print('Term Terminology')
        #print('_____________________')
        return self.Terms
    def set_term(self,year,semester):
        '''
        Takes year and semester as parameters
        year is the school year
        semester is the calendar semester
        passes parameters to form as one string
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
        Takes ee as essential ed variable and passes to form
        '''
        for k,v in self.Times.items():
            if ed in v:
                self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', k)
    def get_cd(self):
        '''
        Returns list of Cult-Diversity Options
        '''
        for key,value in self.CD.items():
            print(value)
    def set_cd(self,option):
        
        '''
        Takes option as a parameter and passes it to form
        option is the case-sensitive variables from get_culdiv()
        '''
        cdo = [k for k,v in self.CD.items() if v.casefold() == option.casefold()]
        self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', cdo[0])

    def set_wi(self, wi):
        '''
        Takes wi as a parameter and passes it to form
        wi is either True or False
        '''
        if wi == True:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'WI')
        elif wi == False:
            self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'none')

    def is_pf(self,pf):
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
        proflist = []
        for key,value in self.Instructor.items():
            proflist.append(value)
        return proflist
        #Get Instructors from Historical data How can we do thatdatetime A combination of a date and a time. Attributes: ()
    def set_instructor(self, name):
        '''
        Takes name as parameter (Instructor's Name) and examines dictionary
        of ID numbers to pass their ID Num to the form.
        '''
        #transform name to id_num
        for k,v in self.Instructor.items():
            if name in v:
                self.page.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_Instructor', k)

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
        course_list = []
        course = []
        counter = 0
        self.page.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
        self.browser.submit_selected()
        table_of_data = self.browser.get_current_page().find('table')
        #print(table_of_data, '\n') HTML
        #print(table_of_data.get_text(), '\n') Text of HTML rendered in format
        data = table_of_data.get_text('td').replace('\n', '').replace('td', '|')
        #print(data)
        data2 = data.split('|')
        #print(data2)
        for index in data2[18:]:
            if counter < 21:
                #print(counter, index)
                course.append(index)
                #print(course)
                counter +=1
                #print('course', course)
            else:
                course.append(index)
                #print('else')
                #print('before',course)
                #print('else', course)
                course_list.append(course)
                course = []
                counter = 0
                #print('after',course)
                
        #print(data2)
        print('--------------------')
        for item in course_list:
            if len(item) > 22:
                print(item)
            #print('\n',item, len(item))
        #print(course_list[0])
        #print(data[3].split('\n'), '\n') CS120 in 1 buggy list
        #exp = data[3].split(',')
        #print(exp, '\n')
        #print(tuple(data))
        #test = exp[0].split('\n')
        #test2 = exp[1].split(' ')
        #print(test)
        #print(test2)
        #for elem in data:
        #
        #     print(elem)
 
        #Notes: Pulled Data data[0-3], 0,1,3 are all blank 2 is the header info
        #Notes: After than its every five with ['Codes','Details','CourseID','CourseTitle','Professor LastNameFInit Time ClassSize Location Term Codes']
        #for course in data:
            #print(course)
        #with open('test_data.txt', 'w') as handler: #output of scraped data
        #    print("writing file...")
        #    for listitem in data:
        #        handler.write('%s\n' % listitem) 
    def display_browser(self):
        '''
        Displays cached copy of webpage
        '''
        self.browser.launch_browser()

    def save_file(self):
        '''
        Saves the Results of the search to a .csv file
        '''
        table_of_data = self.browser.get_current_page().find('table')
        data = table_of_data.get_text().split('\n')
        with open('test_data.txt', 'w') as handler: #output of scraped data
            print("writing file...")
            for listitem in data:
                handler.write('%s\n' % listitem)           
