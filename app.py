import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import threading
import time
import webbrowser

# Create a dictionary with the news websites where you would obtain the information.
news_urls = {
    "BBC": "https://www.bbc.com/news",
    "CNN": "https://us.cnn.com/",
    "Telemundo": "https://www.telemundo.com/noticias/america-latina",
    "Euronews": "https://www.euronews.com/just-in"
}

# Create an instance for the translator.
translator = Translator()

# Building the clock with Python's Time module
def update_clock():
    while True:
        current_time = time.strftime("%d-%m-%Y %H:%M:%S")
        clock_label.config(text=current_time)
        time.sleep(1)

# we define a function called OPEN to capture he string as a link
def open_link(event):
    start = result_box.index("@%s,%s linestart" % (event.x, event.y))
    end = result_box.index("@%s,%s lineend" % (event.x, event.y))
    link = result_box.get(start, end).strip()
    webbrowser.open_new(link)


# Making the scraper, 
def scrape_website():
    result_box.delete(1.0, tk.END)
    for name, url in news_urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # just five articles
        if name == "BBC":
            articles = soup.find_all('div', attrs={'data-testid': 'edinburgh-card'}, limit=5)
            result_box.insert(tk.END, f"\n{name}\n", 'bold')
            for article in articles:
                title = article.find('h2').get_text().lstrip() if article.find('h2') else 'No title'
                link = 'https://www.bbc.com' + article.find('a')['href'] if article.find('a') else 'No link'
                result_box.insert(tk.END, f"• {title}\n", 'title')
                result_box.insert(tk.END, link, ('link', link))
                result_box.insert(tk.END, "\n")
                result_box.insert(tk.END, "\n")

        elif name == "CNN":
            articles = soup.find_all('div', attrs={'data-component-name':'card'}, limit=5)
            result_box.insert(tk.END, f"\n{name}\n", 'bold')
            for article in articles:
                title = article.find('span', class_='container__headline-text').get_text().lstrip() if article.find('span', class_='container__headline-text') else 'No title'
                link = 'https://us.cnn.com' + article.find('a')['href'] if article.find('a') else 'No link'
                result_box.insert(tk.END, f"• {title}\n", 'title')
                result_box.insert(tk.END, link, ('link', link))
                result_box.insert(tk.END, "\n")
                result_box.insert(tk.END, "\n")

        elif name == "Telemundo":
            articles = soup.find_all('div', class_='tease-card__info', limit=5)
            result_box.insert(tk.END, f"\n{name}\n", 'bold')
            for article in articles:
                title = article.find('span').get_text().lstrip() if article.find('span') else 'No title'
                link = article.find('a')['href'] if article.find('a') else 'No link'

                translated_title = translator.translate(title, src='es', dest='en').text

                result_box.insert(tk.END, f"• {translated_title}\n", 'title')
                result_box.insert(tk.END, link, ('link', link))
                result_box.insert(tk.END, "\n")
                result_box.insert(tk.END, "\n")

        elif name == "Euronews":
            articles = soup.find_all('li', class_="js-timeline-item c-timeline-items__content", limit=5)
            result_box.insert(tk.END, f"\n{name}\n", 'bold')
            for article in articles:
                title = article.find('h3').get_text().lstrip() if article.find('h3') else 'No title'
                link = article.find('a', class_='c-timeline-items__article__link')['href'] if article.find('a') else 'No link'
                result_box.insert(tk.END, f"• {title}\n", 'title')
                result_box.insert(tk.END, link, ('link', link))
                result_box.insert(tk.END, "\n")
                result_box.insert(tk.END, "\n")

    # adding the URL to the open function we defined 
    result_box.tag_bind('link', '<Button-1>', open_link)

# defining the main UI of tkinter
root = tk.Tk()
root.title("Stay Informed!")

# defining and customizing a button to launch the application in the main UI
scrape_button = tk.Button(root, text="GET THE NEWS! (from BBC - CNN - Telemenundo - Euronews)", command=scrape_website, width=20, height=2, font=('Helvetica', 10, 'bold'))
scrape_button.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# defining and customizing the result area
result_box = scrolledtext.ScrolledText(root, width=80, height=20)
result_box.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# defining and customizing the clock
clock_label = tk.Label(root, text="", font=('Helvetica', 14, 'bold'))
clock_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# customizing the app fonts
result_box.tag_config('bold', font=('Helvetica', 12, 'bold'))
result_box.tag_config('title', font=('Helvetica', 11))
result_box.tag_config('link', foreground='blue', underline=True)



# initializing the clock when starting the application
clock_thread = threading.Thread(target=update_clock)
clock_thread.daemon = True
clock_thread.start()

# launching the app
root.mainloop()