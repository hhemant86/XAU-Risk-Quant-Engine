"""
Live News Sentinel v3.5 (Institutional Governance Edition)
Includes: Source Quorum Logic, Cool-Down Protocol, and Multi-Source Aggregation.
"""
import feedparser
import os
import ssl
import time

# Fix for SSL certificate issues on Windows
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

FEEDS = {
    'Yahoo Finance': "https://finance.yahoo.com/news/rssindex",
    'Reuters Macro': "https://ir.thomsonreuters.com/rss/news-releases.xml?items=15",
    'The Economist': "https://www.economist.com/finance-and-economics/rss.xml",
    'MarketWatch': "https://www.marketwatch.com/rss/marketupdate",
    'CNBC World': "https://www.cnbc.com/id/100727362/device/rss/rss.html",
    'Investing.com': "https://www.investing.com/rss/news_14.rss",
    'DailyFX': "https://www.dailyfx.com/feeds/market-news",
    'Kitco Gold': "https://www.kitco.com/rss/news.xml",
    'FXStreet': "https://www.fxstreet.com/rss/news/commodities/gold",
    'FX Empire': "https://www.fxempire.com/news/feed",
    'ZeroHedge': "http://feeds.feedburner.com/zerohedge/feed",
    'Al Jazeera': "https://www.aljazeera.com/xml/rss/all.xml",
    'The National': "https://www.thenationalnews.com/arc/outboundfeeds/rss/category/business/"
}

CRITICAL_WORDS = ['war', 'conflict', 'crisis', 'geopolitical', 'sanctions', 'attack', 'nuclear', 'tensions']
MACRO_WORDS = ['fed', 'rate', 'cpi', 'inflation', 'powell', 'hike']

def scan_all_sources():
    start_time = time.time()
    print(f"\n📡 INITIALIZING GLOBAL SCAN: {len(FEEDS)} SOURCES...")
    aggregated_alerts = []
    
    for name, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                headline = entry.title.lower()
                if any(w in headline for w in CRITICAL_WORDS):
                    aggregated_alerts.append(f"🚨 [EXTREME] {name}: {entry.title}")
                elif any(w in headline for w in MACRO_WORDS):
                    aggregated_alerts.append(f"⚠️ [MACRO] {name}: {entry.title}")
        except Exception:
            continue

    # --- 🏛️ INSTITUTIONAL GOVERNANCE LAYER ---
    # 1. Quorum Logic: Verify if EXTREME risk is reported by multiple independent sources
    extreme_sources = set([a.split(":")[0] for a in aggregated_alerts if "[EXTREME]" in a])
    unique_quorum = len(extreme_sources)
    
    risk_level = "NORMAL"
    if unique_quorum >= 2:
        risk_level = "CRITICAL"
    elif len(aggregated_alerts) > 0:
        risk_level = "WARNING"

    # 2. Reporting
    print("\n" + "="*70)
    print(f"--- 🏁 AGGREGATED RISK REPORT | QUORUM: {unique_quorum} ---")
    for alert in aggregated_alerts[:10]: print(alert)
    
    # 3. Persistence & Signaling
    results_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
    if not os.path.exists(results_dir): os.makedirs(results_dir)
    
    signal_path = os.path.join(results_dir, 'live_risk_signal.txt')
    with open(signal_path, "w") as f:
        f.write(risk_level)
    
    print("="*70)
    print(f"📡 SIGNAL: {risk_level} | TIME: {time.time() - start_time:.2f}s")
    print(f"📄 CACHED: {signal_path}\n")

if __name__ == "__main__":
    scan_all_sources()