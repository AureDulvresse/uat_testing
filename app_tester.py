import logging
from colorlog import ColoredFormatter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from medical_data import Actions

class AppTester:
    def __init__(self, app_url: str, username: str, password: str, driver='chrome'):
        self.app_url = app_url
        self.username = username
        self.password = password
        if driver == 'chrome': 
            self.driver = webdriver.Chrome()
        elif driver == 'edge':
            self.driver = webdriver.Edge()
        elif driver == 'firefox':
            self.driver = webdriver.Firefox()

        # Configuration du logger
        self.logger = logging.getLogger("AppTester")
        self.configure_logger()

    def configure_logger(self):
        formatter = ColoredFormatter(
            "%(log_color)s%(levelname)s: %(message)s",
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red,bg_white',
            },
            reset=True,
            style='%'
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        self.logger.setLevel(logging.INFO)

    def login(self):
        self.logger.info("Ouverture de l'URL de l'application")
        self.driver.get(self.app_url)
        time.sleep(2)
        
        self.logger.info("Saisie du nom d'utilisateur")
        login_field = self.driver.find_element(By.NAME, "username")
        login_field.send_keys(self.username)
        
        self.logger.info("Saisie du mot de passe")
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(2)

        self.logger.info("Clique sur le bouton de connexion")
        button = self.driver.find_element(By.ID, "headlessui-popover-button-:r0:")
        button.click()
        time.sleep(2)


    def run_tests(self):
        try:
            self.logger.info("Début des tests UAT")
            self.login()

            Actions.access_configuration(self.driver)
            Actions.access_general_data(self.driver)
            

            self.logger.info("Tous les tests UAT ont été réalisés avec succès !")

        except Exception as e:
            self.logger.error("Test UAT échoué : %s", str(e))

        finally:
            self.logger.info("Fermeture du navigateur")
            self.driver.quit()

