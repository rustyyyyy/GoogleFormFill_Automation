import random 
import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
browser = webdriver.Chrome(executable_path='chromedriver', options=option)

browser.get("https://forms.gle/R3F4HtQUhzHqihpt6")

# listno -- total element in list
# option -- random number generated for option
def checkbox(list):
    listno = len(list) -1
    option = random.randint(0,listno)
    checkbox = browser.find_element_by_xpath(list[option])
    checkbox.click()
    print("\nClicked -> " + str(option)+"\n")
    time.sleep(0.15)


# 1
list = [
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[6]/label/div',
]
checkbox(list)

#2
list=[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div',
]
checkbox(list)

#3
list=[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div',
]
checkbox(list)

#4
list=[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div',
]
checkbox(list)

#5
list=[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div',
]
checkbox(list)

#6
list=[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]',
]
checkbox(list)

#7
list=[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div',
]
checkbox(list)

#8
list=[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div',
]
checkbox(list)

#10
list=[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
]
checkbox(list)


#9
list =[
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div',
    '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div',
]
checkbox(list)


button = browser.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span')
button.click()

print("\nExiting...")
time.sleep(5)
browser.quit()