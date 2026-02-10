
def selection_sor(array_unsort):
    n = len(array_unsort)
    for i in range(n):
        min_index = i
        for x in range(min_index+1, n):
            if array_unsort[x] < array_unsort[min_index]:
                min_index = x

            array_unsort[i], array_unsort[min_index] = array_unsort[min_index], array_unsort[i]

    return array_unsort


def selection_sort(array: list) -> list:
    for selection_index, selection in enumerate(array):
        minimum_index = selection_index
        minimum_value = selection

        for index in range(selection_index, len(array)):
            if array[index] < minimum_value:
                minimum_index = index
                minimum_value = array[index]
        
                array[minimum_index], array[selection_index] = array[selection_index], array[minimum_index]
        
    return array