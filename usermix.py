import sys

if len(sys.argv) < 4:
    print("Usage: python3 script.py input_file.txt output_file.txt -t <template>")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]
template = sys.argv[4]

with open(input_file, 'r') as f:
    lines = f.readlines()

with open(output_file, 'w') as f:
    for i, line in enumerate(lines):
        for j in range(ord('a'), ord('z') + 1):
            f.write(f"{chr(j)}.{line}" if template == "a." else f"{chr(j)}{line}" if template == "a" else f"{chr(j)}{chr(j)}{line}")
