import matplotlib.pyplot as plt

# List of movies
movies = [
    "Avatar",
    "Endgame",
    "Titanic",
    "Star Wars",
    "Infinity War",
    "Jurassic",
    "Lion King"
]

# Box office collections in billions of dollars
box_office_collections = [
    2.847,
    2.798,
    2.208,
    2.068,
    2.048,
    1.671,
    1.656
]
#Changes figsize so that movie titles do not overlap
plt.figure(figsize=(10, 6))
plt.plot(movies, box_office_collections, marker='o', color='blue', linestyle='-')

plt.xlabel('Movies')
plt.ylabel('Box Office Collection (Billions)')

# Adding a title to the graph
plt.title('Box Office Collection of Movies')

# Displaying the graph
plt.grid(True)
plt.savefig("Movie_collection.png")
plt.show()
