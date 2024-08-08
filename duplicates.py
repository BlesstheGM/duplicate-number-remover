# Open the input file for reading
input_file = "random_numbers.txt"
with open(input_file, "r") as file:
    lines = file.readlines()

# Remove duplicates and preserve order using a set
unique_lines = []
seen_lines = set()

for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace and newline characters
    if line not in seen_lines:
        seen_lines.add(line)
        unique_lines.append(line)

# Open the output file for writing and write the unique lines
output_file = "file_without_duplicates.txt"
with open(output_file, "w") as file:
    file.write("\n".join(unique_lines))

print(f"Removed duplicates and saved to {output_file}")

