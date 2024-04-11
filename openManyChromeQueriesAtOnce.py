import webbrowser
import urllib.parse

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def search_and_open_queries():
    """
    Opens Google search results in the default web browser for a list of user-inputted queries.
    """
    search_examples = []
    
    # Prompt the user to enter the number of queries
    arr_length = int(input("Enter number of queries: "))

    # Collect user input queries
    for i in range(arr_length):
        query = input(f"Enter query {i+1}: ")
        search_examples.append(query)

    # Iterate over the list of queries and open them in the web browser
    for index, item in enumerate(search_examples):
        # Encode the search query
        search_query_encoded = urllib.parse.quote(item)
        
        # Construct the Google search URL
        google_url = f"https://www.google.com/search?q={search_query_encoded}"
        print(f"Opening {google_url} ...")

        # Try opening the URL in the web browser
        try:
            webbrowser.get(chrome_path).open(google_url)
        except Exception as e:
            # Handle any errors that occur during opening the URL
            print("An error occurred:", e)

# Call the function to execute the search and open queries
search_and_open_queries()