# Chapter 6 Homework 6-4

python_words = {
    "list" : "A list is a set of items in a particular order.",
    "tuples" : "Tuples allow you to create a list of items that cannot change.",
    "range" : "Range is a list of numbers.",
    "if statements" : "If statements identify when the conditions you want are present.",
    "dictionary" : "Dictionarys alow you to have two kinds of information, keys and values."
}
for word, meaning in python_words.items():
    print(f"A {word.title()}'s meaning = {meaning}")
