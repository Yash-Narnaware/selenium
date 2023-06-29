import os
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


delay = 10

os.environ['PATH'] += r"C:/Users/YASH/Desktop/selenium/seleniumDriver"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://bhulekh.mahabhumi.gov.in/")

division = driver.find_element(By.XPATH, "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/p[2]/select[1]")
division1 = Select(division)
division1.select_by_index(0)

selected_div = division1.first_selected_option
selected_div_label = selected_div.get_attribute("label")

time.sleep(delay)
go = driver.find_element(By.XPATH,
                         "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/p[2]/input[1]")
go.click()

# wait = WebDriverWait(driver, 20)
# wait.until(EC.title_contains("bhulekh.mahabhumi.gov.in/Konkan/Home.aspx"))
driver.switch_to.window(driver.window_handles[-1])
time.sleep(15)

district = driver.find_element(By.XPATH,
                               "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/select[1]")
# district = driver.find_element(By.CSS_SELECTOR, "#distSelect")
district1 = Select(district)
district1.select_by_index(5)

selected_dis = district1.first_selected_option
selected_dis_label = selected_dis.get_attribute("label")

time.sleep(delay)

taluka = driver.find_element(By.XPATH,
                             "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/select[1]")
# taluka = wait.until(EC.visibility_of_element_located((By.XPATH, "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/select[1]")))
taluka1 = Select(taluka)
taluka1.select_by_index(3)

selected_taluka = taluka1.first_selected_option

selected_taluka_label = selected_taluka.get_attribute("label")
#print(selected_label)

time.sleep(delay)

village = driver.find_element(By.XPATH,
                              "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/select[1]")
village1 = Select(village)
village1.select_by_index(107)

selected_vil = village1.first_selected_option
selected_vil_label = selected_vil.get_attribute("label")

time.sleep(delay)

search = driver.find_element(By.XPATH,
                             "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]")
search.click()

input_surname = driver.find_element(By.XPATH,
                                    "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[1]/input[2]")
input_surname.send_keys("vitthal")

search_button = driver.find_element(By.XPATH,
                                    "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
search_button.click()

# alert = wait.until(EC.alert_is_present())

try:
    alert = wait.until(EC.alert_is_present())
    # Switch to the alert and perform actions
    alert.accept()
except TimeoutException:
    results = driver.find_element(By.XPATH,
                                  "//body[1]/form[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]/table[1]/tbody[1]/tr[3]/td[1]/select[4]")
    result1 = Select(results)
    options = result1.options

    temp = str(selected_div_label) + " " + str(selected_dis_label) + " " + str(selected_taluka_label) + " " + str(selected_vil_label) + " "
    for option in options:
        temp += str(option.text) + " "
    temp += "\n"
    print(temp)

    fp = open('result.txt', 'a', encoding="utf-8")
    fp.write(temp)
    fp.close()

time.sleep(10)
