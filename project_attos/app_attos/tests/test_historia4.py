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
class Historia4(LiveServerTestCase):
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
        foto= driver.find_element(By.XPATH, "//input[@name='foto']")
        time.sleep(2)
        foto.send_keys("/home/guilherme/Pictures/teste.png")
        time.sleep(2)
        botao_enviar = driver.find_element(By.XPATH, "//button[@name='enviar']")
        botao_enviar.click()
        confirmar_enviar= driver.find_element(By.XPATH, "//button[@name='enviar']")
        self.assertTrue(confirmar_enviar.is_enabled())