#replace double space with single space
a = input("Enter a sentence: ")
double_space = a.find("  ")   
print(f"Double space found: {double_space}")
sentence=a.replace("  "," ")
print(f"After replacing double space with single space: {sentence}")

