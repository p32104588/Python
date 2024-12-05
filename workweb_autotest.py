import pathlib
from selenium import webdriver #從selenium中用到webdriver
from selenium.webdriver.chrome.service import Service #以前不用，但Chorm已經driver位置參數更新為Service後就需要
from selenium.webdriver.chrome.options import Options #用來設定options用的
from selenium.webdriver.common.keys import Keys #通用用途，可讓開啟的網頁進行enter動作
from selenium.webdriver.common.by import By #通用用途，增加BY，使用於find_element
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time #可直接設定等待幾秒後再繼續
import os
import datetime

def getimg():
    # 檢查資料夾是否存在
    if not os.path.isdir(os.path.basename(__file__).replace('.py','') + "_" + str(datetime.date.today())): #islink,isdir,os.path.exists
        os.makedirs(os.path.basename(__file__).replace('.py','') + "_" + str(datetime.date.today()))

     # 檢查檔案是否存在
    i = 0
    while os.path.isfile(os.path.basename(__file__).replace('.py','') + "_" + str(datetime.date.today()) + "\\" + str(i) + ".png"):
        i = i + 1
    else:
        Browser.get_screenshot_as_file(os.path.basename(__file__).replace('.py','') + "_" + str(datetime.date.today()) + "\\" + str(i) + ".png")

Browser_options = webdriver.ChromeOptions() #本例用的是chrome
Browser_options.add_experimental_option("detach",True)
Browser_options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯
Browser_options.add_argument('--log-level=3') #不知原因，但用了減少連結到系統的某個裝置失去作用及handshake failed問題

driverpath=Service("D:\chromedriver.exe")
Browser = webdriver.Chrome(options=Browser_options,service=driverpath) #已無chrome_options，更新為options
Browser.maximize_window()
Browser.get("http://xxxx.xxxx.xxx.xx/Login.aspx")

searchtext=Browser.find_element(By.ID,"txtID")
searchtext.clear()
searchtext.send_keys("999999")

searchtext=Browser.find_element(By.ID,"txtPwd")
searchtext.clear()
searchtext.send_keys("1")

Login = Browser.find_element(By.ID,"ibtnLogin")
Login.click()

# 判斷彈窗結果 
Loginalert = EC.alert_is_present()(Browser)
if Loginalert:
    Loginalert.accept()


date = Browser.find_element(By.XPATH,"//*[@id='MnuMainn0']/table/tbody/tr/td/a")
hov = ActionChains(Browser).move_to_element(date).perform()

result = Browser.find_element(By.XPATH,"//*[@id='MnuMainn0Items']/table/tbody/tr/td/table/tbody/tr/td/a")

Browser.execute_script("window.open('http://xxxx.xxxx.xxx.xx/" + result.get_attribute('href').replace("javascript:GoPage('","").replace("');","") + "');")
Browser.switch_to.window(Browser.window_handles[1])
getimg()

textbox=Browser.find_element(By.ID,"ctl00_ContentPlaceHolder1_txtGroupID")
textbox.clear()
textbox.send_keys("0040880001")

checkbutton = Browser.find_element(By.NAME,"ctl00$ContentPlaceHolder1$btnSearch")
checkbutton.click()

checkbuttonalert = EC.alert_is_present()(Browser)
if checkbuttonalert:
    checkbuttonalert.accept()
getimg()

checkbutton1 = Browser.find_element(By.ID,"ctl00_ContentPlaceHolder1_lbManualCheck")
checkbutton1.click()
checkbutton1alert = EC.alert_is_present()(Browser)
if checkbutton1alert:
    checkbutton1alert.accept()
getimg()

checkbutton2 = Browser.find_element(By.ID,"ctl00_ContentPlaceHolder1_lblAutoCheckCondition")
checkbutton2.click()
checkbutton2alert = EC.alert_is_present()(Browser)
if checkbutton2alert:
    checkbutton2alert.accept()
getimg()

checkbutton3 = Browser.find_element(By.ID,"ctl00_ContentPlaceHolder1_lnkAutoCheck_Group")
checkbutton3.click()
checkbutton3alert = EC.alert_is_present()(Browser)
if checkbutton3alert:
    checkbutton3alert.accept()
getimg()

time.sleep(2)
Browser.close()

Browser.switch_to.window(Browser.window_handles[0])

time.sleep(2)

#登出並關閉瀏覽器
Logout = Browser.find_element(By.ID,"ibtnLogout")
Logout.click() 

Logoutalert = EC.alert_is_present()(Browser)
if Logoutalert:
    Logoutalert.accept()


Browser.quit()





# time.sleep(2)

#檔案位置
# print(pathlib.Path(__file__).parent.absolute())

# 檢查檔案是否存在
# if os.path.isfile(date.today() + '.png'): #islink,isdir,os.path.exists
#   print("檔案存在。")
# else:
#   print("檔案不存在。")

# DIR = 'C:\\Users\\Wistronits\\Desktop\\PPP'
# print (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])) #資料夾內檔案數量

# time.sleep(5)
# Browser.quit()

# hovv = ActionChains(Browser).move_to_element(date).perform()


# data = driver.find_element_by_xpath('//*[@id="MnuMainn2"]/table[0]/table/tbody/tr[2]/td[4]')
# searchorgddl=Browser.find_element(By.ID,"org")
# orgddlselect = Select(searchorgddl)
# orgddlselect.select_by_value("13")


# cbtype2 = Browser.find_element(By.ID,"type2")
# cbtype2.click()


# searchtext=Browser.find_element(By.ID,"text")
# searchtext.clear()
# searchtext.send_keys("詐欺")


# # 1: 使用關鍵字 __file__
# print('__file__: '+ __file__)
# # 2: 如果你想省略可能存在的目錄部分，你可以使用 os.path.basename(__file__)
# print('Filename: '+ os.path.basename(__file__))
# # 3: 使用參數關鍵字 sys.argv  
# print('sys.argv[0]: '+ sys.argv[0])

# 輸出如下:
# __file__: workspace\tmp\IamTest.py
# Filename: IamTest.py
# sys.argv[0]: workspace\tmp\IamTest.py

