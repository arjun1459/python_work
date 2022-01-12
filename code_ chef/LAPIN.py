# LAPIN
for i in range(int(input())):
    test_string = input()
    # print(test_string)
    len_string = len(test_string)
    # print(len_string)
    if len_string % 2 == 0:
        first_half_string = sorted(test_string[:(len_string//2)])
        second_half_string = sorted(test_string[len_string//2:])
        # print(first_half_string)
        # print(second_half_string)
        print("YES" if first_half_string == second_half_string else "NO")
    else:
        first_half_string = sorted(test_string[:(len_string//2)])
        second_half_string = sorted(test_string[(len_string//2)+1:])
        # print(first_half_string)
        # print(second_half_string)
        print("YES" if first_half_string == second_half_string else "NO")
