from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumModule:
    def __init__(self, driver_path, base_url, wait_time):
        self.driver_path = driver_path
        self.base_url = base_url
        self.wait_time = wait_time
        self.driver = None

    def setup_driver(self):
        service = Service(self.driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get(self.base_url)

    def get_element_properties(self, locator):
        wait = WebDriverWait(self.driver, self.wait_time)
        element = wait.until(EC.visibility_of_element_located(locator))
        return {
            "background_color": element.value_of_css_property("background-color"),
            "font_family": element.value_of_css_property("font-family"),
            "color": element.value_of_css_property("color"),
            "font_size": element.value_of_css_property("font-size"),
            "font_weight": element.value_of_css_property("font-weight"),
            "background_image": element.value_of_css_property("background-image"),
            "background_size": element.value_of_css_property("background-size"),
            "background_position": element.value_of_css_property("background-position"),
            "background_repeat": element.value_of_css_property("background-repeat"),
            "width": element.value_of_css_property("width"),
            "height": element.value_of_css_property("height"),
            "display": element.value_of_css_property("display"),
            "box_shadow": element.value_of_css_property("box-shadow"),
            "border_radius": element.value_of_css_property("border-radius"),
            "position": element.value_of_css_property("position"),
            "left": element.value_of_css_property("left"),
            "top": element.value_of_css_property("top"),
            "box_sizing": element.value_of_css_property("box-sizing"),
            "padding": element.value_of_css_property("padding")
        }

    def teardown(self):
        if self.driver:
            self.driver.quit()
