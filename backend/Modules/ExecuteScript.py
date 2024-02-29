from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def execute_script(driver, generated_test_script):
    try:
        eval(generated_test_script)
        
        return None
    except Exception as e:
        print("Error:", e)
        return None