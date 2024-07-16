favorite_movies = []

def add_movie(movie):
    favorite_movies.append(movie)
    print(f"The movie {movie} was added to your list of favorite movies!")

def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"{movie} was removed from your list of favorite movies!")
    else:
        print(f"The movie {movie} was not found in your list of favorite movies!")

def display_movies():
    print("Favorite Movies")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
    print(f"There are {len(favorite_movies)} in your list of favorite movies!")

def find_movie(movie):
    if movie in favorite_movies:
        print(f"The movie {movie} was found in your list of favorite movies!")
    else:
        print(f"The movie {movie} was not found in your list of favorite movies!")

def clear_movies():
    favorite_movies.clear()
    print("All movies have been removed from your list of favorite movies!")


add_movie("Spirited Away")
add_movie("Princess Mononoke")
add_movie("The Wind Rises")
add_movie("Pompoko")

count_movies()
display_movies()

remove_movie("Pompoko")
count_movies()
display_movies()

remove_movie("Pokpoko")
count_movies()
display_movies()

find_movie("Spirited Away")
find_movie("Pompoko")

clear_movies()
count_movies()
display_movies()
