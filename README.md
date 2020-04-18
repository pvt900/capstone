Welcome to the Wartburg College Course Finder API Githib
This project was done in accordance with the CS 460 class at Wartbrug College and supervised by Dr. Zelle
Main contributors are Robert Farmer and Will Goettl with assistance from Justin Schoppe and Dr. Zelle


This project aims to allow users to write scripts to manipulate and edit course data obtained form Wartburg College's course finders
at http://winnet.wartburg.edu/coursefinder/ and https://my.wartburg.edu. This project uses Selenium, MechanicalSoup, Pandas, and DateTime
Python3 libraries to support and run our functions. 

Below are descriptions of each file, their purpose, and how they function.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Demo.py
  Test file for testing of functions.

cf_api.py
   API for our course finder data that works with Pandas dataframe as well as contains functions to pull data from winnet. 

chromedriver.exe
  Requiered file to run silenium. See https://www.selenium.dev/documentation/en/

course_data_4172020.sql
  SQL export file to allow data use and manipulation in a SQL database if desiered. This flie really only exists if a user would like to
  use SQL instead of Pandas for whatever reason. I (Will) thought it would be a good idea to include just in case. 
  
course_history.txt
  Master course data file containing all course data to date (last update 4.17.2020)

mywartburg_scraper.py
  Web scraper built in silenium to scrape my.wartburg's course finder for hisorical data. Requieres a valid my.wartburg user id and pw.
  This ideally will never need to be used. This is a legacy file in case data loss or corruption occurs and a new scrape of course
  data needs to be preformed. 

