#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r_list = []

    for i in range(list_length):
        try:
            ele_1 = my_list_1[i] if i < len(my_list_1) else 0
            ele_2 = my_list_2[i] if i < len(my_list_1) else 0

            result = ele_1 / ele_2

        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError as e:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            r_list.append(result)

            return r_list
