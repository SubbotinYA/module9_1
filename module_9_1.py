def apply_all_func(int_list:list, *functions)->dict:
    result = {}
    for i in functions:
        key=i.__name__
        value = i(int_list)
        result[key]=value
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

