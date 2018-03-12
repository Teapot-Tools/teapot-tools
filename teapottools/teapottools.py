from selenium import webdriver
from time import sleep

class TeapotTools():
    def __init__(self, browser, driver_exec, delay=2):
        browsers = {
        "Firefox": webdriver.Firefox,
        "Chrome": webdriver.Chrome,
        "Ie": webdriver.Ie,
        "Opera": webdriver.Opera
        }

        try:
            self.driver = browsers[browser](executable_path=driver_exec)
        except KeyError:
            raise ValueError("Invalid browser passed! Valid arguments are 'Firefox', 'Chrome', 'Ie' and 'Opera'")

        self.driver.get('https://google.com/teapot')
        sleep(delay) #page has to load first

        self.teabot = self.driver.find_element_by_id('teabot')

    def rotate(self, degrees):
        return self.driver.execute_script("arguments[0].setAttribute('style', 'transform: rotate({}deg);')".format(degrees), self.teabot)

    def pour(self):
        return self.driver.execute_script("arguments[0].setAttribute('class', 'tip pour')", self.teabot)

    def unpour(self):
        return self.driver.execute_script("arguments[0].setAttribute('class', '')", self.teabot)

    def reset(self):
        self.driver.execute_script("arguments[0].setAttribute('style', 'transform: rotate({}deg);')".format(0), self.teabot)
        self.driver.execute_script("arguments[0].setAttribute('class', '')", self.teabot)

    def close(self):
        self.driver.close()
