from bs4 import BeautifulSoup
import requests
from datetime import datetime

class ScraperService:
    def __init__(self, config):
        self.config = config
    
    def parse_trends(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        trends = soup.find_all('div', {'data-testid': 'trend'})
        
        trend_data = {}
        for index, trend in enumerate(trends, start=1):
            trend_info = trend.find_all('span')
            if len(trend_info) >= 3:
                trend_name = trend_info[1].text
                trend_data[f'nameoftrend_{index}'] = trend_name
        
        trend_data['script_end_date_time'] = datetime.now().isoformat()
        trend_data['ip_address'] = self.get_current_ip()
        
        return trend_data
    
    def get_current_ip(self):
        proxies = {
            'http': f'http://{self.config.PROXY_USERNAME}:{self.config.PROXY_PASSWORD}@{self.config.PROXY_URL}',
            'https': f'http://{self.config.PROXY_USERNAME}:{self.config.PROXY_PASSWORD}@{self.config.PROXY_URL}'
        }
        try:
            response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
            response.raise_for_status()
            return response.json().get('origin')
        except requests.RequestException as e:
            print(f"Failed to get current IP: {e}")
            return None