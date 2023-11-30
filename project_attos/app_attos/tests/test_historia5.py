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

class Historia5(LiveServerTestCase):
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
        time.sleep(2)
        editar_botao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='botao_editar']"))
        )
        editar_botao.click()
        time.sleep(2)
        edit_perfil= driver.find_element(By.XPATH, "//textarea[@name='perfil']")
        edit_perfil.clear()
        time.sleep(2)
        edit_perfil.send_keys("ONG dedicada ao cuidado e proteção de animais vulneráveis, trabalhando incansavelmente para garantir o bem-estar e a qualidade de vida desses seres indefesos.")
        assert edit_perfil.get_attribute('value') == "ONG dedicada ao cuidado e proteção de animais vulneráveis, trabalhando incansavelmente para garantir o bem-estar e a qualidade de vida desses seres indefesos."
        confirmar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Confirmar']"))
        )
        time.sleep(2)
        confirmar.click()
        confirmar = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, "//input[@value='Confirmar']"))
        )
        assert confirmar.is_enabled()
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/ong/teste25")
        assert "ONG dedicada ao cuidado e proteção de animais vulneráveis, trabalhando incansavelmente para garantir o bem-estar e a qualidade de vida desses seres indefesos." in driver.page_source
    