import os
import time
from datetime import datetime
import pandas as pd
from playwright.sync_api import sync_playwright

# Configuration & Output Setup
OUTPUT_DIR = "ad_archives"
os.makedirs(OUTPUT_DIR, exist_ok=True);
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
CSV_FILENAME = os.path.join(OUTPUT_DIR, f"ad_snapshot_{TIMESTAMP}.csv")

def scrape_facebook_ad_library(keyword_or_brand):
    """
    Automates browsing the Meta Ad Library using Playwright to bypass 
    dynamic rendering blocks and extract ad text and image assets.
    """
    scraped_data = []
    
    # Construct search URL (Country: All, Ad Status: All)
    target_url = (
        f"https://www.facebook.com/ads/library/?active_status=all"
        f"&ad_type=all&country=ALL&q={keyword_or_brand}&search_type=keyword_unordered"
    )

    print(f"[*] Initializing headless browser for target: {keyword_or_brand}")
    
    with sync_playwright() as p:
        # Launch browser with custom user-agent to mimic a regular user session
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        try:
            print(f"[*] Navigating to Meta Ad Library...")
            page.goto(target_url, timeout=60000)
            
            # Wait for initial container load & scroll to trigger lazy loading
            print("[*] Waiting for dynamic content to render...")
            time.sleep(5)
            
            for scroll_iteration in range(3):  # Scroll down 3 times to load more ads
                page.mouse.wheel(0, 5000)
                time.sleep(3)

            # Locate ad cards (Note: Meta mutates classes, using fallback structure patterns)
            ad_cards = page.locator("div._7jj-").all()
            print(f"[+] Found {len(ad_cards)} potential ad elements on page.")

            if not ad_cards:
                # Fallback generic container check
                ad_cards = page.locator("div.x9f619.x78zum5").all()

            for idx, card in enumerate(ad_cards[:15]): # Limiting initial batch for safety
                try:
                    text_content = card.inner_text()
                    # Attempt to find creative image elements inside the card
                    img_element = card.locator("img").first
                    image_url = img_element.get_attribute("src") if img_element.count() > 0 else ""

                    if text_content.strip():
                        scraped_data.append({
                            "archive_id": f"ad_{TIMESTAMP}_{idx}",
                            "snapshot_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "brand_query": keyword_or_brand,
                            "ad_text": text_content.replace("\n", " "),
                            "image_url": image_url
                        })
                except Exception as inner_err:
                    continue

            browser.close()
            
        except Exception as e:
            print(f"[!] Error during scraping execution: {e}")
            browser.close()

    # Save to a timestamped CSV file (ensuring historical separation)
    if scraped_data:
        df = pd.DataFrame(scraped_data)
        df.to_csv(CSV_FILENAME, index=False, encoding="utf-8")
        print(f"[SUCCESS] Archived {len(scraped_data)} records to {CSV_FILENAME}")
    else:
        print("[!] No records extracted. Selectors might need adjustment.")

if __name__ == "__main__":
    # Example target test run
    search_query = "nike" 
    scrape_facebook_ad_library(search_query)