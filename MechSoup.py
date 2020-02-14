import mechanicalsoup
from bs4 import BeautifulSoup

#Sets StatefulBrowser Object to winnet then it it grabs form
browser = mechanicalsoup.StatefulBrowser()
winnet = "http://winnet.wartburg.edu/coursefinder/"
browser.open(winnet)
Searchform = browser.select_form()
values = browser.get_current_page().findAll('option')
value_list = []
item_list = []
for item in values:
    value = str(item).split('"')
    value_list.append(value[1])
    item_list.append(item.get_text())

#
# print(value_list)
#print(item_list)
#Selects submit button and has filter options listed.
Searchform.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
print('Input Keywords: ')
x = input()
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', x) #Keyword Searches by Course Name. Inputting string will search by that string ignoring any stored nonsense in the page.
#ACxxx Course Codes have 3 spaces after them, THIS IS REQUIRED. Except the All value for not searching by a Department does not Unless it is 3 Characters in which it uses 2 Blank Spaces.
Searchform.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", 'PHY  ') #takes the CourseCodes as inputs and displays as the Full Name
Searchform.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Term", "2020 Winter Term") # takes a value that is a string. String is Exactly the Term date.
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_MeetingTime', 'all') #Takes the Week Class Time as a String. Need to Retrieve list of options from pages
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', 'none') #takes a small string signialling the EE req or 'all' or 'none'. None doesn't select and option and all selects all coruses w/ a EE
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'none')# Cultural Diversity, Takes none, C, D or all
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'none') # options are none or WI
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail', 'none')# Pass/Faill takes 'none' or 'PF'
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$CheckBox_OpenCourses', False) #Check Box, It's True or False
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_Instructor', '0')# 0 is for None Selected otherwise it is a string of numbers (Instructor ID?)


for i in range(len(value_list)):
    print(value_list[i],':',item_list[i])
    if value_list[i].isdigit():
        print('id found')

#Submits Page, Grabs results and then launches a browser for test purposes.
#browser.submit_selected()# Submits Form. Retrieves Results.
#table = browser.get_current_page().find('table') #Finds Result Table
#print(type(table))
#rows = table.get_text().split('\n') # List of all Class Rows split by \n. 
#print(type(rows))
#browser.launch_browser()

Departments = {'All':'None Selected','AC   ':'Accounting', 'ART  ':'Art','BI   ':'Biology','BA   ':'Business Administration','CH   ':'Chemistry', 'CS   ':'Computer Science',
               'CCJ  ':'Criminology/Criminal Justice','EC   ':'Economics', 'ED   ':'Education', 'ES':'Engineering Science', 'EN   ':'English','EI   ':'English International Students',
               'ENV  ':'Environmental Science', 'EXS  ':'Exercise Science', 'FL  ':'Foreign Language','FR   ':'French','SCI  ':'General Science',
               'GER  ':'German','GM   ':'Global Multicultural','GR   ':'Greek','HE   ':'Health','HB   ':'Hebrew','HI   ':'History','IS   ':'Inquiry Studies',
               'ID   ':'Interdisciplinary','COM  ':'Journalism and Communication','LS   ':'Liberal Studies','MA   ':'Mathematics', 'MU   ':'Music',
               'NSC  ':'Neuroscience','PJ   ':'Peace and Justice Studies','PH   ':'Philiosophy','PE   ':'Physical Education','PHY  ':'Physics','PS   ':'Political Science',
               'NUR  ':'Pre-Professional Nursing Prog', 'PSY  ':'Psychology', 'PBH  ':'Public Health','RE   ':'Religion','SCH  ':'Scholars Program',
               'SW   ':'Social Work','SO   ':'Sociology','SP   ':'Spanish','TH   ':'Theatre','VE   ':'Venture Ed','WW   ':'Wartburg West','WS   ':"Womens Studies"} # Automate to add rest to Dictionary

Terms = {'May':'May Term', 'Summer':'Summer Session', 'Winter':'Winter Term', 'Fall':'Fall Term'} #Maybe Automate to Provide Year Options Instead of All?

Times = {'all':'Show all', 'od':'Other Evening', 'oe':'Other Evening', '7:45AM/MWF':'7:45AM MWF', '9:00AM/MWF':'9:00AM MWF', '10:45AM/MWF':'10:45AM MWF',
         '12:00PM/MWF':'12:00PM MWF', '1:15PM/MWF':'1:15PM MWF', '2:30PM/MWF':'2:30PM MWF', '3:50PM/MWF':'3:50PM MWF', '7:45AM/THX':'7:45AM TH',
          '7:45AM/THX':'7:45AM TH', '9:35AM/THX':'9:35AM TH','11:30AM/THX':'11:30AM TH', '1:00PM/THX':'1:00PM TH', '2:50PM/THX':'2:50PM TH', '3:50PM/THX':'3:50PM TH'}

ED = {'all':'Show all EE courses', 'CP':'CP - Capstone', 'FL':'FL- Foreign Language', 'FR':'FR - Faith & Reflection',
      'HF':'HF - Humanities/Fine Arts Interconnected','MR':'MR - Mathematical Reasoning','NS':'NS - Natural Science Interconnected',
      'SR':'SR - Scientific Reasoning','SS':'SS - Social Science Interconnected'}

CD = {'none':'Not selected','C':'C - Cultural Immersion', 'D': 'D - Diversity Across Curriculum Course'}
WI = {'none':'Not selected', 'WI':'Writing Intensive'}
PF = {'none':'Not selected', 'PF':'Pass/D/F basis'}
Instructor = {'0':'Not Selected'}

# Drop Down Options ### Department Drop down only displays the Department's full title. It passes the Dept. Codes behind the scenes.
# All, ACxxx, ARTxxx, BIxxx, BAxxx, CHxxx, CSxxx, CCJxxx, ECxxx, EDxxx, ESxxx, ENxxx, EIxxx, 
# ENVxxx, EXSxxx, FLxxx, FRxxx, SCIxxx, GERxxx, GMxxx, GRxxx, HExxx, HBxxx, HIxxx, ISxxx,
# IDxxx, COMxxx, LSxxx, MAxxx, MUxxx, NSCxxx, PJxxx, PHxxx, PExxx, PHYxxx, PSxxx, NURxxx, 
# PSYxxx, PBHxxx, RExxx, SWxxx, SOxxx, SPxxx, THxxx, VExxx, WWxxx, WSxxx
# the xxx is placeholder for 3 empty spaces


########## Meeting W/ Zelle Information #################git p
# Methods for Error-Checking Submission  - Since it's all drop-down if the entry is bad it returns an error, do we need another level of error-checking? 
# return list of options and set by index? - W
# Return NExt Week with Concrete API Proposal for Live & Historic
    # Ensure all Queries are Valid.
# Work w/ Setting Form Fields via Script  - Done. Instructor is a odd one, but besdies that 
# 2 Very Different Pieces (Historic Data & "Hot" Queries) - Two APIs one for querying Historic Data one for querying the CourseFinder Pulls. Perhaps make appending to the Historic Data take a CSV full of course information and then append that to the DataBase of Historic Data
# Flag that when object is created. Do you want to update Records? - Method that is called before the Pandas/openpyxl code is properly launched? Ask user input then if == True or Yes/Y/y etc then continue w/ code else terminte and continue w/ Pandas/openpyxl
# Function to check Terms in the Historic Data
    # Save Old Data Somehow?? - Backup File. Backup Sheet?
    # CSV's rather than using Openpyxl look at Pandas
    # Don't Foresee using Excel, Presenting Info using Excel/OpenOffice - OpenPyxl? Using Openpyxl to write data to a sheet. Use Excel Sheets to keep copies?
    # Is there a Panda's file for multiple versions of a dataset - We Can Create a Copy of the DataFrame using pandas.DataFrame.copy(deep=True) [This Create a copy w/ its own indexes of the data so if the Original is Nuked the Copy stayes independent]
    # Take a look if there is something Panda-y we can use to store data present next time.