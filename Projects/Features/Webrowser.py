from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Scripts.Listen import Listen
import time
import json


def YoutubeSearch(SearchQuery):
    try:
        search_keyword = SearchQuery

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.youtube.com")

        search_box = driver.find_element(by=By.NAME, value="search_query")
        search_box.send_keys(search_keyword)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

        video = driver.find_element(by=By.XPATH, value='//*[@id="contents"]/ytd-video-renderer[1]')
        video.click()

    except Exception as e:
        print(f"An error occurred: {e}")

def google_search(google_search):
    try:
        search_keyword = google_search
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.google.com/")

        search_box = driver.find_element(by=By.NAME,value="q")
        search_box.send_keys(search_keyword)
        search_box.send_keys(Keys.RETURN)

        search_results = driver.find_element(by=By.CSS_SELECTOR,value="div.g")

        for result in search_results[:5]:
            title = result.find_element(by=By.CSS_SELECTOR,value="h3").text
            url = result.find_element(by=By.CSS_SELECTOR,value="a").get_attribute("href")
            print(f"{title}: {url}")

    except Exception as e:
                print(f"An error occurred: {e}")

def anime_search(anime_search):

    PathofDriver = "E:\\Projects\\Logs\\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    search_query = anime_search
    search_url = f'https://zoro.to/search?keyword={search_query.replace(" ", "+")}'
    driver.get(search_url)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(5)
    try:
        search_result = driver.find_element(by=By.CSS_SELECTOR,value='.items.col-sm-4.col-xs-6')
        link = search_result.find_element(by=By.CSS_SELECTOR,value='a').get_attribute('href')
        driver.get(link)
        time.sleep(500)
    except Exception as e:
        print(f"An error occurred: {e}")

