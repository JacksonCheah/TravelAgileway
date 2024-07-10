from selenium.webdriver.common.by import By
from POM.PaymentPage import PaymentPage

class PassengerDetailsPage:

    passengerFirstName_locator = (By.NAME, "passengerFirstName")
    passengerLastName_locator = (By.NAME, "passengerLastName")
    next_button_locator = (By.XPATH, "(//input[@value='Next'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def enterPassengerFirstName(self, passengerFirstName):
        self.driver.find_element(*self.passengerFirstName_locator).send_keys(passengerFirstName)

    def enterPassengerLastName(self, passengerLastName):
        self.driver.find_element(*self.passengerLastName_locator).send_keys(passengerLastName)

    def clickNext(self):
        self.driver.find_element(*self.next_button_locator).click()
        payment = PaymentPage(self.driver)
        return payment
