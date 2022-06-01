from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


desired_caps = {
    "app" : "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",
    "getMatchedImageResult" : True,
}
driver = webdriver.Remote(
    'http://127.0.0.1:4723',
    desired_caps)


try:
    seven_button = driver.find_element(MobileBy.NAME, "Seven")
    eight_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "num8Button")
    plus_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "plusButton")
    #equals_button = driver.find_element(MobileBy.XPATH, "//Button[Name='Equals']")
    equals_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "equalButton")
    #seven_button = driver.find_element_by_name('Seven')
    display = driver.find_element(MobileBy.ACCESSIBILITY_ID, "CalculatorResults")

    seven_button.click()
    plus_button.click()
    eight_button.click()
    equals_button.click()
    print(display.text)

    #print(driver.find_element(MobileBy.ACCESIBILITYID, "CalculatorResults").text)
    #driver.get_screenshot_as_png()

 
finally:
    driver.quit()
