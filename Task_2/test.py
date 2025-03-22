from os import environ
import pytest
from appium import webdriver
import pprint
from datetime import date 

#capabilities = dict(
#    platformName='Android',
#    automationName='uiautomator2',
#    deviceName='1742635064076',
#    appPackage='hko.MyObservatory_v1_0',
#    appActivity='hko.homepage3.HomepageActivity',
#    language='en',
#    locale='US',
#    noReset=True
#)

#appium_server_url = 'http://localhost:4723'

@pytest.fixture(scope='session')
def driver(request):
    server_url = 'http://localhost:4723'
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '16.0'
    desired_caps['deviceName'] = '1742635064076'
    desired_caps['appPackage'] = 'hko.MyObservatory_v1_0'
    desired_caps['appActivity'] = 'hko.homepage3.HomepageActivity'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['noReset'] = True
    desired_caps['enableMultiWindows'] = True

    driver = webdriver.Remote(server_url, desired_caps)
    def fin():
        driver.quit()
    request.addfinalizer(fin)
    return driver

def test_setup_android(driver):
    month_map ={
        '1':'Jan',
        '2':'Feb',
        '3':'Mar',
        '4':'Apr',
        '5':'May',
        '6':'Jun',
        '7':'Jul',
        '8':'Aug',
        '9':'Sep',
        '10':'Oct',
        '11':'Nov',
        '12':'Dec'
    }
    todays_date = date.today()
    print("Current month:", todays_date.month) 
    print("Current day:", todays_date.day)
    print("Current month:", month_map[str(todays_date.month)])
    menu_button = driver.find_element_by_accessibility_id('Navigate up')
    menu_button.click()
    try:
        nine_day_forecast = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and @text="9-Day Forecast"]')
    except:
        forecast_service = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and @text="Forecast & Warning Services"]')
        forecast_service.click()
        nine_day_forecast = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and @text="9-Day Forecast"]')
    nine_day_forecast.click()
    try:
        driver.find_element_by_xpath('//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_date"]')
    except:
        driver.implicitly_wait(5)
    #source = driver.page_source
    #pprint.pprint(source)
    first_day_date = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_date"]')
    print(first_day_date.text)
    assert first_day_date.text == str(todays_date.day + 1) + " " + str(month_map[str(todays_date.month)])