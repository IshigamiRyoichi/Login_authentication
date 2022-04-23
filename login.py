from selenium import webdriver
import json
import time

def load_json():
    open_json = open('./json/login_data.json')
    session = json.load(open_json)
    return session

def setup():
    chrome_driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    return chrome_driver

def login_amazon(chrome_driver, session):
    chrome_driver.get(session['amazon']['url'])
    chrome_driver.find_element_by_id('ap_email').send_keys(session['amazon']['mail'])
    # time.sleep(0.5)
    chrome_driver.find_element_by_id('continue').click()
    # time.sleep(0.5)
    chrome_driver.find_element_by_id('ap_password').send_keys(session['amazon']['pass'])
    # time.sleep(0.5)
    chrome_driver.find_element_by_id('signInSubmit').click()

def main():
    session = load_json()
    chrome_driver = setup()
    login_amazon(chrome_driver, session)
    time.sleep(1000)


if __name__ == '__main__':
    main()
