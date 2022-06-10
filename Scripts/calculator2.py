import os
import base64
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


desired_caps = {
    "automationName" : "UiAutomator2",
    "platformName" : "Android",
    "platformVersion" : "11.0",
    "deviceName" : "pixel_2",
    "app" : "F:\COSAS IMPORTANTES\SCRIPSTSTSTSTS\Calculator_v8.1 (403424005)_apkpure.com.apk",
    "fixImageTemplateScale" : False,
    "fixImageTemplateSize" : False,
    "imageMatchThreshold" : 1,
    "fixImageFindScreenshotDims" : False,
    "imageMatchMethod" : "TM_SQDIFF_NORMED",
    "getMatchedImageResult" : True
}
driver = webdriver.Remote(
    'http://127.0.0.1:4723/wd/hub',
    desired_caps)

# driver.update_settings({"fixImageTemplateScale" : False})


try:
    seven_button = driver.find_element(MobileBy.ID, "digit_7")
    nine_button = driver.find_element(MobileBy.ID, "digit_9")
    add_button = driver.find_element(MobileBy.ID, "op_add")
    equals_button = driver.find_element(MobileBy.ID, "eq")
    display = driver.find_element(MobileBy.ID, "formula")
    pre_display = driver.find_element(MobileBy.ID, "result_preview")
    #minus_android = driver.find_element_by_image("minus_android.png")
    with open("minus_android.png", 'rb') as i_file:
            b64_data = base64.b64encode(i_file.read()).decode('UTF-8')
    minus_android = driver.find_element(MobileBy.IMAGE, b64_data)

    seven_button.click()
    add_button.click()
    nine_button.click()
    minus_android.click()
    nine_button.click()
    print(pre_display.text)
    equals_button.click()
    #print(display.text)

    driver.save_screenshot("screenshot.png")


 
finally:
    driver.quit()
