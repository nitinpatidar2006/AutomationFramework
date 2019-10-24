'''
Created on Oct 23, 2019

@author: nitin.patidar
'''
from selenium import webdriver
from Locators.Locators import Locators

class HomePage():
  
  def __init__(self, driver):
      self.driver = driver
      
      
  def click_welcome(self):
      self.driver.find_element_by_id(Locators.welcome_id).click()
          
  def click_on_logout_button(self):
      self.driver.find_element_by_link_text(Locators.logout_button).click()
          

  
      
      
       