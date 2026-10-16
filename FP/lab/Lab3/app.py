import math
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) - 1, 2):
        if x % i == 0:
            return False
    return True

def property1(numbers):
    '''
    Calculeaza lungimea secventei maxime dintr-un sir cu proprietatea ca numerele sunt distincte
    :param numbers: Lista de numere intregi
    :return: Numar intreg max_lenght - lungimea secventei maxime cu prop1
    '''
    curr_list = []
    max_length = []
    for num in numbers:
        while num in curr_list:
            curr_list.pop(0)
        curr_list.append(num)
        if len(curr_list) > len(max_length):
            max_length = curr_list.copy()
    return max_length

def property2(numbers):
    '''
    Calculeaza lungimea secventei maxime dintr-un sir cu proprietatea ca diferentele
    numbers[i+1] - numbers[i] si numbers[i+2] - numbers[i+1] au semne contrare
    :param numbers: Lista de numere intregi
    :return: Numar intreg max_length - lungimea secventei maxime cu prop2
    '''
    if len(numbers) < 2:
        return []
    if len(numbers) == 2:
        return []
    max_lenght = numbers[:2]
    curr_lenght = [numbers[0], numbers[1]]
    for i in range(len(numbers) - 2):
        dif1 = numbers[i + 1] - numbers[i]
        dif2 = numbers[i + 2] - numbers[i + 1]
        if dif1 * dif2 < 0:
            curr_lenght.append(numbers[i + 2])
            if len(curr_lenght) > len(max_lenght):
                max_lenght = curr_lenght.copy()
        elif dif1 * dif2 > 0:
            curr_lenght = [numbers[i + 1], numbers[i + 2]]
    return max_lenght

def property3(numbers):
    '''
    Calculeaza lungimea celei mai lungi secvente de numere prime
    :param numbers: Lista de numere intregi
    :return: Numar intreg max_length - lungimea secventei maxime cu prop3
    '''
    curr_lenght = []
    max_lenght = []
    for el in numbers:
        if is_prime(el):
            curr_lenght.append(el)
            if len(curr_lenght) > len(max_lenght):
                max_lenght = curr_lenght.copy()
        else:
            curr_lenght = []
    return max_lenght

def set_numbers_to_integer(numbers):
    '''
    Transforma elementele listei numbers din string-uri in int
    :param numbers: Lista de string-uri
    :return: Lista de numere intregi numbers
    '''
    for num in range(len(numbers)):
        try:
            numbers[num] = int(numbers[num])
        except ValueError:
            print("Valoare invalida")
            break
    return numbers

def test():
    numbers = ['1', '5', '7', '5', '6', '7', '1', '2', '3', '5', '4']
    set_numbers_to_integer(numbers)
    assert numbers == [1, 5, 7, 5, 6, 7, 1, 2, 3, 5, 4]
    assert property1(numbers) == [6, 7, 1, 2, 3, 5, 4]
    assert property2(numbers) == [5, 7, 5, 6]
    numbers = ['2', '2', '2', '2', '2']
    set_numbers_to_integer(numbers)
    assert numbers == [2, 2, 2, 2, 2]
    assert property1(numbers) == [2]
    assert property2(numbers) == [2, 2]
    numbers = ['1', '2']
    set_numbers_to_integer(numbers)
    assert numbers == [1, 2]
    assert property1(numbers) == [1, 2]
    numbers = ['7']
    set_numbers_to_integer(numbers)
    assert numbers == [7]
    assert property2(numbers) == []
    numbers = ['a', 'b', 'c', 'd']
    set_numbers_to_integer(numbers)
    assert numbers == ['a', 'b', 'c', 'd']
    numbers = ['1', '3', 'a', 'b', '4']
    set_numbers_to_integer(numbers)
    assert numbers == [1, 3, 'a', 'b', '4']
    numbers = ['1', '2', '3', '5', '1', '9', '2', '3', '11', '17']
    set_numbers_to_integer(numbers)
    assert numbers == [1, 2, 3, 5, 1, 9, 2, 3, 11, 17]
    assert property3(numbers) == [9, 2, 3, 11, 17]
    numbers = ['-1', '-2', '3']
    set_numbers_to_integer(numbers)
    assert numbers == [-1, -2, 3]
    assert property3(numbers) == [3]
    numbers = []
    assert property1(numbers) == []
    assert property2(numbers) == []
    assert property3(numbers) == []

def main():
    properties = {"2": property1,
                  "3": property2,
                  "4": property3}
    while True:

        command = input("Selectati o comanda: \n"
                        "1: Dati un sir de numere intregi: \n"
                        "2: Returneaza lungimea celei mai lungi secvente cu proprietatea ca elementele consecutive sunt distincte \n"
                        "3: Returneaza lungimea celei mai lungi secvente in care diferentele consecutive doua cate doua au semne contrare \n"
                        "4: Returneaza lungimea celei mai lungi secvente care contine doar numere prime \n"
                        "exit: Opreste programul \n")
        if command == "1":
            numbers = input("Introduceti un sir de numere intregi: \n")
            numbers = numbers.split()
            numbers = set_numbers_to_integer(numbers)
            continue
        if command == "exit":
            print("bye")
            break
        if command in properties:
            print(f"Secventa de lungime maxima este: {properties[command](numbers)}")
        else:
            print(f"{command} nu este o comanda valida")

test()
main()


