import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.AddcustomerPage import AddcustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_004_SearchCustomerByEmail:

    self.logger.info('------------ Test_004_SearchCustomerByEmail -----------')

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):

        self.logger.info('------------ Start Test Search Customer By Email -----------')

        self.driver = setup

        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        if self.lp.title == 'Dashboard / nopCommerce administration':
            self.logger.info('-------------- Login Successful --------------')
            self.logger.info('-------------- Starting Search Customer By Email Test --------------')

            self.addcust = AddcustomerPage(self.driver)
            self.addcust.clickOnCustomersMenu()
            self.addcust.clickOnCustomersMenuitem()

            self.logger.info('-------------- Searching Customer By Email ID --------------')

            self.searchcust = SearchCustomer(self.driver)
            self.searchcust.setEmail('dilshad@gmail.com')
            self.searchcust.clicksearch()
            time.sleep(5)

            status = self.searchcust.searchCustomerByEmail('dilshad@gmail.com')
            assert True == status
            self.logger.info('------------- Search_CustomerByEmail_004_Finished -------------')
            self.driver.close()
