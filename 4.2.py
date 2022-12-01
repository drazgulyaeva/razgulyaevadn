def get_count_char(str_):
    my_dict = {}
    str_ = str_.lower()
    letters = []
    for bukva in str_:
        if bukva.isalpha():
            letters.append(bukva)
    for letter in letters:
        if letter in my_dict:
            my_dict[letter]+=1
        else:
            my_dict[letter]=1
    return(my_dict)

def percents (str_):
    str_ = str_.lower()
    letters = []
    for bukva in str_:
        if bukva.isalpha():
            letters.append(bukva)
    my_dict = get_count_char(str_)
    for letter in my_dict:
        my_dict[letter] =round((my_dict[letter]/len(letters)*100),1)
    return(my_dict)




# TODO посчитать количество каждой буквы в строке в аргументе
main_str = ("""Данное предложение будет разбиваться на отдельные слова. 
 В качестве разделителя для встроенного метода split будет выбран символ пробела. 
 На выходе мы получим список отдельных слов. 
 Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. 
 Приступим!!!!""")
print(get_count_char(main_str))
print(percents(main_str))
# print(get_count_char(main_str))
