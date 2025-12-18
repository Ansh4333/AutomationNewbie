from scraper.amazon_scraper import fetch_amazon_deals
from storage.db import get_db
from publisher.telegram_bot import post_to_telegram

def run():
    conn = get_db()
    cur = conn.cursor()

    deals = fetch_amazon_deals()
    for d in deals:
        try:
            cur.execute("INSERT INTO deals (title, source) VALUES (?,?)",
                        (d["title"], d["source"]))
            conn.commit()
            post_to_telegram(f"🔥 New Deal: {d['title']}")
        except:
            pass

if __name__ == "__main__":
    run()
