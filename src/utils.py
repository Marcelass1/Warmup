import random
import time
import numpy as np

def random_delay(min_sec, max_sec):
    """
    Sleeps for a random amount of time between min_sec and max_sec.
    """
    delay = random.uniform(min_sec, max_sec)
    print(f"[DEBUG] Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)

def gaussian_random(mean, std_dev, min_val, max_val):
    """
    Returns a random number from a Gaussian distribution, clipped to min_val and max_val.
    Useful for generating human-like reaction times.
    """
    val = np.random.normal(mean, std_dev)
    return max(min_val, min(val, max_val))

def is_niche_content(text, keywords):
    """
    Checks if the text contains any of the keywords.
    """
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)
