#This is the file for main code
print("Let's find a movie to watch!")

genres = ["Action", "Comedy", "Drama", "Mystery/Thriller", "Horror"]
print("Please choose a genre:")
for i in range(len(genres)):
   print(str(i + 1) + ". " + genres[i])

genre_input = int(input("\nEnter the number of the genre you're interested in: "))
selected_genre = genres[genre_input - 1]

print("\nYou selected the " + selected_genre + " genre.")
print("Do you want to see:")
print("1. Most Recent Movies")
print("2. Top Rated Movies")

choice = int(input("\nEnter 1 or 2: "))

if choice == 1:
   display_most_recent_movies(movies_data, selected_genre)
elif choice == 2:
   display_top_rated_movies(movies_data, selected_genre)
else:
   print("Invalid choice, please restart the program.")
