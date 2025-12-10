from pathlib import Path

print("--- Reading in the entire file:")
path = Path(r'C:\Users\norto\git\python_work_2025\chapter10\learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)
