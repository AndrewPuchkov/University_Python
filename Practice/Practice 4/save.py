def read_file(name):
    '''if not os.path.exists(f"{name}.txt"):
        flag = False
        while flag != True:
            name = input('Такого файла нет, вы ошибились, попробуйте ещё раз: ').strip()
            if os.path.exists(f"{name}.txt"):
                flag = True'''
    f = open(f"{name}", mode="r", encoding="utf8")
    strings = f.read().splitlines()
    strings_list = [strings[i].split(' ') for i in range(len(strings))]
    clear_strings_list = []
    for i in range(len(strings_list)):
        for word in strings_list[i]:
            word = ''.join(filter(str.isalnum, word)).lower()
            if len(word) > 0:
                clear_strings_list.append(word)
    words_set = set(clear_strings_list)
    return sorted(words_set)




def save_file(name, words):
    new_text = open(f"{name}", mode='w', encoding='utf8')
    new_text.write(f"{(len(words))} \n")
    for i in range(len(words)):
        new_text.write(f"{(words[i])} \n")

# save_file('count.txt', words)
