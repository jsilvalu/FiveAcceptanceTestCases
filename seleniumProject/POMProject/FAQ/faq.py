from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FAQ:

    @staticmethod
    def navigate_to_faq(driver, data):
        driver.find_element(By.XPATH, data["ELEMENTS"]["FAQ"]).click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["search"]).send_keys("login")
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["search"]).send_keys(Keys.ENTER)

        results = driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["results"]).find_elements(By.TAG_NAME, "h2")
        results_number = len(results)
        assert results_number > 0, "The number of results must be greater than 0, the following have been found " + \
                                   str(results_number)

    @staticmethod
    def check_categories(driver, data):
        driver.find_element(By.XPATH, data["ELEMENTS"]["FAQ"]).click()
        driver.switch_to.window(driver.window_handles[1])

        results = driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["categories"]).find_elements(By.TAG_NAME, "a")
        results_number = len(results)
        assert results_number == 9, "There should be 9 recommended categories in this section, there are " + str(
            results_number)
