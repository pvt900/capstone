from cf_api import CourseSearch as cfapi


def main():
    test = cfapi()
    #test.set_keyword('This is useless')
    #departs = test.get_departments()
    #test.set_department('Psychology')
    #years = test.get_years()
    #terms = test.get_terms()
    #test.set_term(2019,'Fall Term')
    #times = test.get_times()
    #test.set_time()
    #essential_ed = test.get_ed()
    #test.set_ed()
    #cul_div = test.get_cd()
    #test.set_cd()
    #test.set_wi(True)
    #test.is_pf(False)
    #instructors = test.get_instructors()
    #test.set_instructor('John Zelle')
    #test.course_open(True)

    a = test.search_form()
    b= test.update_historic()
    
    #test.display_browser()

    
if __name__ == '__main__':
    main()

    #Default to current year?
    #Unify Winnet and Historical Data with Queries. Hide the differences 
    #Testing Whats the Last Year in Historical and Current Year in Live Data. At such time next year is available do you want to update? compare to historical data and rollover for future
    #Think over 