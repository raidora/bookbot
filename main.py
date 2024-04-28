def countCharacters(text):
    chars = {} 
    for c in text.lower():
        if not c.isalpha():
            continue

        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    structuredCharList = []
    for k, v in chars.items():
        structuredCharList.append({"char": k, "count": v})

    structuredCharList.sort(reverse=True, key=lambda d : d["count"])
    return structuredCharList

def prettyPrintCounts(structuredCharList):
    for i in structuredCharList:
        print(f"The '{i["char"]}' character war found {i["count"]} times")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = file_contents.split()
        print(f"{len(words)} words found in the document\n")

        structuredCharList = countCharacters(file_contents)
        prettyPrintCounts(structuredCharList)

main()
