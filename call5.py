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

def main():
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

if __name__ == "__main__":
    main()