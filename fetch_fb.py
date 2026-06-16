import datetime
from facebook_scraper import get_posts
from feedgen.feed import FeedGenerator

# القائمة الخاصة بالصفحات التي أرسلتها
PAGES = {
    "tech_burning": "100087255284298",
    "abaadnews": "abaadnews",
    "Laamnetwork": "Laamnetwork",
    "news_profile": "100080067696964",
    "CentralBankofLibya": "CentralBankofLibya",
    "SadaMagLY": "SadaMagLY"
}

for page_name, page_id in PAGES.items():
    fg = FeedGenerator()
    fg.id(f'https://facebook.com/{page_id}')
    fg.title(f'Facebook Feed - {page_name}')
    fg.link(href=f'https://facebook.com/{page_id}', rel='alternate')
    fg.description(f'Latest posts from {page_name}')

    try:
        # جلب آخر 5 منشورات من الصفحة
        for post in get_posts(page_id, pages=1):
            fe = fg.add_entry()
            fe.id(post['post_url'])
            fe.title(post['text'][:50] + '...' if post['text'] else 'New Post')
            fe.link(href=post['post_url'])
            fe.description(post['text'] if post['text'] else 'Image/Video Content')
            # ضبط وقت النشر
            if post['time']:
                fe.pubDate(post['time'].replace(tzinfo=datetime.timezone.utc))
            else:
                fe.pubDate(datetime.datetime.now(datetime.timezone.utc))
        
        # حفظ الملف بصيغة RSS XML
        fg.rss_file(f'{page_name}.xml')
        print(f"Successfully generated RSS for {page_name}")
    except Exception as e:
        print(f"Error fetching {page_name}: {e}")
