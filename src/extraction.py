from selenium.webdriver.common.by import By

def extract_posts_info(driver):
    posts = driver.find_elements(By.CSS_SELECTOR, 'div[data-pagelet^="FeedUnit_"]')
    posts_data = []

    for post in posts:
        try:
            post_id = post.get_attribute('id')
            post_url = post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            post_type = detect_post_type(post)
            reactions = extract_reactions(post)
            comments = extract_comments(post)
            views = extract_views(post)

            posts_data.append({
                'post_id': post_id,
                'post_url': post_url,
                'post_type': post_type,
                'reactions': reactions,
                'comments': comments,
                'views': views,
            })
        except Exception as e:
            print(f"Error extracting post info: {e}")
    
    return posts_data
