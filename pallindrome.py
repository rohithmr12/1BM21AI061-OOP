def is_palindrome(string):
    cleaned_string = string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
