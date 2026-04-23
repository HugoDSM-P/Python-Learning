text = input("Write a text: ")
letters = input("Write 3 letters separated by space: ").split()

letter1 = letters[0]
letter2 = letters[1]
letter3 = letters[2]

print(f"The letter '{letter1}' appears {text.count(letter1)} times")
print(f"The letter '{letter2}' appears {text.count(letter2)} times")
print(f"The letter '{letter3}' appears {text.count(letter3)} times")

print(f"The lenght of the text is: {len(text)}")

print(f"The first letter of the text is: {text[0]}")
print(f"The last letter of the text is: {text[-1]}")

print(text[::-1])
python_in_text = "Python" in text
print(f"¿Is the word 'Python' in the text? {python_in_text}")