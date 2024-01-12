class ResultsDisplay {
  constructor() {
    this.resultsContainer = document.getElementById('resultsContainer');
  }

  displayResults(data) {
    // Clear previous results
    this.resultsContainer.innerHTML = '';

    // Check if there are results to display
    if (!data || data.length === 0) {
      this.resultsContainer.innerHTML = '<p>No results found.</p>';
      return;
    }

    // Create a list to display the results
    const list = document.createElement('ul');

    // Iterate over each result and append to the list
    data.forEach(result => {
      const listItem = document.createElement('li');
      listItem.textContent = result.title; // Assuming 'title' is a property of the result object
      list.appendChild(listItem);
    });

    // Append the list to the results container
    this.resultsContainer.appendChild(list);
  }

  displayError(error) {
    this.resultsContainer.innerHTML = `<p>Error: ${error.message}</p>`;
  }
}

// Example usage:
// const resultsDisplay = new ResultsDisplay();
// resultsDisplay.displayResults([{ title: 'Example Title 1' }, { title: 'Example Title 2' }]);
// resultsDisplay.displayError(new Error('Failed to fetch results.'));