from selenium import webdriver
from bs4 import BeautifulSoup

def find_locator(driver, element):
    # driver = webdriver.Chrome()
    # driver.get(url)
    # driver.implicitly_wait(10)
    html_content = driver.page_source
    # driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')
    div_elements = soup.find_all(['div', 'input'])

    for div_element in div_elements:
        element_id = div_element.get('id')
        element_placeholder = div_element.get('placeholder')
        element_value = div_element.get('value')

        if (element_id == element) or (element_placeholder == element) or (element_value == element):
            if element_id:
                return f'By.ID, "{element_id}"'
            elif element_value:
                return f'By.XPATH, "//{div_element}[@value=\'{element_value}\']"'
            elif element_placeholder:
                return f'By.XPATH, "//{div_element}[@value=\'{element_placeholder}\']"'

    return "Invalid input"


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# def find_locator(driver, element):
#     try:
#         # Assuming driver is already instantiated and navigated to the login page
#         # Find the login button and click it
#         # login_button = driver.find_element(By.ID, 'login_button_id')  # Adjust this according to your HTML
#         # login_button.click()
#         driver.find_element(By.ID, "user-name").send_keys("standard_user")
#         driver.find_element(By.ID, "password").send_keys("secret_sauce")
#         driver.find_element(By.ID, "login-button").click()

#         # Wait for the new page to load after clicking the login button
#         # WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

#         # Once the new page is loaded, retrieve its page source
#         html_content = driver.page_source

#         # You can then process the HTML content using BeautifulSoup as before
#         soup = BeautifulSoup(html_content, 'html.parser')
#         div_elements = soup.find_all(['div', 'input'])
#         if div_elements:
#             print("New page HTML:", div_elements)
#         # Perform further processing as needed
        
#         return "Hi"  # Return the HTML content of the new page after login
#     except Exception as e:
#         print("Error:", e)
#         return None

