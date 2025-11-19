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
    WebDriverWait(driver, 5).until(EC.url_contains("/inventory.html"))

    # Adicionar item ao carrinho
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Acessar carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 5).until(EC.url_contains("/cart.html"))

    # Validar item presente
    itens_carrinho = driver.find_element(By.CLASS_NAME, "cart_list").text
    print("Itens no carrinho:")
    print(itens_carrinho)

    # Checkout
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Validar resumo
    resumo = driver.find_element(By.CLASS_NAME, "summary_info").text
    print("Resumo do pedido:")
    print(resumo)

    # Finalizar compra
    driver.find_element(By.ID, "finish").click()
    WebDriverWait(driver, 5).until(EC.url_contains("checkout-complete"))

    mensagem = driver.find_element(By.CLASS_NAME, "complete-header").text
    print("✔ Compra finalizada:", mensagem)

finally:
    driver.quit()
