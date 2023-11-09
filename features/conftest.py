"""
This module contains shared fixtures.
"""

import json
import pytest

from typing import Generator
# from screenplay.pattern import Actor
from screenpy import Actor, given, then, when
from screenpy import AnActor
from selenium.webdriver import Chrome, ChromeOptions, Firefox
from selenium.webdriver.remote.webdriver import WebDriver
from actors.userActor import User
from typing import Generator
from screenpy_selenium.abilities import BrowseTheWeb


@pytest.fixture
def config(scope='session') -> dict:

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config: dict) -> WebDriver:

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = Firefox()
    elif config['browser'] == 'Chrome':
        b = Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = ChromeOptions()
        opts.add_argument('headless')
        b = Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
    

@pytest.fixture(scope="function", name="Dev")
def fixture_actor() -> Generator:
    the_actor = Actor.named("Dev").who_can(BrowseTheWeb.using_chrome())
    yield the_actor
    the_actor.exit_stage_left()

@pytest.fixture(scope="function", name="Prod")
def fixture_prod_actor() -> Generator:
    the_actor = Actor.named("Prod").who_can(BrowseTheWeb.using_chrome())
    yield the_actor
    the_actor.exit_stage_left()