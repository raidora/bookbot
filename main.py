def count_characters(text):
    chars = {} 
    for c in text.lower():
        if not c.isalpha():
            continue

        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    structured_char_list = []
    for k, v in chars.items():
        structured_char_list.append({"char": k, "count": v})

    structured_char_list.sort(reverse=True, key=lambda d : d["count"])
    return structured_char_list

def pretty_print_counts(structured_char_list):
    for i in structured_char_list:
        print(f"The '{i["char"]}' character war found {i["count"]} times")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = file_contents.split()
        print(f"{len(words)} words found in the document\n")

        structured_char_list = count_characters(file_contents)
        pretty_print_counts(structured_char_list)

main()
