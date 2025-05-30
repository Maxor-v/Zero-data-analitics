import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(5)

divans = driver.find_elements(By.CSS_SELECTOR, 'div.LlPhw')
parsed_data = []

for divan in divans:
    try:
        product_name = divan.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        product_price = divan.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        product_link = divan.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([product_name, product_price, product_link])

driver.quit()

print(parsed_data)

with open("price.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название дивана', 'Цена', 'Ссылка на диван'])
    writer.writerows(parsed_data)