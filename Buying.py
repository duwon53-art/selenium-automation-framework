from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#상품 주문하기

start_time = time.time()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

Url = 'https://example.com'
Url210 = 'https://example2.com'
Carturl = 'https://example3.com'

driver.get(Url)

from A_login_page import LoginPage
login_page = LoginPage(driver)
login_page.do_login("test", "test!@#")
time.sleep(2)

driver.get(Url210) #구매 페이지로 이동

search_box = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div[2]/div[2]/div[2]/article[1]/a/div/button'))) 
#담기 버튼
search_box.click()

search_box = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[3]/div/div[2]/button[2]'))) 
#장바구니 담기 버튼
search_box.click()
time.sleep(1)

driver.get(Carturl) #장바구니 페이지로 이동

search_Obox = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[4]/div/div/div[2]/div[3]/button')))
search_Obox.click() #~원 주문하기

time.sleep(2)
search_Pbox = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[4]/div/div/div[8]/div[1]/div[4]/div[2]/div/div[2]/button')))
search_Pbox.click()

time.sleep(2)
search_O3box = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., '결제하기')]"))) 
search_O3box.click() #~원 결제하기

try:
    completed_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'주문을 완료했어요')]")))
    end_time = time.time()  # 끝 시간 기록
    elapsed_time = end_time - start_time
    print(f"주문 완료 페이지 확인됨 ✅ (소요 시간: {elapsed_time:.2f}초)")
    driver.quit()
    
except:
    print("주문 완료 페이지가 아님 ❌")
