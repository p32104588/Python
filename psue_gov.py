from selenium import webdriver #從selenium中用到webdriver
from selenium.webdriver.chrome.service import Service #以前不用，但Chorm已經driver位置參數更新為Service後就需要
from selenium.webdriver.chrome.options import Options #用來設定options用的
from selenium.webdriver.common.keys import Keys #通用用途，可讓開啟的網頁進行enter動作
from selenium.webdriver.common.by import By #通用用途，增加BY，使用於find_element
from selenium.webdriver.support.select import Select
import time #可直接設定等待幾秒後再繼續

Browser_options = Options() #本例用的是chrome
Browser_options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯
Browser_options.add_argument('--log-level=3') #不知原因，但用了減少連結到系統的某個裝置失去作用及handshake failed問題

driverpath=Service("D:\chromedriver.exe")
Browser = webdriver.Chrome(options=Browser_options,service=driverpath) #已無chrome_options，更新為options
Browser.maximize_window()
Browser.get("https://psue.moj.gov.tw/psiqs/index.jsp")

#選擇台北地方檢察署
#要怎麼清除原選擇項呢？
searchorgddl=Browser.find_element(By.ID,"org")
orgddlselect = Select(searchorgddl)
orgddlselect.select_by_value("13")

#偵結日期1100131~1101231
#偵結年起
searchfy1ddl=Browser.find_element(By.ID,"fy1")
fy1ddlselect = Select(searchfy1ddl)
fy1ddlselect.select_by_value("110")
#偵結月起
searchfm1ddl=Browser.find_element(By.ID,"fm1")
fm1ddlselect = Select(searchfm1ddl)
fm1ddlselect.select_by_value("1")
#偵結日起
searchfd1ddl=Browser.find_element(By.ID,"fd1")
fd1ddlselect = Select(searchfd1ddl)
fd1ddlselect.select_by_value("31")

#偵結年起
searchfy2ddl=Browser.find_element(By.ID,"fy2")
fy2ddlselect = Select(searchfy2ddl)
fy2ddlselect.select_by_value("110")
#偵結月起
searchfm2ddl=Browser.find_element(By.ID,"fm2")
fm2ddlselect = Select(searchfm2ddl)
fm2ddlselect.select_by_value("12")
#偵結日起
searchfd2ddl=Browser.find_element(By.ID,"fd2")
fd2ddlselect = Select(searchfd2ddl)
fd2ddlselect.select_by_value("31")

#類別:勾選起訴書 追加起訴書 申請簡易判決書
#起訴書
cbtype1 = Browser.find_element(By.ID,"type1")
cbtype1.click()
#追加起訴書
cbtype1a = Browser.find_element(By.ID,"type1a")
cbtype1a.click()
#申請簡易判決書
cbtype2 = Browser.find_element(By.ID,"type2")
cbtype2.click()

#全文檢索:詐欺
searchtext=Browser.find_element(By.ID,"text")
searchtext.clear()
searchtext.send_keys("詐欺")



#time.sleep(5)
#Browser.quit()