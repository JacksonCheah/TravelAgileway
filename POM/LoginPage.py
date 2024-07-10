from selenium.webdriver.common.by import By
from POM.SelectFlightPage import SelectFlightPage

class LoginPage:

    username_locator = (By.ID, "username")
    password_locator = (By.ID, "password")
    login_button_locator = (By.CSS_SELECTOR, "input[value='Sign in']")

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        self.driver.find_element(*self.username_locator).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*self.login_button_locator).click()
        selectingFlight = SelectFlightPage(self.driver)
        return selectingFlight
