import time
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from Scripts.Listen import Listen




def MsgInstagram():
    PathofDriver = "E:\\Projects\\Logs\\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.instagram.com/")
    time.sleep(5)
    driver.find_element(by=By.NAME, value="username").click()
    pyautogui.write("akun._16")
    time.sleep(1)
    driver.find_element(by=By.NAME, value="password").click()
    pyautogui.write("oXFORD@123")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button").click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div").click()
    time.sleep(5)

def Instagram():
    PathofDriver = "E:\\Projects\\Logs\\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.instagram.com/")
    time.sleep(5)
    driver.find_element(by=By.NAME, value="username").click()
    pyautogui.write("akun._16")
    time.sleep(1)
    driver.find_element(by=By.NAME, value="password").click()
    pyautogui.write("oXFORD@123")
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button").click()
    time.sleep(3)

