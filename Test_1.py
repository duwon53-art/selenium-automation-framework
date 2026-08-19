from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from A_login_page import LoginPage
import time

DOS = 'https://example.com'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get(DOS)

# 아이디, 비밀번호 입력
login_page = LoginPage(driver)
login_page.do_login("testID", "testPW")

time.sleep(4)
search_a = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div[2]/div[1]/button/span'))
)
search_a = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div[2]/div[1]/button/span'))
)
search_a = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div[2]/div[1]/button/span')
    )
)

# 3. 'search_a' WebElement 변환 후 JSON 직렬화
driver.execute_script("arguments[0].scrollIntoView(true);", search_a)

search_a.click()

for i in range(100):
    time.sleep(1)
    print(f"--- {i+1}번째 반복 시작 ---")
    
    time.sleep(2)
    search_DLbox = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/section/section/main/div[3]/div/div[1]/div[2]/div[3]/button/span[2]')))
    search_DLbox.click( )
    
    time.sleep(3)
    search_GYbox = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td/span/div/div')))
    search_GYbox.click( )
    target_text = "정산"
    
    option_xpath = f"//div[@title='{target_text}']"     # 이미지에서 확인된 title 속성을 사용하여 항목 찾기. # '//div[@title=...]'
    
    time.sleep(2)
    target_option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    target_option.click() 
    
    PW_box = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[2]/td/span/span/input')
    PW_box.send_keys("test!@")
    
    search_GYSbox = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]/span')))
    search_GYSbox.click( )
    time.sleep(2)
    
    search_GYSSbox = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span')))
    search_GYSSbox.click( )
    time.sleep(2)
    



