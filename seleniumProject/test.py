#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from POMProject.FAQ.faq import FAQ
from POMProject.Home.home import Home
from POMProject.Account.account import Account


def get_json_data():
    with open('Resources/data.json', 'r', encoding="utf-8") as file:
        return json.load(file)


class TestWebsite:

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get("https://www.voicemod.net/")
        self.data = get_json_data()
        yield
        self.driver.close()
        self.driver.quit()
        print("\n-----TEST DONE-----")

    @pytest.mark.skipif(False, reason="Test skipped by user")
    def test1_download_voicemod_free(self):
        """
        Using the button "DOWNLOAD VOICEMOD FOR FREE" the user will be able to download the executable file to install 
        the software on his computer.
        """""
        print("TEST #1 - Download Voicemod for free")
        Home.click_download_buttom(self.driver, data=self.data)

    @pytest.mark.skipif(False, reason="Test skipped by user")
    def test2_create_new_account(self):
        """

        """""
        print("TEST #2 - Create a new account")
        Account.create_new_account(self.driver, data=self.data)

    @pytest.mark.skipif(False, reason="Test skipped by user")
    def test3_main_links(self):
        """
        By clicking on the links "Voicemod" logo, "Soundboard", "FreeSounds"... I can navigate to different sections of 
        the front-end.
        """""
        print("TEST #3 - Main links")
        Home.navigate_banner_links(self.driver, data=self.data)

    @pytest.mark.skipif(False, reason="Test skipped by user")
    def test4_faq_searching(self):
        """
        By using the search bar, we will be able to enter a topic we wish to search for and the page will give us 
        results relevant to our search.
        """""
        print("TEST #4 - FAQ searching")
        FAQ.navigate_to_faq(self.driver, data=self.data)

    @pytest.mark.skipif(False, reason="Test skipped by user")
    def test5_feedback_support(self):
        """
        By accessing the support form and completing it I will be able to submit my support request.
        """""
        print("TEST #5 - Feedback & Support")
        FAQ.submit_request(self.driver, data=self.data)
