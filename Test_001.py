__author__ = 'Souvik'
'''
Test Case Description : Example-Login to www.saucedemo.com with multiple users from csv file
'''
import Toolbox


def TC_001_run():
    Toolbox.get_data(TC_001,'TC_001')  # sending the Class Function and the Testcase Name


def TC_001(username='standard_user', password='secret_sauce', val='No Run'):

    s = Toolbox.Setup()
    s.open_chrome()
    d = s.driver
    d.implicitly_wait(2)

    de_username = d.find_element_by_id("user-name")
    de_password = d.find_element_by_id("password")
    de_button = d.find_element_by_id("login-button")

    de_username.clear()
    de_password.clear()

    de_username.send_keys(username)
    de_password.send_keys(password)
    de_button.click()
    d.implicitly_wait(2)

    if d.current_url == 'https://www.saucedemo.com/inventory.html':
        val = "Pass"
    else:
        val = "Fail"
    d.quit()
    return val

if __name__ == '__main__':
    TC_001_run()

