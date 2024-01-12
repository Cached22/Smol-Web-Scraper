class ScrapeController {
  constructor() {
    this.startButton = document.getElementById('startButton');
    this.resultsContainer = document.getElementById('resultsContainer');
    this.statusIndicator = document.getElementById('statusIndicator');

    this.addEventListeners();
  }

  addEventListeners() {
    this.startButton.addEventListener('click', () => this.startScraping());
  }

  async startScraping() {
    try {
      const response = await fetch('/start', { method: 'POST' });
      if (response.ok) {
        const data = await response.json();
        this.updateStatus('Scraping started...');
        document.dispatchEvent(new CustomEvent('ScrapeStarted', { detail: data }));
      } else {
        this.updateStatus('Error starting the scrape.');
      }
    } catch (error) {
      this.updateStatus('Failed to start scraping.');
      console.error('Error:', error);
    }
  }

  async getResults() {
    try {
      const response = await fetch('/results');
      if (response.ok) {
        const data = await response.json();
        document.dispatchEvent(new CustomEvent('ScrapeCompleted', { detail: data }));
      } else {
        this.updateStatus('Error fetching results.');
      }
    } catch (error) {
      this.updateStatus('Failed to fetch results.');
      console.error('Error:', error);
    }
  }

  async getStatus() {
    try {
      const response = await fetch('/status');
      if (response.ok) {
        const data = await response.json();
        this.updateStatus(`Status: ${data.status}`);
        document.dispatchEvent(new CustomEvent('ScrapeStatusUpdated', { detail: data }));
      } else {
        this.updateStatus('Error fetching status.');
      }
    } catch (error) {
      this.updateStatus('Failed to fetch status.');
      console.error('Error:', error);
    }
  }

  updateStatus(message) {
    this.statusIndicator.textContent = message;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const controller = new ScrapeController();
});