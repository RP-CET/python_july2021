'''
instruction
1. need to do pip install selenium
2. need to download and install chrome webdriver (https://chromedriver.chromium.org/downloads)
    - the version of the driver must be same version as chrome browser that you are using
3. when you run the script, you will also need to use your phone to scan the QR-code.
    - this is the same when you are using whatsapp on web
    

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

# construct the whatsapp message
# phone number
# message -- need to be urlencoded
message = "hello whatsapp messages"

# replace with your own phone numbers
driver.get("https://api.whatsapp.com/send?phone=6596201234&text="+ message)

# click on send button
elem = driver.find_element_by_id("action-button")
elem.send_keys(Keys.RETURN)

# click on the use WhatsApp Link
driver.implicitly_wait(10) # seconds only need to call once, it will wait for 10 sec
elem = driver.find_element_by_link_text("use WhatsApp Web")
actions = ActionChains(driver)
actions.click(elem)
actions.perform()

# the selector can be found using 'right-click->Inspect' in Chrome browser
# In the copy the chrome developer window, right-click->copy->Copy Selector
elem = driver.find_element_by_css_selector("#main > footer > div._2BU3P.tm2tP.copyable-area > div._1SEwr > div > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")

elem.send_keys(Keys.RETURN)

