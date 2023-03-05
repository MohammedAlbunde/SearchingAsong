# THIS CODE WILL ASK  USER ABOUT WHAT  TO SEARCH IN THE YOUTUBE, GOOGLE AND YAHOO
import webbrowser
import tkinter as tk
from urllib.parse import quote

def play_song():
    song_name = entry.get()
    search_engine = engine_var.get()
    if search_engine == "YouTube":
        search_url = f"https://www.youtube.com/results?search_query={quote(song_name)}"
    elif search_engine == "Google":
        search_url = f"https://www.google.com/search?q={quote(song_name)}"
    elif search_engine == "Yahoo":
        search_url = f"https://search.yahoo.com/search?p={quote(song_name)}"
    webbrowser.open(search_url)
    
root = tk.Tk()
root.title("Song Search")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

engine_var = tk.StringVar()
engine_var.set("YouTube")
engine_options = ["YouTube", "Google", "Yahoo"]
engine_menu = tk.OptionMenu(root, engine_var, *engine_options)
engine_menu.pack(pady=10)

submit_btn = tk.Button(root, text="Search", command=play_song)
submit_btn.pack(pady=10)

browser_control = tk.Frame(root)
browser_control.pack()

root.mainloop()
