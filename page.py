from selenium import webdriver
from locator import MainPageLocators
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "q"


class BasePage:
    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.go_button)
        element.click()


class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
