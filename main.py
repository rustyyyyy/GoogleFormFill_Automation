import random 
import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
browser = webdriver.Chrome(executable_path='chromedriver', options=option)

browser.get("https://forms.gle/D34BaAgJYCkFVR8f8")

# listno -- total element in list
# option -- random number generated for option
def checkbox(list):
    listno = len(list) -1
    option = random.randint(0,listno)
    checkbox = browser.find_element_by_xpath(list[option])
    checkbox.click()
    print("\nClicked -> " + str(option)+"\n")
    time.sleep(0.10)


# 1
list = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[1]','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[2]/label' ]
checkbox(list)

# 2
list = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[3]/label',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[4]/label',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[5]/label'
]
checkbox(list)

# 3
list = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[3]',
]
checkbox(list)

# 4 
list = [
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[2]',
]
checkbox(list)

#  5

# 5.1
list = [ '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]',
]
checkbox(list)

# 5.2
list = [
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]',
]
checkbox(list)

# 5.3
list =[
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]',
]
checkbox(list)

# 6
list =[
    '//*[@id="i61"]/div[3]/div',
    '//*[@id="i64"]/div[3]/div',
]
checkbox(list)

# 7
list =[
    '//*[@id="i71"]/div[3]/div',
    '//*[@id="i74"]/div[3]/div',
    '//*[@id="i77"]/div[3]/div',
]
checkbox(list)

# 8
list =[
    '//*[@id="i84"]/div[3]/div',
    '//*[@id="i87"]/div[3]/div',
    '//*[@id="i90"]/div[3]/div',
    '//*[@id="i93"]/div[3]/div',
    '//*[@id="i96"]/div[3]/div',
]
checkbox(list)

# 9
# 9.1
list =[
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div',
]
checkbox(list)

# 9.2
list =[
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div',
]
checkbox(list)

# 9.3
list =[
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div',
]
checkbox(list)

# 9.4
list =[
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div',
]
checkbox(list)

# 10
list =[
    '//*[@id="i107"]/div[3]/div',
    '//*[@id="i110"]/div[3]/div',
    '//*[@id="i113"]/div[3]/div',
    '//*[@id="i116"]/div[3]/div',
]
checkbox(list)

button = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
button.click()

print("\nExiting...")
time.sleep(5)
browser.quit()