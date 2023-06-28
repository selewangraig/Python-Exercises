def main_func():
    previous_num = 0

    for i in range(10):
        print(i)
        sum_num = i + previous_num

        print("Current Number: %d Previous Number: %d Sum: %d" % (i, previous_num, sum_num))

        previous_num = i
        i += 1

main_func()