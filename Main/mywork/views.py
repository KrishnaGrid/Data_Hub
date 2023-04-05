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
        driver = webdriver.Chrome(options=options)
        movie_list = []
        shows_list = []

        # get movie list
        b = 'https://in.bookmyshow.com/explore/movies-'
        url = b + location
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        sleep(2)
        while True:
            # get the number of elements currently on the page
            num_elements = len(driver.find_elements(By.CLASS_NAME, "sc-7o7nez-0.cBsijw"))

            # scroll down to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # wait for new elements to load
            sleep(2)

            # check if new elements have been loaded
            new_num_elements = len(driver.find_elements(By.CLASS_NAME, "sc-7o7nez-0.cBsijw"))
            if new_num_elements == num_elements:
                break
        elements = driver.find_elements(By.CLASS_NAME, "sc-7o7nez-0.cBsijw")
        movie_list = ["<tr><td>{}</td></tr>".format(elem.text.title()) for elem in elements]
        movie_table = "".join(movie_list)

        # get show list
        url = 'https://in.bookmyshow.com/explore/events-' + location
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        sleep(2)
        while True:
            # get the number of elements currently on the page
            num_elements = len(driver.find_elements(By.CLASS_NAME, "sc-7o7nez-0.cBsijw"))

            # scroll down to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # wait for new elements to load
            sleep(2)

            # check if new elements have been loaded
            new_num_elements = len(driver.find_elements(By.CLASS_NAME, "sc-7o7nez-0.cBsijw"))
            if new_num_elements == num_elements:
                break
        elements = driver.find_elements(By.CLASS_NAME, "sc-7o7nez-0.cBsijw")
        shows_list = ["<tr><td>{}</td></tr>".format(elem.text.title()) for elem in elements]
        show_table = "".join(shows_list)

        driver.quit()

        # movie_table = tabulate([[movie] for movie in movie_list], headers=["Movie"])
        # show_table = tabulate([[shows] for shows in shows_list], headers=["Event Shows"])

        context = {
            'location': location,
            'movie_table': movie_table,
            'show_table': show_table,
        }
        return render(request, 'movie_list.html', context)
    else:
        return render(request,'temp.html')
