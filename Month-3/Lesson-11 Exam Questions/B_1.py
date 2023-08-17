def find_average_word_lengths(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)

        if total_lines % 2 == 0:
            middle_line = total_lines // 2 - 1
            merged_line = lines[middle_line].strip() + ' ' + lines[middle_line + 1].strip()
        else:
            middle_line = total_lines // 2
            merged_line = lines[middle_line].strip()

        words = merged_line.split()
        word_lengths = tuple(len(word) for word in words)

        return word_lengths


input_file = 'input.txt'
result = find_average_word_lengths(input_file)
print("Sozlardagi harflar =", result)