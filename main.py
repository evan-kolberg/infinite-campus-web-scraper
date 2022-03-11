from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
s = Service('C:/Users/ekpro/PycharmProjects/infinite-campus-web-scraper/chromedriver.exe')

driver = webdriver.Chrome(service=s, options=options)
driver.set_window_size(2048, 1080)
driver.set_window_position(1200, 200, windowHandle='current')


def login():
    driver.get('https://campus.bellmore-merrick.k12.ny.us/campus/portal/students/bellmore.jsp')
    WebDriverWait(driver, 8).until(
        expected_conditions.presence_of_element_located((By.ID, 'username'))
    )
    WebDriverWait(driver, 8).until(
        expected_conditions.presence_of_element_located((By.ID, 'password'))
    )

    driver.find_element(By.NAME, 'username').send_keys(input('Student ID:  '))
    driver.find_element(By.NAME, 'password').send_keys(input('Password:  '))
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/input[6]').click()


def grades_page():
    WebDriverWait(driver, 8).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/ic-nav-wrapper-app/ic-sidebar/div/ic-tool-list/nav/ul/li[4]/a'))
    )

    driver.find_element(By.XPATH, '/html/body/ic-nav-wrapper-app/ic-sidebar/div/ic-tool-list/nav/ul/li[4]/a').click()


def get_those_grade_updates():
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for count, data in enumerate(soup.findAll('div', {'_ngcontent-dxc-c716': ''})):
        if count > 6:
            print(data.get_text())

# in progress ~ currently cannot see data inside div.card.ng-star-inserted
'''
def class_averages():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.get_text())

    for i in soup.findAll('div', {'_ngcontent-etu-c716': '', 'class': 'ellipsis-container'}):
        for j in soup.findAll('div', {'_ngcontent-etu-c639': '', 'class': 'ng-star-inserted'}):
            print(f'Your grade in {i.get_text()} is {j.get_text()}')
'''

if __name__ == '__main__':
    login()
    grades_page()
    # class_averages()
    # get_those_grade_updates()
    driver.close()
