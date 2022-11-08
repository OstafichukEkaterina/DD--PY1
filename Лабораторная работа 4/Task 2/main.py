def get_count_char(str_):
    count = 0
    for letter in str_.lower():
        if letter.isalpha():
            dict_[letter] = dict_.get(letter, count) + 1
    return dict_

def percentage(dict_):
    percentage_dict = {}
    sum_ = sum(dict_.values())
    for key, percent in dict_.items():
        percentage_dict[key] = round(percent / sum_ * 100, 2)
    return percentage_dict
dict_ = {}
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
