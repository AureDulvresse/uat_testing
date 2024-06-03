import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class Actions:
    # Initialisation du logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("Actions")

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
            # Accès au module "Configuration"
            configuration_module = driver.find_element(By.XPATH, "//*[contains(text(), 'Configuration')]")
            configuration_module.click()
            time.sleep(2)
            Actions.logger.info("\033[92mAccès réussi au module Configuration.\033[0m")
        except Exception as e:
            Actions.logger.error("\033[91mÉchec de l'accès au module Configuration : %s\033[0m", str(e))

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
            
            # Accès aux "Données générales"
            # Cliquer sur l'élément contenant le texte "Données médicales"
            donnee_medicale_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'div_class_name') and contains(., 'Données générales')]"))
            )
            donnee_medicale_element.click()
            time.sleep(2)
            Actions.logger.info("\033[92mAccès réussi aux Données générales.\033[0m")
        except Exception as e:
            Actions.logger.error("\033[91mÉchec de l'accès aux Données générales : %s\033[0m", str(e))
