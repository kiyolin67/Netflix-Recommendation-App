import customtkinter as ctk

# DATABASE FOR THE MOVIES 
movie_database = {
    "Action": {
        "title": "The Dark Knight",
        "year": 2008,
        "director": "Christopher Nolan",
        "synopsis": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
    },
    "Comedy": {
        "title": "The Grand Budapest Hotel",
        "year": 2014,
        "director": "Wes Anderson",
        "synopsis": "The adventures of Gustave H, a legendary concierge at a famous European hotel between the wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.",
    },
    "Drama": {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "director": "Frank Darabont",
        "synopsis": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    },
    "Science Fiction": {
        "title": "Inception",
        "year": 2010,
        "director": "Christopher Nolan",
        "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
    },
}

def get_recommendation(choice):
    # Get the movie recommendation based on the user's choice
    if choice == '1':
        selected_genre = "Action"
    elif choice == '2':
        selected_genre = "Comedy"
    elif choice == '3':
        selected_genre = "Drama"
    elif choice == '4':
        selected_genre = "Science Fiction"

    movie = movie_database[selected_genre]
    result_text.set(f" Genre: {selected_genre}\nTitle: {movie['title']}\nYear: {movie['year']}\nDirector: {movie['director']}\nSynopsis: {movie['synopsis']}")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x400")
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
output_label = ctk.CTkLabel(app, textvariable=result_text, wraplength=450, justify="left", font=("Helvetica", 16))
output_label.pack(pady=30)

# IMPORTANT DONT DELETE
if __name__ == "__main__":
    app.mainloop()
