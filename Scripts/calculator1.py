from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import base64
from selenium.webdriver.common.action_chains import ActionChains



desired_caps = {
    "app" : "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",
    "getMatchedImageResult" : True,
}
driver = webdriver.Remote(
    'http://127.0.0.1:4723',
    desired_caps)


actions = ActionChains(driver)
#named parameters
try:

    seven_button = driver.find_element(MobileBy.NAME, "Seven")
    eight_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "num8Button")
    plus_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "plusButton")
    #equals_button = driver.find_element(MobileBy.XPATH, "//Button[Name='Equals']")
    equals_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "equalButton")
    #seven_button = driver.find_element_by_name('Seven')
    display = driver.find_element(MobileBy.ACCESSIBILITY_ID, "CalculatorResults")
    display.send_keys("42")
    actions.move_by_offset()
    """
    with open("eight.png", "rb") as image_file:
        eight_b64 = base64.b64encode(image_file.read())

    eight_b64 = eight_b64.decode("utf-8")

    eight_button = driver.find_element(by=MobileBy.IMAGE, value=eight_b64)
    """

    seven_button.click()
    plus_button.click()
    eight_button.click()
    equals_button.click()
    print(display.text)

    #print(driver.find_element(MobileBy.ACCESIBILITYID, "CalculatorResults").text)
    #driver.get_screenshot_as_png()
    
finally:
    driver.quit()


"""
class SimpleCalculatorTests(unittest.TestCase):

    @classmethod

    def setUpClass(self):
        #set up appium
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("Display is " )
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext


    def test_initialize(self):
        self.driver.find_element_by_name("Clear").click()
        self.driver.find_element_by_name("Seven").click()
        self.assertEqual(self.getresults(),"7")
        self.driver.find_element_by_name("Clear").click()

    def test_addition(self):
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"8")

    def test_combination(self):
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Multiply by").click()
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()
        self.driver.find_element_by_name("Divide by").click()
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"8")

    def test_division(self):
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Divide by").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"8")

    def test_multiplication(self):
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Multiply by").click()
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"81") 

    def test_subtraction(self):
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Minus").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"8")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

"""
