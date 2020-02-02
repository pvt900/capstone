import mechanicalsoup
from bs4 import BeautifulSoup

browser = mechanicalsoup.StatefulBrowser()
winnet = "http://winnet.wartburg.edu/coursefinder/"
browser.open(winnet)
Searchform = browser.select_form()
Searchform.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$TextBox_keyword', input()) #Keyword Searches by Class Title. Inputting string will search by that string ignoring any stored nonsense in the page.
# ACxxx Course Codes have 3 spaces after them, THIS IS REQUIRED. Except the All value for not searching by a Department does not.
Searchform.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Department", 'CS   ') #For Department List, it takes the CourseCodes as inputs and displays as the Full Name
Searchform.set("ctl00$ContentPlaceHolder1$FormView1$DropDownList_Term", "2020 Winter Term") # Term Dropdown takes a value that is a string. String is Exactly the Term date.
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_MeetingTime', 'all') #Takes the Week Class Time as a String. Need to Retrieve list of options from pages
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_EssentialEd', 'none') #takes a small string signialling the EE req or 'all' or 'none'. None doesn't select and option and all selects all coruses w/ a EE
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_CulturalDiversity', 'none')# Cultural Diversity, Takes none, C, D or all
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_WritingIntensive', 'none') # options are none or WI
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_PassFail', 'none')# Pass/Faill takes 'none' or 'PF'
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$CheckBox_OpenCourses', False) #Check Box, It's True or False
Searchform.set('ctl00$ContentPlaceHolder1$FormView1$DropDownList_Instructor', '0')# 0 is for None Selected otherwise it is a string of numbers (Instructor ID?)
response1 = browser.submit_selected()# Submits Form. Retrieves Results.
table = browser.get_current_page().find('table') #Finds Result Table
print(type(table))
rows = table.get_text().split('\n') # List of all Class Rows split by \n. 
print(type(rows))
browser.launch_browser()


# Drop Down Options = All, ACxxx, ARTxxx, BIxxx, BAxxx, CHxxx, CSxxx, CCJxxx, ECxxx, EDxxx, ESxxx, ENxxx, EIxxx, ENVxxx, EXSxxx, FLxxx, FRxxx, SCIxxx, GERxxx, GMxxx, GRxxx, HExxx, HBxxx, HIxxx, ISxxx, IDxxx, COMxxx, LSxxx, MAxxx, MUxxx, NSCxxx, PJxxx, PHxxx, PExxx, PHYxxx, PSxxx, NURxxx, PSYxxx, PBHxxx, RExxx, SWxxx, SOxxx, SPxxx, THxxx, VExxx, WWxxx, WSxxx
# the xxx is placeholder for 3 empty spaces


########## Meeting W/ Zelle Information #################
# Methods for Error-Checking Submission
# return list of options and set by index?
# Return NExt Week with Concrete API Proposal for Live & Historic
    # Ensure all Queries are Valid.
# Work w/ Setting Form Fields via Script 
# 2 Very Different Pieces (Historic Data & "Hot" Queries)
# Flag that when object is created. Do you want to update Records?
# Function to check Terms in the Historic Data
    # Save Old Data Somehow?? - Backup File. Backup Sheet?
    # CSV's rather than using Openpyxl look at Pandas
    # Don't Foresee using Excel, Presenting Info using Excel/OpenOffice
    # Is there a Panda's file for multiple versions of a dataset
    # Take a look if there is something Panda-y we can use to store data present next time.