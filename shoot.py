from selenium import webdriver 
import time
from PIL import Image 
import datetime
now = datetime.datetime.now()

browser = webdriver.Chrome() 
browser.get('http://localhost:1880/ui/') 
time.sleep(1) 
browser.save_screenshot("/home/epiphany/node-red-project/img/"+now.strftime("%Y-%m-%d %H:%M:%S")+"_dashboard.png") 
fullImg = Image.open("/home/epiphany/node-red-project/img/"+now.strftime("%Y-%m-%d %H:%M:%S")+"_dashboard.png") 

browser.quit()  