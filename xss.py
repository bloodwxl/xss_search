import requests

def scan_xss(url):
    # Список тегів, які можуть викликати вразливість XSS
    xss_payloads = ['<script>alert("XSS")</script>', '<img src="x" onerror="alert(\'XSS\')">']

    for payload in xss_payloads:
        # Формування GET-запиту з впровадженим XSS-пейлоадом
        payload_url = url + payload
        response = requests.get(payload_url)

        #Перевірка, чи містить відповідь пейлоад
        if payload in response.text:
            print(f"Вразливість на сторінці: {payload_url}")

# Приклад використання
target_url = "http://example.com/page.php?param="
scan_xss(target_url)
