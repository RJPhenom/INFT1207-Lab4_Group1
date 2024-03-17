###############################################################################
#   Title:      test-Lab4_robert_aarif
#   Author(s):  Robert Macklem and Aarif Sikri
#   Date:       March 16, 2024
#   Descr:      Modified import file from Selenium IDE to run test our recorded
#               test case on Selenium WebDriver
###############################################################################
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBodyFatCalculator:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_body_fat_calculator(self):
        self.driver.get("https://www.calculator.net/body-fat-calculator.html")
        self.driver.set_window_size(1158, 791)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "font > b")))
        self.vars["gender"] = "M"

        if self.driver.execute_script("return (arguments[0]===\"F\")", self.vars["gender"]):
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2)").click()
            self.driver.find_element(By.NAME, "cage").click()
            self.driver.find_element(By.NAME, "cage").clear()
            self.driver.find_element(By.NAME, "cage").send_keys("40")
            self.driver.find_element(By.NAME, "cweightkgs").click()
            self.driver.find_element(By.NAME, "cweightkgs").clear()
            self.driver.find_element(By.NAME, "cweightkgs").send_keys("100")
            self.driver.find_element(By.ID, "cheightmeter").click()
            self.driver.find_element(By.ID, "cheightmeter").clear()
            self.driver.find_element(By.ID, "cheightmeter").send_keys("189")
            self.driver.find_element(By.ID, "cneckmeter").click()
            self.driver.find_element(By.ID, "cneckmeter").clear()
            self.driver.find_element(By.ID, "cneckmeter").send_keys("57")
            self.driver.find_element(By.ID, "cwaistmeter").click()
            self.driver.find_element(By.ID, "cwaistmeter").clear()
            self.driver.find_element(By.ID, "cwaistmeter").send_keys("98")
            self.driver.find_element(By.ID, "chipmeter").click()
            self.driver.find_element(By.ID, "chipmeter").clear()
            self.driver.find_element(By.ID, "chipmeter").send_keys("100")
            calculate_button = WebDriverWait(self.driver, 0).until(EC.element_to_be_clickable((By.NAME, "x")))
            calculate_button.click()
            assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 23.0%"
            print("Actual Text:", self.driver.find_element(By.CSS_SELECTOR, "font > b").text)
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1)").click()
            self.driver.find_element(By.NAME, "cage").click()
            self.driver.find_element(By.NAME, "cage").clear()
            self.driver.find_element(By.NAME, "cage").send_keys("15")
            self.driver.find_element(By.NAME, "cweightkgs").click()
            self.driver.find_element(By.NAME, "cweightkgs").clear()
            self.driver.find_element(By.NAME, "cweightkgs").send_keys("220")
            self.driver.find_element(By.ID, "cheightmeter").click()
            self.driver.find_element(By.ID, "cheightmeter").clear()
            self.driver.find_element(By.ID, "cheightmeter").send_keys("90")
            self.driver.find_element(By.ID, "cneckmeter").click()
            self.driver.find_element(By.ID, "cneckmeter").clear()
            self.driver.find_element(By.ID, "cneckmeter").send_keys("18")
            self.driver.find_element(By.ID, "cwaistmeter").click()
            self.driver.find_element(By.ID, "cwaistmeter").clear()
            self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")
            calculate_button = WebDriverWait(self.driver, 0).until(EC.element_to_be_clickable((By.NAME, "x")))
            calculate_button.click()
            assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 60.7%"
            print("Actual Text:", self.driver.find_element(By.CSS_SELECTOR, "font > b").text)


if __name__ == "__main__":
    test = TestBodyFatCalculator()
    test.setup_method(None)
    test.test_body_fat_calculator()
    test.teardown_method(None)