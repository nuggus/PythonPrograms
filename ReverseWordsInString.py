def reverseworde(string):
    wordslist = []
    wordslist = str(string).split()
    index = len(wordslist) - 1
    reverse = ''
    while index >= 0:
        reverse += wordslist[index] + ' '
        index -= 1;
    return reverse


print(reverseworde('This is doesn\'t '))
