from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import getpass
from random import randint
from pyvirtualdisplay import Display

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print('Starting driver. . .')
        self.driver = webdriver.Firefox(executable_path = r'/home/domene/Downloads/geckodriver')
    
    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        print('Loading. . .')
        time.sleep(3)
        print('Done rendering')
        #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #time.sleep(2)
        elem = driver.find_element(By.XPATH, '//a[@href="/accounts/login/?source=auth_switcher"]')
        elem.click()
        time.sleep(3)
        user = driver.find_element(By.NAME, 'username')
        user.clear()
        user.send_keys(self.username)
        pass_in = driver.find_element(By.NAME, 'password')
        pass_in.clear()
        pass_in.send_keys(self.password)
        btn_login = driver.find_element(By.XPATH, '//button[contains(text(), "Log in")]')
        btn_login.click()
    
    def close_notf(self):
        driver = self.driver
        #notification = driver.find_element_by_class_name('mt3GC')
        btn_notification = driver.find_element(By.XPATH,'//button[contains(text(), "Not Now")]')
        btn_notification.click()

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)
        for i in range(1,randint(1,10)):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(randint(1,5))
        #search pic
        hrefs = driver.find_element(By.XPATH, '//a')
        # ERRO AQUI pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' n# fotos: ' + str(len(pic_hrefs)))
        

user = input('Username: ')
pasw = getpass.getpass('Password: ')
Usuario = InstaBot(user, pasw)
Usuario.login()
time.sleep(8)
Usuario.close_notf()

hashtag = input('Digite a hashtag: #')
Usuario.like_photo(hashtag)
