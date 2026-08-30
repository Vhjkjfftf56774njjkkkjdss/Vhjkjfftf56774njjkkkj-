import os
import time
import random
import sys
import subprocess

def auto_install_packages():
    packages = ['selenium', 'fake-useragent']
    for package in packages:
        try:
            if package == 'fake-useragent':
                __import__('fake_useragent')
            else:
                __import__(package)
            print(f"✅ {package} đã được cài đặt")
        except ImportError:
            print(f"📦 Đang cài đặt {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ Đã cài đặt {package}")

auto_install_packages()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

ua = UserAgent()

NGAY_SINH = "30.04.1999"
SO_CCCD = "049234928948"
SO_DT_NGUOI_THAN = "948487344"
SO_DT_TUYEN_DUNG = "912345678"
EMAIL = "huutinh1976743@gmail.com"
HO_TEN = "Nguyễn Văn A"

cac_hang = ["Iphone", "Samsung", "Oppo", "Xiaomi"]

def tao_file_anh_gia(path, kich_thuoc=(800, 600)):
    try:
        with open(path, 'wb') as f:
            f.write(b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x01\x00\x60\x00\x60\x00\x00\xFF\xDB\x00\x43\x00\x03\x02\x02\x02\x02\x02\x03\x02\x02\x02\x03\x03\x03\x03\x04\x06\x04\x04\x04\x04\x04\x08\x06\x06\x05\x06\x09\x08\x0A\x0A\x09\x08\x09\x09\x0A\x0C\x0F\x0C\x0A\x0B\x0E\x0B\x09\x09\x0D\x11\x0D\x0E\x0F\x10\x10\x11\x10\x0A\x0C\x12\x13\x12\x10\x13\x0F\x10\x10\x10\xFF\xC0\x00\x0B\x08\x02\x58\x02\x58\x01\x01\x11\x00\xFF\xC4\x00\x1F\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\xFF\xC4\x00\xB5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01\x7D\x01\x02\x03\x00\x04\x11\x05\x12\x21\x31\x41\x51\x61\x07\x22\x71\x14\x32\x81\x91\xA1\x08\x23\x42\xB1\xC1\x15\x52\xD1\xF0\x24\x33\x62\x72\x82\x09\x0A\x16\x17\x18\x19\x1A\x25\x26\x27\x28\x29\x2A\x34\x35\x36\x37\x38\x39\x3A\x43\x44\x45\x46\x47\x48\x49\x4A\x53\x54\x55\x56\x57\x58\x59\x5A\x63\x64\x65\x66\x67\x68\x69\x6A\x73\x74\x75\x76\x77\x78\x79\x7A\x83\x84\x85\x86\x87\x88\x89\x8A\x92\x93\x94\x95\x96\x97\x98\x99\x9A\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFF\xC4\x00\x1F\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\xFF\xC4\x00\xB5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02\x77\x00\x01\x02\x03\x11\x04\x05\x21\x31\x06\x12\x41\x51\x61\x07\x71\x13\x22\x32\x81\x08\x14\x42\x91\xA1\xB1\xC1\x09\x23\x33\x52\xF0\x15\x62\x72\xD1\x0A\x16\x24\x34\xE1\x25\xF1\x17\x18\x19\x1A\x26\x27\x28\x29\x2A\x35\x36\x37\x38\x39\x3A\x43\x44\x45\x46\x47\x48\x49\x4A\x53\x54\x55\x56\x57\x58\x59\x5A\x63\x64\x65\x66\x67\x68\x69\x6A\x73\x74\x75\x76\x77\x78\x79\x7A\x82\x83\x84\x85\x86\x87\x88\x89\x8A\x92\x93\x94\x95\x96\x97\x98\x99\x9A\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFF\xDA\x00\x0C\x03\x01\x00\x02\x11\x03\x11\x00\x3F\x00')
            for i in range(100):
                f.write(b'\xFF' * 1000)
        print(f"✅ Đã tạo file ảnh giả: {path}")
        return True
    except Exception as e:
        print(f"❌ Lỗi tạo ảnh giả: {e}")
        return False

PATH_ANH_1 = r"C:\Users\Administrator\Downloads\cccd_truoc.jpg"
PATH_ANH_2 = r"C:\Users\Administrator\Downloads\cccd_sau.jpg"
PATH_ANH_3 = r"C:\Users\Administrator\Downloads\chan_dung.jpg"

if not os.path.exists(PATH_ANH_1):
    print("📁 Tạo ảnh giả cho CCCD...")
    temp_dir = os.environ.get('TEMP', r'C:\Users\Administrator\Downloads')
    PATH_ANH_1 = os.path.join(temp_dir, 'cccd_truoc.jpg')
    PATH_ANH_2 = os.path.join(temp_dir, 'cccd_sau.jpg')
    PATH_ANH_3 = os.path.join(temp_dir, 'chan_dung.jpg')
    tao_file_anh_gia(PATH_ANH_1)
    tao_file_anh_gia(PATH_ANH_2)
    tao_file_anh_gia(PATH_ANH_3)

def random_so_tai_khoan():
    so_chu_so = random.choice([8, 9, 10])
    so_tk = ''.join([str(random.randint(0, 9)) for _ in range(so_chu_so)])
    return so_tk, so_chu_so

def kiem_tra_loi_sau_tiep_tuc(driver):
    time.sleep(1.5)
    try:
        loi_element = driver.find_element(By.XPATH, "//*[contains(text(), 'không được để trống') or contains(text(), 'không hợp lệ')]")
        if loi_element.is_displayed():
            return True
    except:
        pass
    return False

def dong_popup(driver):
    try:
        driver.execute_script("""
            var popups = document.querySelectorAll('.modal, .popup, .overlay, [role="dialog"]');
            for(var i=0; i<popups.length; i++) {
                if(popups[i].style.display !== 'none' && popups[i].style.visibility !== 'hidden') {
                    popups[i].style.display = 'none';
                    var closeBtn = popups[i].querySelector('.close, [aria-label="Close"]');
                    if(closeBtn) closeBtn.click();
                }
            }
        """)
        time.sleep(0.5)
        return True
    except:
        return False

def upload_anh_va_otp(driver, lan):
    print("\n" + "="*60)
    print(f"📸 LẦN {lan} - UPLOAD ẢNH CCCD VÀ NHẬN OTP")
    print("="*60)
    
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    
    file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
    print(f"📁 Tìm thấy {len(file_inputs)} input file")
    
    anh_paths = [PATH_ANH_1, PATH_ANH_2, PATH_ANH_3]
    for i in range(min(3, len(file_inputs))):
        try:
            if os.path.exists(anh_paths[i]):
                file_inputs[i].send_keys(anh_paths[i])
                print(f"✅ Đã upload ảnh {i+1}: {os.path.basename(anh_paths[i])}")
            else:
                tao_file_anh_gia(anh_paths[i])
                file_inputs[i].send_keys(anh_paths[i])
                print(f"✅ Đã tạo và upload ảnh {i+1}")
            time.sleep(1)
        except Exception as e:
            print(f"❌ Lỗi upload ảnh {i+1}: {e}")
    
    print("\n📱 XÁC THỰC OTP...")
    time.sleep(3)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    clicked = False
    
    cac_tu_tim = ["cuộc gọi", "gọi điện", "call", "voice call"]
    
    for tu in cac_tu_tim:
        if clicked:
            break
        try:
            otp_btn = driver.find_element(By.XPATH, f"//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{tu}')]")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", otp_btn)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", otp_btn)
            print(f"📞 Đã ấn nút chứa '{tu}'")
            clicked = True
            break
        except:
            continue
    
    if not clicked:
        try:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            for btn in buttons:
                text_btn = btn.text.lower()
                if ("gọi" in text_btn or "cuộc" in text_btn or "call" in text_btn) and "zalo" not in text_btn:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].click();", btn)
                    print(f"📞 Đã ấn nút cuộc gọi: '{btn.text}'")
                    clicked = True
                    break
        except:
            pass
    
    if not clicked:
        try:
            driver.execute_script("""
                var btns = document.querySelectorAll('button');
                for(var i=0; i<btns.length; i++) {
                    var txt = btns[i].innerText.toLowerCase();
                    if((txt.includes('gọi') || txt.includes('cuộc') || txt.includes('call')) && !txt.includes('zalo')) {
                        btns[i].scrollIntoView({block: 'center'});
                        btns[i].click();
                        return true;
                    }
                }
            """)
            print("📞 Đã click nút cuộc gọi bằng JavaScript")
            clicked = True
        except:
            pass
    
    if not clicked:
        print("❌ KHÔNG TÌM THẤY NÚT CUỘC GỌI!")
    
    print("\n⏳ Chờ 10 giây để OTP được gửi qua cuộc gọi...")
    time.sleep(10)

def click_dang_ky_ngay(driver):
    print("🔍 Đang tìm nút Đăng ký Ngay...")
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "button"))
        )
    except:
        pass
    
    for _ in range(3):
        try:
            driver.execute_script("""
                var popups = document.querySelectorAll('[class*="popup"], [class*="modal"], [class*="overlay"]');
                for(var i=0; i<popups.length; i++) {
                    if(popups[i].style.display !== 'none') {
                        popups[i].style.display = 'none';
                    }
                }
            """)
        except:
            pass
        time.sleep(0.3)
    
    cac_cach_tim = [
        (By.XPATH, "//button[contains(text(), 'Đăng ký')]"),
        (By.XPATH, "//button[contains(text(), 'Đăng Ký')]"),
        (By.XPATH, "//button[contains(text(), 'dang ky')]"),
        (By.XPATH, "//button[contains(@class, 'register')]"),
        (By.XPATH, "//button[contains(@class, 'submit')]"),
        (By.XPATH, "//button[@type='submit']"),
        (By.XPATH, "//div[contains(@class, 'btn')]//button"),
        (By.XPATH, "//*[contains(text(), 'Đăng ký Ngay')]"),
        (By.XPATH, "//*[text()='Đăng ký Ngay']"),
    ]
    
    for by, selector in cac_cach_tim:
        try:
            buttons = driver.find_elements(by, selector)
            for btn in buttons:
                if btn.is_displayed():
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", btn)
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].click();", btn)
                    print(f"✅ Đã nhấn nút Đăng ký: {btn.text if btn.text else selector}")
                    return True
        except:
            continue
    
    try:
        result = driver.execute_script("""
            var btns = document.querySelectorAll('button');
            for(var i=0; i<btns.length; i++) {
                var txt = btns[i].innerText.toLowerCase();
                if(txt.includes('đăng ký') || txt.includes('dang ky')) {
                    btns[i].scrollIntoView({block: 'center'});
                    btns[i].click();
                    return true;
                }
            }
            var divs = document.querySelectorAll('div[role="button"], div.clickable, a');
            for(var i=0; i<divs.length; i++) {
                var txt = divs[i].innerText.toLowerCase();
                if(txt.includes('đăng ký') || txt.includes('dang ky')) {
                    divs[i].scrollIntoView({block: 'center'});
                    divs[i].click();
                    return true;
                }
            }
            return false;
        """)
        if result:
            print("✅ Đã nhấn nút Đăng ký bằng JavaScript")
            return True
    except:
        pass
    
    print("\n🔍 DEBUG: Tất cả button trên trang:")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for i, btn in enumerate(buttons):
        print(f"   Button {i}: text='{btn.text}', display={btn.is_displayed()}")
    
    print("❌ KHÔNG TÌM THẤY NÚT ĐĂNG KÝ!")
    return False

def thuc_hien_mot_lan(driver, lan, so_dien_thoai):
    print("\n" + "="*60)
    print(f"🔄 LẦN {lan} - BẮT ĐẦU ĐĂNG KÝ")
    print(f"📞 Số điện thoại: {so_dien_thoai}")
    print("="*60)
    
    random_ua = ua.random
    
    dong_popup(driver)
    
    print("\n🏠 TRANG CHỦ")
    driver.get("https://web.fincalc.vn/")
    time.sleep(5)
    
    dong_popup(driver)
    
    for _ in range(5):
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.3)
    
    dong_popup(driver)
    time.sleep(1)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
    except:
        pass
    
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"📝 Tìm thấy {len(inputs)} input")
    
    if len(inputs) >= 3:
        for i in range(3):
            try:
                if inputs[i].is_displayed() and inputs[i].is_enabled():
                    driver.execute_script("arguments[0].value = '';", inputs[i])
                    time.sleep(0.2)
                else:
                    print(f"⚠️ Input {i+1} không hiển thị hoặc bị disable")
            except:
                print(f"⚠️ Không thể clear input {i+1}")
        
        try:
            inputs[0].send_keys(HO_TEN)
            print(f"✅ Họ tên: {HO_TEN}")
        except:
            driver.execute_script("arguments[0].value = arguments[1];", inputs[0], HO_TEN)
            print(f"✅ Họ tên (JS): {HO_TEN}")
        
        try:
            inputs[1].send_keys(so_dien_thoai)
            print(f"✅ Số điện thoại: {so_dien_thoai}")
        except:
            driver.execute_script("arguments[0].value = arguments[1];", inputs[1], so_dien_thoai)
            print(f"✅ Số điện thoại (JS): {so_dien_thoai}")
        
        try:
            inputs[2].send_keys(EMAIL)
            print(f"✅ Email: {EMAIL}")
        except:
            driver.execute_script("arguments[0].value = arguments[1];", inputs[2], EMAIL)
            print(f"✅ Email (JS): {EMAIL}")
        
        driver.execute_script("document.activeElement?.blur(); document.body.click();")
        time.sleep(1)
    else:
        print(f"❌ Không đủ input (cần 3, có {len(inputs)})")
        return False
    
    print("\n🖱️ ĐANG CLICK NÚT ĐĂNG KÝ NGAY...")
    click_dang_ky_ngay(driver)
    
    print("\n⏳ ĐỢI TRANG CHUYỂN HƯỚNG (TỐI ĐA 20 GIÂY)...")
    
    da_chuyen = False
    for i in range(20):
        time.sleep(1)
        current_url = driver.current_url
        if "reg/personal" in current_url:
            print(f"✅ Đã chuyển sang trang: {current_url}")
            da_chuyen = True
            break
        if "reg" in current_url:
            print(f"✅ Đã chuyển sang: {current_url}")
            da_chuyen = True
            break
        if i == 5:
            print("   ⚠️ Vẫn đang đợi, thử click lại...")
            click_dang_ky_ngay(driver)
        if i == 10:
            print("   ⚠️ Đợi lâu hơn, kiểm tra lại...")
    
    if not da_chuyen:
        print(f"⚠️ Không chuyển được trang, URL hiện tại: {driver.current_url}")
        print("⚠️ Thử lại lần cuối...")
        click_dang_ky_ngay(driver)
        time.sleep(5)
        if "reg" in driver.current_url:
            print(f"✅ Đã chuyển sau khi thử lại: {driver.current_url}")
        else:
            print("❌ VẪN KHÔNG CHUYỂN ĐƯỢC TRANG!")
            return False
    
    time.sleep(2)
    
    print("\n📝 TRANG ĐĂNG KÝ CÁ NHÂN")
    time.sleep(3)
    
    for _ in range(5):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(0.2)
    
    dong_popup(driver)
    time.sleep(1)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
    except:
        pass
    
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"📝 Tìm thấy {len(inputs)} input ở trang cá nhân")
    
    if len(inputs) >= 2:
        try:
            if inputs[0].is_displayed() and inputs[0].is_enabled():
                driver.execute_script("arguments[0].value = '';", inputs[0])
                inputs[0].send_keys(NGAY_SINH)
                print(f"✅ Ngày sinh: {NGAY_SINH}")
            else:
                driver.execute_script("arguments[0].value = arguments[1];", inputs[0], NGAY_SINH)
                print(f"✅ Ngày sinh (JS): {NGAY_SINH}")
        except:
            driver.execute_script("arguments[0].value = arguments[1];", inputs[0], NGAY_SINH)
            print(f"✅ Ngày sinh (JS): {NGAY_SINH}")
        
        try:
            if inputs[1].is_displayed() and inputs[1].is_enabled():
                driver.execute_script("arguments[0].value = '';", inputs[1])
                inputs[1].send_keys(SO_CCCD)
                print(f"✅ CCCD: {SO_CCCD}")
            else:
                driver.execute_script("arguments[0].value = arguments[1];", inputs[1], SO_CCCD)
                print(f"✅ CCCD (JS): {SO_CCCD}")
        except:
            driver.execute_script("arguments[0].value = arguments[1];", inputs[1], SO_CCCD)
            print(f"✅ CCCD (JS): {SO_CCCD}")
        time.sleep(1)
    
    try:
        driver.find_element(By.XPATH, "//*[text()='Nam']").click()
        print("✅ Giới tính: Nam")
    except:
        try:
            driver.find_element(By.XPATH, "//*[contains(text(), 'Nam')]").click()
            print("✅ Giới tính: Nam")
        except:
            print("⚠️ Không chọn được giới tính")
    
    comboboxes = driver.find_elements(By.XPATH, "//button[@role='combobox']")
    if len(comboboxes) > 0:
        tinh_thanh = comboboxes[0]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tinh_thanh)
        time.sleep(0.5)
        tinh_thanh.click()
        print("📍 Đã mở dropdown Tỉnh/Thành")
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, "//*[text()='Bac Giang']").click()
            print("✅ Đã chọn: Bắc Giang")
        except:
            driver.find_element(By.XPATH, "//*[contains(text(), 'Bac Giang')]").click()
            print("✅ Đã chọn: Bắc Giang")
        time.sleep(0.5)
    
    print("\n📱 Chọn hãng điện thoại...")
    if len(comboboxes) > 1:
        hieu_dt = comboboxes[1]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hieu_dt)
        time.sleep(0.5)
        
        for hang in cac_hang:
            try:
                print(f"   🔄 Đang thử: {hang}")
                driver.execute_script("arguments[0].click();", hieu_dt)
                time.sleep(1)
                driver.find_element(By.XPATH, f"//*[text()='{hang}']").click()
                print(f"   ✅ Đã chọn: {hang}")
                time.sleep(1)
                break
            except:
                try:
                    driver.execute_script("arguments[0].click();", hieu_dt)
                    time.sleep(1)
                    driver.find_element(By.XPATH, f"//*[contains(text(), '{hang}')]").click()
                    print(f"   ✅ Đã chọn: {hang}")
                    time.sleep(1)
                    break
                except:
                    print(f"   ❌ Không chọn được {hang}")
                    continue
    
    print("\n📞 Nhập số điện thoại...")
    time.sleep(1)
    
    tat_ca_input_tel = driver.find_elements(By.XPATH, "//input[@type='tel']")
    print(f"📝 Tìm thấy {len(tat_ca_input_tel)} input type=tel")
    
    if len(tat_ca_input_tel) > 2:
        so_nguoi_than = tat_ca_input_tel[2]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", so_nguoi_than)
        time.sleep(0.5)
        so_nguoi_than.click()
        time.sleep(0.3)
        driver.execute_script("arguments[0].value = '';", so_nguoi_than)
        so_nguoi_than.send_keys(SO_DT_NGUOI_THAN)
        print(f"✅ Số người thân: {SO_DT_NGUOI_THAN}")
    
    if len(tat_ca_input_tel) > 3:
        so_tuyen_dung = tat_ca_input_tel[3]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", so_tuyen_dung)
        time.sleep(0.5)
        so_tuyen_dung.click()
        time.sleep(0.3)
        driver.execute_script("arguments[0].value = '';", so_tuyen_dung)
        so_tuyen_dung.send_keys(SO_DT_TUYEN_DUNG)
        print(f"✅ Số tuyển dụng: {SO_DT_TUYEN_DUNG}")
    
    print("\n🏦 Chọn Tên Ngân Hàng...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 400);")
    time.sleep(2)
    
    tat_ca_combobox = driver.find_elements(By.XPATH, "//button[@role='combobox']")
    print(f"   📍 Tìm thấy {len(tat_ca_combobox)} combobox")
    
    if len(tat_ca_combobox) > 2:
        ngan_hang_combobox = tat_ca_combobox[2]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ngan_hang_combobox)
        time.sleep(0.5)
        ngan_hang_combobox.click()
        print("   ✅ Đã mở dropdown ngân hàng")
        time.sleep(1.5)
        
        try:
            options = driver.find_elements(By.CSS_SELECTOR, "li[role='option']")
            if not options:
                options = driver.find_elements(By.CSS_SELECTOR, "ul li")
            if not options:
                options = driver.find_elements(By.CSS_SELECTOR, "[role='option']")
            
            if options:
                driver.execute_script("arguments[0].click();", options[0])
                print(f"   ✅ Đã chọn: {options[0].text[:50]}...")
            else:
                driver.find_element(By.XPATH, "//*[contains(text(), 'Vietcombank')]").click()
                print("   ✅ Đã chọn Vietcombank")
            time.sleep(1)
        except Exception as e:
            print(f"   ❌ Lỗi chọn ngân hàng: {e}")
    
    print("\n💰 NHẬP SỐ TÀI KHOẢN (RANDOM 8/9/10 SỐ)")
    
    tat_ca_input_text = driver.find_elements(By.TAG_NAME, "input")
    so_tk_input = None
    
    for inp in reversed(tat_ca_input_text):
        if inp.is_displayed() and inp.is_enabled():
            so_tk_input = inp
            break
    
    if not so_tk_input:
        print("❌ Không tìm thấy ô nhập số tài khoản!")
        return False
    
    thanh_cong = False
    so_lan_thu = 0
    max_lan = 30
    
    while not thanh_cong and so_lan_thu < max_lan:
        so_lan_thu += 1
        so_tk, so_chu_so = random_so_tai_khoan()
        print(f"\n🔄 Thử số {so_lan_thu}/{max_lan}: {so_tk} ({so_chu_so} số)")
        
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", so_tk_input)
        time.sleep(0.3)
        driver.execute_script("arguments[0].value = '';", so_tk_input)
        so_tk_input.send_keys(so_tk)
        time.sleep(0.5)
        
        driver.execute_script("document.activeElement?.blur(); document.body.click();")
        time.sleep(1)
        
        try:
            tiep_tuc = driver.find_element(By.XPATH, "//button[normalize-space()='Tiếp tục']")
            if tiep_tuc.is_displayed() and tiep_tuc.is_enabled():
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tiep_tuc)
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", tiep_tuc)
                print(f"   ⏩ Đã ấn Tiếp tục")
                time.sleep(2)
            else:
                print(f"   ❌ Nút Tiếp tục không thể click!")
                continue
        except:
            print(f"   ❌ Không tìm thấy nút Tiếp tục!")
            continue
        
        co_loi = kiem_tra_loi_sau_tiep_tuc(driver)
        
        if co_loi:
            print(f"   ❌ Số {so_tk} không hợp lệ. Thử số khác...")
        else:
            try:
                tiep_tuc_check = driver.find_element(By.XPATH, "//button[normalize-space()='Tiếp tục']")
                print(f"   ⚠️ Vẫn còn nút Tiếp tục, thử lại...")
                continue
            except:
                thanh_cong = True
                print(f"\n🎉 THÀNH CÔNG! Số {so_tk} ({so_chu_so} số) được chấp nhận!")
                break
    
    if thanh_cong:
        print(f"\n📌 SỐ TÀI KHOẢN LẦN {lan}: {so_tk}")
        
        print("\n⏩ NHẤN TIẾP TỤC LẦN CUỐI ĐỂ TIẾP TỤC...")
        time.sleep(2)
        try:
            tiep_tuc_lan_cuoi = driver.find_element(By.XPATH, "//button[normalize-space()='Tiếp tục']")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tiep_tuc_lan_cuoi)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", tiep_tuc_lan_cuoi)
            print("✅ Đã nhấn Tiếp tục lần cuối, chuyển sang upload ảnh...")
            time.sleep(3)
        except Exception as e:
            print(f"⚠️ Không tìm thấy nút Tiếp tục: {e}")
        
        upload_anh_va_otp(driver, lan)
        return True
    else:
        print(f"\n❌ LẦN {lan} THẤT BẠI!")
        return False

def main():
    print("="*60)
    print("MONEYCAT - ĐĂNG KÝ TÀI KHOẢN")
    print("="*60)
    
    if len(sys.argv) >= 2:
        SO_DIEN_THOAI = str(sys.argv[1]).lstrip('0')
        print(f"📞 Số điện thoại từ lệnh: {SO_DIEN_THOAI}")
    else:
        SO_DIEN_THOAI = input("📞 Nhập số điện thoại: ").strip()
        SO_DIEN_THOAI = SO_DIEN_THOAI.lstrip('0')
    
    if len(sys.argv) >= 3:
        SO_LAN_LAP = int(sys.argv[2])
        print(f"🔄 Số lần lặp từ lệnh: {SO_LAN_LAP}")
    else:
        SO_LAN_LAP = int(input("🔄 Nhập số lần lặp: "))
    
    print(f"\n✅ Số điện thoại: {SO_DIEN_THOAI} | Số lần lặp: {SO_LAN_LAP}")
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    thanh_cong = 0
    that_bai = 0
    
    for lan in range(1, SO_LAN_LAP + 1):
        print(f"\n{'🌟'*30}")
        print(f"🌟 LẦN {lan}/{SO_LAN_LAP}")
        print(f"{'🌟'*30}")
        
        driver = webdriver.Edge(options=options)
        ket_qua = thuc_hien_mot_lan(driver, lan, SO_DIEN_THOAI)
        driver.quit()
        
        if ket_qua:
            thanh_cong += 1
        else:
            that_bai += 1
        
        if lan < SO_LAN_LAP:
            print(f"\n⏳ Đợi 5 giây trước lần {lan+1}...")
            time.sleep(5)
    
    print("\n" + "="*60)
    print("TỔNG KẾT")
    print("="*60)
    print(f"   ✅ Thành công: {thanh_cong}/{SO_LAN_LAP} lần")
    print(f"   ❌ Thất bại: {that_bai}/{SO_LAN_LAP} lần")
    print("="*60)

if __name__ == "__main__":
    main()