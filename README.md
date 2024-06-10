# function-calling-with-vertex-ai

## Overview

This project simulates a mock restaurant API to check table availability and make reservations. It is designed to demonstrate how such an API might function, using mock data and responses to mimic real-world API behavior. The project consists of three main components:

1. `mock_restaurant_api.py` - Contains the `MockRestaurantAPI` class which provides methods for checking table availability and performing dummy reservations.
2. `utils.py` - Contains utility functions to assist with the processing of responses.
3. `main.py` - Main script to initialize and interact with the mock API using Vertex AI.

## Files and Functions

### `mock_restaurant_api.py`

#### MockRestaurantAPI Class

- **`check_table_availability`**: 
    - Description: Mocks the call to an API to check table availability.
    - Parameters: `party_size`, `date`, `time`, `restaurant_name`.
    - Returns: A tuple with a boolean indicating availability and a message.

- **`perform_dummy_reservation`**:
    - Description: Mocks the call to an API to perform a reservation.
    - Parameters: `party_size`, `date`, `time`, `restaurant_name`.
    - Returns: A tuple with a boolean indicating success and a message with a dummy reservation ID.

### `utils.py`

#### Functions

- **`is_function_calling(response)`**:
    - Description: Determines if there is at least one function call in the response.
    - Parameters: `response` (an object containing response data from a Vertex AI agent).
    - Returns: Boolean indicating if there is a function call in the first candidate response.
    - Raises: `ValueError` if the response does not contain `candidates` or if `candidates` is not a list. `AttributeError` if the first candidate does not have `function_calls` attribute.

### `main.py`

#### Constants

- **`PROJECT_ID`**: Google Cloud project ID.
- **`LOCATION`**: Google Cloud location.

#### Libraries

- `vertexai` for Vertex AI initialization.
- `requests` for making HTTP requests.

#### Functions and Usage

- **Vertex AI Initialization**:
    - Initializes Vertex AI with the specified project ID and location.
    
- **Function Declarations**:
    - `check_table_availability`: Checks table availability for a given date, time, and party size.
    - `place_reservation`: Places a reservation with contact information.

- **Tool Initialization**:
    - `restaurant_tool`: Adds declared functions to the tool instance.

- **GenerativeModel Initialization**:
    - Initializes a `GenerativeModel` with specified model name and configuration.

- **Chat Session**:
    - Starts a chat session with the initialized model.

#### Main Logic

- **Prompt Definition**:
    - Defines the initial user prompt for checking table availability.

- **Handling Function Calls**:
    - **`handle_function_call(response)`**: Handles function calls extracted from the response.
    - **`handle_user_message(response)`**: Handles user input messages.

- **Process Completion**:
    - **`complete_process()`**: Checks if the reservation process is completed and prints the reservation text if successful.

## Usage

1. **Initialization**: 
   - Ensure you have the required libraries installed (`vertexai`, `requests`).
   - Set the `PROJECT_ID` and `LOCATION` in `main.py`.

2. **Running the Script**:
   - Execute `main.py` to start the mock restaurant API interaction.
   - Follow the prompts to check table availability and make reservations.

## Example

Here is an example of how you might interact with the script:

```bash
python main.py
```

When prompted, the script will simulate checking table availability and making reservations using mock data.


## License

This project is licensed under the MIT License.

---

This README provides an overview of the project, detailed descriptions of the files and functions, and instructions on how to use the script. For further information or questions, please refer to the documentation within the code or reach out to the maintainers.