
def property1(numbers):
    curr_list = []
    max_length = 0
    for num in numbers:
        while num in curr_list:
            curr_list.pop(0)
        curr_list.append(num)
        if len(curr_list) > max_length:
            max_length = len(curr_list)
    return max_length

def property2(numbers):
    if len(numbers) < 2:
        return 0
    if len(numbers) == 2:
        return 2
    max_lenght = 2
    curr_lenght = 2
    for i in range(len(numbers) - 2):
        dif1 = numbers[i + 1] - numbers[i]
        dif2 = numbers[i + 2] - numbers[i + 1]
        if dif1 * dif2 < 0:
            curr_lenght += 1
            if curr_lenght > max_lenght:
                max_lenght = curr_lenght
        elif dif1 * dif2 > 0:
            curr_lenght = 2

    return max_lenght

def set_numbers_to_integer(numbers):
    for num in range(len(numbers)):
        try:
            numbers[num] = int(numbers[num])
        except ValueError:
            print("Valoare invalida")
            break
    return numbers

def test():
    numbers = ['1', '4', '3', '4', '5', '8', '8']
    set_numbers_to_integer(numbers)
    assert numbers == [1, 4, 3, 4, 5, 8, 8]
    assert property1(numbers) == 4
    assert property2(numbers) == 4

def main():
    test()
    properties = {"1": property1,
                  "2": property2}
    while True:
        command = input("Selectati o comanda: \n"
                        "1: Returneaza lungimea celei mai lungi secvente cu elemente distincte \n"
                        "2: Returneaza lungimea celei mai lungi secvente in care sume consecutive doua cate doua au semne contrare \n"
                        "exit: Opreste programul \n")
        if command == "exit":
            print("bye")
            break
        elif command in properties:
            numbers = input("Introduceti un sir de numere intregi: \n")
            numbers = numbers.split()
            numbers = set_numbers_to_integer(numbers)
            print(f"Lungimea secventei maxime este: {properties[command](numbers)}")
        elif command != "":
            print(f"{command} nu este o comanda valida!")
            continue


main()


