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