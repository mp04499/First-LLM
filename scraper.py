from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json

# for holding the resultant list
categories = ["physical", "special", "other"]
dataset = []

driver = webdriver.Chrome()


moveset = []
page_url = "https://www.serebii.net/attackdex-dp/"

for category in categories:
    driver.get(page_url + category + ".shtml")

    effects = driver.find_elements(By.CLASS_NAME, "fooinfo")
    for i in range(len(effects)):
        if i % 2 != 0:
            moveset.append(
                {
                    "category": category,
                    "effect": effects[i].text
                }
            )

driver.close()

# print(moveset)
with open('movesets.json', 'w') as fp:
    json.dump(moveset, fp)