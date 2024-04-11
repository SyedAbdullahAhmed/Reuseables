
/**
 * Searches GitHub repositories based on a given search term and logs the top 5 most starred repositories.
 * @param {string} searchTerm - The term to search for in GitHub repositories.
 * @returns {Promise<void>} A promise that resolves once the search and logging process is complete.
 */
async function searchGithubRepos(searchTerm) {
    // Base URL for GitHub repository search API
    const baseUrl = "https://api.github.com/search/repositories";
    const sort = "stars"; // Sorting by stars
    const order = "desc"; // Descending order (most stars first)
  
    // Constructing the URL with search parameters
    const url = new URL(baseUrl);
    url.searchParams.append("q", searchTerm); // Appending search term
    url.searchParams.append("sort", sort);    // Appending sort parameter
    url.searchParams.append("order", order);  // Appending order parameter
  
    try {
      // Fetching data from the constructed URL
      const response = await fetch(url);
  
      // Handling response
      if (!response.ok) {
        // Throw error if response is not OK
        throw new Error(`Error searching repositories: ${response.status}`);
      }
  
      // Parsing response body as JSON
      const data = await response.json();
  
      // Logging top 5 most starred repositories
      console.log("Top 5 most starred repositories for", searchTerm);
      const topRepos = data.items.slice(0, 5); // Extracting top 5 repositories
      for (const repo of topRepos) {
        // Logging repository name, stars count, and URL
        console.log(`* Name: ${repo.name}, Stars: ${repo.stargazers_count}, URL: ${repo.html_url}`);
      }
    } catch (error) {
      // Error handling
      console.error("Error:", error);
    }
  }
  
  // Example usage: searching GitHub repositories for "Porfolio + Nextjs"
  searchGithubRepos("Porfolio + Nextjs ");
  