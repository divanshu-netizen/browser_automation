# browser_automation
Video playback automation of a demo website using Python Selenium

Task:
1. Go to demo.castlabs.com
2. Play 'HLS - HLS Clear' by clicking on the stream.
3. The browser opens with the details of the video. 
4. Seek to 70% of the video duration.
5. Validate the “Player state change” in the console logs.
6. Click the options button (three dots), click 'Videos'.
7. Select any video value eg: '960x540 @ 2.48 Mbps' and Validate the selection

# Guide to run the automation script

Prerequisite:

1. Python3
2. IDE like PyCharm or VS-Code
3. Browser like Chrome, Firefox, Edge, Safari etc
4. Webdriver (After downlaoding Webdriver, either keep it in the path varaibles of your local system or in the root directory where the script is)

Steps:

1. Clone the above reop by running below command:

```git clone https://github.com/divanshu-netizen/browser_automation.git```

2. Open a terminal or Command promt and run below command:

```pip install selenium```

3. Run the script in the terminal or cmd:

```py castLabsDemotest.py```

websites:

https://pypi.org/project/selenium/

https://chromedriver.chromium.org/downloads

