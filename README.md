## 📰 News Scraper <img src="https://github.com/user-attachments/assets/a91aca68-1ff0-4fe1-ae7e-c1c0be7b5639" width="20px" />

<div align="center"><img src="https://github.com/user-attachments/assets/b1c5a9c4-ff1a-4324-83e6-beba7b97a2bd"  /> </div>

## About the APP
<p>Welcome to News Scraper, an application I built to explore web scraping and understand its potential for automating data extraction. This tool fetches the top 5 news articles from popular sources like CNN, BBC, Telemundo, and Euronews, and displays them in a user-friendly interface using Python’s Tkinter library.</p>

## 📋 Features
- **Interactive Interface:** A simple graphical interface powered by Tkinter.
- **One-Click Scraping:** Fetches and displays news headlines and clickable links with a single click.
- **Real-Time Updates:** Clears old results and fetches fresh news on every scrape.
- **Cross-Platform Compatibility:** Runs seamlessly on any system with Python installed.
  
## 🛠️ Requirements
<p>Before running the application, ensure the following Python libraries are installed:</p>

    import tkinter as tk  
    from tkinter import scrolledtext  
    import requests  
    from bs4 import BeautifulSoup  
    from googletrans import Translator  
    import threading  
    import time  
    import webbrowser

Use `pip install <library_name>` to install any missing dependencies.

## 🚀 How It Works
### News Sources
The app targets specific news websites using a dictionary of URLs:

<div align="center"><img src="https://github.com/user-attachments/assets/2a62327e-7081-47d2-8a0b-5afaac2e3023"  /> </div>

### Scraper Engine
The scraper iterates through the dictionary to extract news headlines and links:

1. **Clear Previous Results:** Clears the display area for new data.
2. **Fetch Content:** Uses `BeautifulSoup` to parse the HTML of each site.
3. **Extract Data:** Finds specific HTML tags to fetch titles and links for each article.
4. **Display Data:** Outputs the news title and a clickable link in the result box.

Here’s an example:
<div align="center"><img src="https://github.com/user-attachments/assets/8a4c5c99-69a3-44cd-9093-a8ccd191da85"  /> </div> 

## 🎨 Interface Customization
- **Button:** Created with `tk.Button` to define its size, font, and label.
<div align="center"><img src="https://github.com/user-attachments/assets/718c9091-bec0-4dab-8ac4-c8d640a28b9d"  /> </div>

  
- **Scrollable Results Area:** Built using `scrolledtext.ScrolledText`, allowing styled text display.
<div align="center"><img src="https://github.com/user-attachments/assets/c61100e1-c5c2-4c41-80d0-7e51b8299638"  /> </div>

  
- **Styled Text:** Configured with `result_box.tag_config` for bold headlines, title fonts, and clickable links.
<div align="center"><img src="https://github.com/user-attachments/assets/8a60a0bd-b797-4d4e-8bbd-225b3717e4c3"  /> </div>


- **Clock Widget:** Displays the current time using `tk.Label` and updates every second via `time.strftime`. The clock runs on a separate thread to ensure smooth performance.
<div align="center"><img src="https://github.com/user-attachments/assets/35d5234f-88f8-4369-9d79-cc12c695c66b"  /> </div>


## 🌟 How to Run
1. Clone the repository.
2. Install the required libraries.
3. Run the script using `python app.py`.
4. Interact with the GUI to fetch and view news articles.

## 🤝 Contribution
I’m open to suggestions! Feel free to fork this repository, improve the code, and submit a pull request. Let’s make this tool even better together.
