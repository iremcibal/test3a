from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains



class Test_Sauce:
    def initializeDriver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window() #ekranı büyütür
        return driver
    
    def test_invalid_login(self):
        driver = self.initializeDriver()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("1")
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = driver.find_element(By.NAME,"password")
        password.send_keys("1")
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU:  {testResult}")
       
    def test_valid_login(self):
        driver = self.initializeDriver()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        appLogo = driver.find_element(By.CLASS_NAME,"app_logo")
        testResult = appLogo.text == "Swag Labs"
        print(f"TEST SONUCU:  {testResult}")


testClass = Test_Sauce()
testClass.test_valid_login()
testClass.test_invalid_login()