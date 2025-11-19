from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validar redirecionamento
    WebDriverWait(driver, 5).until(EC.url_contains("/inventory.html"))
    print("✔ Redirecionamento OK")

    # Validar que existe pelo menos 1 produto
    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    if len(produtos) > 0:
        print("✔ Produtos encontrados: teste aprovado!")
    else:
        print("❌ Nenhum produto encontrado!")

finally:
    driver.quit()
