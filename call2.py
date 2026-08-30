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


def main():
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


if __name__ == "__main__":
    main()