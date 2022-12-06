from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

# import time
import datetime

# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

# отключение контроля автоматизации
# options.add_argument("--disable-blink-features=AutomationControlled")

# запуск браузера в фоновом режиме
# options.add_argument("--headless")   # или   # options.headless = True

driver = webdriver.Chrome(executable_path=r"/chromedriver", options=options)
# url = "https://www.avito.ru/yaroslavl/avtomobili/mitsubishi/l200/iv-ASgBAgICA0Tgtg3ymCjitg3mqCjqtg3W2Sg?cd=1&localPriority=1&radius=75"
url = "https://www.avito.ru/yaroslavl/avtomobili?cd=1&f=ASgBAQECBESeEqC4AuC2Df6YKOK2DZ61KOq2DZ7gKAFA8LYNFOy3KAJF~AIXeyJmcm9tIjoyODQ0LCJ0byI6bnVsbH2MFBh7ImZyb20iOjE0NzY2LCJ0byI6bnVsbH0&radius=0"
try:
    start_time = datetime.datetime.now()
    driver.get(url=url)
    print(f"Список объявление: {driver.current_url}")
    item = driver.find_elements("xpath", "//div[@data-marker='item-photo']")
    print(f"Всего объявлений {len(item)} шт.")
    driver.implicitly_wait(2)

    for i in range(len(item)):
    # for i in range(2):
        item[i].click()
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(2)
        print("#" * 20)
        title_ad = driver.find_element("class name", "style-title-info-main-_sKj0").text
        print(title_ad)
        prace_ad = driver.find_element("class name", "style-item-price-text-_w822").text
        print(f'Цена: {prace_ad}')
        adress = driver.find_element("class name", "style-item-address-KooqC")
        print(f"Местоположение: {adress.text}")
        print("=" * 20)
        username = driver.find_element("class name", "js-seller-info-name")
        print(f"Ссылка объявления: {driver.current_url}")
        print(f"Продавец: {username.text}")
        print("=" * 20)
        params = driver.find_element("class name", "params-paramsList-zLpAu").text
        print(params)
        opisanie = driver.find_element("xpath", "//div[@data-marker='item-view/item-description']")
        print("+" * 20)
        print(opisanie.text)
        driver.close() #закрыть текущую вкладку
        driver.switch_to.window(driver.window_handles[0])#перейти к первой вкладке
    print("#" * 20)

    finish_time = datetime.datetime.now()
    spent_time = finish_time - start_time
    print(spent_time)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
