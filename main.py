from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
  
usr=input('Enter Email Id:')  
pwd=input('Enter Password:')  
  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://twitter.com/') 
print ("Opened facebook") 
sleep(1) 
  
username_box = driver.find_element_by_css_selector("#react-root > div > div > div > main > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-1d2f490.r-7v430y.r-1j3t67a.r-u8s1d.r-1s7wq8y.r-13qz1uu > div > form > div > div:nth-child(6) > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input")
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_css_selector("#react-root > div > div > div > main > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-1d2f490.r-7v430y.r-1j3t67a.r-u8s1d.r-1s7wq8y.r-13qz1uu > div > form > div > div:nth-child(7) > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input")
password_box.send_keys(pwd) 
print ("Password entered") 
login_box = driver.find_element_by_css_selector("#react-root > div > div > div > main > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-1d2f490.r-7v430y.r-1j3t67a.r-u8s1d.r-1s7wq8y.r-13qz1uu > div > form > div > div.css-1dbjc4n.r-eqz5dr.r-1777fci > div > div") 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 