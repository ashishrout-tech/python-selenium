from flask import Blueprint, jsonify, render_template
from app.services.browser import BrowserService
from app.services.scraper import ScraperService
from app.services.database import DatabaseService
from config import Config
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/run-script', methods=['GET'])
def run_script():
    config = Config()
    browser_service = BrowserService(config)
    scraper_service = ScraperService(config)
    db_service = DatabaseService(config.MONGO_URI)
    
    explore_html = browser_service.get_explore_content()
    
    trend_data = scraper_service.parse_trends(explore_html)
    
    with open("data.json", 'w', encoding='utf-8') as json_file:
        json.dump(trend_data, json_file, ensure_ascii=False, indent=4)
    
    inserted_id = db_service.insert_data(trend_data)
    if inserted_id:
        latest_record = db_service.get_record_by_id(inserted_id)
        if latest_record:
            latest_record['_id'] = str(latest_record['_id'])
            return jsonify(latest_record)
    
    return jsonify({"error": "Failed to process request"}), 500