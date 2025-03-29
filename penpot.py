import requests
import json
import os
from dotenv import load_dotenv
from pprint import pprint
from typing import List, Dict
from termcolor import colored # to make reading the output easier
from urllib.parse import urlparse, parse_qs

# Load environment variables from .env file
load_dotenv()


def penpot_api_call(command: str, payload: dict):
    # Penpot API endpoint
    api_url = f"https://design.penpot.app/api/rpc/command/{command}"

    # Authentication token from environment variable
    auth_token = os.getenv("PENPOT_TOKEN")


    # Headers for authentication
    headers = {
        "Authorization": f"Token {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json", # Important else we get some weird format
    }

    # Send POST request to retrieve the file fragment
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"Failed to retrieve the file fragment. Status code: {response.text}")

    return response.json()

def penpot_api_get_file(file_id: str):
    payload = {"id": file_id}
    return penpot_api_call("get-file", payload)


def penpot_parse_url(url: str) -> Dict | None :
    # Split the URL into parts
    if not url:
        print("Missing Penpot URL")
        return None

    # Remove the # symbol and everything before it
    reformatted_url = url.split('#')[-1]

    # Add a dummy scheme and domain to create a valid URL
    valid_url = f"https://dummy.com{reformatted_url}"

    # Parse the reformatted URL
    parsed_url = urlparse(valid_url)
    query_params = parse_qs(parsed_url.query)

    team_id = query_params.get("team-id", [""])[0]
    file_id = query_params.get("file-id", [""])[0]
    page_id = query_params.get("page-id", [""])[0]

    return {
        "team_id": team_id,
        "file_id": file_id,
        "page_id": page_id,
    }

def penpot_save_file_info(file_info: Dict, saved_file_name: str):
    with open(saved_file_name, "w") as file:
        json.dump(file_info, file)


file_info = penpot_parse_url(os.getenv("PENPOT_URL", ""))

if not file_info:
    print("Invalid or Missing Penpot URL")
    exit()

file_fragment = penpot_api_get_file(file_info["file_id"])
# pprint(file_fragment)

# Save the file fragment to a file
penpot_save_file_info(file_fragment, "response.json")

# Extacting information
print(colored("Extracting information from the file", "green", attrs=["underline", "bold"]))

file_name = file_fragment["name"]
print(f"File name': {colored(file_name, 'yellow')}")

file_pages = file_fragment["data"]["pages"]

# Then we can loop through the pages and extract the text objects
for page_id in file_pages:
    page_info = file_fragment["data"]["pagesIndex"][page_id]

    page_name = page_info["name"]
    print(f"Page name: {colored(page_name, 'yellow')}")

    page_objects = page_info["objects"]
    root_frame = page_objects["00000000-0000-0000-0000-000000000000"]
    shapes = root_frame["shapes"]

    for shape_id in shapes:
        shape_info = page_objects[shape_id]
        shape_type = shape_info["type"]

        if shape_type == "text":
            component_name = shape_info["name"]
            print(f"Component Name: {colored(component_name, 'yellow')}")

            component_content = shape_info["content"]

            if component_content:
                print(f"Content: {colored(component_content, 'green')}")
                print("####################")
                # for now we just print the content
