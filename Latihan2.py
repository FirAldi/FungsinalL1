random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "world", 412, 5.5, "AI"]

int_dict = {}
float_tuple = ()
string_list = []

for item in random_list:
    if isinstance(item, int):
        # Pisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = (item // 100) % 10
        int_dict[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        string_list.append(item)

print("Data int dalam bentuk dictionary:", int_dict)
print("Data float dalam bentuk tuple:", float_tuple)
print("Data string dalam bentuk list:", string_list)
