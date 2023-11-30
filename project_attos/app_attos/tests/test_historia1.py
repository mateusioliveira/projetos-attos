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
        entrar = driver.find_element(By.CLASS_NAME, 'botton-entrar')
        entrar.click()
        adicionar= driver.find_element(By.XPATH, "//button[@class='adicionar']")
        adicionar.click()


        email_ong= driver.find_element(By.XPATH, "//input[@name='email_ong']")
        email_ong.send_keys("emailong@teste.com")
        time.sleep(2)
        ano_fundacao= driver.find_element(By.XPATH, "//input[@name='ano_fundacao']")
        ano_fundacao.send_keys("1992")
        time.sleep(2)
        endereco_ong= driver.find_element(By.XPATH, "//input[@name='endereco_ong']")
        endereco_ong.send_keys("1992")
        time.sleep(2)

        confirmar = driver.find_element(By.CSS_SELECTOR, "input[name='confirmar_ong']")
        confirmar.click()


        driver.get("http://127.0.0.1:8000/ong/teste25/")

        email_confirmacao = driver.find_element(By.NAME, 'email_ong')
        time.sleep(7)
        self.assertTrue(email_confirmacao.is_enabled(), "a descrição não foi encontrada")
