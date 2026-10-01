import customtkinter as ctk
import random

# DATABASE FOR THE MOVIES 
movie_database = {
    "Action": [
        {
            "title": "The Dark Knight",
            "year": 2008,
            "director": "Christopher Nolan",
            "synopsis": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham."
        },
        {
            "title": "Mad Max: Fury Road",
            "year": 2015,
            "director": "George Miller",
            "synopsis": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners."
        },
        {
            "title": "Gladiator",
            "year": 2000,
            "director": "Ridley Scott",
            "synopsis": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery."
        }
    ],
    "Comedy": [
        {
            "title": "The Grand Budapest Hotel",
            "year": 2014,
            "director": "Wes Anderson",
            "synopsis": "The adventures of Gustave H, a legendary concierge at a famous European hotel between the wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend."
        },
        {
            "title": "Superbad",
            "year": 2007,
            "director": "Greg Mottola",
            "synopsis": "Two co-dependent high school seniors are forced to deal with separation anxiety as their plan to stage a booze-soaked party goes awry."
        },
        {
            "title": "Knives Out",
            "year": 2019,
            "director": "Rian Johnson",
            "synopsis": "A detective investigates the death of a patriarch of an eccentric, combative family."
        }
    ],
    "Drama": [
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "director": "Frank Darabont",
            "synopsis": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
        },
        {
            "title": "Parasite",
            "year": 2019,
            "director": "Bong Joon Ho",
            "synopsis": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan."
        },
        {
            "title": "The Godfather",
            "year": 1972,
            "director": "Francis Ford Coppola",
            "synopsis": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
        }
    ],
    "Science Fiction": [
        {
            "title": "Inception",
            "year": 2010,
            "director": "Christopher Nolan",
            "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
        },
        {
            "title": "The Matrix",
            "year": 1999,
            "director": "The Wachowskis",
            "synopsis": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."
        },
        {
            "title": "Interstellar",
            "year": 2014,
            "director": "Christopher Nolan",
            "synopsis": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
        }
    ]
}

def get_recommendation(choice):
    if choice == '1':
        selected_genre = "Action"
    elif choice == '2':
        selected_genre = "Comedy"
    elif choice == '3':
        selected_genre = "Drama"
    elif choice == '4':
        selected_genre = "Science Fiction"

    movie = random.choice(movie_database[selected_genre])
    
    result_text.set(f" Genre: {selected_genre}\n\nTitle: {movie['title']} ({movie['year']})\nDirector: {movie['director']}\n\nSynopsis: {movie['synopsis']}")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x450")
app.title("Netflix Recommendation App")

title_label = ctk.CTkLabel(app, text="Netflix Recommendation App", font=("Helvetica", 20, "bold"), text_color="white")
title_label.pack(pady=20)

instruction_label = ctk.CTkLabel(app, text="Select a genre to get a movie recommendation:", font=("Helvetica", 14), text_color="white")
instruction_label.pack(pady=10)

button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

btn_action = ctk.CTkButton(button_frame, text="1. Action", command=lambda: get_recommendation('1'))
btn_action.grid(row=0, column=0, padx=10, pady=10)

btn_comedy = ctk.CTkButton(button_frame, text="2. Comedy", command=lambda: get_recommendation('2'))
btn_comedy.grid(row=0, column=1, padx=10, pady=10) 

btn_drama = ctk.CTkButton(button_frame, text="3. Drama", command=lambda: get_recommendation('3'))
btn_drama.grid(row=1, column=0, padx=10, pady=10)

btn_scifi = ctk.CTkButton(button_frame, text="4. Science Fiction", command=lambda: get_recommendation('4'))
btn_scifi.grid(row=1, column=1, padx=10, pady=10)

result_text = ctk.StringVar(value="")
output_label = ctk.CTkLabel(app, textvariable=result_text, wraplength=500, justify="left", font=("Helvetica", 14))
output_label.pack(pady=20)
# IMPORTANT DONT DELETE
if __name__ == "__main__":
    app.mainloop()
