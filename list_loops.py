# Question 1 
songs = ["ROCKSTAR", "Do It", "For The Night"]

# Question 2
print(songs[0:2])
print(songs[1:])

# Question 3
songs[2] = "Easy"
print(songs[2])

# Question 4
songs.extend([
    "Reachin' 2 Much", 
    "Time Alone With You", 
    "All I Need"])
songs.pop(1)

# Question 5
for song in songs:
    print(song)
for i in range(len(songs)):
    print(songs[i])

# Question 6
animals = [
    "Dogs",
    "Lions",
    "Penguins"
]
animals.append("Bulls")
print(animals[2])
animals.pop(0)
for i in animals:
    print(i)