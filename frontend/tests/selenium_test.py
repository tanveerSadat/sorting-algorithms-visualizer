import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

#  python frontend/tests/selenium_test.py

# TODO:
# test a full run of the sorting functions and the verify the outputs
# need to add automated testing for validation input
# maybe: ensure cross-page consistency (similar structure)
# maybe: integrate loggingPrefs and capture console errors to ensure no JS exceptions are thrown

class TestFrontendPages(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Sets up the Chrome WebDriver instance before running tests
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager

        options = Options()
        # Always use headless mode in CI, but still allow GUI when running locally
        if os.getenv("CI", "false") == "true":
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Use WebDriverManager to auto-install ChromeDriver
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.implicitly_wait(3)
        
        # Base path to local frontend folder
        cls.base_path = os.path.abspath("./frontend")

    # Tests that the main page loads and contains the correct title
    def test_main_page_loads(self):
        file_path = os.path.join(self.base_path, "main.html")
        self.driver.get("file://" + file_path)
        self.assertIn("Sorting Algorithm Visualizer", self.driver.title)

    # Tests that the main page includes at least one link element (<a>)
    def test_links_exist(self):
        file_path = os.path.join(self.base_path, "main.html")
        self.driver.get("file://" + file_path)
        links = self.driver.find_elements(By.TAG_NAME, "a")
        self.assertGreater(len(links), 0, "Expected links to exist (e.g. Bubble/Selection Sort).")
    
    # Tests that the "Bubble Sort" link navigates correctly to bubblesort.html
    def test_main_link_to_bubble_sort(self):
        file_path = os.path.join(self.base_path, "main.html")
        self.driver.get("file://" + file_path)
        link = self.driver.find_element(By.LINK_TEXT, "Bubble Sort")
        link.click()
        self.assertIn("bubblesort.html", self.driver.current_url)

        # Tests that the Bubble Sort page contains the correct header text
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("Bubble Sort", header.text)

    # Tests that the "Selection Sort" link navigates correctly to selectionsort.html
    def test_main_link_to_selection_sort(self):
        file_path = os.path.join(self.base_path, "main.html")
        self.driver.get("file://" + file_path)
        link = self.driver.find_element(By.LINK_TEXT, "Selection Sort")
        link.click()
        self.assertIn("selectionsort.html", self.driver.current_url)

        # Tests that the Selection Sort page contains the correct header text
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("Selection Sort", header.text)

     # Tests that the Bubble Sort page contains input and button elements
    def test_bubble_sort_page_fields(self):
        file_path = os.path.join(self.base_path, "bubblesort.html")
        self.driver.get("file://" + file_path)

        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")

        self.assertGreater(len(inputs), 0, "No input field found on Bubble Sort page.")
        self.assertGreater(len(buttons), 0, "No button found on Bubble Sort page.")

    # Tests that the Selection Sort page contains input and button elements
    def test_selection_sort_page_fields(self):
        file_path = os.path.join(self.base_path, "selectionsort.html")
        self.driver.get("file://" + file_path)

        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")

        self.assertGreater(len(inputs), 0, "No input field found on Selection Sort page.")
        self.assertGreater(len(buttons), 0, "No button found on Selection Sort page.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # Closes the browser after all tests are complete

if __name__ == "__main__":
    unittest.main()
