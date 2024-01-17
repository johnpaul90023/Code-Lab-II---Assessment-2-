import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
import requests
import random
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import messagebox
import json

base_image_url = "https://image.tmdb.org/t/p/w500"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNmJiNTRkYjVjOTNiM2E0YzFjYWUyZTllMjhiYmRlYiIsInN1YiI6IjY1YTAyN2RlOTQ1ZDM2MDEyNGFlYmU4MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.A4Voc19KzDDvh_AE-6UXw3K14GhjBhn9fWqt3uKU0es"
}

class WMoviesGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x450')
        self.root.title('WMovies Generator')

        self.options_frame = OptionsFrame(self.root)
        self.main_frame = MainFrame(self.root, self.options_frame)

    def run(self):
        self.root.mainloop()

class OptionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#c9c0a7")

        self.main_frame = None  # Initialize main_frame as None

        self.home_btn = tk.Button(self, text='Home', font=('Bold', 12), bd=0, bg="#c9c0a7", fg="#1F1F1F", command=self.show_home)
        self.home_btn.place(x=10, y=50)

        self.movies_btn = tk.Button(self, text='Movies', font=('Bold', 12), bd=0, bg="#c9c0a7", fg="#1F1F1F", command=self.show_movies)
        self.movies_btn.place(x=10, y=100)

        self.tvshows_btn = tk.Button(self, text='TV Shows', font=('Bold', 12), bd=0, bg="#c9c0a7", fg="#1F1F1F", command=self.show_tv_shows)
        self.tvshows_btn.place(x=10, y=150)

        self.instructions_btn = tk.Button(self, text='Instructions', font=('Bold', 12), bd=0, bg="#c9c0a7", fg="#1F1F1F", command=self.show_instructions)
        self.instructions_btn.place(x=10, y=200)

        self.pack(side=tk.LEFT, fill=tk.Y)  # Adjusted the pack method
        self.pack_propagate(False)
        self.configure(width=120, height=450)

    def set_main_frame(self, main_frame):
        self.main_frame = main_frame  # Set the main_frame reference

    def show_home(self):
        self.main_frame.show_home()

    def show_movies(self):
        self.main_frame.show_movies()

    def show_tv_shows(self):
        self.main_frame.show_tv_shows()

    def show_instructions(self):
        self.main_frame.show_instructions()

class MainFrame(tk.Frame):
    def __init__(self, parent, options_frame):
        super().__init__(parent, bg="#75736a", bd=0)

        self.options_frame = options_frame
        self.options_frame.set_main_frame(self) 

        self.pages = {
            'home': HomePage(self),
            'movies': MoviesPage(self),
            'tv_shows': TVShowsPage(self),
            'instructions': InstructionsPage(self)
        }

        self.show_home()

        self.pack(side=tk.LEFT)
        self.pack_propagate(False)
        self.configure(width=680, height=450)

    def show_home(self):
        self.show_page('home')

    def show_movies(self):
        self.show_page('movies')

    def show_tv_shows(self):
        self.show_page('tv_shows')

    def show_instructions(self):
        self.show_page('instructions')

    def show_page(self, page_name):
        for page in self.pages.values():
            page.hide()
        self.pages[page_name].show()

class Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#75736a")

    def show(self):
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 
        self.pack_propagate(False)

    def hide(self):
        self.pack_forget()

class HomePage(Page):
    def __init__(self, parent):
        super().__init__(parent)

        self.img = PhotoImage(file="original/TV.png")
        self.label = tk.Label(self, image=self.img, bd=0)
        self.label.place(x=0, y=0)

        welcome = tk.Label(self, text='W E L C O M E !', bg="#8f9086", font=('Bold', 30))
        welcome.place(x= 120, y=150)

        name = tk.Label(self, text='Made by John Paul T. Gonzales', bg="#8f9086", font=('Bold', 10))
        name.place(x= 120, y=250)

class MoviesPage(Page):
    def __init__(self, parent):
        super().__init__(parent)

        Details = Frame(self, bg="#6b6860", width=400, height=340)
        Details.place(x=30, y=100)

        self.lb = tk.Label(self, text='Random Movies', bg="#6b6860", font=('Times New Roman', 30), width=15)
        self.lb.place(x=375, y=20)

        self.random_button = Button(self, text="Generate a Random Movie", bg="#604837", fg="white", font=('Roboto',15), command=self.Movie_Data)
        self.random_button.place(x=30, y=28)

        self.Title_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15) , wraplength=300, width=30, height=2, anchor=W)
        self.Title_output.place(x=80, y=9)

        title = Label(Details, text = "Title: ", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        title.place(x=10, y=18)

        self.Overview_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',9), wraplength=300, width=45, height=10, anchor=W)
        self.Overview_output.place(x=86, y=200)

        overview = Label(Details, text = "Overview: ", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        overview.place(x=10, y=210)

        self.ID_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        self.ID_output.place(x=120, y=110)

        id = Label(Details, text = "ID: ", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        id.place(x=10, y=110)

        self.Release_date_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        self.Release_date_output.place(x=120, y=65)  

        releasedate = Label(Details, text = "Release date: ", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        releasedate.place(x=10, y=65)

        self.popularity_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        self.popularity_output.place(x=120, y=160)

        popularity_output = Label(Details, text = "Popularity", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        popularity_output.place(x=10, y=160)


    def Movie_Data(self):
        url = f"https://api.themoviedb.org/3/movie/popular" 
        response = requests.get(url, headers=headers)
        data = response.json()

        with open('Popular_movies.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

        randomized = random.randint(0, len(data['results']))

        Title= (data["results"][randomized]["original_title"])
        self.Title_output.config(text=Title)
        Overview= (data["results"][randomized]["overview"])
        self.Overview_output.config(text=Overview)
        Id= (data["results"][randomized]["id"])
        self.ID_output.config(text=Id)
        release_date= (data["results"][randomized]["release_date"])
        self.Release_date_output.config(text=release_date)
        popularity= (data["results"][randomized]["popularity"])
        self.popularity_output.config(text=popularity)
        image_path = (data['results'][randomized]["poster_path"])
        full_image_url = base_image_url + image_path

        image_response = requests.get(full_image_url)

        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            image = image.resize((200, 300))
            image = ImageTk.PhotoImage(image)
            image_label = Label(self, image=image, bg="#6b6860")
            image_label.image = (image)
            image_label.place(x=460, y=100)

class TVShowsPage(Page):
    def __init__(self, parent):
        super().__init__(parent)

        Details = Frame(self, bg="#6b6860", width=400, height=340)
        Details.place(x=30, y=100)

        self.lb = tk.Label(self, text='Random TV Show', bg="#6b6860", font=('Times New Roman', 30), width=15)
        self.lb.place(x=360, y=20)

        self.random_button = Button(self, text="Generate a Random TV Show", bg="#604837", fg="white", font=('Roboto',15), command=self.TV_Data)
        self.random_button.place(x=30, y=28)

        self.Title_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15) , wraplength=300, width=30, height=2, anchor=W)
        self.Title_output.place(x=80, y=9)

        title = Label(Details, text = "Title: ", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        title.place(x=10, y=18)

        self.Overview_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',9), wraplength=300, width=45, height=10, anchor=W)
        self.Overview_output.place(x=86, y=200)

        overview = Label(Details, text = "Overview: ", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        overview.place(x=10, y=210)

        self.ID_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        self.ID_output.place(x=120, y=110)

        id = Label(Details, text = "ID: ", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        id.place(x=10, y=110)

        self.Release_date_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        self.Release_date_output.place(x=120, y=65)  

        releasedate = Label(Details, text = "Release date: ", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        releasedate.place(x=10, y=65)

        self.popularity_output = Label(Details, text = "", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        self.popularity_output.place(x=120, y=160)

        popularity_output = Label(Details, text = "Popularity", bg="#6b6860", fg="#2c2a2b", font=('Roboto',15))
        popularity_output.place(x=10, y=160)


    def TV_Data(self):
        url = f"https://api.themoviedb.org/3/tv/popular"
        response = requests.get(url, headers=headers)
        data = response.json()

        with open('Popular_TV_shows.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

        randomized = random.randint(0, len(data['results']))

        Title= (data["results"][randomized]["original_name"])
        self.Title_output.config(text=Title)
        Overview= (data["results"][randomized]["overview"])
        self.Overview_output.config(text=Overview)
        Id= (data["results"][randomized]["id"])
        self.ID_output.config(text=Id)
        release_date= (data["results"][randomized]["first_air_date"])
        self.Release_date_output.config(text=release_date)
        popularity= (data["results"][randomized]["popularity"])
        self.popularity_output.config(text=popularity)
        image_path = (data['results'][randomized]["poster_path"])
        full_image_url = base_image_url + image_path

        image_response = requests.get(full_image_url)

        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            image = image.resize((200, 300))
            image = ImageTk.PhotoImage(image)
            image_label = Label(self, image=image, bg="#6b6860")
            image_label.image = (
                image  # keep a reference to the image to prevent garbage collection
            )
            image_label.place(x=460, y=100)

class InstructionsPage(Page):
    def __init__(self, parent):
        super().__init__(parent)

        self.img = PhotoImage(file="original/TV.png")
        self.label = tk.Label(self, image=self.img, bd=0)
        self.label.place(x=0, y=0)

        InstrButton = Button(self, text = "Instructions",bg="#8f9086" ,font=('Roboto',15,'bold'),command=self.manual)
        InstrButton.place(x=200, y=200)

    def manual(self):
        message = "This application generates random movies and TV shows \n \n 1. The Movie and TV Show sections are located on the left side of the screen \n \n 2. In the Movie section there will be a button that will generate a random movie with its details printing out, you can generate movies multiple times \n \n 3. In the TV Show section there will be a button where you can press and generate multiple TV Shows printing out also its details. \n \n 4. Enjoy!"
        messagebox.showinfo("Instructions",message)

if __name__ == "__main__":
    app = WMoviesGenerator()
    app.run()
