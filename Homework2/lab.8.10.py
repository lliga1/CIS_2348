#Marianel Liga 
#CIS 2348
#Lab 8.10
#Student ID: 1394330

def is_palindrome(text):
    front, reverse = '', ''
    for letter in text:
        if letter == ' ': continue
        front = front + letter
        reverse = letter + reverse
    return front == reverse

def main():

    text = input()
    if is_palindrome(text):
        print(text,'is a palindrome')
    else:
        print(text, 'is not a palindrome')
main()