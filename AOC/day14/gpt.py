import os
from PIL import Image, ImageDraw

def visualize_robots(positions, grid_width, grid_height, output_folder, iteration):
    # Create a blank white image
    img = Image.new('RGB', (grid_width * 10, grid_height * 10), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw grid lines (optional)
    for x in range(0, grid_width * 10, 10):
        draw.line((x, 0, x, grid_height * 10), fill='lightgray')
    for y in range(0, grid_height * 10, 10):
        draw.line((0, y, grid_width * 10, y), fill='lightgray')
    
    # Draw robots (as red squares)
    for x, y in positions:
        draw.rectangle([x*10, y*10, (x+1)*10, (y+1)*10], fill='red')
    
    # Save image
    img.save(f"{output_folder}/frame_{iteration:03d}.png")
def solve():
    from collections import defaultdict

    # Read input
    with open("/home/guillaume/Documents/7331/AOC/day14/input.txt", "r") as file:
        data = [line.strip("\n") for line in file]
    
    
    # Initialize robot positions and velocities
    robots = []
    for line in data:
        if not line.strip():
            continue
        p_part, v_part = line.split(' v=')
        x, y = map(int, p_part.replace('p=', '').split(','))
        vx, vy = map(int, v_part.split(','))
        robots.append(((x, y), (vx, vy)))
    
    # Grid dimensions (101x103 for the actual problem)
    # grid_width, grid_height = 11, 7
    grid_width, grid_height = 101, 103
    
    # Simulate for 100 seconds
    positions_after_100 = []
    for (x, y), (vx, vy) in robots:
        x_final = (x + vx * 100) % grid_width
        y_final = (y + vy * 100) % grid_height
        positions_after_100.append((x_final, y_final))
    
    # Split into quadrants
    mid_x = (grid_width - 1) // 2
    mid_y = (grid_height - 1) // 2
    
    q1 = q2 = q3 = q4 = 0
    for x, y in positions_after_100:
        if x == mid_x or y == mid_y:
            continue  # Ignore midline robots
        if x < mid_x and y < mid_y:
            q1 += 1
        elif x > mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y > mid_y:
            q3 += 1
        elif x > mid_x and y > mid_y:
            q4 += 1
    
    # Compute safety factor
    safety_factor = q1 * q2 * q3 * q4
    print(safety_factor)

solve()

