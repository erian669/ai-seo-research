import requests
from datetime import datetime

URLS_TO_CHECK = [
    "https://blog.hubspot.com/marketing/ai-seo",
]

def check_ai_readiness(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"\nURL: {url}")
            print(f"  ⚠️ REJECTION: Site returned status code {response.status_code}")
            return

        content = response.text.lower()

        # TL;DR / summary detection
        has_tldr = any(keyword in content for keyword in [
            "tl;dr", "key takeaways", "summary"
        ])

        # Freshness detection
        current_year = datetime.now().year
        is_fresh = str(current_year) in content

        print(f"\nURL: {url}")
        print(f"  - TL;DR Block: {'✅ Detected' if has_tldr else '❌ Missing'}")
        print(f"  - Freshness ({current_year}): {'✅ Active' if is_fresh else '❌ Stale'}")

        if not has_tldr or not is_fresh:
            print("  ⚠️ ALERT: Missing or outdated citation signals")

    except Exception as e:
        print(f"Error checking {url}: {e}")


if __name__ == "__main__":
    print("--- AI SEO Readiness Monitor (v1.3.0) ---")
    for site in URLS_TO_CHECK:
        check_ai_readiness(site)
