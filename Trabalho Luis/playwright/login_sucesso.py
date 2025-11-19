from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # coloque True se quiser oculto
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    # Login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Validar redirecionamento
    page.wait_for_url("**/inventory.html")
    print("✔ Redirecionamento OK")

    # Validar pelo menos 1 produto
    count = page.locator(".inventory_item").count()
    if count > 0:
        print(f"✔ Produtos encontrados: {count}")
    else:
        print("❌ Nenhum produto encontrado")

    browser.close()
