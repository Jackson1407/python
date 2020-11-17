# Chapter 5 Homework 5-10

current_users = [ "Steve", "Frank", "Sam", "Jess", "Jo"]
new_users = [ "Henry", "Carl", "Sam", "Luke", "Jo"]
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is unavaliable.")
    else:
        print(f"{new_user} is avaliable!")
