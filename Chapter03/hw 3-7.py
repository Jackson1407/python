# Chapter 3 Homework 3-7

names = [ "Hezz", "Eli", "Jay"]
print(names)


message = f" {names[0]}, you are invited to dinner today at 6:00."
print(message)

message = f" {names[1]}, you are invited to dinner today at 6:00."
print(message)

message = f" {names[2]}, you are invited to dinner today at 6:00."
print(message)

message = " I found a bigger table!"
print(message)

names.insert(0, 'Ezra')
print(names)

names.insert(1, 'Allen')
print(names)

names.insert(5, 'Fed')
print(names)

message = f" {names[0]}, you are invited to dinner today at 6:00."
print(message)

message = f" {names[1]}, you are invited to dinner today at 6:00."
print(message)

message = f" {names[5]}, you are invited to dinner today at 6:00."
print(message)


popped_names = names.pop(0)
print(f"Sorry, I can only invite two prople tonight {popped_names}")

popped_names = names.pop(1)
print(f"Sorry, I can only invite two prople tonight {popped_names}")

#ask Mr. Fed