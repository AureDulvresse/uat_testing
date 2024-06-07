import logging
from colorlog import ColoredFormatter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
    def access_laboratory(driver):
        """
        Accède au module "Laboratoire" dans l'application.

        Args:
            driver: Instance du navigateur web.

        Returns:
            None
        """
        try:
            # Attendre que l'élément soit cliquable et cliquer
            laboratory_module = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Laboratoire')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", laboratory_module)
            driver.execute_script("arguments[0].click();", laboratory_module)
            Actions.logger.info("Accès réussi au module Laboratoire.")
        except Exception as e:
            Actions.logger.error("Échec de l'accès au module Laboratoire : %s", str(e))

    @staticmethod
    def access_list_of_bons(driver):
        """
        Accède à "Liste des bons" dans le module Laboratoire.

        Args:
            driver: Instance du navigateur web.

        Returns:
            None
        """
        try:
            # Accéder au module "Laboratoire" d'abord
            Actions.access_laboratory(driver)
            
            # Attendre que l'élément contenant "Liste des bons" soit visible et cliquable, puis cliquer en utilisant JavaScript
            list_of_bons_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Liste des bons')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", list_of_bons_element)
            driver.execute_script("arguments[0].click();", list_of_bons_element)
            Actions.logger.info("Accès réussi à la Liste des bons.")
        except Exception as e:
            Actions.logger.error("Échec de l'accès à la Liste des bons : %s", str(e))
