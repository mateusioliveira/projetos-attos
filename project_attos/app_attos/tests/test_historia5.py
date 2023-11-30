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

        email.send_keys("teste2557@teste.com")
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

        edit_perfil= driver.find_element(By.XPATH, "//textarea[@name='editar']")
        edit_perfil.click()
        time.sleep(2)

        edit_perfil.send_keys("ONG dedicada ao cuidado e proteção de animais vulneráveis, trabalhando incansavelmente para garantir o bem-estar e a qualidade de vida desses seres indefesos.")
        confirmar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Confirmar']"))
        )
        time.sleep(2)
        confirmar.click()

        driver.get("http://127.0.0.1:8000/ong/teste2557")

        nova_descricao= driver.find_element(By.XPATH, "//div[@name='descricao_perfil']")
        self.assertTrue(nova_descricao.is_enabled(), "a descrição não foi encontrada")
        time.sleep(2)