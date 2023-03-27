def from_big_to_lower (data):
    for i in range(0, len(data)):
        if data[i] != data[i].lower():
            data[i] = data[i].lower()
            print(data[i])
    return data

def change_only (data, to_change):
    for i in range(0, len(data)):
        if data[i] == to_change[0]:
            data[i] = to_change[1]
            print(data[i])
    return data
def rozbij_na_liste (data):
    data = list(data)
    return data


def enigma(message, przesun, *to_change):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    shift = przesun % len(alphabet)
    if shift == 0 :
        shift = przesun

    abc = rozbij_na_liste(message)
    from_big_to_lower(abc)

    for i in range(0, len(abc)):
        if abc[i] in alphabet:
            k = alphabet.index(abc[i])
            if (k + shift) >= len(alphabet):
                shift2 = (k + shift) - len(alphabet)
            else:
                shift2 = shift + k
            abc[i] = alphabet[shift2]

    for c in to_change:
        abc = change_only(abc, c)

    return ''.join(abc)

# Tu zmieniamy STRINGA
my_string = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll!"


print(enigma(my_string, 5, ["p", "B"], ["o", "QQ"]))




