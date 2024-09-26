movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]

def is_high_score(movie):
    return movie['imdb'] > 5.5

def filter_high_scores(movies):
    return [movie for movie in movies if is_high_score(movie)]

def filter_by_category(movies, category):
    return [movie for movie in movies if movie['category'].lower() == category.lower()]

def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

def average_score_by_category(movies, category):
    filtered_movies = filter_by_category(movies, category)
    return average_imdb_score(filtered_movies)

print("Is the first movie a high score?:", is_high_score(movies[0]))

high_score_movies = filter_high_scores(movies)
print("\nMovies with an IMDB score above 5.5:")
for movie in high_score_movies:
    print(f"- {movie['name']} (IMDB: {movie['imdb']}, Category: {movie['category']})")

romance_movies = filter_by_category(movies, "Romance")
print("\nRomance movies:")
for movie in romance_movies:
    print(f"- {movie['name']} (IMDB: {movie['imdb']})")

average_score = average_imdb_score(movies)
print(f"\nAverage IMDB score of all movies: {average_score:.2f}")

average_suspense_score = average_score_by_category(movies, "Suspense")
print(f"Average IMDB score of Suspense movies: {average_suspense_score:.2f}")
