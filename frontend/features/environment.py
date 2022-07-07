import os
import sys
from selenium import webdriver
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


def before_all(context):
    context.driver = webdriver.Chrome(executable_path='..\\drivers\\chromedriver.exe')
    context.driver.delete_all_cookies()
    context.driver.maximize_window()


def before_feature(context, feature):
    if feature.name == 'Find professors':
        context.base_url = context.config.userdata['icmc_usp_url']
    elif feature.name == 'Find adress by cep':
        context.base_url = context.config.userdata['find_address_url']
