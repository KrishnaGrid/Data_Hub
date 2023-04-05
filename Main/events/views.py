from django.shortcuts import render
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tabulate import tabulate
from django.shortcuts import render

def movie_and_show_list(request):
    location = request.GET.get('location')
    # set up the options
    options = Options()
    options.headless = True
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    # set up the driver
    if location is not None:
        movie_list = []
        shows_list = []
        b = str('https://insider.in/all-events-in-')
        # print(b + a + '?type=physical')
        url = b + location + '?type=physical'
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # wait for the page to load
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        sleep(2)

        # simulate scrolling to load more elements
        while True:
            # get the number of elements currently on the page
            num_elements = len(driver.find_elements(By.CLASS_NAME, "css-bw9c27"))

            # scroll down to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # wait for new elements to load
            sleep(2)

            # check if new elements have been loaded
            new_num_elements = len(driver.find_elements(By.CLASS_NAME, "css-bw9c27"))
            if new_num_elements == num_elements:
                break

        # extract all elements
        elements = driver.find_elements(By.CLASS_NAME, "css-bw9c27")
        Offline_event_list = ["<tr><td>{}</td></tr>".format(elem.text.title()) for elem in elements]
        Offline_event_list_table = "".join(Offline_event_list)

        '''
        
        Below codes are for the online Events 
        
        '''

        # url1 = b + location + '?type=online'
        # driver.get(url1)
        # wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        # sleep(2)
        #
        #
        # while True:
        #     # get the number of elements currently on the page
        #     num_elements = len(driver.find_elements(By.CLASS_NAME, "css-bw9c27"))
        #
        #     # scroll down to the bottom of the page
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #     # wait for new elements to load
        #     sleep(2)
        #
        #     # check if new elements have been loaded
        #     new_num_elements = len(driver.find_elements(By.CLASS_NAME, "css-bw9c27"))
        #     if new_num_elements == num_elements:
        #         break
        #
        # # extract all elements
        # elements = driver.find_elements(By.CLASS_NAME, "css-bw9c27")
        # Online_event_list = ["<tr><td>{}</td></tr>".format(elem.text.title()) for elem in elements]
        # Online_event_list_table = "".join(Online_event_list)
        #


        driver.quit()
        context = {
            'location': location,
            'movie_table': Offline_event_list_table,
            # 'show_table': Online_event_list_table,
        }
        return render(request, 'list.html', context)
    else:
        return render(request,'event.html')
