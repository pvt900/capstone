import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
winnet = "http://winnet.wartburg.edu/coursefinder/"
browser.open(winnet)
form = browser.select_form()

form.print_summary()
form.choose_submit('ctl00$ContentPlaceHolder1$FormView1$Button_FindNow')
browser.submit_selected()
browser.launch_browser()