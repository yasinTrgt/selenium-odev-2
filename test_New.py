from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
import pytest

class Test_New:
    #prefix => test_ 
    def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 

    def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("problem_user","secret_sauce"),("visual_user","secret_sauce")])
    def test_invalid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        addToCart = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCart.click()
        shoppingCart = self.driver.find_element(By.ID,"shopping_cart_container")
        shoppingCart.click()
        checkout = self.driver.find_element(By.ID,"checkout")
        checkout.click()
        sleep(3)

