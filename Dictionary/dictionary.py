dictionary = {
    "abandon": "To leave something behind forever.",
    "ability": "The skill or power to do something.",
    "achieve": "To reach a goal or succeed.",
    "active": "Doing things; busy or moving.",
    "advice": "Helpful suggestions or guidance.",
    "angry": "Feeling mad or upset.",
    "arrive": "To reach a place.",
    "beautiful": "Very nice to see or hear.",
    "believe": "To think something is true.",
    "brave": "Not afraid; showing courage.",
    "build": "To make something by putting parts together.",
    "calm": "Quiet and peaceful; not excited.",
    "care": "To feel concern or interest.",
    "catch": "To grab or take hold of something.",
    "clean": "Free from dirt or mess.",
    "clever": "Quick to understand; smart.",
    "cold": "Having a low temperature.",
    "create": "To make something new.",
    "danger": "The chance of harm or injury.",
    "decide": "To make a choice.",
    "dream": "Thoughts during sleep or a big goal.",
    "easy": "Not difficult; simple.",
    "enjoy": "To take pleasure in something.",
    "fail": "To not succeed.",
    "friend": "Someone you like and trust."
}


while True:

    user_input = input("Enter word(s) to search and exit to quit (separate multiple words with space): ").lower()

    words = user_input.split()
    if user_input == "exit":
        print("Exiting the dictionary search.")
        break

    for word in words:
        if word in dictionary:
            print(f"{word}: {dictionary[word]}")
        else:
            print(f"{word}: Word not found.")
   
