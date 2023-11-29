from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time



options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

class Historia4(LiveServerTestCase):
    def test_0(self):
        driver.get("http://127.0.0.1:8000")
        try:
            submit2 = driver.find_element(By.CLASS_NAME, "submit2")
            submit2.click()
            time.sleep(3)

            nome_usuario = driver.find_element(By.NAME, "nome-usuario")
            nome_usuario.send_keys("TesteNomee")
            time.sleep(3)

            email = driver.find_element(By.NAME, "email")
            email.send_keys("teste@teste1.com")
            time.sleep(3)

            senha = driver.find_element(By.NAME, "senha")
            senha.send_keys("senha123")
            time.sleep(3)
            
        
            botao_submit = driver.find_element(By.CLASS_NAME, "submit")
            botao_submit.click()
            time.sleep(3)

            elemento_adicionar = driver.find_element(By.CLASS_NAME, "adicionar")
            assert elemento_adicionar.is_displayed(), "Elemento 'adicionar' não encontrado após a submissão"

        except NoSuchElementException as e:
            print("Elemento não encontrado:", e)