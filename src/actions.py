from playwright.sync_api import Page
import random
from src.utils import random_delay, gaussian_random

def human_scroll(page: Page, duration_minutes):
    """
    Scrolls the feed for a specified duration with human-like pauses and speed.
    """
    start_time = time.time()
    end_time = start_time + (duration_minutes * 60)
    
    print(f"[INFO] Starting scroll session for {duration_minutes} minutes.")

    while time.time() < end_time:
        # Random scroll distance
        scroll_amount = gaussian_random(300, 100, 100, 800)
        
        # Smooth scroll (simulated by small steps if needed, but wheel is okay for now)
        page.mouse.wheel(0, scroll_amount)
        
        # Random pause after scroll (reading time)
        # 20% chance of a long pause (reading a post)
        if random.random() < 0.2:
             random_delay(2, 5)
        else:
             random_delay(0.5, 1.5)
             
        # Occasional scroll up (checking something again)
        if random.random() < 0.05:
            page.mouse.wheel(0, -scroll_amount * 0.5)
            random_delay(1, 2)

import time

def like_post(page: Page):
    """
    Attempts to like a visible post using robust Playwright locators for Instagram.
    """
    try:
        # Strategy: Find posts (articles) and look for the 'Like' button inside them.
        # Instagram's 'Like' button usually has an aria-label="Like" or is a button with an SVG containing that title.
        
        # targeting the feed container first helps narrow down context
        feed_articles = page.locator('article')
        count = feed_articles.count()
        
        if count > 0:
            # Pick a random article from the first few visible ones to avoid jumping too far
            idx = random.randint(0, min(count, 4) - 1)
            post = feed_articles.nth(idx)
            
            # Ensure the post is in view
            post.scroll_into_view_if_needed()
            random_delay(0.5, 1.0)
            
            # Look for the Like button. 
            # Note: "Unlike" means it's already liked. We only want "Like".
            like_button = post.get_by_role("button", name="Like", exact=True)
            
            if like_button.count() > 0 and like_button.is_visible():
                like_button.first.click()
                print("[ACTION] Liked a post.")
                random_delay(1, 2)
            else:
                # specific check to see if we already liked it
                if post.get_by_role("button", name="Unlike").count() > 0:
                     print("[DEBUG] Post already liked.")
                else:
                     print("[DEBUG] Like button not found or not visible.")
        else:
            print("[DEBUG] No posts (articles) found in feed.")
            
    except Exception as e:
        print(f"[ERROR] Failed to like post: {e}")

def view_story(page: Page):
    """
    Simulates viewing a story.
    """
    try:
        # Stories are located in the top tray. The container often identifies as a 'menu' or list.
        # We look for the distinct button role used for stories (often unlabeled circular buttons).
        
        # This selector targets the story ring buttons in the main feed header.
        # Canvas elements inside buttons are often the tell-tale sign of a story ring.
        story_buttons = page.locator("main header button, main div[role='menu'] button") 
        
        if story_buttons.count() > 0:
            # Click the second or third one to avoid "Your Story" (index 0) if empty
            target_story = story_buttons.nth(random.randint(1, 3))
            
            if target_story.is_visible():
                print(f"[ACTION] Clicking story at index...")
                target_story.click()
                
                # Watch for a random duration
                watch_time = random.randint(3, 10)
                print(f"[ACTION] Watching story for {watch_time}s...")
                time.sleep(watch_time)
                
                # Close the story modal
                # Instagram stories can be closed with Escape or clicking the close button
                page.keyboard.press("Escape") 
                print("[ACTION] Closed story.")
            else:
                 print("[DEBUG] Story button not visible.")
        else:
            print("[DEBUG] No story buttons found.")
            
    except Exception as e:
        print(f"[ERROR] Failed to view story: {e}")
