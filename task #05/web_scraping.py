from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

total_cases=[] 
total_deaths=[] 
total_recovered=[]
country=[]
driver.get("https://www.worldometers.info/coronavirus/#countries")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'tab-content'}):
    countries=a.find('div', attrs={'class':'sorting'})
    total_case=a.find('div', attrs={'class':'sorting_desc'})
    total_death=a.find('div', attrs={'class':'sorting'})
    total_recover=a.find('div', attrs={'class':'sorting'})
    
country.append(countries.text)
total_cases.append(total_case.text)
total_deaths.append(total_death.text)
total_recovered.append(total_recover.text)

df = pd.DataFrame({'total cases':total_cases,'total deaths':total_deaths,'total recovered':total_recovered}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
