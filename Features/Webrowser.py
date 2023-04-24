from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Scripts.Listen import Listen
import time

def YoutubeSearch(SearchQuery):

    SearchQuery = Listen().lower()
    # Specify the search keyword
    search_keyword = SearchQuery

    # Set up the webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")

    # Find the search box and enter the search keyword
    search_box = driver.find_element(by=By.NAME,value="search_query")
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

    # Find the first video element and click on it
    video = driver.find_element(by=By.XPATH,value='//*[@id="contents"]/ytd-video-renderer[1]')
    video.click()


    time.sleep(10)
