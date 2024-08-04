import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p

class Videoyt:
    def __init__(self):
        # Initialize the Chrome WebDriver with the correct service
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def play_song(self, song_name):
        self.song_name = song_name
        self.driver.get("https://www.youtube.com")
        time.sleep(2)  # Give the page some time to load
        
        # Locate the search bar and enter the song name
        search_box = self.driver.find_element(By.NAME, 'search_query')
        search_box.send_keys(song_name)
        search_box.submit()
        
        time.sleep(2)  # Wait for search results to load
        
        # Click on the first video in the search results
        first_video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        first_video.click()
        
        # Wait for the user to close the browser manually
        print("Playing video. Close the browser when done.")
        while True:
            time.sleep(10)  # Check every 10 seconds if the user has closed the browser
            if self.driver.current_url == "https://www.youtube.com":
                print("Browser closed by user.")
                break

    # def read_text(self, text):
    #     engine = p.init()
    #     rate = engine.getProperty('rate')
    #     engine.setProperty('rate', 170)
    #     voices = engine.getProperty('voices')
    #     engine.setProperty('voice', voices[1].id)
    #     engine.say(text)
    #     engine.runAndWait()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p

class Videoyt:
    def __init__(self):
        # Initialize the Chrome WebDriver with the correct service
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def play_song(self, song_name):
        self.song_name = song_name
        self.driver.get("https://www.youtube.com")
        time.sleep(2)  # Give the page some time to load
        
        # Locate the search bar and enter the song name
        search_box = self.driver.find_element(By.NAME, 'search_query')
        search_box.send_keys(song_name)
        search_box.submit()
        
        time.sleep(2)  # Wait for search results to load
        
        # Click on the first video in the search results
        first_video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        first_video.click()
        
        # Wait for the user to close the browser manually
        print("Playing video. Close the browser when done.")
        while True:
            time.sleep(10)  # Check every 10 seconds if the user has closed the browser
            if self.driver.current_url == "https://www.youtube.com":
                print("Browser closed by user.")
                break

    # def read_text(self, text):
    #     engine = p.init()
    #     rate = engine.getProperty('rate')
    #     engine.setProperty('rate', 170)
    #     voices = engine.getProperty('voices')
    #     engine.setProperty('voice', voices[1].id)
    #     engine.say(text)
    #     engine.runAndWait()

# Create an instance of Videoyt and call the play_song method
# Replace with the song you want to play
# assist = Videoyt()
# assist.play_song("Your Song Title Here")  # Replace with the song you want to play
