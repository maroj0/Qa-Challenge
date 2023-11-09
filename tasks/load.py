from screenplay.pattern import Actor, Task, Question
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from testlib.pages import SearchPage, ResultPage

class LoadPage(Task):
    def __init__(self, url: str) -> None:
        self.url = url

    def perform_as(self, actor: Actor) -> None:
        browser: WebDriver = actor.using('browser')
        browser.get(self.url)