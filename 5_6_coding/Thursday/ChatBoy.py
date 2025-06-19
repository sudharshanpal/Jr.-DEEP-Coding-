# 1. A place
# 1. What continent is my place
# 2. What language to people in my place speak
# 3. What does my place look like??
# 4. What is the weather like
# 5. What fun things can i do?

import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "b8d224b0-4d1f-11f0-8b39-c5e1c8b7b07892f12741-fff7-4a0a-a40c-56a25f3c8374"
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