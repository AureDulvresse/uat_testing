import logging
from colorlog import ColoredFormatter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Actions:
    # Initialisation du logger
    logger = logging.getLogger("Actions")
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
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)

    @staticmethod
    def access_configuration(driver):
        """
        Accède au module "Configuration" dans l'application.

        Args:
            driver: Instance du navigateur web.

        Returns:
            None
        """
        try:
            # Attendre que l'élément soit cliquable et cliquer
            configuration_module = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Configuration')]"))
            )
            configuration_module.click()
            Actions.logger.info("Accès réussi au module Configuration.")
        except Exception as e:
            Actions.logger.error("Échec de l'accès au module Configuration : %s", str(e))

    @staticmethod
    def access_general_data(driver):
        """
        Accède aux "Données générales" dans l'application.

        Args:
            driver: Instance du navigateur web.

        Returns:
            None
        """
        try:
            # Accéder au module "Configuration" d'abord
            Actions.access_configuration(driver)
            
           # Attendre que l'élément contenant "Données générales" soit visible et cliquable, puis cliquer en utilisant JavaScript
            general_data_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Données générales')]"))
            )
            driver.execute_script("arguments[0].click();", general_data_element)
            Actions.logger.info("Accès réussi aux Données générales.")
        except Exception as e:
            Actions.logger.error("Échec de l'accès aux Données générales : %s", str(e))

        time.sleep(2000)
