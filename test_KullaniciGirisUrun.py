from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
import pytest

class Test_KullaniciGirisUrun:
     def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 
     
     def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()
    
     def test_invalid_login(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)  # import time
        try:
         WebDriverWait(self.driver, 10).until(ec.url_to_be("https://www.saucedemo.com/inventory.html"))
         print("Kullanıcı /inventory.html sayfasına yönlendirildi.")
        except:
         print("Yönlendirme başarısız oldu.")
        product_items = self.driver.find_elements(By.XPATH, "//*[@id='inventory_container']/div/div/div/div/div/div[2]")  # Ürünlerin bulunduğu elementlerin listesi
        if len(product_items) == 6:
          print("Ürün sayısı doğru.(6 adet)")
        else:
         print(f"Ürün sayısı doğru değil, beklenen 6 adet, bulunan {len(product_items)} adet.")