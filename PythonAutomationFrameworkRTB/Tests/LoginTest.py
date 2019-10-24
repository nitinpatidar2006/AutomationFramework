'''
Created on Oct 23, 2019

@author: nitin.patidar
'''

from selenium import webdriver
import time
import unittest
from Pages.Login import LoginPage
from Pages.HomePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    
  
  
  @classmethod
  def setUp(cls):
     cls.driver = webdriver.Chrome(executable_path="D:/Learning_again/PythonAutomationFrameworkRTB/Drivers/chromedriver.exe")
     cls.driver.implicitly_wait(10)
     cls.driver.maximize_window()

  

  def test_01_login_valid(self):
     
     driver = self.driver
     driver.get("https://opensource-demo.orangehrmlive.com/")
     login = LoginPage(driver)    
     login.enter_username("Admin")
     login.enter_password("admin123")
     login.click_on_login()
              
     home = HomePage(driver)
     home.click_welcome()
     home.click_on_logout_button()
     
    
  def test_02_login_invalid(self):
     
     driver = self.driver
     driver.get("https://opensource-demo.orangehrmlive.com/")
     login= LoginPage(driver)    
     login.enter_username("Admin1")
     login.enter_password("admin123")
     login.click_on_login()
     message = login.verify_invalid_username_message()
     self.assertEqual(message, "Invalid credentials")
         
  
  def tearDown(self):

      time.sleep(3) 
      self.driver.close()
      self.driver.quit()

if __name__ == '__main__': 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Learning_again/PythonAutomationFrameworkRTB/Reports"))
                  