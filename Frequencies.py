with open('Frequencies.txt', 'r') as files:
    # Read the file contents
    contents = files.read()

# Here we can define as it we  Extract the character-frequency pairs from the file contents
pairs = []
for lines in contents.split('\n'):
    if lines.strip() != '':
        line_parts = lines.split('=')
        if len(line_parts) == 2:
            characters = line_parts[0].strip().split('[', 1)[1].strip()[0]
            frequencies = int(line_parts[1].strip().split('[', 1)[1].split(']')[0].strip())
            pairs.append((characters, frequencies))

# Here we can define as it we  Sort the pairs based on frequency in descending order
sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

# Here we can define as it we  Extract the first 10 characters with the highest frequencies
results = [pairs[0] for pairs in sorted_pairs[:10]]

# Here we can define as it we Print the result
print(results)