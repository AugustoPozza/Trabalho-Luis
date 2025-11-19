*** Keywords ***
Login Com Credenciais
    [Arguments]    ${user}    ${password}
    Input Text    id:user-name    ${user}
    Input Text    id:password     ${password}
    Click Button    id:login-button
    Wait Until Page Contains Element    css:.inventory_list
