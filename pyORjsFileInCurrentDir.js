/**
 * Fetches files from a specific GitHub repository and processes them.
 * @returns {Promise<Array<Object>>} A promise that resolves to an array of objects representing the fetched files.
 */
const fetchDataAndProcess = () => {
    // GitHub username and repository name
    const username = 'SyedAbdullahAhmed';
    const repoName = 'Weather-App';
    
    // Constructing the URL for fetching repository contents
    const url = `https://api.github.com/repos/${username}/${repoName}/contents`;
  
    // Fetching repository contents
    return fetch(url)
      .then(response => {
        // Handling response
        if (!response.ok) {
          // Throw error if fetching failed
          throw new Error('Failed to fetch repository files');
        }
        // Parse response body as JSON
        return response.json();
      })
      .then(data => {
        // Processing fetched data
        if (data.length === 0) {
          // Log if repository is empty
          console.log("Repo is Empty");
          return [];
        } else {
          // Iterate through fetched files
          data.forEach((element, index) => {
            // Check if file ends with .js or .py extension
            if (element.name.endsWith('.js') || element.name.endsWith('.py')) {
              // If file is JavaScript or Python file, construct item object
              let item = {
                name: element.name,
                url: element.html_url
              }
              // Log repository index and item details
              console.log("Repository:", index);
              console.log(item);
            }
          });
          // Return the fetched data
          return data;
        }
      })
      .catch(error => {
        // Error handling
        console.error('Error fetching or processing data:', error);
        return []; // Returning empty array in case of error
      });
  }
  
  // Call the function to execute
  fetchDataAndProcess();