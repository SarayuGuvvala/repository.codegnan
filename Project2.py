import re
# ======================================
# NAME VALIDATION
# ======================================
def validate_name(name):
    pattern = "^[A-Za-z ]+$"

    if re.fullmatch(pattern, name):
        return True
    return False


# ======================================
# EMAIL VALIDATION
# ======================================
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$'

    if re.fullmatch(pattern, email):
        return True
    return False


# ======================================
# PHONE NUMBER VALIDATION
# ======================================
def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'

    if re.fullmatch(pattern, phone):
        return True
    return False


# ======================================
# PASSWORD VALIDATION
# ======================================
def validate_password(password):
    # Minimum 8 characters
    # At least 1 uppercase
    # At least 1 lowercase
    # At least 1 digit
    # At least 1 special character

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if re.fullmatch(pattern, password):
        return True
    return False


# ======================================
# MAIN PROGRAM
# ======================================

name = input("Enter Name: ")
email = input("Enter Email: ")
phone = input("Enter Phone Number: ")
password = input("Enter Password: ")

print("\n===== VALIDATION RESULTS =====")

if validate_name(name):
    print("Name is Valid")
else:
    print("Invalid Name")

if validate_email(email):
    print("Email is Valid")
else:
    print("Invalid Email")

if validate_phone(phone):
    print("Phone Number is Valid")
else:
    print("Invalid Phone Number")

if validate_password(password):
    print("Password is Strong")
else:
    print("Weak Password")
