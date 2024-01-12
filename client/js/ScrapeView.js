document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('startButton');
    const resultsContainer = document.getElementById('resultsContainer');
    const statusIndicator = document.getElementById('statusIndicator');

    startButton.addEventListener('click', function() {
        ScrapeController.startScraping();
    });

    document.addEventListener('ScrapeStarted', function() {
        statusIndicator.textContent = 'Scraping in progress...';
        resultsContainer.innerHTML = '';
    });

    document.addEventListener('ScrapeCompleted', function(event) {
        statusIndicator.textContent = 'Scraping completed.';
        ResultsDisplay.showResults(event.detail, resultsContainer);
    });

    document.addEventListener('ScrapeStatusUpdated', function(event) {
        statusIndicator.textContent = event.detail;
    });
});