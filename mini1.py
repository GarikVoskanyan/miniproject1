import random

def get_input(prompt):
    return input(prompt)

def generate_hospital_story():
    number = get_input("Input a number: ")
    time_measure = get_input("Measure of time: ")
    transportation = get_input("Mode of transportation: ")
    adjective1 = get_input("Input an adjective: ")
    adjective2 = get_input("Input another adjective: ")
    noun = get_input("Input a noun: ")
    color = get_input("Input a color: ")
    body_part = get_input("Input a body part: ")
    verb = get_input("Input a verb: ")
    animal = get_input("Input an animal: ")
    silly_word = get_input("Input a silly word: ")

    story = f"It was about {number} {time_measure} ago when I arrived at the hospital in a {transportation}. " \
            f"The hospital is a/an {adjective1} place; there are a lot of {adjective2} {noun} here. " \
            f"There are nurses here who have {color} {body_part}. If someone wants to come into my room, " \
            f"I told them that they have to {verb} first. I've decorated my room with {number} {noun}." \
            f"Today I talked to a doctor, and they were wearing a {animal} on their {body_part}. " \
            f"I heard that all doctors {verb} {silly_word} every day for breakfast. " \
            f"The most delicious thing about being in the hospital is the {silly_word} {noun}!"

    return story

def generate_camping_story():

    person_name = get_input("Proper Noun (Person's Name): ")
    adjective_feeling1 = get_input("Adjective (Feeling): ")
    verb1 = get_input("Verb: ")
    adjective_feeling2 = get_input("Adjective (Feeling) 2: ")
    animal = get_input("Animal: ")
    color = get_input("Color: ")
    verb_ing = get_input("Verb + ing: ")
    adverb_ly = get_input("Adverb + ly: ")
    number = get_input("Number: ")
    silly_word = get_input("Silly Word: ")
    noun2 = get_input("Noun: ")

    story = f"This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {noun2}. " \
            f"I am so {adjective_feeling1} to {verb1} in a tent. I am {adjective_feeling2} we might see a(n) " \
            f"{animal}, I hear they're kind of dangerous. While we're camping, we are going to hike, fish, " \
            f"and {verb_ing}. I have heard that the {color} lake is great for {verb_ing}. Then we will " \
            f"{adverb_ly} hike through the forest for {number} minutes. If I see a {color} {animal} while hiking, " \
            f"I am going to bring it home as a pet! At night, we will tell {number} {silly_word} stories " \
            f"and roast {noun2} around the campfire!"

    return story

def generate_castle_letter():
    person_name = get_input("Input Proper Noun (Person's Name): ")
    adjective = get_input("Input an adjective: ")
    color = get_input("Input a color: ")
    animal = get_input("Input an animal: ")
    place = get_input("Input a place: ")
    adjective2 = get_input("Input another adjective: ")
    magical_creature_plural1 = get_input("Input a magical creature (plural): ")
    adjective3 = get_input("Input yet another adjective: ")
    magical_creature_plural2 = get_input("Input another magical creature (plural): ")
    room_in_a_house = get_input("Input a room in a house: ")
    noun = get_input("Input a noun: ")
    noun2 = get_input("Input another noun: ")
    noun_plural3 = get_input("Input a plural noun: ")
    adjective4 = get_input("Input one more adjective: ")
    noun_plural4 = get_input("Input another plural noun: ")
    number = get_input("Input a number: ")
    measure_of_time = get_input("Input a measure of time: ")
    verb_ing = get_input("Input a verb (ending in -ing): ")
    adjective5 = get_input("Input yet another adjective: ")
    noun5 = get_input("Input one last noun: ")

    story = f"Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. " \
            f"I found myself here one day after going for a ride on a {color} {animal} in {place}. " \
            f"There are {adjective2} {magical_creature_plural1} and {adjective3} {magical_creature_plural2} here! " \
            f"In the {room_in_a_house}, there is a pool full of {noun}. " \
            f"I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adjective4} {noun_plural4}. " \
            f"It feels as though I have lived here for {number} {measure_of_time}. " \
            f"I hope one day you can visit, although the only way to get here now is {verb_ing} on a " \
            f"{adjective5} {noun5}!!"

    return story

def main():
    print("Choose a template:")
    print("1. Hospital Adventure")
    print("2. Camping Adventure")
    print("3. Castle Letter")

    choice = input("Enter the number of the template you'd like to use: ")

    if choice == "1":
        story = generate_hospital_story()
    elif choice == "2":
        story = generate_camping_story()
    elif choice == "3":
        story = generate_castle_letter()
    else:
        print("Invalid choice. Please select 1,2 or 3.")
        return

    print("\nYour adventure awaits!\n")
    print(story)

if __name__ == "__main__":
    main()
