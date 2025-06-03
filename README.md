WEB SCRAPER & IP RESOLVER

Overview


The Web Scraper & IP Resolver is a Python-based GUI application built with Tkinter, designed to fetch HTML content from websites and resolve their IP addresses. It uses the ScrapingBee API for web scraping and Python's socket module for IP resolution, providing a user-friendly interface with a modern design, history tracking, and error handling. The application is ideal for developers, researchers, or anyone needing to extract web content or retrieve IP information efficiently.
Features

•	HTML Fetching: Retrieves HTML content from a specified URL using the ScrapingBee API, with custom CSS styling for improved readability.
•	IP Resolution: Resolves the IP address of a website's domain using socket.gethostbyname.
•	Asynchronous Operations: Performs fetching and IP resolution in separate threads to keep the GUI responsive.
•	History Tracking: Maintains a sortable table of up to 20 recent URL fetches, including URLs, IP addresses, and timestamps.
•	Responsive Design: Features a clean, resizable interface with a light blue gradient (#E0E7FF) and dark blue (#1A237E) accents, inspired by professional GUI aesthetics.
•	Error Handling: Validates URLs with regex, retries failed requests (up to 3 attempts), and displays clear error messages.
•	Interactive UI: Includes hover effects on buttons, alternating row colors in the history table, and a status bar for real-time feedback.
•	Clear Functionality: A "Clear" button resets the input, results, and history for a fresh start.

Requirements

•	Python: Version 3.6 or higher (tested with Python 3.13).

	Dependencies
 
o	tkinter: For the GUI (usually included with Python).
o	requests: For HTTP requests to the ScrapingBee API.
o	tkinterweb: For rendering HTML content in the GUI.


Install dependencies using:
pip install requests tkinterweb

•	ScrapingBee API Key: A valid API key from ScrapingBee is required for web scraping. Replace the placeholder key in the code (JETZB07W7FB2G03KUSQ3XPZ55XX24NHCEZHZJU9J6TTADP78NWVT765LO49F05IOZXW254926OSU0AAY) with your own.

Installation
1.	Clone or Download the Repository:
2.	git clone <repository-url>
cd <repository-directory>
3.	Install Dependencies:
pip install requests tkinterweb
4.	Update the API Key:
o	Open web_scraper_app.py.
o	Replace the SCRAPINGBEE_API_KEY variable with your ScrapingBee API key:
SCRAPINGBEE_API_KEY = "YOUR_API_KEY_HERE"
5.	Run the Application:


python web_scraper_app.py
Usage

1.	Launch the Application:

o	Run the script to open the GUI window titled "Web Scraper & IP Resolver" (900x700 pixels).

3.	Enter a URL:

o	Input a valid URL (e.g., https://example.com) in the text field.
o	The URL must start with http:// or https:// and follow standard URL formats (validated via regex).
4.	Fetch HTML:
o	Click the Fetch HTML button (green) to retrieve the website's HTML content.
o	The content is displayed in the result area with custom styling (e.g., Arial font, white background, shadow effects).
o	The status bar updates to "Fetching HTML..." and then "HTML fetched successfully" or an error message.

5.	Resolve IP:

o	Click the Resolve IP button (red) to get the IP address of the website's domain.
o	The IP is displayed in the result area, and the status bar updates accordingly.

6.	View History:

o	The history table at the bottom shows recent fetches (URL, IP, timestamp).
o	Click column headers (URL, IP, Timestamp) to sort the table in ascending or descending order.
o	Rows alternate between light blue (#F9FBFF) and gray (#ECF0F7) for readability.

7.	Clear All:

o	Click the Clear button (yellow) to reset the URL input, result area, and history table.
o	The status bar updates to "Cleared".
Code Structure

•	WebScraperApp Class:

o	Initializes the Tkinter GUI with frames for header, input, buttons, results, history, and status bar.
o	Configures styles for buttons, labels, and the history table using ttk.Style.
o	Defines methods for URL validation, HTML fetching, IP resolution, history management, and sorting.

•	Key Methods:

o	validate_url: Uses regex to check URL format.
o	fetch_html_async / _fetch_html: Fetches HTML via ScrapingBee API with retry logic (3 attempts).
o	resolve_ip_async / _resolve_ip: Resolves IP addresses with retry logic.
o	_update_history / update_history_table: Manages and displays fetch history.
o	sort_column: Sorts the history table by column.
o	clear_all: Resets the interface.

•	Styling:

o	Custom CSS is injected into HTML content for consistent rendering (e.g., #1A237E headings, #28A745 borders).
o	Button hover effects change colors (e.g., green #28A745 to #218838).
o	Gradient background (#E0E7FF) and dark blue header (#1A237E) enhance aesthetics.
Logging

•	The application uses Python's logging module to log warnings and errors (e.g., failed fetch attempts, invalid API keys).
•	Logs are formatted with timestamps and levels (INFO, WARNING, ERROR).
•	Example log:
2025-06-03 18:00:00,000 - WARNING - Attempt 1 failed: Request timed out. Retrying...
  	
Limitations

•	API Dependency: Requires a valid ScrapingBee API key; invalid keys result in a 401 error.
•	History Limit: Stores up to 20 entries to prevent memory overuse.
•	Internet Connection: Requires an active internet connection for fetching HTML and resolving IPs.
•	Rendering: Complex websites may not render perfectly in tkinterweb.HtmlFrame due to JavaScript limitations.
•	Retry Logic: Limited to 3 attempts for failed requests to balance performance and reliability.

Troubleshooting
•	"Invalid ScrapingBee API key":
o	Ensure the API key in _fetch_html is valid. Sign up at ScrapingBee for a key.
•	"Error fetching content":
o	Check your internet connection or try a different URL.
o	Verify the ScrapingBee API key and ensure you haven't exceeded your API quota.
•	"Error resolving IP":
o	Ensure the URL's domain is valid and resolvable.
o	Check your network's DNS settings.
•	GUI Not Responsive:
o	Ensure tkinterweb is installed (pip install tkinterweb).
o	Update Python to version 3.6 or higher.

Future Improvements
•	Add support for saving fetched HTML to files, similar to the Hostel Management System's text file storage.
•	Implement a scrollable result

