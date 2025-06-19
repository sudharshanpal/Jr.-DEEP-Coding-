# 1. A place
# 1. What continent is my place
# 2. What language to people in my place speak
# 3. What does my place look like??
# 4. What is the weather like
# 5. What fun things can i do?

import requests
from dotenv import load_dotenv
import os
# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    load_dotenv()
    key = os.getenv("API_KEY")
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    if answerclass == "Location":
        print("Toronto is Located in Ontario, Canada")
    if answerclass == "Weather":
        print("Toronto is very sunny and warm in the summer but very cold in the winter")
    if answerclass == "Type of People":
        print("Toronto is very diverse in terms of the people there. They speak english")
    if answerclass == "Activities":
        print("You can watch sports games, go to lake ontario, and much more")
    if answerclass == "Visual":
        print("Very scenic with waterfronts and nice buildings")

print("What would you like to know about Toronto?")

while True:
    answer_question()
