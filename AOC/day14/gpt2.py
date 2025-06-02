import os
from PIL import Image, ImageDraw
n = 5000
from collections import defaultdict

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
    # Read input
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    
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
    grid_width, grid_height = 101, 103
    
    # Create output folder
    output_folder = "robot_simulation_frames"
    os.makedirs(output_folder, exist_ok=True)
    
    # Simulate for 100 seconds and save each frame
    current_positions = [(x, y) for (x, y), _ in robots]
    for iteration in range(n+1):  # 0 to 100 inclusive
        # Visualize current state
        visualize_robots(current_positions, grid_width, grid_height, output_folder, iteration)
        
        if iteration == n:
            break  # We've reached our target iteration
            
        # Update positions for next iteration
        new_positions = []
        for (x, y), (vx, vy) in robots:
            new_x = (x + vx * (iteration + 1)) % grid_width
            new_y = (y + vy * (iteration + 1)) % grid_height
            new_positions.append((new_x, new_y))
        current_positions = new_positions
    
    # Calculate final quadrant counts
    mid_x = (grid_width - 1) // 2
    mid_y = (grid_height - 1) // 2
    
    q_counts = [0, 0, 0, 0]  # Q1, Q2, Q3, Q4
    for x, y in current_positions:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            q_counts[0] += 1
        elif x > mid_x and y < mid_y:
            q_counts[1] += 1
        elif x < mid_x and y > mid_y:
            q_counts[2] += 1
        elif x > mid_x and y > mid_y:
            q_counts[3] += 1
    
    safety_factor = q_counts[0] * q_counts[1] * q_counts[2] * q_counts[3]
    print(f"Safety factor after 100 iterations: {safety_factor}")

if __name__ == "__main__":
    solve()
