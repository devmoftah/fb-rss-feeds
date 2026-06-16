import requests

# هنا تضع معرّفات الصفحات مباشرة على طول بدون الحاجة لأي موقع أو حساب!
PAGES = {
    "tech_burning": "100087255284298",
    "abaadnews": "abaadnews",
    "Laamnetwork": "Laamnetwork",
    "news_profile": "100080067696964",
    "CentralBankofLibya": "CentralBankofLibya",
    "SadaMagLY": "SadaMagLY"
}

def update_feeds():
    for file_name, page_id in PAGES.items():
        try:
            print(f"جاري جلب وتحديث صفحة: {file_name}")
            
            # الكود يقوم بتركيب الرابط وجلب الـ RSS فوراً وتلقائياً
            url = f"https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=Facebook&u={page_id}&format=Atom"
            
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                # حفظ الملف في مستودع جيت هب الخاص بك
                with open(f"{file_name}.xml", "wb") as f:
                    f.write(response.content)
                print(f"✅ تم التحديث بنجاح")
            else:
                print(f"❌ فشل الجلب من فيسبوك، رمز الخطأ: {response.status_code}")
        except Exception as e:
            print(f"❌ خطأ تقني أثناء التحديث: {e}")

if __name__ == "__main__":
    update_feeds()
