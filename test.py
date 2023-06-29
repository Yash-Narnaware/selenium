import os
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

delay = 2

os.environ['PATH'] += r"C:/Users/YASH/Desktop/selenium/seleniumDriver"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 60)


def magic(l=0, i=1, j=1, k=1, go_to_main_page=True):
    global selected_vil_label, selected_dis_label, selected_taluka_label

    # current_district_index, current_taluka_index, current_village_index = 1

    for current_div_index in range(l, 5):

        if go_to_main_page:
            driver.get("https://bhulekh.mahabhumi.gov.in/")

            division = driver.find_element(By.XPATH,
                                           "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/p[2]/select[1]")
            division1 = Select(division)
            division1.select_by_index(current_div_index)

            selected_div = division1.first_selected_option
            selected_div_label = selected_div.get_attribute("label")

            time.sleep(delay)

            go = driver.find_element(By.XPATH,
                                     "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/p[2]/input[1]")
            go.click()

            driver.switch_to.window(driver.window_handles[-1])
        # time.sleep(15)

        ###################################################################################################################################

        district = wait.until(EC.presence_of_element_located((By.XPATH,
                                                              "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/select[1]")))
        district1 = Select(district)

        number_of_districts = len(district1.options)

        for current_district_index in range(i, number_of_districts):
            try:
                district1.select_by_index(current_district_index)

                selected_dis = district1.first_selected_option
                selected_dis_label = selected_dis.get_attribute("label")

                time.sleep(delay)
            except TimeoutException:

                driver.refresh()
                go_to_main_page = False
                magic(current_div_index, current_district_index, current_taluka_index, current_village_index, False)

            taluka = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/select[1]")))
            taluka1 = Select(taluka)

            number_of_taluka = len(taluka1.options)

            for current_taluka_index in range(j, number_of_taluka):
                try:
                    taluka1.select_by_index(current_taluka_index)
                    selected_taluka = taluka1.first_selected_option

                    selected_taluka_label = selected_taluka.get_attribute("label")
                    # print(selected_label)

                    time.sleep(delay)

                except TimeoutException:

                    driver.refresh()
                    magic(current_div_index, current_district_index, current_taluka_index, current_village_index, False)

                village = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/select[1]")))
                village1 = Select(village)

                number_of_village = len(village1.options)

                for current_village_index in range(k, number_of_village):
                    try:
                        village1.select_by_index(current_village_index)

                        selected_vil = village1.first_selected_option
                        selected_vil_label = selected_vil.get_attribute("label")

                    except TimeoutException:

                        driver.refresh()
                        magic(current_div_index, current_district_index, current_taluka_index, current_village_index,
                              False)

                    search = driver.find_element(By.XPATH,
                                                 "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]")
                    # search = wait.until(EC.presence_of_element_located((By.XPATH,
                    #                    "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]")))
                    search.click()

                    input_surname = driver.find_element(By.XPATH,
                                                        "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[1]/input[2]")
                    input_surname.send_keys("narnaware")

                    search_button = driver.find_element(By.XPATH,
                                                        "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
                    search_button.click()

                    try:
                        alert = EC.alert_is_present()
                        ep = EC.presence_of_element_located((By.XPATH,
                                                             "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]/table[1]/tbody[1]/tr[3]/td[1]/select[4]"))
                        alert_or_ep = wait.until(EC.alert_is_present() if EC.alert_is_present() else ep)

                        if alert_or_ep == alert:

                            alert.accept()
                        else:

                            results = driver.find_element(By.XPATH,
                                                          "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]/table[1]/tbody[1]/tr[3]/td[1]/select[4]")
                            result1 = Select(results)
                            options = result1.options

                            temp = str(selected_div_label) + " " + str(selected_dis_label) + " " + str(
                                selected_taluka_label) + " " + str(selected_vil_label) + " #### "
                            for option in options:
                                temp += str(option.text).split("(", 1)[0] + "***"
                            temp += "\n"

                            fp = open('result.txt', 'a', encoding="utf-8")
                            fp.write(temp)
                            fp.close()

                    except TimeoutException:
                        driver.refresh()
                        magic(current_div_index, current_district_index, current_taluka_index, current_village_index,
                              False)

                    # except TimeoutException:
                    #
                    #     driver.refresh()
                    #     magic(current_div_index, current_district_index, current_taluka_index,current_village_index, False)

        magic(current_div_index + 1, 1, 1, 1, True)


magic()
