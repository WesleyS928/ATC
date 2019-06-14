'''footlocker script'''
#Wes Smith
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()
driver.get("https://kith.com/collections/kith-x-tommy-hilfiger-ss19/products/kith-x-tommy-hilfiger-satin-boxing-short-red")
time.sleep(7)
#dismiss subscription request
driver.find_element_by_xpath('//*[@id="kith-x-tommy-hilfiger-satin-boxing-short-red"]/div[6]/div/div/div/button/img').click()
time.sleep(3)
#size
driver.find_element_by_xpath('//*[@id="shopify-section-product--kith"]/section[1]/div[4]/form/div[1]/div[2]/label').click()
time.sleep(3)
#atc
driver.find_element_by_name('add').click()
time.sleep(3)
#checkout button
driver.find_element_by_xpath('//*[@id="CartContainer"]/form/div[3]/button').click()
#email input
time.sleep(1)
driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys('john@john.com')
#time.sleep()
#input 1st name
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('john')
time.sleep(1)

#input last name
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys('john')
#time.sleep()

#input address
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('john drive')
#time.sleep()

#input city
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('johnson city')
#time.sleep(1)
#input zip
#time.sleep(1)
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('73130')
#inout phone num
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('1234567890')
#cont to ship metho button
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button').click()
#cont to payment method
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button').click()
#CC numb
time.sleep(7)
driver.find_element_by_xpath('//*[@id="number"]').send_keys('123')
