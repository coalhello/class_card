import time
import warnings
import  random
import tkinter as tk
from tkinter import messagebox

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException, NoSuchElementException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import info

# def show_warning():
#     root = tk.Tk()
#     root.withdraw()
#     root.attributes('-topmost', True)
#     messagebox.showwarning("경고", "끝")
#     root.destroy()

warnings.filterwarnings("ignore", category=DeprecationWarning) # 옛날 기능 경고 무시 함수
account = info.get_id()
class_site = input("학습할 세트 URL을 입력하세요 : ")
ch_d = info.chd_wh()
time_1 = round(random.uniform(0.7, 1.3), 4)
time_2 = round(random.uniform(1.7, 2.3), 4)
time_1_5 = round(random.uniform(1.2, 1.8), 4)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--mute-audio')
driver = webdriver.Chrome(options=options)

driver.get("https://www.classcard.net/Login")
tag_id = driver.find_element(By.ID, "login_id")
tag_pw = driver.find_element(By.ID, "login_pwd")
tag_id.clear()
tag_id.send_keys(account["id"])
tag_pw.send_keys(account["pw"])
driver.find_element(By.CSS_SELECTOR,
                    "#loginForm > div.checkbox.primary.text-primary.text-center.m-t-md > button"
                    ).click()

try:
    time.sleep(1)
    driver.get(class_site)
    driver.find_elements(By.XPATH, "//div[@class='p-b-sm']")
except:
    print("\n입력한 URL이 잘못되어 프로그램을 종료합니다\n")
    quit()

driver.find_element(By.CSS_SELECTOR,
                    "body > div.test > div.p-b-sm > div.set-body.m-t-25.m-b-lg > div.m-b-md > div > a"
                    ).click()
driver.find_element(By.CSS_SELECTOR,
                    "body > div.test > div.p-b-sm > div.set-body.m-t-25.m-b-lg > div.m-b-md > div > ul > li:nth-child(1)"
                    ).click()

html = BeautifulSoup(driver.page_source, "html.parser")
cards_ele = html.find("div", class_="flip-body")
num_d = len(cards_ele.find_all("div", class_="flip-card")) + 1 # 단어 수
time.sleep(0.5)

word_d = info.word_get(driver, num_d)
da_e = word_d[0]
da_k = word_d[1]
da_kn = word_d[2]
da_kyn = word_d[3]

while True:
    if ch_d == 1:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[1]"))
            )
            element.click()  # 요소가 로드된 후 클릭 작업 실행
        except Exception as e:
            print(f"요소를 찾을 수 없습니다: {e}")
        driver.find_element(By.CSS_SELECTOR,
                            "#wrapper-learn > div.start-opt-body > div > div > div > div.m-t > a"
                            ).click()
        for i in range(1, num_d):
            time.sleep(2.5)
            try:
                driver.find_element(By.CSS_SELECTOR,
                                    "#wrapper-learn > div > div > div.study-bottom > div.btn-text.btn-down-cover-box"
                                    ).click()
                time.sleep(0.5)
                driver.find_element(By.CSS_SELECTOR,
                                    "#wrapper-learn > div > div > div.study-bottom.down > div.btn-text.btn-know-box"
                                    ).click()
            except:
                break
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.study-header-body > div > div:nth-child(1) > div:nth-child(1) > a"
                            ).click()
    elif ch_d == 2:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div[2]/div/div[2]/div[1]/div[2]"))
            )
            element.click()  # 요소가 로드된 후 클릭 작업 실행
        except Exception as e:
            print(f"요소를 찾을 수 없습니다: {e}")
        driver.find_element(By.CSS_SELECTOR,
                            "#wrapper-learn > div.start-opt-body > div > div > div > div.m-t > a"
                            ).click()
        time.sleep(time_2)
        for i in range(1, num_d):
            try:
                cash_d = driver.find_element(By.XPATH,
                                             f"//*[@id='wrapper-learn']/div/div/div[2]/div[2]/div[{i}]/div[1]/div/div/div/div[1]/span"
                                             ).text

                cash_dby = [0, 0, 0]

                for j in range(0, 3):
                    cash_dby[j] = driver.find_element(By.XPATH,
                                                      f"//*[@id='wrapper-learn']/div/div/div[2]/div[2]/div[{i}]/div[3]/div[{j + 1}]/div[2]/div"
                                                      ).text

                ck = False
                if cash_d.upper() != cash_d.lower():
                    try:
                        for j in range(0, 3):
                            if da_e.index(cash_d) == da_kyn.index(cash_dby[j]):
                                driver.find_element(By.XPATH,
                                                    f"//*[@id='wrapper-learn']/div/div/div[2]/div[2]/div[{i}]/div[3]/div[{j + 1}]/div[2]"
                                                    ).click()
                                ck = True
                                break
                    except:
                        pass
                    if ck != True:
                        print("\nDetected Missing Words!!, Randomly Selected\n")
                        driver.find_element(By.XPATH,
                                            f"//*[@id='wrapper-learn']/div/div/div[2]/div[2]/div[{i}]/div[3]/div[{random.randint(1, 4)}]/div[2]"
                                            ).click()
                        time.sleep(time_2)
                        try:
                            driver.find_element(By.XPATH,
                                                f"//*[@id='wrapper-learn']/div/div/div[3]/div[2]"
                                                ).click()
                        except:
                            pass
                time.sleep(time_2)
            except:
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/div/div[1]/div[1]"
                                    ).click()
                time.sleep(1)
                driver.find_element(By.XPATH,
                                    f"//*[@id='wrapper-learn']/div[2]/div/div/div/div[5]/a[3]"
                                    ).click()
                break
    elif ch_d == 3:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div[2]/div/div[2]/div[1]/div[3]"))
            )
            element.click()  # 요소가 로드된 후 클릭 작업 실행
        except Exception as e:
            print(f"요소를 찾을 수 없습니다: {e}")
        driver.find_element(By.CSS_SELECTOR,
                            "#wrapper-learn > div.start-opt-body > div > div > div > div.m-t > a"
                            ).click()
        time.sleep(2)
        try:
            for i in range(1, num_d):
                cash_d = driver.find_element(By.XPATH,
                                             f"//*[@id='wrapper-learn']/div/div/div[2]/div[2]/div[{i}]/div[1]/div/div/div/div[1]/span[1]"
                                             ).text
                if cash_d.upper() != cash_d.lower():
                    try:
                        text = da_k[da_e.index(cash_d)]
                    except ValueError:
                        text = da_e[da_k.index(cash_d)]
                else:
                    text = da_e[da_k.index(cash_d)]
                in_tag = driver.find_element(By.CSS_SELECTOR,
                                             "#wrapper-learn > div > div > div.study-content.cc-table.middle > div.study-body.fade.in > div.CardItem.current.showing > div.card-bottom > div > div > div > div.text-normal.spell-input > input"
                                             )
                in_tag.click()
                in_tag.send_keys(text)
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id='wrapper-learn']/div/div/div[3]"))
                    )
                    element.click()  # 요소가 로드된 후 클릭 작업 실행
                except Exception as e:
                    print(f"요소를 찾을 수 없습니다: {e}")
                time.sleep(1.5)
                try:
                    driver.find_element(By.XPATH,
                                        "//*[@id='wrapper-learn']/div/div/div[3]/div[2]"
                                        ).click()
                except:
                    pass
                i += 1
                time.sleep(1)
        except NoSuchElementException:
            pass
    elif ch_d == 4:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div"))
            )
            element.click()  # 요소가 로드된 후 클릭 작업 실행
        except Exception as e:
            print(f"요소를 찾을 수 없습니다: {e}")
        time.sleep(time_1)
        driver.find_element(By.CSS_SELECTOR,
                            "#wrapper-test > div > div.quiz-start-div > div.layer.retry-layer.box > div.m-t-xl > a"
                            ).click()
        driver.find_element(By.XPATH,
                            "//*[@id='wrapper-test']/div/div[1]/div[3]/div[3]/a"
                            ).click()

        # 이미 학습 기록이 존재한다는 알림창이 나타날 시 아래 코드 사용
        # for _ in range(2):
        #     time.sleep(1)
        #     driver.find_element(By.XPATH,
        #                         "//*[@id='confirmModal']/div[2]/div/div[2]/a[3]"
        #                         ).click()

        for i in range(1, num_d):
            time.sleep(0.5)
            cash_d = driver.find_element(By.XPATH,
                                         f"//*[@id='testForm']/div[{i}]/div/div[1]/div[2]/div/div/div"
                                         ).text

            element = driver.find_element(By.XPATH,
                                          f"//*[@id='testForm']/div[{i}]/div/div[1]/div[2]"
                                          )
            driver.execute_script("arguments[0].click();", element)
            time.sleep(0.5)

            cash_dby = [0, 0, 0, 0, 0, 0]
            for j in range(0, 6):
                cash_dby[j] = driver.find_element(By.XPATH,
                                                  f"//*[@id='testForm']/div[{i}]/div/div[2]/div/div[1]/div[{j + 1}]/label/div/div"
                                                  ).text

            notFindData = False
            if cash_d.upper() != cash_d.lower():
                for j in range(0, 6):
                    try:
                        if da_e.index(cash_d) == da_k.index(cash_dby[j]):
                            element = driver.find_element(By.XPATH,
                                                        f"//*[@id='testForm']/div[{i}]/div/div[2]/div/div[1]/div[{j + 1}]/label/div/div"
                                                        )
                            driver.execute_script("arguments[0].click();", element)
                            notFindData = True
                            break
                    except:
                        try:
                            if da_e.index(cash_d) in da_kn:
                                if da_e.index(cash_d) == da_kn.index(cash_dby[j]):
                                    element = driver.find_element(By.XPATH,
                                                                f"//*[@id='testForm']/div[{i}]/div/div[2]/div/div[1]/div[{j + 1}]/label/div/div"
                                                                )
                                    driver.execute_script("arguments[0].click();", element)
                                    notFindData = True
                                    break
                        except:
                            time.sleep(2.7)
            else:
                for j in range(0, 6):
                    try:
                        if da_k.index(cash_d) == da_e.index(cash_dby[j]):
                            element = driver.find_element(By.XPATH,
                                                        f"//*[@id='testForm']/div[{i}]/div/div[2]/div/div[1]/div[{j + 1}]/label/div/div"
                                                        )
                            driver.execute_script("arguments[0].click();", element)
                            notFindData = True
                            break
                    except:
                        if da_e.index(cash_d) in da_kn:
                            if da_kn.index(cash_d) == da_e.index(cash_dby[j]):
                                element = driver.find_element(By.XPATH,
                                                              f"//*[@id='testForm']/div[{i}]/div/div[2]/div/div[1]/div[{j + 1}]/label/div/div"
                                                              )
                                driver.execute_script("arguments[0].click();", element)
                                notFindData = True
                                break
            if notFindData != True:
                print("\n누락된 단어가 있어서 단어가 랜덤하게 선택됩니다!\n")
                driver.find_element(By.XPATH,
                                    f"//*[@id='testForm']/div[{i}]/div/div[2]/div/div[1]/div[{random.randint(1, 6)}]/label/div/div"
                                    ).click()
                time.sleep(2.7)
            time.sleep(1.2)