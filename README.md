# Solving-Large-Mazes-Using-Steepest-Ascent-Hill-Climbing

This project implements the Steepest-Ascent Hill-Climbing algorithm to solve large grid-based mazes. It is part of a course assignment exploring heuristic-based optimization methods in AI.

## 🔍 Overview

- The algorithm starts from a random path and iteratively tweaks it to improve fitness.
- Each path is evaluated based on how close it gets to the goal and how many walls it hits.
- The project includes experiments on two maze sizes: 100x100 and 200x200.
- Results are compared across different iteration levels: 1000, 10000, and 100000.

## 📁 Contents

| File                                 | Description                                  |
|--------------------------------------|----------------------------------------------|
| `maze_100x100.txt`                   | Maze input (100x100)                         |
| `maze_200x200.txt`                   | Maze input (200x200)                         |
| `hill_climbing_final_analysis.py`    | Python code to run experiments and plotting  |
| `tweak_operator_diagram_fixed.png`   | Diagram explaining the tweak operator        |
| `hill_climbing_comparison_chart.png` | Result chart comparing fitness, cost & time  |

## 📈 Results Summary

- Fitness slightly improved with more iterations.
- Algorithm struggled with 200x200 maze due to local maxima.
- Execution time increased linearly with iterations.

## 🧠 Improvements Suggested

- Random restarts to escape local optima
- Smarter tweak strategies
- Using hybrid algorithms like simulated annealing or genetic search

## 🛠️ How to Run

Make sure you have Python and matplotlib installed:

```bash
pip install matplotlib
```
Then run the experiment code
```bash
python hill_climbing_final_analysis.py

