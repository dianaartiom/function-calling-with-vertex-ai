def is_function_calling(response):
    """
    Determines if there is at least one function call in the response.

    Args:
        response: An object containing the response data from a Vertex AI agent.
                  Expected to have a 'candidates' attribute which is a list of candidate responses.
                  Each candidate should have a 'function_calls' attribute which is a list.

    Returns:
        bool: True if the first candidate response contains any function calls, False otherwise.

    Raises:
        ValueError: If the response does not contain 'candidates' or if 'candidates' is not a list.
        AttributeError: If the first candidate does not have 'function_calls' attribute.

    Example usage:
    response = {
        "candidates": [
            {
                "function_calls": ["call1", "call2"]
            }
        ]
    }
    print(is_function_calling(response))  # Output: True
    """

    # Ensure the response object has 'candidates' attribute and it is a list
    if not hasattr(response, 'candidates') or not isinstance(response.candidates, list):
        raise ValueError("The response must have an attribute 'candidates' which should be a list.")

    # Ensure there is at least one candidate in the list
    if len(response.candidates) == 0:
        return False

    # Check if the first candidate has 'function_calls' attribute and it is a list
    first_candidate = response.candidates[0]
    if not hasattr(first_candidate, 'function_calls') or not isinstance(first_candidate.function_calls, list):
        raise AttributeError("The first candidate must have an attribute 'function_calls' which should be a list.")

    # Determine if there is at least one function call in the first candidate
    return len(first_candidate.function_calls) > 0


