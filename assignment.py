#chris
#PM class
#personal profile & age calc assignment


print("Welcome to the personal profile and age calc")
print("I'm going to ask you a few questions about you.")
print("then i'll calculate approximately how long you have been alive")

name= str(input("Enter your name: "))
favorite_food = str(input("enter your favortie food:"))
favorite_hobby = str(input("enter your favorite hobby:" ))
city = str(input("enter the city you live in: "))
dream_job = str(input("enter your dream job: "))
favorite_video_game = str(input("enter your favotrite game: "))

Birth_year = int(input("Enter your birth year: "))
age = 2026 - Birth_year
months_lived = age * 12
days_lived = months_lived * 31
hours_lived = days_lived * 24 
mins_lived = hours_lived * 60
seconds = mins_lived * 60 



print(" -----------" + str(name) + "'s PROFILE ---------")
print("hello " + str(name)+"!")
print("your from " + str(city))
print("your favorite food is " + str(favorite_food))
print("you enjoy "+ str(favorite_hobby))
print("your dream job " + str(dream_job))
print("your favorite video game is " + str(favorite_video_game))

print("Your age is, " + str(age) + "!")
print("you've been alive for " + str(months_lived) + " months!")
print("you've been alive for " + str(days_lived) + " days!")
print("you've been alive for " + str(hours_lived) + " hours!")
print("you've been alive for " + str(seconds) + " seconds!")

print("thats insane!")
