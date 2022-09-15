def won_strategi(how_many_pancil):
    if how_many_pancil % 4 == 0:
        print('3')
        how_many_pancil -= 3
    elif how_many_pancil % 4 == 3:
        print('2')
        how_many_pancil -= 2
    elif how_many_pancil % 4 == 2:
        print('1')
        how_many_pancil -= 1
    elif how_many_pancil % 4 == 1:
        print('1')
        how_many_pancil -= 1
    elif how_many_pancil == 1:
        print('1')
        how_many_pancil -= 1
    return how_many_pancil

while True:
    try:
        how_many_pancil = int(input("How many pencils: "))
    except ValueError:
        print("The number of pencils should be numeric")
    else:
        if how_many_pancil <= 0:
            print("The number of pencils should be positive")
        else:
            break
while True:
    who_the_first = input("Who will be the first (John, Jack): ")
    if "John" != who_the_first != "Jack":
        print("Choose between 'John' and 'Jack'")
    else:
        break
while how_many_pancil > 0:
    if who_the_first == "John":
        print(how_many_pancil * '|')
        print(f"{who_the_first}'s turn!")
        while True:
            try:
                gamer_pancil = int(input())
            except ValueError:
                print("Possible values: '1', '2' or '3'")
            else:
                if gamer_pancil <= 0 or gamer_pancil > 3:
                    print("Possible values: '1', '2' or '3'")
                else:
                    how_many_pancil -= gamer_pancil
                    who_the_first = "Jack"
                    if how_many_pancil < 0:
                        print("Too many pencils were taken")
                        how_many_pancil += gamer_pancil
                        who_the_first = "Jack"
                    else:
                        break
    else:
        print(how_many_pancil * '|')
        print(f"{who_the_first}'s turn:")
        how_many_pancil = won_strategi(how_many_pancil)
        who_the_first = "John"

print(f"{who_the_first} won!")
