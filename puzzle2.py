def read_values(filename):
    """
    Belirtilen dosyayı okuyarak a ve b listelerini oluşturur ve sıralar.
    :param filename: Okunacak dosya adı.
    :return: a ve b listeleri.
    """
    a = []
    b = []
    current_flag = "a"
    current_value = ""

    with open(filename, "r", encoding="utf-8") as file:
        while True:
            char = file.read(1)
            if not char:
                if current_value:
                    if current_flag == "a":
                        a.append(current_value.strip())
                    elif current_flag == "b":
                        b.append(current_value.strip())
                break
            if char == " ":
                if current_flag == "a":
                    a.append(current_value.strip())
                    current_value = ""
                current_flag = "b"
            elif char == "\n":
                if current_flag == "b":
                    b.append(current_value.strip())
                    current_value = ""
                current_flag = "a"
            else:
                current_value += char
    return a, b

a,b = read_values("puzzle2_input.txt")
a = list(map(int, a))
b = list(map(int, b))

for i in len(a): 
    if a[i] in b:
        count= 
# with open("final.txt", "w", encoding="utf-8") as output_file:
#     output_file.write(f"{'A':<10} {'B':<10} {'A Sorted':<10} {'B Sorted':<10} {'Difference':<10} {'Cumulative':<10}\n")
#     output_file.write("-" * 70 + "\n")
#     for i in range(len(differences)):
#         cumulative_total = sum(differences[:i + 1])
#         output_file.write(
#             f"{a[i] if i < len(a) else '':<10} "
#             f"{b[i] if i < len(b) else '':<10} "
#             f"{a_sorted[i] if i < len(a_sorted) else '':<10} "
#             f"{b_sorted[i] if i < len(b_sorted) else '':<10} "
#             f"{differences[i]:<10} "
#             f"{cumulative_total:<10}\n"
#         )
#     output_file.write("-" * 70 + "\n")
#     output_file.write(f"{'':<50}{'Sum':<10}{total:<10}\n")

# print("Results have been written to final.txt.")
