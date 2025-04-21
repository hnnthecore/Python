# Exercise 01: List Basics

# Step 1: Create a list of 5 favorite movies
movies = ["Inception", "Interstellar", "The Matrix", "The Godfather", "Pulp Fiction"]

# Step 2: Print the entire list
print("My favorite movies:", movies)

# Step 3: Access and print the first and last movie
print("First movie:", movies[0])
print("Last movie:", movies[-1])

# Step 4: Change the third movie
movies[2] = "The Dark Knight"
print("Updated movie list:", movies)

# Step 5: Add a new movie to the list
movies.append("Forrest Gump")
print("After adding a new movie:", movies)

# Step 6: Print the total number of movies
print("I have", len(movies), "favorite movies.")
