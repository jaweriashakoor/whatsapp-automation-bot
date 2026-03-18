import pyttsx3
import pywhatkit
import pyautogui
import time
import os
import shutil

# Initialize engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greeting
speak("Hello! How can I help you today?")

# Input
phone_number = input("Enter phone number with country code (e.g., +923001234567): ")
message = input("Enter your message: ")

speak("Opening WhatsApp Web and sending your message")

# Open WhatsApp immediately
pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=False)

time.sleep(10) 

# Click the center of the screen to ensure the browser is focused
pyautogui.click()

# Explicitly press 'Enter' to send
pyautogui.press('enter')
# Wait for message to appear
time.sleep(10)

# Take screenshot
screenshot = pyautogui.screenshot()
screenshot.save("image.png")

# 2. Folder creation and movement logic
folder_name = "newfolder"
os.makedirs(folder_name, exist_ok=True)
shutil.copy2("image.png", os.path.join(folder_name, "image.png"))



speak("Your message has been sent and screenshot saved")

engine.stop()