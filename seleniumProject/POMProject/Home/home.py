from selenium.webdriver.common.by import By


class Home:

    @staticmethod
    def click_download_buttom(driver, data):
        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["download_bottom"]).click()
        """The perfect assertion in this verification would be to check if Selenium has correctly downloaded the 
        executable file, we could check the binaries, size, metadata... However, in my environment I use MAC OS and I 
        have seen that there is no version available to download voicemod on MAC. 
        We can check it with os.path.isfile ()
        """

    @staticmethod
    def navigate_banner_links(driver, data):

        driver.find_element(By.CSS_SELECTOR, data["ELEMENTS"]["logo_banner"]).click()
        assert driver.title == data["TITLES"]["home_title"], "The page title should be "+data["ELEMENTS"][
            "logo_banner"]+" but the current is "+driver.title

        driver.find_element(By.XPATH, data["ELEMENTS"]["voice_banner"]).click()
        assert driver.title == data["TITLES"]["voice_title"], "The page title should be " + data["ELEMENTS"][
            "logo_banner"] + " but the current is " + driver.title

        driver.find_element(By.XPATH, data["ELEMENTS"]["soundbar_banner"]).click()
        assert driver.title == data["TITLES"]["soundbar_title"], "The page title should be " + data["ELEMENTS"][
            "logo_banner"] + " but the current is " + driver.title

        driver.find_element(By.XPATH, data["ELEMENTS"]["voicelab_banner"]).click()
        assert driver.title == data["TITLES"]["voicelab_title"], "The page title should be " + data["ELEMENTS"][
            "logo_banner"] + " but the current is " + driver.title
