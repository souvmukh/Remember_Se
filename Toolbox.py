__author__ = 'Souvik'

import time
from selenium import webdriver
import csv



# Setup class is used for connection and launch of browser
class Setup():

    def open_chrome(self, link='https://www.saucedemo.com/'):
        self.driver = webdriver.Chrome("/Users/Souvik/PycharmProjects/chrome_driver/chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        try:
            self.driver.get(link)
            time.sleep(5)
            print(str(time.strftime('%H:%M:%S'))+ "  Webpage opened in Chrome successfully")
        except:
            print(str(time.strftime('%H:%M:%S'))+ "  Exception opening Webpage on Chrome")

    #def open_firefox(self, link = 0): -- Not Developed





#Used to get test data from csv file for controlling and reporting Test Execution
def get_data(testcase_f, testcase_n):

    f = open('datasheet.csv', 'r', newline='')
    fout = open(str(int(time.monotonic()))+'_status.csv', 'w', newline='')
    file = csv.reader(f)
    fileout = csv.writer(fout)

    for row in file:
        tc = row[2]
        if tc == testcase_n:
            data1 = row[3]
            data2 = row[4]
            data3 = row[1]
            status = testcase_f(data1, data2, data3)
            l_status = (row[0], row[2], status)
            fileout.writerow(l_status)
    k = (time.asctime(),)
    fileout.writerow(k)
    f.close()
    fout.close()




if __name__ == '__main__':
    print("Toolbox Only")