from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class AdParser:
    BASE_URL = "https://www.farpost.ru"

    def __init__(self, url):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=self.options)
        self.ads_data = []

    def fetch_ads(self):
        self.driver.get(self.url)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "bull-list-item-js"))
            )
        except Exception as e:
            self.driver.quit()
            raise Exception("Timeout waiting for page to load")

        content = self.driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        ads = soup.find_all('tr', class_='bull-list-item-js')
        self.parse_ads(ads[:10])
        self.driver.quit()

    def parse_ads(self, ads):
        for index, ad in enumerate(ads):
            ad_data = self.parse_ad(ad, index)
            if ad_data:
                self.ads_data.append(ad_data)

    def parse_ad(self, ad, index):
        ad_data = {}
        title_element = ad.find('a', class_='bulletinLink')
        if title_element:
            ad_data['title'] = title_element.text.strip()
            ad_url = self.BASE_URL + title_element['href']
        else:
            ad_data['title'] = "No title"
            ad_url = None

        ad_data['ad_id'] = ad.get('data-doc-id')
        views_element = ad.find('span', class_='views')
        ad_data['views_count'] = int(views_element.text.strip()) if views_element else 0
        ad_data['position'] = index + 1

        if ad_url:
            ad_data['author'] = self.fetch_author(ad_url)
        else:
            ad_data['author'] = "Unknown Author"

        return ad_data

    def fetch_author(self, url):
        self.driver.get(url)
        ad_page_content = self.driver.page_source
        ad_soup = BeautifulSoup(ad_page_content, 'html.parser')
        author_element = ad_soup.find('span', class_='userNick')
        if author_element and author_element.find('a'):
            return author_element.find('a').text.strip()
        return "Unknown Author"
