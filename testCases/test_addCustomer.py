import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddcustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_003_AddCustomer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):

        self.logger.info('------------------- Test_003_AddCustomer -------------------')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        if self.lp.title == 'Dashboard / nopCommerce administration':
            self.logger.info('-------------- Login Successful --------------')
            self.logger.info('-------------- Starting Add_Customer Test --------------')

            self.addcust = AddcustomerPage(self.driver)
            self.addcust.clickOnCustomersMenu()
            self.addcust.clickOnCustomersMenuitem()

            self.addcust.clickOnAddnew()

            self.logger.info('----------- Providing Customer Info ----------')

            self.email = random_generator() + '@gmail.com'
            self.addcust.setEmail(self.email)
            self.addcust.setPassword('test123')
            self.addcust.setCustomerRoles('Guests')
            self.addcust.setManagerOfVendor('Vender 2')
            self.addcust.setGender('Male')
            self.addcust.setFirstName('Deepa')
            self.addcust.setLastName('shelar')
            self.addcust.setDob('11/2/1990')
            self.addcust.setCompanyName('busyQA')
            self.addcust.setAdminContent('This is for testing purpose ...')
            self.addcust.clickOnSave()

            self.logger.info('--------- Saving customer info --------')

            self.logger.info('----------- Add customer validation started ------------')

            self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

            print(self.msg)
            if 'customer has been added successfully.' in self.msg:
                self.logger.info('---------- Add customer test passed ----------')
                self.driver.close()
                assert True
            else:
                self.driver.save_screenshot('.\\Screenshots\\'+'test_addCustomer.png')
                self.logger.error('----- Add Customer Test Failed ------')
                self.driver.close()
                assert False

        else:
            self.driver.save_screenshot('.\\Screenshots\\'+'test_addCustomer.png')
            self.driver.close()
            self.logger.error('---------------- Test_003_AddCustomer Failed ----------------- ')
            assert False

import random
import string

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))