number = float(input("Input a decimal to convert: "))
percent = number * 100
round_percent = "{:.1f}".format(percent)
print(f"The percentage is {round_percent}%")
