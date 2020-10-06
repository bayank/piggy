def pig_latin(text):
    words = text.split(' ')
    pig3 = []
    for x in words:
        # Remove the 0th character for each string in the xth element in list words
        pig2 = x.strip(x[0])
        # Concactenate the resulting string with the 0th character and add "ay" to the end
        pigay = [pig2 + x[0] + "ay"]
        # Create a new list by adding the xth element
        pig3 = pig3 + pigay
        # Join all the elements in the list into a string separated by a space, and capitalize the first letter
        pig4 = " ".join(pig3).capitalize()
    return pig4

text = input("Enter your input: ")
print(pig_latin(text))
