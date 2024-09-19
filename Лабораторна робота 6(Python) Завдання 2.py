def find_short_word():
    
    input_list = input("Введіть список слів через пробіл: ").split()
    
    min_length = min(len(word) for word in input_list)
    
    short_word = [word for word in input_list if len(word) == min_length]
    
    print("Найкоротші слова в списку:", ", ".join(short_word))

#
find_short_word()
