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
    Attempts to like a visible post. 
    Note: Selectors are generic placeholders and need to be updated for specific sites (IG/TikTok).
    """
    # Example selector for Instagram's heart icon (this changes often, so using a broad example)
    # Ideally, find an aria-label or specific class
    try:
        # This is a very generic "like" button selector strategy. 
        # For production, this needs robust selectors.
        like_buttons = page.locator('article svg[aria-label="Like"]').all()
        
        if like_buttons:
            btn = random.choice(like_buttons)
            # Scroll into view if needed
            btn.scroll_into_view_if_needed()
            random_delay(0.5, 1.5)
            btn.click()
            print("[ACTION] Liked a post.")
            random_delay(1, 2)
        else:
            print("[DEBUG] No like buttons found.")
            
    except Exception as e:
        print(f"[ERROR] Failed to like post: {e}")

def view_story(page: Page):
    try:
        stories = page.locator('div[role="button"][aria-disabled="false"]').all() # VERY generic
        # Real IG selector usually involves checking the top story tray
        
        # Placeholder logic
        if stories:
            random.choice(stories).click()
            print("[ACTION] Viewing story...")
            random_delay(3, 10)
            # Close story or click next
            page.keyboard.press("Escape") 
            print("[ACTION] Closed story.")
    except Exception as e:
        print(f"[ERROR] Failed to view story: {e}")
