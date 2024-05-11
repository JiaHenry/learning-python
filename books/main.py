def main():
    book_path = "frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    dict = count_letters(text)
    # print(dict)
    count_info = get_sorted(dict)
    gen_report(words, count_info)



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())

def count_letters(text):
    result = {}
    lower = text.lower()
    for c in lower:
        result[c] = result.get(c, 0) + 1
    return result

def sort_on(dict):
    return dict["count"]

def get_sorted(dict):
    result = []
    for c in dict.keys():
        if c.isalpha():
            result.append({ "char": c, "count": dict.get(c) })
    result.sort(reverse=True, key=sort_on)
    # print(result)
    return result

def gen_report(words, count_info):
    print("--- Begin ---")
    print(f"{words} words found in the document")
    print()
    for item in count_info:
        char = item["char"]
        count = item["count"]
        print(f"The '{char}' character was found {count} times")
    print("--- End ---")

main()