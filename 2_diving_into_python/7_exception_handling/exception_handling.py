# Exception handling in Python is a way to deal with errors or "exceptions" that might occur
# while a program is running. It ensures that a program can continue operating even when
# unexpected issues arise. A real-world example could be a program designed to download files
# from the internet. The program may encounter issues, such as a lost internet connection or an
# invalid URL. Exception handling allows the program to gracefully manage these issues without
# crashing

import requests

# Example Usage


def download_file(link, file_name):
    try:
        # Try to fetch the content of the URL
        response = requests.get(link, timeout=10)
        response.raise_for_status()  # Raises an error if the request failed (e.g., 404 or 500
                                             # status code)

        # Write content to a file
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your internet connection and try again.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


url = "https://example.com/samplefile.txt"
filename = "samplefile.txt"

download_file(url, filename)


# Explanation
# try block: This block contains the code that may raise an exception. In this example,
# we attempt to download a file.

# except blocks: Each except handles a specific type of exception:

#      requests.exceptions.Timeout: This handles cases where the request times out, often due to
#         connectivity issues.

#      requests.exceptions.HTTPError: This handles HTTP-related errors, such as a 404 (Not Found)
#        or 500 (Server Error).

#      requests.exceptions.RequestException: This is a more general exception for other
#          requests-related errors.

#      A general Exception is also included at the end to catch any other errors not previously
#        specified.
