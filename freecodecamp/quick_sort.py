def quick_sort(list_integers):
    if len(list_integers) <= 1:
        return list_integers  # ← Return the array, not None!
    
    pivot = list_integers[0]
    left = [x for x in list_integers[1:] if x <= pivot]
    right = [x for x in list_integers[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)