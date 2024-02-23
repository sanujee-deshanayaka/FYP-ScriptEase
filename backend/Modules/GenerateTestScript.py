def generate_test_script(verb, locator, element, step_description, test_data=None):
    if verb.lower() == 'enter':
        script = f'driver.find_element({locator}).send_keys("{test_data}")'
    elif verb.lower() == 'click':
        script = f"driver.find_element({locator}).click()"
    elif verb.lower() == 'navigate':
        script = f"driver.implicitly_wait(2)"
    elif verb.lower() == 'verify':
        script = f'assert {locator}.text, "{element}"'
    else:
        script = "Unsupported action verb"

    return script


# -------java-------------
# def generate_test_script(verb, locator, element, step_description, test_data=None):
#     if verb.lower() == 'enter':
#         script = f'driver.findElement({locator}).sendKeys("{test_data}");'
#     elif verb.lower() == 'click':
#         script = f"driver.findElement({locator}).click();"
#     elif verb.lower() == 'navigate':
#         script = f"driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));"
#     elif verb.lower() == 'verify':
#         script = f'Assert.assertEquals(driver.findElement({locator}).getText(), "{element}", "{step_description}");'
#     else:
#         script = "Unsupported action verb"

#     return script
