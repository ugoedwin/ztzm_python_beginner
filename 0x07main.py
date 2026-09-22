is_logged_in = False
is_admin = False

if is_logged_in and is_admin:
    print("Welcome, Admin!")
elif is_logged_in and not is_admin:
    print("Welcome, User!")
else:
    print("Access Denied. Please log in.")