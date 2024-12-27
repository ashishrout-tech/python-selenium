from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

class BrowserService:
    def __init__(self, config):
        self.config = config
    
    def setup_driver(self):
        path = os.path.dirname(os.path.abspath(__file__))

        seleniumwire_options = {
            'proxy': {
                'http': f'http://{self.config.PROXY_USERNAME}:{self.config.PROXY_PASSWORD}@{self.config.PROXY_URL}',
                'https': f'http://{self.config.PROXY_USERNAME}:{self.config.PROXY_PASSWORD}@{self.config.PROXY_URL}'
            },
            'disable_encoding': True,
            'suppress_connection_errors': False
        }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--user-data-dir={self.config.CHROME_USER_DATA_DIR}')
        chrome_options.add_argument(f'--profile-directory={self.config.CHROME_PROFILE}')

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        chrome_options.add_argument(f'--user-agent={user_agent}')

        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        
        driver = webdriver.Chrome(
            options=chrome_options,
            seleniumwire_options=seleniumwire_options
        )

        return driver
    
    def get_explore_content(self):
        driver = self.setup_driver()
        try:
            driver.get("https://x.com/home")
            time.sleep(25)
            explore_div = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Timeline: Trending now"]')
            return explore_div.get_attribute('outerHTML')
        finally:
            driver.quit()