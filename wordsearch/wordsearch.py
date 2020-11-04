from .models import Word


# word search function that accepts file path
def word_search(filename):
    # raise error if file extension is not valid .pzl
    if not _is_file_extension_valid(filename):
        raise Exception("Invalid file extension.")

    horizontal_texts = []  # list of text in horizontal position
    vertical_texts = []  # list of text in vertical position
    words_to_find = []  # list of Word object to search
    search_flag = False

    # raise error if file doesn't exists
    with open(filename) as f:
        for line in f:
            string = line.rstrip()

            if not string:
                search_flag = True
                continue

            if search_flag:
                words_to_find.append(Word(text=string))
                continue

            # append/add texts to list
            string = line.rstrip()
            horizontal_texts.append(string)
            for index in range(len(string)):
                if len(horizontal_texts) == 1:
                    vertical_texts.append(string[index])
                else:
                    vertical_texts[index] = "{}{}".format(vertical_texts[index], string[index])

    _create_output_file(
        filename,
        words=_search_words(horizontal_texts, vertical_texts, words_to_find),
    )


def _is_file_extension_valid(filename):
    return filename.endswith(".pzl")


def _search_words(horizontal_texts, vertical_texts, words_to_find):
    words_to_find = _update_words_if_found(horizontal_texts, words_to_find, horizontal=True)
    words_to_find = _update_words_if_found(vertical_texts, words_to_find, horizontal=False)

    return words_to_find


# iterate over list of text searching for word forward and backward way
def _update_words_if_found(list_of_texts, words_to_find, horizontal=True):
    for index, string in enumerate(list_of_texts, start=1):
        for word in words_to_find:
            if not word.found:
                start_index = string.lower().find(word.text.lower())
                start_index_reverse = string.lower()[::-1].find(word.text.lower())

                # if word found either forward or backward text
                # set common values for either horizontal or vertical texts
                if start_index > -1 or start_index_reverse > -1:
                    word.found = True
                    if horizontal:
                        word.start_y = index
                        word.end_y = index
                    else:
                        word.start_x = index
                        word.end_x = index

                # set specific value for forward text
                # either horizontal or vertical text
                if start_index > -1:
                    if horizontal:
                        word.start_x = start_index + 1
                        word.end_x = start_index + len(word.text)
                    else:
                        word.start_y = start_index + 1
                        word.end_y = start_index + len(word.text)

                # set specific value for backward text
                # either horizontal or vertical text
                elif start_index_reverse > -1:
                    if horizontal:
                        word.start_x = len(string) - start_index_reverse
                        word.end_x = (len(string) + 1) - (start_index_reverse + len(word.text))
                    else:
                        word.start_y = len(string) - start_index_reverse
                        word.end_y = (len(string) + 1) - (start_index_reverse + len(word.text))

    return words_to_find


def _create_output_file(filename, words=[]):
    output_filename = "{}.{}".format(filename.split(".")[0], "out")
    with open(output_filename, "w") as f:
        for word in words:
            f.write("{word}\n".format(word=str(word)))
