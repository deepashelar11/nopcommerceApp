import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.AddcustomerPage import AddcustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_005_SearchCustomerByName:

    self.logger.info('------------ Test_005_SearchCustomerByName -----------')

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):

        self.logger.info('------------ Start Test Search Customer By Name -----------')

        self.driver = setup

        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        if self.lp.title == 'Dashboard / nopCommerce administration':
            self.logger.info('-------------- Login Successful --------------')
            self.logger.info('-------------- Starting Search Customer By Name Test --------------')

            self.addcust = AddcustomerPage(self.driver)
            self.addcust.clickOnCustomersMenu()
            self.addcust.clickOnCustomersMenuitem()

            self.logger.info('-------------- Searching Customer By Name --------------')

            self.searchcust = SearchCustomer(self.driver)
            self.searchcust.setFirstName('dilshad')
            self.searchcust.setLaststName('sharma')
            self.searchcust.clicksearch()
            time.sleep(5)

            status = self.searchcust.searchCustomerByName('dilshad')
            assert True == status
            self.logger.info('------------- Search_CustomerByName_005_Finished -------------')
            self.driver.close()
