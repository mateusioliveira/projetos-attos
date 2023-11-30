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
        driver.get("http://127.0.0.1:8000/ong/teste25/")
        nome = driver.find_element(By.NAME, 'nome')
        nome.send_keys('Julia')
        email = driver.find_element(By.NAME, 'email')
        email.send_keys('julia@gmail.com')
        email = driver.find_element(By.NAME, 'comentario')
        email.send_keys('Muito boa!')
        time.sleep(2)
        enviar = driver.find_element(By.NAME, 'enviar')
        enviar.click()
        comentario = driver.find_element(By.NAME, 'comentario')
        time.sleep(7)
        self.assertTrue(comentario.is_enabled(), "o comentario não foi encontrado")
