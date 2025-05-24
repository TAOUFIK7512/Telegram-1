main.py


   ```python
   import requests
   import time

   TOKEN = "7357253957:AAEOY-xE8mrptYYpEDyYYP2Eve6ykMovzvs"
   CHAT_ID = "7357253957"
   MESSAGE = "✅ البوت شغال بنجاح على Render!"

   def send_message():
       url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
       data = {"7357253957": CHAT_ID, "text": MESSAGE}
       requests.post(url, data=data)

   if _name_ == "_main_":
       while True:
           send_message()
           time.sleep(3600)  # كل ساعة
   ```