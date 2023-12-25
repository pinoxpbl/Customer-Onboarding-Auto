from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import os
from pathlib import Path

# Acessar o site e baixar a planilha

browser = webdriver.Chrome()
browser.get('https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html?_fsi=KkQkrgkA&_gl=1*1j3g7vh*_ga*OTU3ODQ2NDk5LjE3MDMyNTE5Mzk.*_ga_DG1BTLENXK*MTcwMzI1MTkzOS4xLjEuMTcwMzI1MjM0My4yMy4wLjA.&_ga=2.80322322.483533305.1703251939-957846499.1703251939&_fsi=KkQkrgkA')

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn customer-onboarding__btn-orange"]')))
browser.find_element(By.XPATH, '//a[@class="btn customer-onboarding__btn-orange"]').click()
sleep(2)

# Iniciando a planilha

for file in os.listdir(Path.home()/"Downloads/"):
    if file.startswith("customer") and file.endswith(".csv"):
        df = pd.read_csv(Path.home()/"Downloads/customer-onboarding-challenge.csv", sep=",")
        break

# Coletando informações
  
for i, name in enumerate(df["Company Name"]):
    id = df.loc[i, "Customer ID"]
    contact = df.loc[i, "Primary Contact"]
    street = df.loc[i, "Street Address"]
    city = df.loc[i, "City"]
    state = df.loc[i, "State"]
    zip_code = df.loc[i, "Zip"]
    email = df.loc[i, "Email Address"]
    offers = df.loc[i, "Offers Discounts"]
    nda = df.loc[i, "Non-Disclosure On File"]

#Inserindo Dados
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="customerName"]')))
    browser.find_element(By.XPATH, '//*[@id="customerName"]').send_keys(name)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="customerID"]')))
    browser.find_element(By.XPATH, '//*[@id="customerID"]').send_keys(id)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="primaryContact"]')))
    browser.find_element(By.XPATH, '//*[@id="primaryContact"]').send_keys(contact)  
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="street"]')))
    browser.find_element(By.XPATH, '//*[@id="street"]').send_keys(street)  
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="city"]')))
    browser.find_element(By.XPATH, '//*[@id="city"]').send_keys(city)  
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="state"]')))
    browser.find_element(By.XPATH, '//*[@id="state"]').send_keys(state)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="zip"]')))
    browser.find_element(By.XPATH, '//*[@id="zip"]').send_keys(str(zip_code))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    if offers == "YES":
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="activeDiscountYes"]')))
        browser.find_element(By.XPATH, '//*[@id="activeDiscountYes"]').click()
    else:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="activeDiscountNo"]')))
        browser.find_element(By.XPATH, '//*[@id="activeDiscountNo"]').click()

    if nda == "YES":
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="NDA"]')))
        browser.find_element(By.XPATH, '//*[@id="NDA"]').click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit_button"]')))
    browser.find_element(By.XPATH, '//*[@id="submit_button"]').click()


input()