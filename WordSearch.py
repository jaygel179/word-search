import sys

from wordsearch.wordsearch import word_search


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = str(sys.argv[1])
        word_search(filename)
    else:
        raise Exception("Missing filename. Example usage: `$ python WordSearch.py /path/to/file.pzl`")
