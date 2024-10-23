import re

def password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None
    
    # Strength score
    score = 0
    
    # Add points based on the criteria met
    if length_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_criteria:
        score += 1
    
    # Assess the strength based on the score
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"


def main():
    print("Password Strength Checker")
    password = input("Enter your password to assess: ")
    strength = password_strength(password)
    print(f"Password Strength: {strength}")
    
    # Provide feedback
    if strength == "Very Weak" or strength == "Weak":
        print("Your password is weak. Consider the following tips to improve it:")
        print("- Make sure it is at least 8 characters long.")
        print("- Include both uppercase and lowercase letters.")
        print("- Add numbers and special characters.")
    elif strength == "Moderate":
        print("Your password is okay, but it could be stronger. Consider adding more variety (uppercase letters, numbers, or special characters).")
    elif strength == "Strong":
        print("Your password is strong, but adding more characters or special characters could make it even more secure.")
    elif strength == "Very Strong":
        print("Your password is very strong! Well done.")
        

if __name__ == "__main__":
    main()
