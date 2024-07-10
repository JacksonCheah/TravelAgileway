import allure
import time
from utilities.BaseClass import BaseClass
from POM.LoginPage import LoginPage

@allure.epic("Flight Booking")
@allure.feature("Booking a Flight")
class TestAgileTravelWay(BaseClass):

    @allure.story("Logging In")
    def test_book_flight(self):
        # Logging in
        with allure.step("Logging in"):
            homepage = LoginPage(self.driver)
        with allure.step("Entering Username"):
            homepage.enterUsername("agileway")
        with allure.step("Entering Password"):
            homepage.enterPassword("testwise")
        selectingFlight = homepage.clickLogin()
        # Selecting the flight
        selectingFlight.clickRadioButton()
        selectingFlight.clickDepartureLocation()
        selectingFlight.clickDestinationLocation()
        selectingFlight.clickDepartureDay()
        selectingFlight.clickDepartureMonth()
        selectingFlight.clickPickFlight()
        passengerPage = selectingFlight.clickContinueButton()
        # Filling Passenger Details
        passengerPage.enterPassengerFirstName("John")
        passengerPage.enterPassengerLastName("Doe")
        paymentPage = passengerPage.clickNext()
        # Making Payment
        paymentPage.clickCardType()
        paymentPage.enterCardNumber("1234567890123456")
        paymentPage.clickExpiryDay()
        paymentPage.clickExpiryMonth()
        paymentPage.clickPaymentButton()
        time.sleep(5)
