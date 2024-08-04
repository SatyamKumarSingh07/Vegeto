import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p

class Infow:
    def __init__(self):
        # Initialize the Chrome WebDriver with the correct service
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def getinfo(self, query):
        self.query = query
        self.driver.get("https://en.wikipedia.org/wiki/" + query.replace(" ", "_"))
        time.sleep(3)  # Give the page some time to load
        
        # Extract the first two lines of the article
        paragraphs = self.driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p')
        first_two_lines = ""
        lines_count = 0
        
        for paragraph in paragraphs:
            if lines_count >= 2:
                break
            text = paragraph.text.strip()
            if text:
                first_two_lines += text + " "
                lines_count += 1
        
        # self.driver.quit()
        
        # Read the extracted text
        self.read_text(first_two_lines.strip())

    def read_text(self, text):
        engine = p.init()
        rate=engine.getProperty('rate')
        engine.setProperty('rate',170)
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.say(text)
        engine.runAndWait()
