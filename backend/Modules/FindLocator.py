from selenium import webdriver
from bs4 import BeautifulSoup

def find_locator(url, element):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    html_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')
    div_elements = soup.find_all(['div', 'input'])

    for div_element in div_elements:
        element_id = div_element.get('id')
        element_placeholder = div_element.get('placeholder')
        element_value = div_element.get('value')

        if (element_id == element) or (element_placeholder == element) or (element_value == element):
            if element_id:
                return f"(By.ID, '{element_id}')"
            elif element_value:
                return f"(By.XPATH, '//{div_element}[@value=\'{element_value}\']')"
            elif element_placeholder:
                return f"(By.XPATH, '//{div_element}[@value=\'{element_placeholder}\']')"

    return "Invalid input"
