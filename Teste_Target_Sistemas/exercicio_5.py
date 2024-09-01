# Criando uma str exemplo
string_exemplo = "targetsistemas"

# Criando função para receber a str, transformar em lista e colocar seus valores em uma nova lista,
# usando indices negativos, que começam do final da lista, e depois transformando em str novamente
def revert_string(string):
    old_string = list(string)
    new_list = []

    for index, items in enumerate(old_string):
        new_list.insert(-index, old_string[index])
    new_string = ' '.join(new_list)
    return new_string


print(revert_string(string_exemplo))

