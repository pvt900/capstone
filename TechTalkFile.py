from cf_api import search as cfapi


def main():
    test = cfapi()
    test.set_keyword('This is useless')
    departs = test.get_deptartments()
    for elem in departs:
        if elem == 'Computer Science':
            test.set_department(elem)
    instructors = test.get_instructors()
    for staff in instructors:
        if staff == 'Zelle':
            test.set_instructor(staff)
    terms = test.get_terms()
    test.set_term(2018,'Fall Term')
    test.search_form()
    #test.display_browser()
    
    
    
if __name__ == '__main__':
    main()
    
    
    #Default to current year?
    #Unify Winnet and Historical Data with Queries. Hide the differences 
    #Testing Whats the Last Year in Historical and Current Year in Live Data. At such time next year is available do you want to update? compare to historical data and rollover for future
    #Think over 