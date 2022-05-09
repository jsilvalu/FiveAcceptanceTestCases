from selenium.webdriver.common.by import By


class Home:

    @staticmethod
    def click_download_buttom(driver, data):
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["download_bottom"]).click()
        assert driver.title == data["TITLES"]["Account"]

    @staticmethod
    def navigate_banner_links(driver, data):

        driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["logo_banner"]))
        assert driver.title == data["TITLES"]["home_title"]

        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, data["ELEMENTS"]["voice_banner"]))
        assert driver.title == data["TITLES"]["voice_title"]

        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, data["ELEMENTS"]["soundbar_banner"]))
        assert driver.title == data["TITLES"]["soundbar_title"]

        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, data["ELEMENTS"]["voicelab_banner"]))
        assert driver.title == data["TITLES"]["voicelab_title"]
