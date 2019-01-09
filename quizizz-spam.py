#!/usr/bin/env python3
from selenium import webdriver
import time, json, sys, random, string, requests 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
#----------------------------CODE----------------------------------#
def check(pin,name,bot):
  #Check inputs for errors
  errCount=0
  if len(str(pin))!=6:
    print(err)
    print("Invalid Game Pin")
    errCount=errCount+1
  if bot<1 or bot>20:
    print(err)
    print("Number of bots incorrect")
    print("Can't be >1 or <20")
    errCount=errCount+1
  if name<1 or name>2:
    print(err)
    print("Usrname Var incorrect")
    print("Can't be >1 or <2")
    errCount=errCount+1
  if errCount!=0:
    print(str(errCount)+" Error(s)")
  else:
    while bot<0:
      play(pin)
      bot=bot-1
def play(pin):
  usrname=''.join(random.sample(char_set*6, 10))
  #start the bot
  driver = webdriver.Chrome()
  driver.get("https://quizizz.com/join/")
  print("+---Starting Bot---+")
  waitForItem(driver,'.check-room-input')
  driver.find_element_by_css_selector('.check-room-input').send_keys(pin)
  driver.find_element_by_css_selector('.proceed-button').click()
  waitForItem(driver,'.check-player-input')
  driver.find_element_by_css_selector('.check-player-input').send_keys(usrname)
  driver.find_element_by_css_selector('.proceed-button').click()
  time.sleep(4)
  driver.find_element_by_css_selector('.skip-btn').click()
  time.sleep(1)
  driver.find_element_by_css_selector('.game-start-btn').click()
if __name__ == '__main__':
  char_set = string.ascii_uppercase + string.digits
  err="+---ERROR---+"
  check(input("Game PIN >>> "), input("Names 1=rand, 2=real >>> "),input("# of Bots >>>"))
