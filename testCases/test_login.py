import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info('################ Test 001 Login ################')
        self.logger.info('################ Verifying home page title ################')

        # Initiate driver
        self.driver = setup

        # Launch application
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info('################ Verifying home page title is passed ################')
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error('################ Verifying home page title is failed ################')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info('################ Verifying login test ################')

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info('################ Verifying login test is passed ################')
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error('################ Verifying login test is failed ################')
            assert False
