with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
def get_data() -> list[list[int]]:
    with open("./input.txt", "r") as file:
        # Read and process all lines, splitting into two sorted arrays
        data = [list(map(str, line.strip().split())) for line in file]
    if not data:
        raise ValueError("Failed: Input data is empty or invalid")

    return data
inputt = get_data()

for i in range(len(lines)):
    print(inputt[i])

