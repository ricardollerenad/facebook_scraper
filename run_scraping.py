from src.scraping import scrape_facebook
from src.driver_setup import setup_driver
from src.database import upload_to_mongodb

def main():
    fanpage_file = 'fanpages/fanpages.txt'
    max_posts = 5
    driver = setup_driver()

    with open(fanpage_file, 'r') as file:
        fanpages = file.readlines()

    for page in fanpages:
        page = page.strip()
        posts = scrape_facebook(driver, page, max_posts)
        upload_to_mongodb(posts)
    
    driver.quit()

if __name__ == "__main__":
    main()
