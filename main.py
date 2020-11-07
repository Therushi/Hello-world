import datetime
from selenium import webdriver
import schedule
import time
import join
import info


driver = webdriver.Chrome()
driver.get('https:www.google.com')

signIn = driver.find_element_by_xpath('//*[@id="gb_70"]')
signIn.click()

#input Email
emailField = driver.find_element_by_xpath('//*[@id="identifierId"]')
emailField.send_keys("")#enter your domain emailid that have classroom access
emailField = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()

driver.implicitly_wait(10)

passwordFieldPass = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
passwordFieldPass.send_keys("")# Enter Your Password (Do not share with anyone)
passwordFieldPass = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

driver.implicitly_wait(10)

#search classroom
classRoom = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("https://classroom.google.com/")
driver.implicitly_wait(10)

#button
button = driver.find_element_by_name("btnK").click()
driver.implicitly_wait(10)

#googleClassroom = driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div[1]/a/h3/div/span').click()
driver.get("https://classroom.google.com/")
driver.implicitly_wait(15)

#check timing
e = datetime.datetime.now()

day = (e.strftime("%a"))
print(day)

if day=="Mon":
    monday()
elif day=="Tue":
    tuesday() 
elif day=="Wed":
    wednesday()
elif day=="Thu":
    thursday()
elif day=="Fri":
    friday()
elif day=="Sat":
    saturday()
else:
    print("Its sunday bro")

#timeTable.py combined 

def monday():
    schedule.every().monday.at(firstClass).do(joinCs)
    schedule.every().monday.at(secondClass).do(joinMe)
    schedule.every().monday.at(thirdClass).do(joinOc)
    schedule.every().monday.at(fourthClass).do(joinMcom)
    
def tuesday():
    schedule.every().tuesday.at(firstClass).do(joinBda)
    schedule.every().tuesday.at(secondClass).do(joinMcom)
    schedule.every().tuesday.at(thirdClass).do(joinMe)
    schedule.every().tuesday.at(fourthClass).do(joinBdaLab)

def wednesday():
    schedule.every().wednesday.at(firstClass).do(joinCs)
    schedule.every().wednesday.at(secondClass).do(joinMe)
    schedule.every().wednesday.at(thirdClass).do(joinMcom)
    schedule.every().wednesday.at(fourthClass).do(joinOc)

def thursday():
    schedule.every().thursday.at(firstClass).do(joinMcom)
    schedule.every().thursday.at(secondClass).do(joinBda)
    schedule.every().thursday.at(thirdClass).do(joinOc)
    schedule.every().thursday.at(fourthClass).do(joinMeLab)

def friday():
    schedule.every().friday.at(firstClass).do(joinOc)
    schedule.every().friday.at(secondClass).do(joinCs)
    schedule.every().friday.at(thirdClass).do(joinBda)

def dummy():
    schedule.every().saturday.at(dummyClass).do(joindummy)

while True:
    schedule.run_pending()
    time.sleep(5)#seconds
