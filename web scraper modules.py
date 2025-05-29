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
