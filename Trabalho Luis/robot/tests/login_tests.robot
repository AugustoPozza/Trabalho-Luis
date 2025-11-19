*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    https://www.saucedemo.com    chrome
Suite Teardown    Close Browser
Resource    ../resources/keywords.robot

*** Test Cases ***
Cenario A - Login Bem Sucedido
    [Documentation]    Login com standard_user e validações
    Login Com Credenciais    standard_user    secret_sauce
    Location Should Contain    /inventory.html
    Page Should Contain Element    css:.inventory_item    # verifica pelo menos um produto

Cenario B - Login Invalido
    [Documentation]    Usuario inválido deve exibir erro e permanecer no login
    Input Text    id:user-name    fake_user
    Input Text    id:password     some_password
    Click Button    id:login-button
    Page Should Contain Element    css:.error-message-container
    Location Should Be    https://www.saucedemo.com/
