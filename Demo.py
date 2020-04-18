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
    b = test.update_historic()
    
    #test.display_browser()


if __name__ == '__main__':
    main()
#(ノಠ益ಠ)ノ彡┻━┻ (ಥ╭╮ಥ) ლ(ಠ益ಠლ) Yes ! <3
# (•_•) ( •_•)>⌐■-■ (⌐■_■) <3