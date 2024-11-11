from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

def stock_data_finder(ticker):
    try:
        driver = webdriver.Chrome()
        driver.get(f"https://www.5paisa.com/stocks/{ticker}-share-price")

        url = f"https://www.5paisa.com/stocks/{ticker}-share-price.html"

        driver.implicitly_wait(20)
        
        open = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/main/div/section[1]/div/section/div/div/div[1]/div[1]/div[7]/div/div[3]/ul/li[1]/strong").text
        prev_close = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/main/div/section[1]/div/section/div/div/div[1]/div[1]/div[7]/div/div[3]/ul/li[2]/strong").text
        current_stock_price = driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/section[1]/div/section/div/div/div[1]/div[1]/div[7]/div/div[1]/div/div/div").text
        current_stock_price = str(current_stock_price.encode("utf-8"))
        current_stock_price = current_stock_price[14:-1]

        open = float(open.replace(",",""))
        prev_close = float(prev_close.replace(",",""))
        current_stock_price = float(current_stock_price.replace(",",""))
        driver.implicitly_wait(20)

        if type(open) == None or type(prev_close) == None or type(current_stock_price) == None:
            open = 0
            prev_close = 0
            current_stock_price = 0
            return open, prev_close, current_stock_price
        else:
            return open, prev_close, current_stock_price
    except NoSuchElementException:
        open = 0
        prev_close = 0
        current_stock_price = 0
        return open, prev_close, current_stock_price
