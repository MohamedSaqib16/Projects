import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def anime_search(anime_search):

    PathofDriver = "E:\\Projects\\Logs\\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    search_query = anime_search

    search_url = f'https://zoro.to/search?keyword={search_query.replace(" ", "+")}'

    driver.get(search_url)

    time.sleep(5)

    try:
        search_result = driver.find_element(by=By.CSS_SELECTOR,value='.items.col-sm-4.col-xs-6')

        link = search_result.find_element(by=By.CSS_SELECTOR,value='a').get_attribute('href')

        driver.get(link)

        time.sleep(500)

    except Exception as e:
        print(e)

anime_search("My star")