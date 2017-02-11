input_array = [5, 4, 1, 3, 8, 2, 99, 0, 10, 11, 7, 89, 0, -1]

def merge_sort(array):
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[1] >= array[0]:
            return array
        else:
            return array[::-1]
    n = len(array) / 2
    l_array = array[:n]
    r_array = array[n:]
    return merge_sorted_arrays(merge_sort(l_array), merge_sort(r_array))

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

print merge_sort(input_array)
