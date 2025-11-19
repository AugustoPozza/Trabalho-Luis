from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    # Login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")

    # Adicionar backpack ao carrinho
    page.click("#add-to-cart-sauce-labs-backpack")

    # Ir ao carrinho
    page.click(".shopping_cart_link")
    page.wait_for_url("**/cart.html")

    # Validar produto no carrinho
    carrinho_texto = page.text_content(".cart_list")
    print("Itens no carrinho:")
    print(carrinho_texto)

    # Checkout
    page.click("#checkout")

    page.fill("#first-name", "Test")
    page.fill("#last-name", "User")
    page.fill("#postal-code", "12345")

    page.click("#continue")
    page.wait_for_url("**/checkout-step-two.html")

    # Validar resumo
    resumo = page.text_content(".summary_info")
    print("Resumo do pedido:")
    print(resumo)

    # Finalizar compra
    page.click("#finish")
    page.wait_for_url("**/checkout-complete.html")

    mensagem = page.text_content(".complete-header")
    print("✔ Compra finalizada:", mensagem)

    browser.close()
