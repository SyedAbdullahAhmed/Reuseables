
/**
 * Fetches repositories of a given GitHub username.
 * @param {string} username - The GitHub username.
 * @returns {Promise<Array<{name: string, url: string}>>} A promise that resolves to an array of objects containing repository names and URLs.
 */
async function getReposByUsername(username) {
  const url = `https://api.github.com/users/${username}/repos`;
  const headers = {
    'Accept': 'application/vnd.github+json'
  };

  try {
    // Fetching repositories from GitHub API
    const response = await fetch(url, { headers });
    
    // Handling response
    if (response.ok) {
      const data = await response.json();
      
      // Mapping repository data to required format
      return data.map(repo => ({
        name: repo.name,
        url: repo.html_url
      }));
    } else {
      // Handling non-successful responses
      throw new Error(`Error: ${response.status}`);
    }
  } catch (error) {
    // Handling errors
    console.error('Error fetching repositories:', error);
    return []; // Returning empty array in case of error
  }
}

// Example usage
getReposByUsername('SyedAbdullahAhmed')
  .then(repos => {
    console.log(repos); // Logging repositories to the console
  })
  .catch(error => {
    console.error(error); // Logging errors to the console
  });

