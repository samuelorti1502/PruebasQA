from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

cap:Dict[str, Any] = {
    'platformName':'Android',
    'platformVersion':'14',
    'automationName':'uiautomator2',
    'deviceName':'mondrian',
    'appPackage':'com.sortizm.GeoFuelGTV2',
    'appActivity':'.MainActivity',
    "autoGrantPermissions":"true",
    "autoAcceptAlerts":"true",
}

appium_server_url = 'http://localhost:4723/wd/hub'

driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(cap))

tiempo = 3;

#1. Carga de estaciones en listado
el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="󰺸, Encuentra"]')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)

print("Prueba 1 ejecutada con exito")

#2. Barra de busqueda de lugar
el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Busca aquí"]')
time.sleep(tiempo)
el.click()
el.send_keys("Mixco")

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Mixco Zona 1, 5A Calle, Ciudad de Guatemala, Guatemala"]/android.view.ViewGroup')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Mapa"]')
time.sleep(tiempo)
el.click()

print("Prueba 2 ejecutada con exito")

#10. Configuracion de cantidad a mostrar
el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc=", Configuracion"]')
time.sleep(tiempo)
el.click()
time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Ingrese un valor"]')
time.sleep(tiempo)
el.send_keys("5")

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="󰺸, Encuentra"]')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Lista"]')
time.sleep(tiempo)
el.click()

print("Prueba 3 ejecutada con exito")

#11. Configuracion de esstacion preferida
time.sleep(tiempo)
el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc=", Configuracion"]')
time.sleep(tiempo)
el.click()
time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="android:id/text1"]')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)
buttons_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Aro"]')
time.sleep(tiempo)
grid_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Jm"]')
time.sleep(tiempo)
# Swipe Up
driver.swipe(start_x=grid_el.location['x'], start_y=grid_el.location['y'], end_x=buttons_el.location['x'], end_y=buttons_el.location['y'])

time.sleep(tiempo)
el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Puma Energy"]')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="󰺸, Encuentra"]')
time.sleep(tiempo)
el.click()

print("Prueba 4 ejecutada con exito")

#6. Boton Flash 7. Boton Captura
time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc=", Captura"]')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text=""]')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[2]')
time.sleep(tiempo)
el.click()

time.sleep(5)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="CERRAR"]')
time.sleep(tiempo)
el.click()

time.sleep(5)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text=""]')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[2]')
time.sleep(tiempo)
el.click()

time.sleep(tiempo)

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="CERRAR"]')
time.sleep(tiempo)
el.click()

print("Pruebas 5 y 6 ejecutadas con exito")


""" driver.quit() """