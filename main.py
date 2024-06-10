PROJECT_ID = "<PROJECT_ID>"
LOCATION = "<LOCATION>"


import json
import vertexai

# Initialize the Vertex AI with the specified project ID and location
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Importing the requests library for making HTTP requests
import requests

# Importing necessary classes from the vertexai.generative_models module
from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Part,
    Tool,
)

from mock_restaurant_api import MockRestaurantAPI
from utils import is_function_calling

# Declaring a function for checking table availability
check_table_availability = FunctionDeclaration(
    name="check_table_availability",
    description="Check the availability of tables for a given date and time. ",
    parameters={
        "type": "object",
        "properties": {
            "restaurant_name": {"type": "string", "description": "Name of the restaurant"},
            "date": {"type": "string", "description": "Date for the reservation"},
            "time": {"type": "string", "description": "Time for the reservation"},
            "party_size": {"type": "integer", "description": "Number of people"}
        },
    },
)

# Declaring a function for placing a reservation
place_reservation = FunctionDeclaration(
    name="place_reservation",
    description="Place a reservation at a restaurant",
    parameters={
        "type": "object",
        "properties": {
            "restaurant_name": {"type": "string", "description": "Name of the restaurant"},
            "date": {"type": "string", "description": "Date for the reservation"},
            "time": {"type": "string", "description": "Time for the reservation"},
            "party_size": {"type": "integer", "description": "Number of people"},
            "contact_info": {"type": "string", "description": "Contact information for the reservation"},
        },
    },
)

# Creating a Tool instance and adding the declared functions to it
restaurant_tool = Tool(
    function_declarations=[
        check_table_availability,
        place_reservation,
    ],
)

# Initializing a GenerativeModel with a specified model name and generation configuration
model = GenerativeModel(
    "gemini-1.5-flash-001",
    generation_config=GenerationConfig(temperature=0),
    tools=[restaurant_tool],
)

# Starting a chat session with the initialized model
chat = model.start_chat()

# Defining the prompt to be sent to the chat model
prompt = """
Is there a table available at La Piazza?"
"""
# for 4 people on June 15th at 7 PM?

# handle function call
def handle_function_call(response):
    if is_function_calling(response):
        function_call = response.candidates[0].content.parts[0].function_call
        kwargs = dict(function_call.args.items())

        if function_call.name == "check_table_availability":
            api_response, api_response_msg = MockRestaurantAPI.check_table_availability(**kwargs)
            response_content = json.dumps({"available": api_response})

        elif function_call.name == "place_reservation":
            api_response_msg = MockRestaurantAPI.perform_dummy_reservation(**kwargs)
            response_content = api_response_msg

        response = chat.send_message(
            Part.from_function_response(
                name=function_call.name,
                response={
                    "content": response_content,
                },
            ),
        )

        return response


def handle_user_message(response):
    # extract user message
    user_input = input(response.candidates[0].content.parts[0].text)
    return chat.send_message(user_input)

def complete_process():
    reservation_text = response.candidates[0].content.parts[0].text
    if "reservation ID" in reservation_text:
        print(reservation_text)
        return True

print("Initial user prompt:")
print(prompt)
response = chat.send_message(prompt)

while True:
    if is_function_calling(response):
        response = handle_function_call(response)
    else:
        if complete_process():
            break
        else:
            response = handle_user_message(response)

