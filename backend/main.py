from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path
from Modules.ReadJsonFile import read_json_file
from Modules.SplitSentence import split_sentence
from Modules.FindLocator import find_locator
from Modules.GenerateTestScript import generate_test_script
from Modules.WriteTestFile import write_test_file
from Modules.CompressFolder import compress_folder
import os
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        upload_folder = Path("Data/input")
        upload_folder.mkdir(parents=True, exist_ok=True)

        file_path = upload_folder / file.filename

        with file_path.open("wb") as buffer:
            buffer.write(file.file.read())

        print("File uploaded successfully.", file.filename)
        responses = main(file.filename)
        return responses

    except HTTPException as e:
        return e
    

# @app.get('/{file_path}')
def main(file_path):
    directory = 'Data/input/'
    full_path = os.path.join(directory, file_path)
    json_data = read_json_file(full_path)

    if json_data:
        print("JSON data read successfully:")

    # Get current date and time
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")

    # Iterate through each suit
    for suit_name, suit_data in json_data["suits"].items():
        print(f"Suit: {suit_name}")

        # Iterate through each module in the suit
        for module_name, test_cases in suit_data.items():
            print(f"  Module: {module_name}")

            # Iterate through each test case in the module
            for test_case, steps in test_cases.items():
                print(f"    Test Case: {test_case}")

                # Iterate through each test step in the test case
                for step_number, step_description in steps.items():
                    print(f"      Step {step_number}: {step_description}")
                    splitted_sentence = split_sentence(step_description)

                    verb = splitted_sentence[0]
                    element = splitted_sentence[1]
                    test_data = splitted_sentence[2]
                    print(f"Verb: {verb} \t Element :{element} \t Test Data : {test_data}")

                    locator = find_locator(json_data["url"], element)
                    print(f"\nLocator:  {locator}")

                    generated_test_scripts = generate_test_script(verb, locator, test_data)
                    print(f"\nGenerated Script: {generated_test_scripts}")

                    new_file_path = write_test_file(json_data["url"], formatted_datetime, suit_name, module_name, test_case, generated_test_scripts)

    new_file_path = compress_folder(f"Data/output/{formatted_datetime}")

    print(str(f"Generated Zip: {new_file_path}.zip"))
    return {"new_path":str(new_file_path)}

