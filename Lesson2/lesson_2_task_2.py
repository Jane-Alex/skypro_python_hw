def is_year_leap(year):

    if(year % 4 == 0):
        print("год", " ", year,":", " ", True, sep="")
    else:
        print("год", " ", year,":", " ", False, sep="")

is_year_leap(int(input("Введите год: ")))