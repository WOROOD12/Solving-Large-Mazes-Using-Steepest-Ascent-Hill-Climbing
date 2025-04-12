
import random
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def apply_path(start, path, maze):
    x, y = start
    positions = [start]
    for move in path:
        if move == 'U': x -= 1
        elif move == 'D': x += 1
        elif move == 'L': y -= 1
        elif move == 'R': y += 1
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            positions.append((x, y))
        else:
            break
    return positions

def fitness(path, maze, start, goal, alpha=0.5):
    positions = apply_path(start, path, maze)
    last = positions[-1]
    distance = abs(goal[0] - last[0]) + abs(goal[1] - last[1])
    penalty = len(path) - len(positions)
    return 1 / (1 + distance + alpha * penalty)

def tweak(path):
    new_path = path[:]
    index = random.randint(0, len(path) - 1)
    new_path[index] = random.choice(['U', 'D', 'L', 'R'])
    return new_path

def steepest_hill_climbing(maze, start, goal, iterations=1000, path_length=300):
    current = [random.choice(['U', 'D', 'L', 'R']) for _ in range(path_length)]
    current_score = fitness(current, maze, start, goal)
    for _ in range(iterations):
        neighbors = [tweak(current) for _ in range(20)]
        best_neighbor = max(neighbors, key=lambda p: fitness(p, maze, start, goal))
        best_score = fitness(best_neighbor, maze, start, goal)
        if best_score > current_score:
            current, current_score = best_neighbor, best_score
        else:
            break
    return current, current_score

def load_maze(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    max_len = max(len(line.strip()) for line in lines[1:-1])
    maze = [[0 if ch == ' ' else 1 for ch in line.strip().ljust(max_len)] for line in lines[1:-1]]
    start = (1, lines[0].index(' '))
    goal = (len(maze) - 1, lines[-1].index(' '))
    return maze, start, goal

mazes = {
    "100x100": load_maze("maze_100x100.txt"),
    "200x200": load_maze("maze_200x200.txt")
}
iterations_list = [1000, 10000, 100000]
metrics = {name: {"fitness": [], "path_cost": [], "time": []} for name in mazes}

for name, (maze, start, goal) in mazes.items():
    for iters in iterations_list:
        fitness_vals = []
        cost_vals = []
        time_vals = []
        for _ in range(3):
            t0 = time.time()
            path, score = steepest_hill_climbing(maze, start, goal, iterations=iters)
            elapsed = time.time() - t0
            valid_positions = apply_path(start, path, maze)
            path_cost = len(valid_positions) - 1
            fitness_vals.append(score)
            cost_vals.append(path_cost)
            time_vals.append(elapsed)
        metrics[name]["fitness"].append(sum(fitness_vals)/len(fitness_vals))
        metrics[name]["path_cost"].append(sum(cost_vals)/len(cost_vals))
        metrics[name]["time"].append(sum(time_vals)/len(time_vals))

labels = ['1000', '10000', '100000']
x = np.arange(len(labels))

fig, axs = plt.subplots(3, 1, figsize=(10, 12))
axs[0].plot(x, metrics["100x100"]["fitness"], marker='o', label='100x100')
axs[0].plot(x, metrics["200x200"]["fitness"], marker='o', label='200x200')
axs[0].set_title("Average Fitness vs Iterations")
axs[0].set_xticks(x)
axs[0].set_xticklabels(labels)
axs[0].set_ylabel("Fitness")
axs[0].legend()
axs[0].grid(True)

axs[1].plot(x, metrics["100x100"]["path_cost"], marker='o', label='100x100')
axs[1].plot(x, metrics["200x200"]["path_cost"], marker='o', label='200x200')
axs[1].set_title("Average Path Cost vs Iterations")
axs[1].set_xticks(x)
axs[1].set_xticklabels(labels)
axs[1].set_ylabel("Path Cost")
axs[1].legend()
axs[1].grid(True)

axs[2].plot(x, metrics["100x100"]["time"], marker='o', label='100x100')
axs[2].plot(x, metrics["200x200"]["time"], marker='o', label='200x200')
axs[2].set_title("Average Execution Time vs Iterations")
axs[2].set_xticks(x)
axs[2].set_xticklabels(labels)
axs[2].set_ylabel("Time (s)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig("hill_climbing_comparison_chart.png")
