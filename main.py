import sys
import argparse
import time
import random
from playwright.sync_api import sync_playwright
from config import SCHEDULE, TARGET_URL, HEADLESS, SLOW_MO
from src.actions import human_scroll, like_post, view_story
from src.utils import random_delay

def run_warmup(day, dry_run=False):
    print(f"--- Starting Day {day} Warmup ---")
    
    tasks = SCHEDULE.get(day)
    if not tasks:
        print(f"Error: Day {day} not found in schedule.")
        return

    print(f"Plan: {tasks}")

    if dry_run:
        print("[DRY RUN] Simulation mode on. No browser will be launched.")
        print(f"[DRY RUN] Would scroll for {tasks['duration']} minutes.")
        print(f"[DRY RUN] Would like {tasks['likes']} posts.")
        print(f"[DRY RUN] Would view {tasks['stories']} stories.")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context(
            viewport={'width': 390, 'height': 844}, # iPhone 12/13/14 Pro dimensions
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
        )
        page = context.new_page()
        
        try:
            print(f"Navigating to {TARGET_URL}...")
            page.goto(TARGET_URL)
            random_delay(5, 10) # Initial load wait

            # Main Loop
            start_time = time.time()
            duration_sec = tasks['duration'] * 60
            
            likes_performed = 0
            stories_viewed = 0
            
            while time.time() - start_time < duration_sec:
                # 1. Scroll is the main activity
                scroll_session_time = random.uniform(1, 3) # Scroll for 1-3 minutes chunks
                human_scroll(page, scroll_session_time)
                
                # 2. Randomly perform actions if quota not met
                if likes_performed < tasks['likes'] and random.random() < 0.3:
                    like_post(page)
                    likes_performed += 1
                
                if stories_viewed < tasks['stories'] and random.random() < 0.2:
                    view_story(page)
                    stories_viewed += 1
                
                # Check point to handle login or popups would go here
                
            print("--- Warmup Daily Goal Completed ---")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            page.screenshot(path=f"error_day_{day}.png")
        finally:
            browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Social Media Warmup Script")
    parser.add_argument("--day", type=int, required=True, help="Day of the warmup schedule (1-7)")
    parser.add_argument("--dry-run", action="store_true", help="Run without launching browser to test logic")
    
    args = parser.parse_args()
    
    run_warmup(args.day, args.dry_run)
