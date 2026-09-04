#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        div_result = 0
        try:
            val_1 = my_list_1[i]
            val_2 = my_list_2[i]
            div_result = val_1 / val_2
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(div_result)
    return result_list
