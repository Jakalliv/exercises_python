def verify_card_number(card_number: str):
    #invertito ordine delle cifre, [0] ora è cifra di controllo

    only_numbers = [int(i) for i in card_number[::-1] if i.isnumeric()]
    #print(only_numbers)
    #sommatoria su numeri in posizioni pari e poi dispari
    sum_numbers_control = [i*2 for i in only_numbers[1::2]] + [i for i in only_numbers[2::2] ] + [only_numbers[0]]
    listà_to_sum = []
    for x in sum_numbers_control:
        if x//10 != 0:
            listà_to_sum.append(x-9)
        else:
            listà_to_sum.append(x)
    
    #print(sum(listà_to_sum))
    if sum(listà_to_sum)%10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
    

print(verify_card_number('4111-1111-1111-1111'))