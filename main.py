def sort_on(e):
    for value in e.values():
        return value

def main():
    with open("books/frankenstein.txt") as f:
        count_characters = {}

        file_contents = f.read()

        count_spaces = file_contents.count(" ")
        count_characters[" "] = count_spaces

        words = file_contents.split()
        words_len = str(len(words))
        #print(file_contents)
        #print(len(words))
        for word in words:
            word_lc = word.lower()
            for w in word_lc:
                if w in count_characters:
                    count_characters[w] += 1
                else:
                    count_characters[w] = 1

        print("--- Begin report of books/frankenstein.txt ---")
        print(words_len + " words found in the document")
        print(" ")

        count_characters_alph = {}

        for character in count_characters:
            if character.isalpha():
                aux_key = character
                aux_val = count_characters[character]
                count_characters_alph[aux_key] = aux_val
        
        ordered_list = []
        for key, value in count_characters_alph.items():
            aux_dict = {}
            aux_dict[key] = value
            ordered_list.append(aux_dict)

        ordered_list.sort(reverse=True, key=sort_on)

        for element in ordered_list:
            for e in element:
                count_string = str(element[e])
                print(f"The '{e}' character was found {count_string} times")
            
        print("--- End report ---")


main()
