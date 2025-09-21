def count_a_letter(sentence, letter):
    if isinstance(letter, int):
        return "Please enter letter, not integer"

    if not letter.isalpha():
        return None
    if not sentence:
        return None
    
    count = 0
    for char in sentence:
        if char == letter:
            count +=1
    
    return count

print(count_a_letter("world", 3))