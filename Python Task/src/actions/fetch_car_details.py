import os
import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.questions.car_details_checklist import CarDetailsCheckList


def take_screenshot(driver, name):
    screenshots_dir = "reports/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
    print(f"Screenshot saved: {screenshot_path}")



class FetchCarDetails:
    make = ""
    model = ""
    year = ""

    @staticmethod
    def fetch(reg_number):
        url = "https://car-checking.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

        try:
            search_box = driver.find_element(By.XPATH, "//*[@id='subForm1']")
            search_box.send_keys(reg_number)
            search_box.send_keys(Keys.RETURN)

            make_element = driver.find_element(By.XPATH, CarDetailsCheckList.CAR_MAKE)
            model_element = driver.find_element(By.XPATH, CarDetailsCheckList.CAR_MODEL)
            year_element = driver.find_element(By.XPATH, CarDetailsCheckList.CAR_YEAR)

            # Highlight elements for verification
            driver.execute_script("arguments[0].style.border='3px solid red'", make_element)
            driver.execute_script("arguments[0].style.border='3px solid red'", model_element)
            driver.execute_script("arguments[0].style.border='3px solid red'", year_element)

            make = make_element.text
            model = model_element.text
            year = year_element.text
            take_screenshot(driver, f"success_{reg_number}")
            print(f"Extracted Details for {reg_number}: MAKE={make}, MODEL={model}, YEAR={year}")

            return {
                "VARIANT_REG": reg_number,
                "MAKE": make,
                "MODEL": model,
                "YEAR": year
            }
        except Exception as e:
            print(f"Error fetching details for {reg_number}: {e}")
            take_screenshot(driver, f"failure_{reg_number}")
            return {"VARIANT_REG": reg_number, "MAKE": "NOT FOUND", "MODEL": "NOT FOUND", "YEAR": "NOT FOUND"}
        finally:
            driver.quit()
