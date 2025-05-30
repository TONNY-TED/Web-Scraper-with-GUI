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


