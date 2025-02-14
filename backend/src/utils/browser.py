from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    def __init__(self, headless: bool = False):
        """Initialize the browser with specified options."""
        self.headless = headless
        self.driver = self.setup_browser()

    def setup_browser(self):
        """Set up the browser with options."""
        options = Options()
        options.headless = self.headless  # Set headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Initialize the Chrome driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def open_url(self, url: str):
        """Open a URL in the browser."""
        self.driver.get(url)

    def close(self):
        """Close the browser."""
        self.driver.quit()

    def take_screenshot(self, filename: str):
        """Take a screenshot of the current page."""
        self.driver.save_screenshot(filename)