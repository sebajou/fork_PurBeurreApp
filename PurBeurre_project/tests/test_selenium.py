import os
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


# BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.path.join('/gecko')


class AccountTestCase(LiveServerTestCase):

    @pytest.mark.selenium_mk
    def test_create_then_login_user(self):
        driver = webdriver.Firefox(
            executable_path="/home/sebastien/Documents/Cours_Programation/Projet_8/PurBeurreApp/gecko/geckodriver")

        # Create user
        driver.get('http://127.0.0.1:8000/user_form/')
        username = driver.find_element_by_id('id_username')
        firstname = driver.find_element_by_id('id_first_name')
        lastname = driver.find_element_by_id('id_last_name')
        email = driver.find_element_by_id('id_email')
        diet = driver.find_element_by_id('id_diet_type_0')
        allergy = driver.find_element_by_id('id_alergy_0')
        psw1 = driver.find_element_by_id('id_password1')
        psw2 = driver.find_element_by_id('id_password2')
        submit = driver.find_element_by_id('submit')
        username.send_keys('seleium_test5_username')
        firstname.send_keys('seleium_test5_firstname')
        lastname.send_keys('seleium_test5_lastname')
        email.send_keys('seleium_test5_email@gmail.com')
        driver.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()
        driver.find_elements_by_css_selector("input[type='checkbox'][value='1']")[0].click()
        psw1.send_keys('seleium_test5_psw1AQWXSZ2')
        psw2.send_keys('seleium_test5_psw1AQWXSZ2')
        submit.send_keys(Keys.RETURN)

        # Logout
        driver.get('http://127.0.0.1:8000/accounts/logout/')

        # Login
        driver.get('http://127.0.0.1:8000/accounts/login/')
        username = driver.find_element_by_id('id_username')
        password = driver.find_element_by_id('id_password')
        submit = driver.find_element_by_id('submit')
        username.send_keys('legopolicier')
        password.send_keys('1AQWXSZ2')
        submit.send_keys(Keys.RETURN)

        # Search food
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "profile"))
        )
        search = driver.find_element_by_id('search')
        search.send_keys('choucroute')
        search.send_keys(Keys.RETURN)

        # Add food like favorite
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "favorite_submit_id_0"))
        )
        driver.find_element_by_id('favorite_submit_id_0').click()
        driver.implicitly_wait(20)
        driver.find_element_by_id('id_submit_off_0').click()
