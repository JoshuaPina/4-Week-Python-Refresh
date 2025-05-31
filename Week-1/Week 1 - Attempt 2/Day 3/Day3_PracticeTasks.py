#Favorite Animes List
print()
fav_anime_list = ["Attack on Titan","Jujutsu Kaisen", 
                  "My Hero Academia", "Dragon Ball Z", 
                  "Deathnote"]

print("The list for my favorite anime is: ", fav_anime_list)
print()

for anime in fav_anime_list:
    print(anime)
print()
print(f"Total number of elements in this list: {len(fav_anime_list)}")
print()
# Enumerate the favorite anime list
print("Enumerating my favorite anime list:")
for anime in enumerate(fav_anime_list):
    print(anime)
print()
print("Lists are ordered, mutable containers that allow duplicates. " \
"Element 0 is my current favorite anime.")
print()
print(f"The first anime in my list (element 0) is: {fav_anime_list[0]}")
print()
fav_anime_list.append("One Piece")
print("After appending a new anime, the list is now:\n ")

for anime in fav_anime_list:
    print(anime)
print()
print(f"The length of my favorite anime list is: {len(fav_anime_list)}")
print()
fav_anime_list.remove("One Piece")
print("After removing the last anime element, the list is now: \n")
for anime in fav_anime_list:
    print(anime)
print()

