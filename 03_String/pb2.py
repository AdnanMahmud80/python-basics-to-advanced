# name = input("Enter your name: ")
# date = input("selecting date : ")
# letter = f"Dear {name},\n\nI hope this letter finds you well. I am writing to inform you about the upcoming event on {date}. We are excited to have you join us and look forward to your participation.\n\nBest regards,\n{name}"
# print(letter)
letter = ''' Dear <|name|>
You are selected for this position. Your joining date is <|date|>. 
Please report to the office on time.'''
letter = letter.replace("<|name|>", "Adnan").replace("<|date|>", "2024-06-15")
print(letter)
