from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FAQ:

    @staticmethod
    def navigate_to_faq(driver, data):
        driver.find_element(By.XPATH, data["ELEMENTS"]["FAQ"]).click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["search"]).send_keys("login")
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["search"]).send_keys(Keys.ENTER)
        assert driver.title == data["TITLES"]["search_results"]
        results = driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["results"]).find_elements(By.TAG_NAME, "h2")
        results_number = len(results)
        assert results_number > 0

    @staticmethod
    def submit_request(driver, data):
        driver.find_element(By.XPATH, data["ELEMENTS"]["FAQ"]).click()
        driver.switch_to.window(driver.window_handles[1])

        driver.find_element(By.XPATH, data["ELEMENTS"]["submit_request"]).click()
        driver.switch_to.window(driver.window_handles[2])

        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["accept_cookies"]).click()

        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["drop_list"]).click()
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["download"]).click()
        driver.find_element(By.LINK_TEXT, "HERE")
        assert driver.title == data["TITLES"]["lets talk"]