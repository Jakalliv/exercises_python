from functools import reduce


# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def filter_5min(songs):
    return songs[1] > 5

print(list(filter(filter_5min, playlist)))

def convert_to_s(songs):
    return songs[1]* 60

print(list(map(convert_to_s, playlist)))

def add_durations(total, songs):
    return total + songs[1]

total  = reduce(add_durations, playlist, 0)
print(total)


