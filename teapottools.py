from selenium import webdriver
from time import sleep

class TeapotTools():
    def __init__(self, gecko_exec, delay=2):
        self.driver = webdriver.Firefox(executable_path=gecko_exec)

        self.driver.get('https://google.com/teapot')
        sleep(delay) #page has to load first

        self.teabot = self.driver.find_element_by_id('teabot')

    def rotate(self, degrees):
        return self.driver.execute_script("arguments[0].setAttribute('style', 'transform: rotate({}deg);')".format(degrees), self.teabot)

    def pour(self):
        return self.driver.execute_script("arguments[0].setAttribute('class', 'tip pour')", self.teabot)

    def unpour(self):
        return self.driver.execute_script("arguments[0].setAttribute('class', '')", self.teabot)
