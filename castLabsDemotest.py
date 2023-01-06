import time
from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Setting up logs and driver
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome('C:/development/Frameworks/browser_automation/chromedriver.exe', desired_capabilities=d)
driver.maximize_window()

# 1) Go to demo.castlabs.com

driver.get("https://demo.castlabs.com/")
print("Launching Demo castLabs url")
time.sleep(3)


#2) Play 'HLS - HLS Clear' by clicking on the stream.
#3) The browser opens with the details of the video.

HLS_stream = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//li[text()='HLS']")))
HLS_stream.click()
print("Selecting & playing HLS video stream")
time.sleep(3)

#4) Seek to 70% of the video duration.

#Clicking on player to reveal the timeline
player = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "player-container")))
player.click()
time.sleep(3)
#Finding the timeline and slider
timeline = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "pp-ui-clickable")))
slider = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[5]/div["
                                              "3]/div/div[1]/div/div[4]")))
time.sleep(2)

#Getting the slider width and performing drag and drop slider from the starting position to 70% (0,7 of width)
ActionChains(driver).drag_and_drop_by_offset(slider, 0.7 * timeline.size['width'], 0).perform()
print("Forwarding player duration to 70%")
time.sleep(5)



# 5) Validate the "Player state Change" in the console logs.

assert "Player state change" in driver.page_source
print("Validating the Player state change in the console logs.")


# 6) Click the option button (three dots), click 'Videos'.

#Clicking on option button
options = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[5]/div["
                                              "1]/button[4]")))
options.click()
#Clicking on 'Videos'
video = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".pp-ui-options-bar > div:nth-child(3) > div:nth-child(1)")))
video.click()
print("Clicking on the Videos option")

# 7) Select any video value eg: '960x540 @ 2.48 Mbps' and Validate the selection.
time.sleep(6)
#Selecting 960x540 @ 2.48 Mbps
video_value = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "body > div.pp-app-container > div.pp-content > div > div.player-container > div.player > div > div:nth-child(4) > div > div.pp-ui-options-bar.pp-ui-options-bar-show > div:nth-child(3) > div.pp-ui-options-selection > div:nth-child(4)")))
video_value.click()
print("Selecting video format 960x540 @ 2.48 Mbps and validating")
time.sleep(10)

rendition_value = driver.find_element_by_xpath("//td[text()='960x540@2.48Mbps']")
assert rendition_value.text == "960x540@2.48Mbps"


driver.quit()


