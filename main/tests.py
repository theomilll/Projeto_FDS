from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .forms import SignUpForm
class cleo(TestCase):
    def test(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(r"C:\Users\caiob\OneDrive\Área de Trabalho\driver chrome\chromedriver.exe", options=chrome_options)

        driver.get("http://127.0.0.1:8000/")
        register = driver.find_element(By.ID,"signUp")
        register.click()
        time.sleep(2)
        username_register = driver.find_element(By.NAME,"username")
        username_register.click()
        username_register.send_keys("thanos")
        time.sleep(1)
        email_register = driver.find_element(By.NAME,"email")
        email_register.click()
        email_register.send_keys("thanos@gmail.com")
        time.sleep(1)
        password_register = driver.find_element(By.NAME,"password1")
        password_register.click()
        password_register.send_keys("inevitavel40")
        time.sleep(1)
        confirm_register = driver.find_element(By.NAME,"password2")
        confirm_register.click()
        confirm_register.send_keys("inevitavel40")
        time.sleep(2)
        botao_registrar = driver.find_element(By.XPATH, '//button[text()="Sign Up"]')
        botao_registrar.click()

        login = driver.find_element(By.ID,"signIn")
        login.click()
        username = driver.find_element(By.ID,"username")
        username.click()
        username.send_keys("thanos")
        time.sleep(2)
        password = driver.find_element(By.ID,"password")
        password.click()
        password.send_keys("inevitavel40")
        time.sleep(2)
        botao_login = driver.find_element(By.XPATH, '//button[text()="Log In"]')
        botao_login.click()
        adicionar_carrinho = driver.find_element(By.NAME,"Adicionar ao carrinho")
        adicionar_carrinho.click()
        time.sleep(2)
        driver.quit()
