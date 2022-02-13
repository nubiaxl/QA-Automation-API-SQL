from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "http://demo.guru99.com/test/newtours/"
expectedTitle = "Welcome: Mercury Tours"
actualTitle = ""

driver = webdriver.Firefox()

# launch Fire fox and direct it to the Base URL
driver.get(url)

# get the actual value of the title
actualTitle = driver.title

        
# * compare the actual title of the page with the expected one and print
# * the result as "Passed" or "Failed"
         
if actualTitle == expectedTitle:
    print("Test Passed!")
else:
    print("Test Failed")

       
# Go to the Registration Page

# find_element_by_* commands are deprecated. Please use find_element() instead        
RegisterLink = driver.find_element_by_xpath("//td[@class='mouseOut']/a[@href='register.php']")
RegisterLink.click()
       
expectedTitle = "Register: Mercury Tours"
# get the actual value of the title
actualTitle = driver.title


# compare the actual title of the page with the expected one and print
# the result as "Passed" or "Failed"

if actualTitle == expectedTitle:
    print("Test Passed!")
else:
    print("Test Failed")

        
firstName = driver.find_element_by_name("firstName") 
lastName = driver.find_element_by_name("lastName")
phone = driver.find_element_by_name("phone")
email = driver.find_element_by_id("userName")
address1 = driver.find_element_by_name("address1")
city = driver.find_element_by_name("city")
state = driver.find_element_by_name("state")
postalCode = driver.find_element_by_name("postalCode")

from selenium.webdriver.support.select import Select
country = driver.find_element_by_name("country")
username = driver.find_element_by_id("email")
password = driver.find_element_by_name("password")
confirmPassword = driver.find_element_by_name("confirmPassword")
submit = driver.find_element_by_name("submit") 
       
       
firstName.click()
firstName.send_keys("Nubila")
lastName.click()
lastName.send_keys("Levon")
phone.click()
phone.send_keys("999659876")
email.click()
email.send_keys("nubila.levon@outlook.com")
address1.click()
address1.send_keys("222 Pine Road")
city.click()
city.send_keys("Phoenix")
state.click()
state.send_keys("Arizona")
postalCode.click()
postalCode.send_keys("85004")
       
sel = Select(country)       
sel.select_by_value("UNITED STATES")
username.click()
username.send_keys("nubi1234")
password.click()
password.send_keys("1234")
confirmPassword.click()
confirmPassword.send_keys("1234")

thankyou = driver.find_element_by_xpath("//*[contains(text(), 'Thank you for registering')]")
if thankyou.is_displayed():
    print("Test Passed!")
else:
    print("Test Failed")
   
    	   
       
       
# close Firefox
driver.quit();
