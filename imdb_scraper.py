#import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()

driver.get('https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS9zZWFyY2gvdGl0bGUvP3JlZl89bG9naW4ifQ&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20')

#read the input from a file instead of using input()
#imdb_email=input("Enter email: ")
#imdb_password=input("Enter password: ")

driver.find_element(By.ID,'ap_email').send_keys(imdb_email+Keys.ENTER)
driver.find_element(By.ID,'ap_password').send_keys(imdb_password+Keys.ENTER)
