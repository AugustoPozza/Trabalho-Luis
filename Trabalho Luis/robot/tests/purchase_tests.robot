*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    https://www.saucedemo.com    chrome
Suite Teardown    Close Browser
Resource    ../resources/keywords.robot

*** Test Cases ***
Cenario C - Fluxo de Compra Curto
    [Documentation]    Compra curta: add to cart, checkout, finalizar
    Login Com Credenciais    standard_user    secret_sauce
    Wait Until Element Is Visible    css:.inventory_list
    # Adicionar Sauce Labs Backpack
    Click Button    id:add-to-cart-sauce-labs-backpack
    Click Link    css:.shopping_cart_link
    Page Should Contain    Sauce Labs Backpack
    Click Button    id:checkout
    Input Text    id:first-name    Test
    Input Text    id:last-name     User
    Input Text    id:postal-code   12345
    Click Button    id:continue
    Page Should Contain    Overview
    Click Button    id:finish
    Page Should Contain    THANK YOU FOR YOUR ORDER
