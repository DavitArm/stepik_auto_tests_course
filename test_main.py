from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def test_registration_page_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    input3.send_keys("Smolensk")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == welcome_text_elt.text, "Поздравляем! Вы успешно зарегистировались!"


def test_registration_page_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    input3.send_keys("Smolensk")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == welcome_text_elt.text, "Поздравляем! Вы успешно зарегистировались!"


if __name__ == '__main__':
    pytest.main()
