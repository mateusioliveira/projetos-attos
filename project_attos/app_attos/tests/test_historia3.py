from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

class Historia3(LiveServerTestCase):
    def test_01(self):
        driver.get("http://127.0.0.1:8000")
        try:
            email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
            senha = driver.find_element(By.CSS_SELECTOR, "input[name='senha']")
        except NoSuchElementException:
            print("Email or senha element not found.")
            return

        email.send_keys("teste25@teste.com")
        senha.send_keys("123")
        entrar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,  ".submit"))
        )
        entrar.click()
        time.sleep(2)
        adicionar= driver.find_element(By.XPATH, "//button[@class='adicionar']")
        adicionar.click()
        name= driver.find_element(By.XPATH, "//input[@name='nomeRede']")
        link= driver.find_element(By.XPATH, "//input[@name='instagram_link']")
        time.sleep(2)
        name.send_keys("Instagram teste")
        link.send_keys("https://www.instagram.com/teste")
        time.sleep(2)
        confirmar = driver.find_element(By.CSS_SELECTOR, "input[name='confirmar1']")
        confirmar.click()
        confirmar_button = driver.find_element(By.CSS_SELECTOR, "input[name='confirmar1']")
        self.assertTrue(confirmar_button.is_enabled(), "O botão 'confirmar' não está selecionado")
