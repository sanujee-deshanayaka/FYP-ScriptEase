import os

def write_test_file(url, formatted_datetime, suit_name, module_name, test_case_name, generated_test_scripts):

    output_folder = f"Data/output/{formatted_datetime}/{suit_name}"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_path = os.path.join(output_folder, f"{module_name}.txt")

    test_cases = [
        generated_test_scripts,
    ]

    with open(file_path, "a") as file:
        file.seek(0, os.SEEK_END)
        if file.tell() == 0:
            headers = headerFiles()
            for header in headers:
                file.write(header + "\n")

            file.write(f"\ndef {test_case_name}(driver):\n")
            file.write(f"\tdriver.get('{url}')\n")

        for test_case in test_cases:
            # file.write(test_case + "\n")
            file.write("\t" + test_case + "\n")

        file.write("\n" + "driver.quit()" + "\n")

    return {"file_path": file_path}

def headerFiles():
    return [
        "from selenium import webdriver",
        "from selenium.webdriver.chrome.service import Service",
        "from selenium.webdriver.common.by import By",
        "import time",
        "\n", 
        "service_obj = Service(executable_path='chromedriver.exe')",
        "driver = webdriver.Chrome(service=service_obj)"]
