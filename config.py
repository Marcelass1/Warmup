# config.py

# 7-Day Warmup Schedule
# Duration in minutes
SCHEDULE = {
    1: {"duration": 15, "likes": 0, "follows": 0, "stories": 2},
    2: {"duration": 20, "likes": 3, "follows": 0, "stories": 4},
    3: {"duration": 25, "likes": 5, "follows": 1, "stories": 5},
    4: {"duration": 30, "likes": 8, "follows": 1, "stories": 8},
    5: {"duration": 40, "likes": 12, "follows": 2, "stories": 10},
    6: {"duration": 50, "likes": 15, "follows": 2, "stories": 12},
    7: {"duration": 60, "likes": 20, "follows": 3, "stories": 15},
}

# General Settings
TARGET_URL = "https://www.instagram.com/"  # Example target, can be changed
HEADLESS = False  # Set to True for production/hidden runs
SLOW_MO = 50  # Slow down Playwright operations by ms
