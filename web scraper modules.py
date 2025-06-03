import tkinter as tk  # GUI framework
from tkinter import ttk, messagebox  # Themed widgets and dialog boxes
import requests  # HTTP requests library
import socket  # Networking (IP/hostname)
from urllib.parse import urlparse  # URL parsing
import re  # Regular expressions
from tkinterweb.htmlwidgets import HtmlFrame  # HTML display in Tkinter
import threading  # Multithreading support
import logging  # Logging utilities
from datetime import datetime  # Date and time handling

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper & IP Resolver")
        self.root.geometry("900x700")
        self.root.configure(bg="#E0E7FF") 


 # Style configuration
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 11), padding=12)
        self.style.configure("TLabel", font=("Arial", 12), background="#E0E7FF", foreground="#2C3E50")
        self.style.configure("Header.TLabel", font=("Arial", 18, "bold"), background="#1A237E", foreground="#2980B9")
        self.style.configure("TTreeview", background="#FFFFFF", fieldbackground="#FFFFFF", foreground="#2C3E50")
        self.style.configure("TTreeview.Heading", font=("Arial", 10, "bold"), background="#1A237E", foreground="#FFFFFF")


  # Header with gradient
        self.header_frame = tk.Frame(root, bg="#1A237E")
        self.header_frame.pack(fill="x", pady=15)
        self.header_label = ttk.Label(self.header_frame, text="Web Scraper & IP Resolver", style="Header.TLabel")
        self.header_label.pack()


  # Input Frame
        self.input_frame = tk.Frame(root, bg="#E0E7FF")
        self.input_frame.pack(pady=10, padx=20, fill="x")
        self.url_label = ttk.Label(self.input_frame, text="Enter URL (e.g., https://example.com):")
        self.url_label.pack(anchor="w", pady=5)
        self.url_entry = ttk.Entry(self.input_frame, width=60, font=("Arial", 11))
        self.url_entry.pack(pady=5, fill="x")

  # Button Frame
        self.button_frame = tk.Frame(root, bg="#E0E7FF")
        self.button_frame.pack(pady=10)
         self.fetch_button = tk.Button(self.button_frame, text="Fetch HTML", command=self.fetch_html_async,
                                      bg="#28A745", fg="white", font=("Arial", 11), relief="flat", padx=15, pady=8)
        self.fetch_button.pack(side="left", padx=5)
        self.fetch_button.bind("<Enter>", lambda e: self.fetch_button.config(bg="#218838"))
        self.fetch_button.bind("<Leave>", lambda e: self.fetch_button.config(bg="#28A745"))

        self.ip_button = tk.Button(self.button_frame, text="Resolve IP", command=self.resolve_ip_async,
                                   bg="#DC3545", fg="white", font=("Arial", 11), relief="flat", padx=15, pady=8)
        self.ip_button.pack(side="left", padx=5)
        self.ip_button.bind("<Enter>", lambda e: self.ip_button.config(bg="#C82333"))
        self.ip_button.bind("<Leave>", lambda e: self.ip_button.config(bg="#DC3545"))

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_all,
                                      bg="#FFC107", fg="black", font=("Arial", 11), relief="flat", padx=15, pady=8)
        self.clear_button.pack(side="left", padx=5)
        self.clear_button.bind("<Enter>", lambda e: self.clear_button.config(bg="#E0A800"))
        self.clear_button.bind("<Leave>", lambda e: self.clear_button.config(bg="#FFC107"))

        
# Result Frame
        self.result_frame = tk.Frame(root, bg="#E0E7FF")
        self.result_frame.pack(pady=10, padx=20, fill="both", expand=True)
        self.result_label = ttk.Label(self.result_frame, text="Results:")
        self.result_label.pack(anchor="w", pady=5)
        self.result_html = HtmlFrame(self.result_frame, horizontal_scrollbar="auto", messages_enabled=False)
        self.result_html.pack(pady=5, fill="both", expand=True)


        # History Frame
        self.history_frame = tk.Frame(root, bg="#E0E7FF")
        self.history_frame.pack(pady=10, padx=20, fill="x")
        self.history_label = ttk.Label(self.history_frame, text="Fetch History:")
        self.history_label.pack(anchor="w", pady=5)
        self.history_tree = ttk.Treeview(self.history_frame, columns=("URL", "IP", "Timestamp"), show="headings",
                                         height=6)
        self.history_tree.heading("URL", text="URL", command=lambda: self.sort_column("URL", False))
        self.history_tree.heading("IP", text="IP Address", command=lambda: self.sort_column("IP", False))
        self.history_tree.heading("Timestamp", text="Timestamp", command=lambda: self.sort_column("Timestamp", False))
        self.history_tree.column("URL", width=400)
        self.history_tree.column("IP", width=150)
        self.history_tree.column("Timestamp", width=150)
        self.history_tree.pack(pady=5, fill="x")

  # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(root, textvariable=self.status_var, font=("Arial", 10), background="#E0E7FF",
                                    foreground="#7F8C8D")
        self.status_bar.pack(side="bottom", fill="x", pady=5)

        # History storage with limit
        self.history = []
        self.MAX_HISTORY = 20

        # Precompile regex for efficiency
        self.url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)


 # Custom CSS for styling rendered content
        self.custom_css = """
        <style>
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                background-color: #F9FBFF;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                max-width: 100%;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #1A237E;
                margin-bottom: 15px;
                font-weight: 600;
            }
            p {
                color: #2C3E50;
                margin-bottom: 15px;
            }
            a {
                color: #2980B9;
                text-decoration: none;
                transition: color 0.3s ease;
            }
            a:hover {
                color: #3498DB;
                text-decoration: underline;
            }
            ul, ol {
                padding-left: 25px;
                color: #34495E;
            }
            li {
                margin-bottom: 10px;
            }
            .content-box {
                background-color: #FFFFFF;
                padding: 15px;
                border-radius: 5px;
                margin-bottom: 15px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
                border-left: 4px solid #28A745;
            }
            img {
                max-width: 100%;
                height: auto;
            }
        </style>
        """

    def validate_url(self, url):
        """Validate URL format with precompiled regex."""
        return bool(self.url_pattern.match(url.strip()))
        
    def fetch_html_async(self):
        """Fetch HTML content asynchronously using ScrapingBee API."""
        url = self.url_entry.get().strip()
        if not self.validate_url(url):
            messagebox.showerror("Error", "Invalid URL format!")
            return
        self.status_var.set("Fetching HTML...")
        threading.Thread(target=self._fetch_html, args=(url,), daemon=True).start()



    def _fetch_html(self, url):
        """Internal method to fetch HTML with ScrapingBee API and retry logic."""
        SCRAPINGBEE_API_KEY = "JETZB07W7FB2G03KUSQ3XPZ55XX24NHCEZHZJU9J6TTADP78NWVT765LO49F05IOZXW254926OSU0AAY"  # Your ScrapingBee API key
        api_url = f"https://app.scrapingbee.com/api/v1?url={url}&api_key={SCRAPINGBEE_API_KEY}&render_js=true"
        try:
            for attempt in range(3):
                try:
                    response = requests.get(api_url, timeout=10)
                    response.raise_for_status()
                    html_content = response.text
                    if "<head>" in html_content:
                        html_content = html_content.replace("<head>", f"<head>{self.custom_css}")
                    else:
                        html_content = f"<html><head>{self.custom_css}</head><body>{html_content}</body></html>"
                    self.root.after(0, lambda: self.result_html.load_html(html_content))
                    ip = self.resolve_ip_silent(url)
                    self._update_history(url, ip)
                    self.status_var.set("HTML fetched successfully")
                    return
                except requests.exceptions.RequestException as e:
                    if attempt < 2:
                        logging.warning(f"Attempt {attempt + 1} failed: {str(e)}. Retrying...")
                        continue
                    raise
        except Exception as e:
            logging.error(f"Failed to fetch HTML: {str(e)}")
            error_message = str(e)
            if "401" in error_message:
                self.root.after(0, lambda: self.result_html.load_html("<h3>Error: Invalid ScrapingBee API key. Please update the API key in the code.</h3>"))
            else:
                self.root.after(0, lambda: self.result_html.load_html("<h3>Error fetching content</h3>"))
            self.status_var.set("Fetch failed")

    def resolve_ip_async(self):
        """Resolve IP address asynchronously."""
        url = self.url_entry.get().strip()
        if not self.validate_url(url):
            messagebox.showerror("Error", "Invalid URL format!")
            return
        self.status_var.set("Resolving IP...")
        threading.Thread(target=self._resolve_ip, args=(url,), daemon=True).start()

    def _resolve_ip(self, url):
        """Internal method to resolve IP with retry logic."""
        try:
            for attempt in range(3):
                try:
                    domain = urlparse(url).netloc
                    ip = socket.gethostbyname(domain)
                    self.root.after(0, lambda: self.result_html.load_html(f"<h3>IP Address for {url}</h3><p>{ip}</p>"))
                    self._update_history(url, ip)
                    self.status_var.set("IP resolved successfully")
                    return
                except socket.gaierror as e:
                    if attempt < 2:
                        logging.warning(f"Attempt {attempt + 1} failed: {str(e)}. Retrying...")
                        continue
                    raise
        except Exception as e:
            logging.error(f"Failed to resolve IP: {str(e)}")
            self.root.after(0, lambda: self.result_html.load_html("<h3>Error resolving IP</h3>"))
            self.status_var.set("IP resolution failed")

 def resolve_ip_silent(self, url):
        """Resolve IP silently for history."""
        try:
            domain = urlparse(url).netloc
            return socket.gethostbyname(domain)
        except socket.gaierror:
            return "N/A"


 def _update_history(self, url, ip):
        """Update history with timestamp and limit."""
        timestamp = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        self.history.append((url, ip, timestamp))
        if len(self.history) > self.MAX_HISTORY:
            self.history.pop(0)
        self.root.after(0, self.update_history_table)
     
    

       


