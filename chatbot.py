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

# 1. Get user input for message
phone_number = input("Enter phone number: ")
message = input("Enter message: ")

speak("Opening WhatsApp Web and sending your message")
pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=20, tab_close=False)

# Wait for WhatsApp to load and send
time.sleep(15) 
pyautogui.click()
pyautogui.press('enter')
time.sleep(10)

# 2. Ask before taking screenshot
confirm = input("Message sent. Do you want to take a screenshot? (y/n): ")
if confirm.lower() == 'y':
    screenshot = pyautogui.screenshot()
    
    # 3. Ask where to store the screenshot
    save_path = input("Enter the folder path to save the screenshot: ")

    speak("Please wait, switching to WhatsApp for the screenshot")
    
    # --- FIX STARTS HERE ---
    # 1. Give yourself 2 seconds to move your mouse over the browser 
    # OR let the script try to switch back.
    print("Switching windows... Screenshot in 3 seconds.")
    time.sleep(3) 
    
    # 2. Click to ensure the browser window is focused again
    pyautogui.click() 
    
    # 3. Take the screenshot NOW while the browser is focused
    screenshot = pyautogui.screenshot()
    
    # Create directory if it doesn't exist
    folder_name='ss_folder'
    os.makedirs(folder_name, exist_ok=True)
    
    # Save the file
    file_name = os.path.join(save_path, "screenshot.png")
    screenshot.save(file_name)
    print(f"Screenshot saved at: {file_name}")
    speak("Screenshot has been saved successfully")
else:
    speak("Screenshot skipped")

engine.stop()