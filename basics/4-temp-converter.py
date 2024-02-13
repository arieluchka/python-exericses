# do we convert c to f or f to c
# do the conversion

temp_of_choice = input("choose the starting temperature (F or C) ").upper()
temp_value = int(input("choose the value: "))


#from F to C
if temp_of_choice == "F":
    conversion_value = (temp_value - 32) * (5 / 9)
    print(f"{temp_value} from F to C will be {conversion_value}")

#from C to F
elif temp_of_choice == "C":
    conversion_value = (temp_value * (9 / 5)) + 32
    print(temp_value, "from c to f would be", conversion_value)

else:
    print("invalid choice")


