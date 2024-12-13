#This is the file for main code

#Import the file with the functions
import Utility.ipynb

print("Let's find a movie to watch!")

allgenres = ["Action", "Comedy", "Drama", "Mystery/Thriller", "Horror"]
print("Please choose a genre:")
for i in range(len(genres)):
   print(str(i + 1) + ". " + genres[i])

genre_input = int(input("\nEnter the number of the genre you're interested in: "))
user_genre = genres[genre_input - 1]

print("\nYou selected the " + user_genre + " genre.")
print("Do you want to see:")
print("1. Most Recent Movies")
print("2. Top Rated Movies")

choice = int(input("\nEnter 1 or 2: "))

if choice == 1:
   Utility.ipynb.func1()
elif choice == 2:
   Utility.ipynb.func2()
else:
   print("Invalid choice, please restart the program.")
