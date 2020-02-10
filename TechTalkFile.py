from cf_api import search as cfapi


def main():
    test = cfapi()
    #test.get_deptartments()
    test.by_department('Computer Science')
    test.by_instructor('65105')
    test.get_terms()
    test.by_term(2018,'Fall Term')
    test.search_form()
    #test.display_browser()
    #test.save_file()
    
    


if __name__ == '__main__':
    main()