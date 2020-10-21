__author__ = 'Souvik'
'''
Test Case Description : Navigation test different items under purchase without unittest
'''
import Toolbox
import Snapshot

def TC_002_run():
    Toolbox.get_data(TC_002, 'TC_002')  # sending the TC_002 Class Function and the Testcase Name in string


def TC_002(test_data1 = '0', test_data2 = '0', val='No Run', ):

    try:

        s = Toolbox.Setup()
        s.std_login()
        d = s.driver

        item_id = 'item_' + test_data1 + '_title_link'
        de_item = d.find_element_by_id(item_id)
        de_item.click()
        d.implicitly_wait(2)

        de_item = d.find_element_by_css_selector(".btn_primary")
        de_item.click()
        d.implicitly_wait(1)

        de_item = d.find_element_by_css_selector(".btn_secondary")
        de_item.click()
        d.implicitly_wait(1)

        de_item = d.find_element_by_css_selector(".inventory_details_back_button")
        de_item.click()

        if d.current_url == 'https://www.saucedemo.com/inventory.html':
            val = "Pass"
        else:
            val = "Fail"
            Snapshot.grab_snap('TC_002_Fail')

        d.quit()
        return val

    except:
        Snapshot.grab_snap('TC_002_Fail')
        print('ERROR in execution of TC002')
        d.quit()
        return "Fail"

if __name__ == '__main__':
    TC_002_run()

