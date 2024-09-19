def convert_to_cili():
    input_list = input("Введіть список дійсних чисел через пробіл: ").split()
    
    disni_numbers = [float(num) for num in input_list]
    
    cili_numbers = [round(num) for num in disni_numbers]
    

    print("Список цілих чисел після округлення:", cili_numbers)

#
convert_to_cili()
