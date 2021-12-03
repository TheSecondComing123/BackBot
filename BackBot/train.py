data = {
    "Hello there!",
    "I'm leaving.",
    "How are you today?",
    "I like programming.",
    "Apples taste good.",
    "Is the weather good?",
    "What did you eat today?",
    "No",
    "Yes",
    "I am smart.",
    "Do you like exersising?",
    "I like to sing.",
    "What is your favorite summer game?"
}

with open("traindata.txt", mode="w") as file:
    file.write(str(data))
