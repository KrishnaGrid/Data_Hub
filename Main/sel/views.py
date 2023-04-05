from django.shortcuts import render,HttpResponse
from django.contrib import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# for headless browsing we need to setup it i.e:-
options = Options()
options.headless = True
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')


def search_movie(request):
    if request.method == 'POST':
        movie_name = request.POST.get('movie_name').lower()
        location = request.POST.get('location').lower()
        ticket_number = request.POST.get('ticket_no')
        email_id = request.POST.get('email_id')
        phone_no = request.POST.get('phone_no')
        Upi_name = request.POST.get('Upi_app').lower()
        print(Upi_name)
        if (Upi_name) == 'phonepe':
            Upi_name = 'ybl'
        elif(Upi_name).lower() == 'paytm':
            Upi_name = 'paytm'
        else:
            return HttpResponse("Upi Not Supported")
        driver = webdriver.Chrome(options=options)
        url = "https://in.bookmyshow.com/explore/movies-"+location
        print(url)
        while True:
            driver.get(url)

            try:
                wait = WebDriverWait(driver, 5)
                l=[]
                elements = driver.find_elements(By.CLASS_NAME, "sc-7o7nez-0.cBsijw")
                for elem in elements:
                    name = elem.text.lower()
                    l.append(name)
                print(l)

                if movie_name in l:
                    sleep(2)
                    driver = webdriver.Chrome()
                    """
                    Notification as playing Youtube songs
                    """
                    # driver.get('https://www.youtube.com/')
                    # sleep(2)
                    # search_field = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
                    # search_field.send_keys('kgf ringtone')
                    # sleep(2)
                    # click_button = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button')
                    # click_button.click()
                    # sleep(2)
                    # song_click = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
                    # song_click.click()
                    # sleep(15)
                    """
                    Movie Ticket Booking to start 
                    """

                    driver.get(url)
                    sleep(3)
                    print('hello')
                    search_button_click = driver.find_element(By.XPATH,'//*[@id="3"]')
                    search_button_click.click()
                    print('Hello')
                    sleep(5)
                    input_field = driver.find_element(By.CLASS_NAME,"sc-hCaUpS")

                    # Clear the input field (optional)
                    input_field.clear()
                    print('ok')
                    # Send keys to the input field to provide input
                    input_field.send_keys(movie_name)

                    # search_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/input')
                    # search_button.clear()
                    sleep(2)
                    input_field.send_keys(Keys.ENTER)
                    # search_button.send_keys('')
                    # search_button.send_keys(Keys.ENTER)
                    sleep(5)
                    print('Now')
                    # search_button.send_keys(movie_name)
                    # sleep(2)
                    # search_button.click()
                    book_ticket_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/div[2]/div/button/div')
                    book_ticket_button.click()
                    sleep(5)
                    quality_list = [
                        '//*[@id="super-container"]/div[2]/div/div[2]/div/div/ul/li/section[2]/div[1]',
                        '//*[@id="super-container"]/div[2]/div/div[2]/div/div/ul/li/section[2]/div[2]',
                        '//*[@id="super-container"]/div[2]/div/div[2]/div/div/ul/li/section[2]/div[3]'
                    ]
                    for xpath in quality_list:
                        try:
                            element = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, xpath))
                            )
                            element.click()
                            print('Clicked element:', xpath)
                            break
                        except Exception as e:
                            print(f"Caught exception: {e}")
                            break
                    sleep(2)
                    print('Notification')
                    #Notification Cancel
                    try:
                        element = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/div[20]/div[2]/div[3]/button[1]'))
                        )
                        element.click()
                        print('Clicked element')
                    except Exception as e:
                        print(f"Caught exception: {e}")

                    sleep(5)
                    print('notification okk')


                    xpath_list = [
                        '//*[@id="venuelist"]/li[2]/div[2]/div[2]/div[1]/a',
                        '//*[@id="venuelist"]/li[2]/div[2]/div[2]/div[2]/a',
                        '//*[@id="venuelist"]/li[2]/div[2]/div[2]/div[3]/a',
                        '//*[@id="venuelist"]/li[1]/div[2]/div[2]/div[1]/a',
                        '//*[@id="venuelist"]/li[2]/div[2]/div[2]/div[4]/a',
                        '//*[@id="venuelist"]/li[3]/div[2]/div[2]/div[1]/a',
                        '//*[@id="venuelist"]/li[3]/div[2]/div[2]/div[2]/a',
                    ]
                    for xpath in xpath_list:
                        try:
                            element = WebDriverWait(driver, 20).until(
                                EC.element_to_be_clickable((By.XPATH, xpath))
                            )
                            element.click()
                            break
                        except:
                            print('fine')
                            continue

                    # SELECTING AGREE BUTTON AND NOTIFICATION CANCEL WITH SELECTING NUMBER OF TICKETS ENTERED BY USER
                    agree_button = driver.find_element(By.XPATH,'/html/body/div[18]/strong/div[4]/div[2]/div[2]/div/div[3]')
                    agree_button.click();
                    sleep(5)
                    button = driver.find_element(By.XPATH,'/html/body/div[18]/strong/div[6]/div[2]/div[2]/ul/li[' + ticket_number + ']')
                    button.click();
                    sleep(2)
                    select_button = driver.find_element(By.XPATH,'/html/body/div[18]/strong/div[6]/div[2]/div[4]/div')
                    select_button.click();
                    sleep(2)

                    seats_with_A = driver.find_elements(By.CSS_SELECTOR,"[id^='A_']")
                    seats_with_B = driver.find_elements(By.CSS_SELECTOR, "[id^='B_']")

                    # Extract the seat IDs and store them in a list
                    available_seats = [seat.get_attribute("id") for seat in seats_with_A]
                    available_seat = [seat.get_attribute("id") for seat in seats_with_B]

                    # Print the available seats list
                    print(available_seats)
                    sleep(4)
                    if len(available_seat)!=0:
                        for seat_id in available_seat:
                            try:
                                element = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.ID, seat_id))
                                )
                                element.click()
                                sleep(2)
                                pay_option_visible = WebDriverWait(driver, 10).until(
                                    EC.visibility_of_element_located(
                                        (By.XPATH, "/html/body/section/div[3]/section[1]/div/div[6]/a[1]"))
                                )
                                if pay_option_visible:
                                    print("Pay option is visible. Stopping seat selection.")
                                    break
                            except Exception as e:
                                print(f"An error occurred: {e}")
                                continue

                    if len(available_seats)!=0:
                        for seat_id in available_seats:
                            try:
                                element = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.ID, seat_id))
                                )
                                # if len(selected_seats) < int(ticket_number):
                                #     selected_seats.append(seat_id)
                                element.click()
                                sleep(2)
                                # elif len(selected_seats) == int(ticket_number):
                                #     print(len(selected_seats),ticket_number)
                                #     break
                                # else:
                                #     print('hi')
                                #     continue
                                pay_option_visible = WebDriverWait(driver, 10).until(
                                    EC.visibility_of_element_located(
                                        (By.XPATH, "/html/body/section/div[3]/section[1]/div/div[6]/a[1]"))
                                )
                                if pay_option_visible:
                                    print("Pay option is visible. Stopping seat selection.")
                                    break
                            except Exception as e:
                                print(f"An error occurred: {e}")
                                continue


                    # selected_seats = []
                    # for seat_id in available_seats:
                    #     if (selected_seats) < int(ticket_number):
                    #         element = driver.find_element(By.ID, seat_id)
                    #         element.click()
                    #         sleep(2)
                    #         selected_seats.append(seat_id)
                    #     elif len(selected_seats) == int(ticket_number):
                    #         break
                    #     else:
                    #         continue



                    # for i in range(ticket_number):
                    #     try:
                    #         element = WebDriverWait(driver, 20).until(
                    #             EC.element_to_be_clickable((By.ID, available_seats[i]))
                    #         )
                    #         element.click()
                    #         sleep(2)
                    #         # ActionChains(driver).move_to_element(element).click().perform()
                    #         # sleep(3)
                    #         print('yes')
                    #     except Exception as e:
                    #         print(f"An error occurred: {e}")
                    #         continue

                    # for seat_id in available_seats:
                    #     try:
                    #         element = WebDriverWait(driver, 5).until(
                    #             EC.element_to_be_clickable((By.ID, seat_id))
                    #         )
                    #         element.click()
                    #         sleep(2)
                    #         # ActionChains(driver).move_to_element(element).click().perform()
                    #         # sleep(3)
                    #         break
                    #     except Exception as e:
                    #         print(f"An error occurred: {e}")
                    #         continue

                    # for xpath in seat_list:
                    #     try:
                    #         element = WebDriverWait(driver, 5).until(
                    #             EC.element_to_be_clickable((By.XPATH, xpath))
                    #         )
                    #         element.click()
                    #         sleep(2)
                    #         ActionChains(driver).move_to_element(element).click().perform()
                    #         sleep(3)
                    #         break
                    #     except Exception as e:
                    #         print(f"An error occurred: {e}")
                    #         continue

                    # Payment Part
                    payment = driver.find_element(By.XPATH,'/html/body/section/div[3]/section[1]/div/div[6]/a[1]')
                    payment.click()
                    sleep(4)

                    proced_to_pay = driver.find_element(By.XPATH,'/html/body/section/div[3]/section[2]/div[3]/div/div[5]/div')
                    proced_to_pay.click()
                    sleep(3)

                    email_field = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[1]/input')

                    email_field.send_keys(email_id)
                    sleep(2)
                    phone_field = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[2]/input')
                    phone_field.send_keys(phone_no)

                    #More Payment Options
                    more_payment_option = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[3]/div[1]/div[9]/div[1]/div[2]')
                    more_payment_option.click()
                    sleep(2)
                    select_upi = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[3]/div[1]/div[9]/div[2]/div/div[2]/ul/li[6]')
                    select_upi.click()
                    sleep(2)
                    upi_id = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[3]/div[1]/div[9]/div[2]/div/div[3]/div[17]/div/aside[5]/label/span[1]/img')
                    upi_id.click()
                    sleep(2)
                    send_upi_id = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[3]/div[1]/div[9]/div[2]/div/div[3]/div[18]/div[1]/div/div[1]/input')
                    send_upi_id.send_keys(phone_no)
                    sleep(1)

                    bank_name = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[3]/div[1]/div[9]/div[2]/div/div[3]/div[18]/div[1]/div/div[3]/input')
                    bank_name.send_keys(Upi_name)
                    sleep(2)

                    click_to_pay = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[3]/div[1]/div[9]/div[2]/div/div[3]/div[18]/button')
                    click_to_pay.click()
                    sleep(2)

                    notification_text = "Your Ticket has been booked proceed to pay from your phone UPI"
                    messages.success(request, notification_text)
                    sleep(2)
                    break

                else:
                    driver.refresh()
                    l.clear()
                    sleep(5)
                    driver = webdriver.Chrome(options=options)
            except:

                driver.quit()
                notification_text = "Something went wrong. Please try again later."
                messages.error(request, notification_text)
                return render(request, 'search_movie.html')

        driver.quit()  # close the browser

    return render(request, 'search_movie.html')









