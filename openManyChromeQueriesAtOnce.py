import webbrowser
import urllib.parse

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def search_and_open_queries_using_input():
    """
    Opens Google search results in the default web browser for a list of user-inputted queries.
    """
    search_examples = []
    
    # Prompt the user to enter the number of queries
    arr_length = int(input("Enter number of queries: "))
    print("1> Google\n2> Google Scholar\n3> Google Patent")

    search_engine = int(input("What search engine you want to use: "))

    # Collect user input queries
    for i in range(arr_length):
        query = input(f"Enter query {i+1}: ")
        search_examples.append(query)

    # Iterate over the list of queries and open them in the web browser
    for index, item in enumerate(search_examples):
        # Encode the search query
        search_query_encoded = urllib.parse.quote(item)
        url = ""
        # Construct the Google search URL
        if search_engine == 1:
            url = f"https://www.google.com/search?q={search_query_encoded}"
        elif search_engine == 3:
            url = f"https://patents.google.com/?q={search_query_encoded}"
        elif search_engine == 2:
            url = f"https://scholar.google.com/scholar?q={search_query_encoded}"

        print(f"Opening {url} ...")

        # Try opening the URL in the web browser
        try:
            webbrowser.get(chrome_path).open(url)
        except Exception as e:
            # Handle any errors that occur during opening the URL
            print("An error occurred:", e)

# Call the function to execute the search and open queries
search_and_open_queries_using_input()




# def search_and_open_queries_using_array(search_examples):
#     """
#     Opens Google search results in the default web browser for a list of user-inputted queries.
#     """
    
#     print("1> Google\n2> Google Scholar\n3> Google Patent")

#     search_engine = int(input("What search engine you want to use: "))


#     # Iterate over the list of queries and open them in the web browser
#     for index, item in enumerate(search_examples):
#         # Encode the search query
#         search_query_encoded = urllib.parse.quote(item)
#         url = ""
#         # Construct the Google search URL
#         if search_engine == 1:
#             url = f"https://www.google.com/search?q={search_query_encoded}"
#         elif search_engine == 3:
#             url = f"https://patents.google.com/?q={search_query_encoded}"
#         elif search_engine == 2:
#             url = f"https://scholar.google.com/scholar?q={search_query_encoded}"

#         print(f"Opening {url} ...")

#         # Try opening the URL in the web browser
#         try:
#             webbrowser.get(chrome_path).open(url)
#         except Exception as e:
#             # Handle any errors that occur during opening the URL
#             print("An error occurred:", e)

# # Call the function to execute the search and open queries
# search_and_open_queries_using_array(search_examples)



