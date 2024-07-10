from selenium.webdriver.common.by import By


class PaymentPage:

    card_type_locator = (By.XPATH, "(//input[@value='master'])[1]")
    card_number_locator = (By.NAME, "card_number")
    expiry_day_locator = (By.XPATH, "(//option[@value='05'])[1]")
    expiry_month_locator = (By.XPATH, "(//option[@value='2025'])[1]")
    payment_button_locator = (By.XPATH, "(//input[@value='Pay now'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def clickCardType(self):
        self.driver.find_element(*self.card_type_locator).click()

    def enterCardNumber(self, card_number):
        self.driver.find_element(*self.card_number_locator).send_keys(card_number)

    def clickExpiryDay(self):
        self.driver.find_element(*self.expiry_day_locator).click()

    def clickExpiryMonth(self):
        self.driver.find_element(*self.expiry_month_locator).click()

    def clickPaymentButton(self):
        self.driver.find_element(*self.payment_button_locator).click()