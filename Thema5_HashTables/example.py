"""Кэширую имена людей"""

users = {}

def was_in_a_users(users, username):
    if username in users:
        return True
    else:
        users[username] = True
        return False

print(was_in_a_users(users, 'Gleb'))
print(was_in_a_users(users, 'Sanya'))
print(was_in_a_users(users, 'Valentin'))
print(was_in_a_users(users, 'Egor'))
print(was_in_a_users(users, 'Valentin'))