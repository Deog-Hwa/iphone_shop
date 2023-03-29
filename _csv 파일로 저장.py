from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv






# 크롬 드라이버 자동 업데이트 
from webdriver_manager.chrome import ChromeDriverManager


import time 

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기 
chrome_options.add_experimental_option("excludeSwitches", ["enavle-logging"])

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options = chrome_options)

# 웹페이지 해당 주소 이동 
driver.implicitly_wait(5) # 웹페이지가 로딩 될 때까지 5초는 기다림
driver.maximize_window() # 화면 최대화 

driver.get("https://shopping.naver.com/home")
time.sleep(2)

# 검색창 클릭 
search = driver.find_element(By.CSS_SELECTOR,"#__next > div > div.pcHeader_header__tXOY4 > div > div > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div._searchInput_search_input_QXUFf > input")
search.click()

# 검색어 입력 
search.send_keys("아이폰 14")
search.send_keys(Keys.ENTER)


# 스크롤 전 높이 
before_h = driver.execute_script("return window.scrollY")

# 무한 스크롤 
while True:
    # 맨 아래로 스크롤을 내린다. 
    driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(2)

    # 스크롤 후 높이 
    after_h = driver.execute_script("return window.scrollY")
    
    if after_h == before_h:
        break 
    before_h = after_h

 # 파일 생성 
f = open(r"C:\Users\duck\Documents\selenium\duck_test\shop.csv",'w', encoding= 'CP949', newline='')
csvWriter = csv.writer(f)

 # 상품 정보 div
items = driver.find_elements(By.CSS_SELECTOR,".basicList_info_area__TWvzp")

for item in items:
    name =  item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c").text
    price = item.find_element(By.CSS_SELECTOR,".price_num__S2p_v").text
    link =  item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c > a").get_attribute('href')
    print(name,price,link)
    csvWriter.writerow([name,price,link])

# 파일 닫기
f.close

