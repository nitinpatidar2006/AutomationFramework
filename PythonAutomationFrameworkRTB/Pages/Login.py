'''
Created on Oct 23, 2019

@author: nitin.patidar
'''
from selenium import webdriver
from Locators.Locators import Locators

class LoginPage():
    
  def __init__(self, driver):
     self.driver = driver
        
  def enter_username(self, username):
      self.driver.find_element_by_id(Locators.username_id).clear()
      self.driver.find_element_by_id(Locators.username_id).send_keys(username)
  
  def enter_password(self, password):
      self.driver.find_element_by_id(Locators.password_id).clear()
      self.driver.find_element_by_id(Locators.password_id).send_keys(password)
    
  def click_on_login(self):
      self.driver.find_element_by_id(Locators.loginbutton_id).click()
      
  def verify_invalid_username_message(self):      
      msg = self.driver.find_element_by_xpath(Locators.invalid_error_message).text
      return msg
      
       

    
    
