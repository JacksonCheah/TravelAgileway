from selenium.webdriver.common.by import By
from POM.PassengerDetailsPage import PassengerDetailsPage

class SelectFlightPage:

    radio_button_locator = (By.XPATH, "//input[@type='radio' and @value='oneway']")
    departure_location_locator = (By.XPATH, "(//option[contains(text(),'New York')])[1]")
    destination_location_locator = (By.XPATH, "//select[@name='toPort']//option[contains(text(),'New York')]")
    departure_day_locator = (By.XPATH, "//select[@id='departDay']//option[contains(text(),'03')]")
    departure_month_locator = (By.XPATH, "//select[@id='departMonth']//option[@value='022024'][normalize-space()='Feburary 2024']")
    pick_flight_locator = (By.XPATH, "(//input[@type='checkbox'])[2]")
    continue_button_locator = (By.XPATH, "(//input[@value='Continue'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def clickRadioButton(self):
        self.driver.find_element(*self.radio_button_locator).click()

    def clickDepartureLocation(self):
        self.driver.find_element(*self.departure_location_locator).click()

    def clickDestinationLocation(self):
        self.driver.find_element(*self.destination_location_locator).click()

    def clickDepartureDay(self):
        self.driver.find_element(*self.departure_day_locator).click()

    def clickDepartureMonth(self):
        self.driver.find_element(*self.departure_month_locator).click()

    def clickPickFlight(self):
        self.driver.find_element(*self.pick_flight_locator).click()

    def clickContinueButton(self):
        self.driver.find_element(*self.continue_button_locator).click()
        passengerInfo = PassengerDetailsPage(self.driver)
        return passengerInfo
