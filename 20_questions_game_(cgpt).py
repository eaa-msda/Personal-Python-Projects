# -*- coding: utf-8 -*-
"""20 Questions Game (CGPT)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-woGWKFIoeqS_95BKVN8iLkSr3RramQW
"""

# Errol Ian Ave Acosta
# 20 Questions (CGPT)
# Personal Python Projects
# November 26, 2024

# Import necessary libraries
import json

# Define a simple knowledge base
objects = [
    {"name": "dog", "attributes": ["alive", "animal", "domestic", "four-legged"]},
    {"name": "cat", "attributes": ["alive", "animal", "domestic", "four-legged"]},
    {"name": "elephant", "attributes": ["alive", "animal", "wild", "large"]},
    {"name": "car", "attributes": ["not alive", "vehicle", "man-made", "four-wheeled"]},
    {"name": "airplane", "attributes": ["not alive", "vehicle", "man-made", "flies"]},
    {"name": "tree", "attributes": ["alive", "plant", "stationary", "green"]},
    {"name": "rock", "attributes": ["not alive", "natural", "stationary", "hard"]},
]

# Define the main game function
def twenty_questions_game():
    print("Think of an object, and I'll try to guess it in 20 questions!")

    possible_objects = objects.copy()
    for i in range(20):
        if len(possible_objects) == 1:
            print(f"I guess you're thinking of a {possible_objects[0]['name']}!")
            return
        elif len(possible_objects) == 0:
            print("I can't figure it out. You stumped me!")
            return

        # Pick the most common attribute to ask about
        attributes_count = {}
        for obj in possible_objects:
            for attr in obj["attributes"]:
                attributes_count[attr] = attributes_count.get(attr, 0) + 1

        # Sort attributes by frequency
        sorted_attributes = sorted(attributes_count.items(), key=lambda x: -x[1])
        most_common_attr = sorted_attributes[0][0]

        # Ask the user about the most common attribute
        response = input(f"Does it have the attribute '{most_common_attr}'? (yes/no): ").strip().lower()
        if response == "yes":
            possible_objects = [obj for obj in possible_objects if most_common_attr in obj["attributes"]]
        elif response == "no":
            possible_objects = [obj for obj in possible_objects if most_common_attr not in obj["attributes"]]
        else:
            print("Please answer with 'yes' or 'no'.")

    print("I couldn't guess it in 20 questions. You win!")

# Run the game in Google Colab
if __name__ == "__main__":
    twenty_questions_game()