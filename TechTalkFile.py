from cf_api import search as cfapi


def main():
    test = cfapi()
    test.by_department('CS   ')
    test.by_instructor('65105')
    test.by_term('2018 Fall Term')
    test.search_form()
    test.display_browser()
    test.save_file()
    
    


if __name__ == '__main__':
    main()