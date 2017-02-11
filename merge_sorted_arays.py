def merge_sorted_arrays_pop(left_array, right_array):
    l_array = left_array[:]
    r_array = right_array[:]
    final_array = []
    while (l_array and r_array):
        if ( l_array[0] <= r_array[0] ):
            item = l_array.pop(0)
        else:
            item = r_array.pop(0)

        final_array.append(item)
    final_array.extend(l_array + r_array)
    return final_array

def merge_sorted_arrays(l_array, r_array):
    l_index = 0
    r_index = 0
    l_length = len(l_array)
    r_length = len(r_array)
    final_array = []
    print((l_index < l_length) and (r_array < r_length))
    while ((l_index < l_length) and (r_index < r_length)):
        print(l_index, r_index)
        if ( l_array[l_index] <= r_array[r_index] ):
            item = l_array[l_index]
            l_index += 1
        else:
            item = r_array[r_index]
            r_index += 1
        final_array.append(item)
    final_array.extend(l_array[l_index:] + r_array[r_index:])
    return final_array

print merge_sorted_arrays([1, 3, 5, 6, 34], [2, 4, 8, 10, 8, 90, 9000,911])
