from selenium.webdriver.common.by import By


class Account:

    @staticmethod
    def create_new_account(driver, data):
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, data["ELEMENTS"]["my_account"]))
        driver.switch_to.window(driver.window_handles[1])
        assert driver.title == data["TITLES"]["Account"]

        driver.find_element(By.XPATH,  data["ELEMENTS"]["email"]).send_keys(data["CREDENTIALS"]["email"])
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["continue_email"]).click()
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["validation_code"]).send_keys(data["CREDENTIALS"]["code"])
        assert driver.title == data["TITLES"]["validate_email"]

