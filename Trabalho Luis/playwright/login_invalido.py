from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    # Login inválido
    page.fill("#user-name", "fake_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")

    # Validar mensagem de erro
    erro = page.locator(".error-message-container")
    erro.wait_for()
    print("✔ Mensagem de erro exibida:", erro.text_content())

    # Validar que permanece no login
    if page.url == "https://www.saucedemo.com/":
        print("✔ Permaneceu na tela de login")
    else:
        print("❌ Saiu da tela de login")

    browser.close()
