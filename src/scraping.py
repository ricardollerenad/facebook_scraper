from src.driver_setup import setup_driver
from src.scrolling import scroll_down
from src.extraction import extract_posts_info
from src.database import upload_to_mongodb
import time

def scrape_facebook(driver, url, max_posts):
    driver.get(url)
    time.sleep(5)

    posts_data = []

    while len(posts_data) < max_posts:
        new_posts = extract_posts_info(driver)
        posts_data.extend(new_posts)

        if len(posts_data) >= max_posts:
            break

        scroll_down(driver)
        time.sleep(5)
    
    return posts_data[:max_posts]
