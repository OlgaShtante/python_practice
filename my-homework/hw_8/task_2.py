def vending_machine(drinks):
    input_money = 0
    chosen_drink = None

    print("Выберите напиток:")
    for drink, price in drinks.items():
        print(f"{drink} - {price} руб.")

    while True:
        drink = yield

        if drink in drinks:
            chosen_drink = drink
            print(f"Вы выбрали {chosen_drink}. Внесите {drinks[chosen_drink]} руб.")
        elif isinstance(drink, (int, float)):
            input_money += drink
            if chosen_drink:
                if input_money >= drinks[chosen_drink]:
                    change = input_money - drinks[chosen_drink]
                    print(f"Ваша сдача {change} руб.")

                    chosen_drink = None
                    input_money = 0
                    print("\nВыберите напиток:")
                    for drink, price in drinks.items():
                        print(f"{drink} - {price} руб.")
                else:
                    print(f"Недостаточно денег.")
            else:
                print("Выберите напиток:")
        else:
            print("Некорректный ввод")

def select_drink(drink_of_choice, input_money):
    stock = {'coffee': 10, 'cola': 20}
    vm = vending_machine(stock)
    next(vm)

    if drink_of_choice == 'coffee':
        vm.send(drink_of_choice)
    else:
        vm.send('cola')
    vm.send(input_money)


print(' * '*20)
select_drink('cola', 20) #Ваша сдача 0 руб.
print(' * '*20)
select_drink('coffee', 30) #Ваша сдача 20 руб.
print(' * '*20)
select_drink('cola', 0.99) #Недостаточно денег.
print(' * '*20)
select_drink('coffee', -8) #Недостаточно денег.
