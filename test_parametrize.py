import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


links = ['https://stepik.org/lesson/236895/step/1','https://stepik.org/lesson/236896/step/1','https://stepik.org/lesson/236897/step/1','https://stepik.org/lesson/236898/step/1','https://stepik.org/lesson/236899/step/1','https://stepik.org/lesson/236903/step/1','https://stepik.org/lesson/236904/step/1','https://stepik.org/lesson/236905/step/1']

@pytest.mark.parametrize('link', links)
def test_login_stepik(browser,link):
    browser.get(link)
    WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, "//a[@id = 'ember33']"))).click()
    login = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, "//input[@name= 'login']")))
    login.click()
    login.send_keys('david-aleksanyan@mail.ru')
    password = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, "//input[@name= 'password']")))
    password.click()
    password.send_keys('R9d9armenia')
    time.sleep(5)
    WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.XPATH, "//button[@type= 'submit']"))).click()
    answer = math.log(int(time.time()))
    print(answer)
    time.sleep(5)
    placeholder = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, '//textarea')))
    placeholder.click()
    placeholder.send_keys(answer)
    WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.XPATH, '//button[@class="submit-submission"]'))).click()
    correct_text = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, '//p[@class="smart-hints__hint"]'))).text
    browser.implicitly_wait(10)
    assert correct_text == "Correct!"