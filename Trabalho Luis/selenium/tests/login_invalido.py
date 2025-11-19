from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Login inválido
    driver.find_element(By.ID, "user-name").send_keys("fake_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # Validar mensagem de erro
    erro = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container"))
    )
    print("✔ Mensagem de erro exibida:", erro.text)

    # Validar que continua na tela de login
    if driver.current_url == "https://www.saucedemo.com/":
        print("✔ Continuou na tela de login")
    else:
        print("❌ Foi para outra página!")

finally:
    driver.quit()
