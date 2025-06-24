def number_of_words(content):
    return len(content.split())

def sort_dictionary(dict_arg):
    output = [{"char": key, "num": dict_arg[key]} for key in dict_arg]
    output.sort(reverse=True, key=lambda char_dict: char_dict["num"])
    return output

def number_of_characters(content):
    split_content = list(content)
    char_counts = {}
    for char in split_content:
        current = char.lower()
        if current in char_counts:
            char_counts[current] += 1
        else:
            char_counts[current] = 1
    return sort_dictionary(char_counts)