
from collections import Counter

input = "5178527 8525 22 376299 3 69312 0 275"
example = "125 17"

def stringToVect(text):
    temp_str = "" 
    vec = []
    for i in range(len(text)):
        if text[i] == " ":
            vec.append(int(temp_str))
            temp_str = ""
        else:
            temp_str += text[i]
    vec.append(int(temp_str))
    return vec

def count_stones_after_presses(initial_stones, button_presses):
    stones = Counter(initial_stones)
    
    for _ in range(button_presses):
        new_stones = Counter()
        
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            else:
                num_str = str(stone)
                if len(num_str) % 2 == 0:  # Even number of digits
                    split_pos = len(num_str) // 2
                    first_part = int(num_str[:split_pos])
                    second_part = int(num_str[split_pos:])
                    new_stones[first_part] += count
                    new_stones[second_part] += count
                else:  # Odd number of digits
                    new_stones[stone * 2024] += count
        
        stones = new_stones
    
    return sum(stones.values())


n = 75
print(count_stones_after_presses(stringToVect(input),n))
