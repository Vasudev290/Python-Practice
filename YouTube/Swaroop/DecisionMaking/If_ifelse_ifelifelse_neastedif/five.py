#Neasted if condition

weather = input("Enter the Weather condition :")
time_of_day = 'night'

if weather == 'sunny':
    if time_of_day == 'day':
        print("I'll go and play the cricket in ground🏏")
    else:
        print("It's night, time to sleep")
        
elif weather == 'rainy':
    print("I want to eat icecream 🤤")
    
elif weather == 'snowy':
    if time_of_day == 'night':
        print("Go for ride with WOLF 🐺")
    else:
        print("You can play with your snowman toy")
        
else:
    print("At Home, Play the Video Game 🎲 (FreeFire)")
    
print("Code Ended Here..!!")