"""Here are the lists of workout categories and the lists of exercises within each category"""
import webbrowser
import nltk
import random
import time

Workout_Categories = ["Cardio", "High Intensity Interval Training", "Pilates", "Strength Training"]
Cardio = ["burpees", "jumping jacks", "high knees", "skaters", "mountain climbers", "donkey kicks", "jump rope", "jumping squats", "jumping lunges", "tuck jumps"]
High_Intensity_Interval_Training = ["burpees", "push ups", "plank jacks", "air squats", "lunges", "shoulder tap plank", "goblet squats", "tuck jumps", "walking lunges"]
Pilates = ["superman situps", "sit ups", "v crunches", "plank hip taps","leg scissors", "leg lifts", "up down planks"]
Strength_Training = ["goblet squats", "push ups", "kettlebell swings", "dumbell curls", "weighted lunges", "tricep dips", "overhead press", "shoulder press", "bent over row", "standing fly"]

"""Allows user to tell chatbot if they want more instruction on how to execute each exercise. This is the function that ends the chat. If YES, chatbot will provide user with link. If NO, chatbot will let user know they can quit chat at anytime. If QUIT, you end the chat."""

def workout_demo():
    stop = False
    
    demo_website_1 = "http://www.healthline.com/health/cardio-exercises-at-home"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    
    print("\nWould you like instruction on how to complete the exercises?")
    while stop == False:
        input_line = input("Choose YES, NO or QUIT")
        if "YES" in input_line:
            print("Ok! We will send you to a link that will explain these exerices. You can exit FitFinds by typing quit at any time")
            webbrowser.get(chrome_path).open(demo_website_1)
            time.sleep(1)
            return demo_website_1
        elif "NO" in input_line:
            print("Ok! You can exit FitFinds by typing quit at any time")
        elif "QUIT" in input_line:
            return ("Ok! Thanks for using FitFinds")
        else:
            print("Sorry! This is not an option. Choose YES or NO")
"""This function allows user to define how long they would like to exercise for. It will pull up a link demonstrating how to do the exercises if the user wants more instruction."""
    
def workout_time():
    stop = False
    print("\nHow long would you like to workout for?")
    while stop == False:
        input_line = input("Choose from 15, 30, or 45 minutes")
        if "15 minutes" in input_line:
            print("Ok! Complete 10 reps of each exercise for 3 rounds. Short and sweaty!")
            return workout_demo()
        elif "30 minutes" in input_line:
            print("Cool! Complete 20 reps of each exercise for 4 rounds. Just right!")
            return workout_demo()
        elif "45 minutes" in input_line:
            print("Good choice! Complete 30 reps of each exercise for 5 rounds. You've got this!")
            return workout_demo()
        else:
            print("Sorry! That time is not an option. Choose from 15, 30 or 45 minutes")
"""This function allows user to chose which category of workout they would like to do. This function will randomly choose 5 exercises from the list that matches the workout category of their choice"""

def workout_categories():
    stop = False
    print("\nWelcome to FitFinds!")
    while stop == False:
        input_line = input("What kind of workout are you in the mood for? Choose from Cardio, Pilates, High Intensity Interval Training, or Strength Training")
        if "Cardio" in input_line:          
            num_to_select = 5                         
            list_of_random_cardio = random.sample(Cardio, num_to_select)
            first_random_item = Cardio[0]
            second_random_item = Cardio[1] 
            print (list_of_random_cardio)
            return workout_time()
        elif "High Intensity Interval Training" in input_line:          
            num_to_select = 5                         
            list_of_random_high_intensity_interval_training = random.sample(High_Intensity_Interval_Training, num_to_select)
            first_random_item = High_Intensity_Interval_Training[0]
            second_random_item = High_Intensity_Interval_Training[1] 
            print (list_of_random_high_intensity_interval_training)
            return workout_time()
        elif "Pilates" in input_line:
            num_to_select = 5                         
            list_of_random_pilates = random.sample(Pilates, num_to_select)
            first_random_item = Pilates[0]
            second_random_item = Pilates[1] 
            print (list_of_random_pilates)
            return workout_time()
        elif "Strength Training" in input_line:
            num_to_select = 5                         
            list_of_random_strength = random.sample(Strength_Training, num_to_select)
            first_random_item = Strength_Training[0]
            second_random_item = Strength_Training[1] 
            print (list_of_random_strength)
            return workout_time()
        else:
            print("Sorry! That workout is not an option. Pick from Cardio, High Intensity Interval Training, Strength Training and Pilates.")

"""This function ends the chat officially"""
def end_chat(input_line):
    if 'quit' in input_line:
        return True
    else:
        return False
"""This is the main function that runs our chatbot, FitFinds"""

def FitFindsChat():

    chat = True
    while chat:
        msg = input('Greetings! :\t')
        out_msg = None

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'quit'
            print("Have a good workout!")
            chat = False
            break     
        return workout_categories()
        return workout_time()
        return workout_demo()
        
FitFindsChat()