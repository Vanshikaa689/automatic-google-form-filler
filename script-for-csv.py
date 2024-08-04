import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

# Path to the WebDriver executable (make sure it's in your PATH or provide the full path)
driver_path = r"path/to/your/driver"
service = Service(driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Open the Google Form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdXByiUnlGu1xturiM2gDq_nkLJhQtKmblnuj5gEqkTbw7Brg/viewform'
driver.get(form_url)

# Dictionary for category XPaths
category_xpaths = {
    'Politics': '//*[@id="i34"]/div[3]/div',
    'International News': '//*[@id="i37"]/div[3]/div',
    'National News': '//*[@id="i40"]/div[3]/div',
    'Local News': '//*[@id="i43"]/div[3]/div',
    'Politics(repeated)': '//*[@id="i46"]/div[3]/div',
    'Business and Finance': '//*[@id="i49"]/div[3]/div',
    'Science and Technology': '//*[@id="i52"]/div[3]/div',
    'Health and Wellness': '//*[@id="i55"]/div[3]/div',
    'Entertainment': '//*[@id="i58"]/div[3]/div',
    'Sports': '//*[@id="i61"]/div[3]/div',
    'Lifestyle and Features': '//*[@id="i64"]/div[3]/div',
    'Opinion and Editorial': '//*[@id="i67"]/div[3]/div',
    'Environment': '//*[@id="i70"]/div[3]/div',
    'Education': '//*[@id="i73"]/div[3]/div',
    'Crime and Justice': '//*[@id="i76"]/div[3]/div',
    'Human Interest': '//*[@id="i79"]/div[3]/div',
    'Obituaries': '//*[@id="i82"]/div[3]/div',
    'Weather': '//*[@id="i85"]/div[3]/div',
    'Religion and Spirituality': '//*[@id="i88"]/div[3]/div',
    'Technology and Gadgets': '//*[@id="i91"]/div[3]/div',
    'Automotive': '//*[@id="i94"]/div[3]/div',
    'Other': '//*[@id="i97"]/div[3]/div'
}

def safe_send_keys(element, data):
    """ Break data into smaller chunks and send keys safely """
    chunks = [data[i:i+200] for i in range(0, len(data), 200)]
    for chunk in chunks:
        element.send_keys(chunk)
        time.sleep(0.2)  # small delay to let the input process

# Convert the category_xpaths keys to lowercase for case-insensitive matching
category_xpaths = {key.lower(): value for key, value in category_xpaths.items()}

# Read the data from the CSV file
with open(r'path/to/your/csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    entries = list(reader)

for entry in entries:
    full_name = entry.get("Full Name", "")
    newspaper = entry.get("Newspaper", "")
    link = entry.get("Link", "")
    headline = entry.get("Headline", "")
    date = entry.get("Date", "")
    
    article_content = entry.get("Content", "")
    article_summary = entry.get("Summary", "")
    category = entry.get("Category", "").lower()

    try:
        # Fill the form fields using WebDriverWait to ensure elements are present
        print("Filling full name field")
        full_name_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        full_name_field.send_keys(full_name)

        print("Filling newspaper field")
        newspaper_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        newspaper_field.send_keys(newspaper)

        print("Filling date field")
        date_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'))
        )
        date_field.send_keys(date)

        print("Filling link field")
        link_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        link_field.send_keys(link)

        print("Filling headline field")
        headline_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        headline_field.send_keys(headline)

        print("Filling content field")
        content_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea'))
        )
        safe_send_keys(content_field, article_content)

        print("Filling summary field")
        summary_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea'))
        )
        safe_send_keys(summary_field, article_summary)

        # Select the category based on the dictionary
        print(f"Selecting category: {category}")
        if category in category_xpaths:
            category_field = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, category_xpaths[category]))
            )
            category_field.click()
        else:
            print(f"Category '{category}' not found in the dictionary.")

        # Submit the form
        print("Submitting the form")
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
        )
        submit_button.click()

        # Wait for the form to process the submission and reload
        time.sleep(2)

        # Go back to the form for the next entry
        driver.get(form_url)

    except Exception as e:
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
        # Take a screenshot for debugging
        driver.save_screenshot('error_screenshot.png')
        # Save the page source for debugging
        with open('error_page_source.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        break

# Keep the browser open
input("Press Enter to close the browser...")

# Close the WebDriver
driver.quit()
