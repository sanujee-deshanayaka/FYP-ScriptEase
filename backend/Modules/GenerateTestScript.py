def generate_test_script(verb, locator, test_data=None):
    if verb.lower() == 'enter':
        script = f'driver.find_element({locator}).send_keys("{test_data}")'
    elif verb.lower() == 'click':
        script = f"driver.find_element({locator}).click()"
    else:
        script = "Unsupported action verb"

    return script
