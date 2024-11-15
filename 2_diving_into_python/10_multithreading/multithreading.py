import threading
import requests
import time


# In Python, multithreading allows a program to run multiple threads (smaller units of a process)
# concurrently, enabling it to perform multiple tasks at once. However, Python's Global
# Interpreter Lock (GIL) limits true parallel execution in CPU-bound tasks. Still, multithreading
# can be very effective for I/O-bound tasks, such as reading and writing files, network
# operations, and web scraping.

def compute_area(length, width):
    time.sleep(4)
    return length * width


def compute_perimeter(length, width):
    time.sleep(2)
    return 2 * (length + width)


task1 = threading.Thread(target=compute_area, args=(10, 6))
task1.start()
task2 = threading.Thread(target=compute_perimeter, args=(10, 6))
task2.start()

print(f"The area is {task1}")
print(f"The perimeter is {task2}")

# ###### CASE 2 #####


# List of URLs to scrape
urls = ["http://example.com/page1", "http://example.com/page2", ..., "http://example.com/page50"]


# Function to fetch content from a single URL
# def fetch_url(url):
#     try:
#         response = requests.get(url)
#         print(f"Fetched {url} with status: {response.status_code}")
#     except requests.RequestException as e:
#         print(f"Error fetching {url}: {e}")
#
#
# # Create threads for each URL
# threads = []
# for url in urls:
#     thread = threading.Thread(target=fetch_url, args=(url,))
#     threads.append(thread)
#     thread.start()
#
# # Wait for all threads to complete
# for thread in threads:
#     thread.join()
#
# print("Finished fetching all URLs")

