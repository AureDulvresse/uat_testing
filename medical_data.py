import logging
from selenium.webdriver.common.by import By
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
            # Accéder au module "Configuration" d'abord
            Actions.access_configuration(driver)
            
            # Accès aux "Données générales"
            general_data_div = driver.find_element(By.XPATH, "//*[contains(@class, 'div_class_name') and contains(., 'Données générales')]")
            general_data_element = general_data_div.find_element(By.XPATH, ".//*[contains(text(), 'Données générales')]")
            general_data_element.click()
            time.sleep(2)
            Actions.logger.info("\033[92mAccès réussi aux Données générales.\033[0m")
        except Exception as e:
            Actions.logger.error("\033[91mÉchec de l'accès aux Données générales : %s\033[0m", str(e))
import logging
from selenium.webdriver.common.by import By
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
            # Accéder au module "Configuration" d'abord
            Actions.access_configuration(driver)
            
            # Accès aux "Données générales"
            general_data_div = driver.find_element(By.XPATH, "//*[contains(@class, 'div_class_name') and contains(., 'Données générales')]")
            general_data_element = general_data_div.find_element(By.XPATH, ".//*[contains(text(), 'Données générales')]")
            general_data_element.click()
            time.sleep(2)
            Actions.logger.info("\033[92mAccès réussi aux Données générales.\033[0m")
        except Exception as e:
            Actions.logger.error("\033[91mÉchec de l'accès aux Données générales : %s\033[0m", str(e))
import logging
from selenium.webdriver.common.by import By
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
            # Accéder au module "Configuration" d'abord
            Actions.access_configuration(driver)
            
            # Accès aux "Données générales"
            general_data_div = driver.find_element(By.XPATH, "//*[contains(@class, 'div_class_name') and contains(., 'Données générales')]")
            general_data_element = general_data_div.find_element(By.XPATH, ".//*[contains(text(), 'Données générales')]")
            general_data_element.click()
            time.sleep(2)
            Actions.logger.info("\033[92mAccès réussi aux Données générales.\033[0m")
        except Exception as e:
            Actions.logger.error("\033[91mÉchec de l'accès aux Données générales : %s\033[0m", str(e))
