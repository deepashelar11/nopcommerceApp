from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AddcustomerPage:

    # Add locators
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    lnkCustomer_menu_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(), ' Customers')]"
    btnAddnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = 'Gender_Male'
    rdFemaleGender_id = 'Gender_Female'
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrator_xpath = "//li[contains(text(), 'Administrators)]"
    lstitemRegistered_xpath = "//li[contains(text(), 'Registered)]"
    lstitemGuests_xpath = "//li[contains(text(), 'Guests)]"
    lstitemVendors_xpath = "//li[contains(text(), 'Vendors)]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminContent']"
    btnSave_xpath = "//button[@name='save']"

    # Initialize web driver
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_item_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).click()
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath).click()
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrator_xpath).click()
        elif role == 'Guest':
            # Here user can be only Registered ( OR) guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerroleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath).click()
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath).click()
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath).click()
        time.sleep(3)

        # self.listitem.click()

        # If Selenium fails to locate the element reliably, you can execute JavaScript to find and interact with it
        self.driver.execute_script("arguments[0].click;", self.listitem)


    def setManagerOfVendor(self, value):
        drp = select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_vissible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).click()
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).click()
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).click()
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).click()
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).click()
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()








