import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_login:

    baseURL = ReadConfig.getApplicationURL()
    path = '.\\TestData\\LoginData.xlsx'

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info('-------------- test_login_ddt -------------')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.column = XLUtils.getColumnCount(self.path, 'Sheet1')

        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            ac_title = 'Dashboard / nopCommerce administration'
            exp_title = self.driver.title

            if ac_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info('passed')
                    #self.lp.clickLogout()
                    lst_status.append('pass')
                elif self.exp == 'fail':
                    self.logger.info('failed')
                    #self.lp.clickLogout()
                    lst_status.append('fail')
            elif ac_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info('failed')
                    lst_status.append('fail')
                elif self.exp == 'fail':
                    self.logger.info('passed')
                    lst_status.append('pass')

        if 'fail' in lst_status:
            self.logger.info('-------------- test_login_ddt is failed -------------')
            self.driver.close()
            assert False
        else:
            self.logger.info('-------------- test_login_ddt is passed -------------')
            self.driver.close()
            assert True
