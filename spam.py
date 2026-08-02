import os
import sys
import time
import json
import subprocess
import threading
import random
import signal
import re
import socket
import ssl
import concurrent.futures
import html
import hashlib
import base64
import logging
import math
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs, urlencode, urljoin
from typing import Optional, Dict, Any, List
from collections import Counter, deque
import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from telebot import types
import cloudscraper
import dns.resolver
from fake_useragent import UserAgent

BOT_TOKEN = "7845936454:AAEmDDbt4SqQRXxoEubgnf9T09Q8blb4muI"
ADMIN_ID = "7235906278"
GROUP_CHAT_ID = "-1004420189760"

FOLDER_DATA = "huuminh"
if not os.path.exists(FOLDER_DATA):
    os.makedirs(FOLDER_DATA)

HISTORY_FILE = os.path.join(FOLDER_DATA, "du_doan_history.json")
BET_HISTORY_FILE = os.path.join(FOLDER_DATA, "bet_history.json")
USERS_FILE = os.path.join(FOLDER_DATA, "users.json")
VIP_FILE = os.path.join(FOLDER_DATA, "vip_users.json")
RDP_FILE = os.path.join(FOLDER_DATA, "rdp_info.txt")

bot = telebot.TeleBot(BOT_TOKEN)
bot_mode = "normal"

SPAM_FILES = ["1.py", "2.py", "3.py", "4.py", "5.py", "6.py", "7.py", "8.py", "9.py", "10.py"]

users = {}
banned_users = {}
running_processes = {}
user_last_use = {}
stop_flags = {}
bot_running = True
tx_running = False
tx_thread = None
tx_data = {
    "dung": 0,
    "sai": 0,
    "lich_su": [],
    "ket_qua": [],
    "du_doan_hien_tai": None,
    "id_da_xu_ly": set()
}
lc79_bot = None
vip_users = {}

ua = UserAgent()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def format_message(content):
    msg = f"<blockquote expandable>{content}</blockquote>"
    msg += "\n<blockquote>👑 Admin: @Hahahhshah</blockquote>"
    return msg

def create_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("👑 Admin", url="https://t.me/Hahahhshah"),
        InlineKeyboardButton("💬 Nhóm chat", url="https://t.me/chungtoithichspam")
    )
    keyboard.add(
        InlineKeyboardButton("💥 Thuê bot tele", url="https://t.me/Hahahhshah"),
        InlineKeyboardButton("📦 Mua VIP", url="https://t.me/Hahahhshah")
    )
    return keyboard

def format_money(amount):
    if amount >= 0:
        return f"{amount:,.0f}".replace(",", ".")
    return f"-{abs(amount):,.0f}".replace(",", ".")

def load_users():
    global users, banned_users, user_last_use
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r", encoding='utf-8') as f:
                data = json.load(f)
                users = data.get("users", {})
                banned_users = data.get("banned", {})
                user_last_use = data.get("last_use", {})
        else:
            users = {}
            banned_users = {}
            user_last_use = {}
            save_users()
    except:
        users = {}
        banned_users = {}
        user_last_use = {}

def save_users():
    try:
        with open(USERS_FILE, "w", encoding='utf-8') as f:
            json.dump({
                "users": users,
                "banned": banned_users,
                "last_use": user_last_use
            }, f, ensure_ascii=False, indent=2)
        try:
            subprocess.run(['git', 'add', USERS_FILE], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'🔄 Update Users: {datetime.now().strftime("%H:%M:%S %d/%m/%Y")} [skip ci]'], check=True, capture_output=True)
            subprocess.run(['git', 'push', 'origin', 'main', '--force'], check=True, capture_output=True)
            print("✅ Đã commit users.json lên repo")
        except Exception as e:
            print(f"⚠️ Lỗi push users.json: {e}")
    except Exception as e:
        print(f"❌ Lỗi lưu users.json: {e}")

def load_vip_users():
    global vip_users
    try:
        if os.path.exists(VIP_FILE):
            with open(VIP_FILE, 'r', encoding='utf-8') as f:
                vip_users = json.load(f)
        else:
            vip_users = {}
            save_vip_users()
    except:
        vip_users = {}

def save_vip_users():
    try:
        with open(VIP_FILE, 'w', encoding='utf-8') as f:
            json.dump(vip_users, f, indent=2, ensure_ascii=False)
        try:
            subprocess.run(['git', 'add', VIP_FILE], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'🔄 Update VIP Users: {datetime.now().strftime("%H:%M:%S %d/%m/%Y")} [skip ci]'], check=True, capture_output=True)
            subprocess.run(['git', 'push', 'origin', 'main', '--force'], check=True, capture_output=True)
            print("✅ Đã commit vip_users.json lên repo")
        except Exception as e:
            print(f"⚠️ Lỗi push vip_users.json: {e}")
    except Exception as e:
        print(f"❌ Lỗi lưu vip_users.json: {e}")

def load_bet_history():
    try:
        if os.path.exists(BET_HISTORY_FILE):
            with open(BET_HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except:
        return []

def save_bet_history(history):
    try:
        with open(BET_HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
        try:
            subprocess.run(['git', 'add', BET_HISTORY_FILE], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'🔄 Update Bet History: {datetime.now().strftime("%H:%M:%S %d/%m/%Y")} [skip ci]'], check=True, capture_output=True)
            subprocess.run(['git', 'push', 'origin', 'main', '--force'], check=True, capture_output=True)
            print("✅ Đã commit bet_history.json lên repo")
        except Exception as e:
            print(f"⚠️ Lỗi push bet_history.json: {e}")
    except Exception as e:
        print(f"❌ Lỗi lưu bet_history.json: {e}")

class TeleBot:
    def __init__(self):
        self.info_file = RDP_FILE
        self.users_file = USERS_FILE
        self.vip_file = VIP_FILE
        self.history_file = HISTORY_FILE
        self.bet_history_file = BET_HISTORY_FILE
        self.is_running = True
        self.video = "https://offvn.io.vn/sms.mp4"
        self.last_rdp = None
        load_users()
        load_vip_users()
        
    def hide_phone(self, phone):
        if len(phone) >= 10:
            return phone[:3] + "********" + phone[-3:]
        elif len(phone) >= 7:
            return phone[:2] + "********" + phone[-2:]
        else:
            return "********" + phone[-2:] if len(phone) > 2 else "********"

    def save_rdp_to_github(self, full_address, port):
        timestamp = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        content = f"""=======================================================
🖥️ RDP INFO - Huu Minh Bot
=======================================================
📌 Full Address   : {full_address}
🔌 Port           : {port}
🌐 Host           : bore.pub
-------------------------------------------------------
👤 Username       : Administrator
🔑 Password       : Huuminh123@
📅 Created        : {timestamp}
=======================================================
"""
        with open(self.info_file, 'w', encoding='utf-8') as f:
            f.write(content)
        try:
            subprocess.run(['git', 'add', self.info_file], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'🔄 Update RDP: {port} [skip ci]'], check=True, capture_output=True)
            subprocess.run(['git', 'push', 'origin', 'main', '--force'], check=True, capture_output=True)
            print(f"✅ Đã commit thông tin RDP lên repo: {full_address}")
            return True
        except Exception as e:
            print(f"❌ Lỗi push RDP: {e}")
            return False

    def monitor_rdp(self):
        print("🚀 Đang khởi động Bore...")
        while bot_running:
            try:
                process = subprocess.Popen(
                    ["./bore/bore.exe", "local", "3389", "--to", "bore.pub"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1
                )
                while bot_running:
                    line = process.stdout.readline()
                    if not line:
                        if process.poll() is not None:
                            print("⚠️ Bore đã dừng, sẽ khởi động lại sau 5 giây...")
                            break
                        continue
                    print(f"[Bore] {line.strip()}")
                    if "listening at" in line:
                        full_address = line.strip().split("listening at ")[1].strip()
                        port = full_address.split(":")[1]
                        if full_address != self.last_rdp:
                            self.last_rdp = full_address
                            self.save_rdp_to_github(full_address, port)
                            keyboard = create_keyboard()
                            content = f"""🎉 RDP ĐÃ SẴN SÀNG!

📌 Address: {full_address}
🔌 Port: {port}
🌐 Host: bore.pub

👤 Username: Administrator
🔑 Password: Huuminh123@

📅 {datetime.now().strftime('%H:%M:%S %d/%m/%Y')}"""
                            bot.send_message(ADMIN_ID, format_message(content), parse_mode='HTML', reply_markup=keyboard)
                            with open(self.info_file, 'rb') as f:
                                bot.send_document(ADMIN_ID, f)
                    if "connection exited with error" in line or "An existing connection was forcibly closed" in line:
                        print("⚠️ Lỗi kết nối Bore, sẽ khởi động lại...")
                        break
                try:
                    process.terminate()
                    process.wait(timeout=5)
                except:
                    process.kill()
                if bot_running:
                    print("🔄 Khởi động lại Bore sau 5 giây...")
                    time.sleep(5)
            except Exception as e:
                print(f"❌ Lỗi monitor RDP: {e}")
                if bot_running:
                    time.sleep(5)

    def run_spam_file(self, file_name, phone, count, user_id):
        if file_name in stop_flags and stop_flags[file_name]:
            return f"⏹️ Đã dừng {file_name}"
        try:
            cmd = f"python {file_name} {phone} {count}"
            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            key = f"{user_id}_{file_name}_{phone}"
            running_processes[key] = process
            output = []
            while True:
                if file_name in stop_flags and stop_flags[file_name]:
                    process.terminate()
                    return f"⏹️ Đã dừng {file_name}"
                line = process.stdout.readline()
                if not line:
                    break
                output.append(line.strip())
            process.wait()
            if key in running_processes:
                del running_processes[key]
            if process.returncode == 0:
                return f"✅ {file_name} thành công"
            else:
                return f"❌ {file_name} lỗi"
        except Exception as e:
            return f"❌ {file_name} {str(e)}"

    def run_all_spam_async(self, phone, count, user_id, chat_id, is_vip=False, full_name="", username=""):
        global stop_flags
        stop_flags = {}
        results = {}
        
        def run_file_once(file_name):
            if not os.path.exists(file_name):
                results[file_name] = f"❌ {file_name} không tồn tại"
                return
            
            stop_flags[file_name] = False
            print(f"🔄 Đang chạy file: {file_name}")
            
            cmd = f"python {file_name} {phone} {count}"
            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            key = f"{user_id}_{file_name}_{phone}"
            running_processes[key] = process
            output = []
            
            try:
                while True:
                    if file_name in stop_flags and stop_flags[file_name]:
                        process.terminate()
                        results[file_name] = f"⏹️ Đã dừng {file_name}"
                        break
                    line = process.stdout.readline()
                    if not line:
                        break
                    output.append(line.strip())
                    if line.strip():
                        print(f"[{file_name}] {line.strip()}")
                process.wait()
            except Exception as e:
                results[file_name] = f"❌ {file_name} lỗi: {str(e)}"
            finally:
                if key in running_processes:
                    del running_processes[key]
                if file_name not in results:
                    if process.returncode == 0:
                        results[file_name] = f"✅ {file_name} thành công"
                    else:
                        results[file_name] = f"❌ {file_name} lỗi (code: {process.returncode})"
            
            print(f"✅ Đã xong: {file_name}")
        
        for index, file_name in enumerate(SPAM_FILES, 1):
            if any(stop_flags.values()):
                print("⏹️ Đã nhận lệnh dừng")
                for f in SPAM_FILES:
                    if f not in results:
                        results[f] = "⏹️ Chưa chạy (bị dừng)"
                break
            
            print(f"\n{'='*50}")
            print(f"📁 CHẠY FILE {index}/{len(SPAM_FILES)}: {file_name}")
            print(f"{'='*50}")
            
            run_file_once(file_name)
        
        print(f"\n✅ ĐÃ CHẠY XONG TẤT CẢ {len(SPAM_FILES)} FILES")
        
        def send_result():
            time.sleep(2)
            result_text = "\n".join([results.get(f, "❌ Chưa có kết quả") for f in SPAM_FILES])
            admin_keyboard = create_keyboard()
            
            success_count = sum(1 for f in SPAM_FILES if results.get(f, "").startswith("✅"))
            fail_count = sum(1 for f in SPAM_FILES if results.get(f, "").startswith("❌") or results.get(f, "").startswith("⏹️"))
            
            admin_content = f"""📊 THÔNG TIN TẤN CÔNG CHI TIẾT

👤 THÔNG TIN NGƯỜI DÙNG:
 ├ 🆔 ID: {user_id}
 ├ 📛 Họ tên: {full_name}
 ├ 🔗 Username: @{username if username else 'Không có'}
 └ 🌐 Ngôn ngữ: vi

📱 DANH SÁCH SỐ ĐIỆN THOẠI (1 số):
  └ 📱 {phone}

📊 THÔNG SỐ TẤN CÔNG:
 ├ 🔄 Số lần: {count}
 ├ 💳 Gói: {'VIP' if is_vip else 'Thường'}
 └ ⏰ Thời gian: {datetime.now().strftime('%H:%M:%S')} {datetime.now().strftime('%d/%m/%Y')}

📈 KẾT QUẢ:
 ├ ✅ Thành công: {success_count}/{len(SPAM_FILES)}
 ├ ❌ Thất bại: {fail_count}/{len(SPAM_FILES)}
 └ 📊 Tỷ lệ: {success_count/(success_count+fail_count)*100 if success_count+fail_count > 0 else 0:.1f}%

📊 Kết quả từng file:
{result_text}

📞 LIÊN HỆ: @Hahahhshah"""
            bot.send_message(ADMIN_ID, format_message(admin_content), parse_mode='HTML', reply_markup=admin_keyboard)
        
        result_thread = threading.Thread(target=send_result)
        result_thread.daemon = True
        result_thread.start()

    def check_cooldown(self, user_id, is_vip=False):
        current_time = time.time()
        cooldown = 800 if not is_vip else 300
        if user_id in user_last_use:
            last_use = user_last_use[user_id]
            time_passed = current_time - last_use
            if time_passed < cooldown:
                remaining = int(cooldown - time_passed)
                return False, remaining
        return True, 0

    def update_last_use(self, user_id):
        user_last_use[user_id] = time.time()
        save_users()

    def stop_spam(self, phone, user_id):
        stopped = []
        for key, process in list(running_processes.items()):
            key_parts = key.split('_')
            if len(key_parts) >= 3:
                key_user_id = key_parts[0]
                key_phone = key_parts[2]
                if key_user_id == user_id and key_phone == phone:
                    try:
                        process.terminate()
                        stopped.append(key)
                        del running_processes[key]
                    except:
                        pass
        if stopped:
            return True
        return False

    def stop_all_spam_admin(self):
        stopped = []
        for key, process in list(running_processes.items()):
            try:
                process.terminate()
                stopped.append(key)
                del running_processes[key]
            except:
                pass
        if stopped:
            return True
        return False

    def check_user(self, user_id):
        if str(user_id) == ADMIN_ID:
            return True
        if str(user_id) in banned_users:
            return False
        if str(user_id) in users:
            expire = datetime.strptime(users[str(user_id)]['expire'], '%d/%m/%Y')
            if datetime.now() <= expire:
                return True
            else:
                del users[str(user_id)]
                save_users()
                return False
        return False

    def check_vip(self, user_id):
        if str(user_id) == ADMIN_ID:
            return True
        if str(user_id) in users:
            return users[str(user_id)].get('vip', False)
        return False

    def delete_user_message(self, message):
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass

    def delete_user_message_after_delay(self, message, delay=0.1):
        def _delete():
            time.sleep(delay)
            self.delete_user_message(message)
        threading.Thread(target=_delete, daemon=True).start()

    def get_tiktok_profile(self, user_input):
        try:
            user_input = user_input.strip()
            if not user_input:
                return {"error": "Vui lòng nhập username TikTok hợp lệ"}
            if user_input.startswith("@") and len(user_input) > 1:
                username = user_input[1:]
                user_input = f"https://www.tiktok.com/@{username}"
            elif not user_input.startswith("http") and not user_input.startswith("@"):
                user_input = f"https://www.tiktok.com/@{user_input}"
            if "tiktok.com" not in user_input:
                return {"error": "Link không hợp lệ. Vui lòng nhập username hoặc link TikTok"}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            response = requests.get(user_input, headers=headers, timeout=15)
            if response.status_code != 200:
                return {"error": f"Không thể truy cập trang, status code: {response.status_code}"}
            script_pattern = re.compile(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>([^<]+)</script>')
            script_match = script_pattern.search(response.text)
            if not script_match:
                return {"error": "Không tìm thấy dữ liệu profile"}
            data = json.loads(script_match.group(1))
            user_data = data.get('__DEFAULT_SCOPE__', {}).get('webapp.user-detail', {})
            if not user_data:
                return {"error": "Không thể lấy thông tin user"}
            user_info = user_data.get('userInfo', {})
            user = user_info.get('user', {})
            stats = user_info.get('stats', {})
            user_id = user.get('id', '')
            if user_id:
                try:
                    additional_url = f"https://api16-core-c-alisg.tiktokv.com/lite/v2/user/detail/other/?user_id={user_id}&lite_flow_schedule=new&aid=1340"
                    add_response = requests.get(additional_url, timeout=10)
                    if add_response.status_code == 200:
                        add_data = add_response.json()
                        add_user = add_data.get('user', {})
                        stats['followerCount'] = add_user.get('follower_count', stats.get('followerCount', 0))
                        stats['followingCount'] = add_user.get('following_count', stats.get('followingCount', 0))
                        stats['heartCount'] = add_user.get('total_favorited', stats.get('heartCount', 0))
                        user['bio_email'] = add_user.get('bio_email', user.get('bioEmail', ''))
                        user['original_musician'] = add_user.get('original_musician', False)
                except:
                    pass
            region = user.get('region', '')
            create_time = user.get('createTime', '')
            if create_time:
                try:
                    dt = datetime.fromtimestamp(int(create_time))
                    create_time = dt.strftime('%H:%M:%S || %d/%m/%Y')
                except:
                    pass
            unique_id_modify = user.get('uniqueIdModifyTime', '')
            if unique_id_modify:
                try:
                    dt = datetime.fromtimestamp(int(unique_id_modify))
                    unique_id_modify = dt.strftime('%H:%M:%S || %d/%m/%Y')
                except:
                    pass
            nick_modify = user.get('nickNameModifyTime', '')
            if nick_modify:
                try:
                    dt = datetime.fromtimestamp(int(nick_modify))
                    nick_modify = dt.strftime('%H:%M:%S || %d/%m/%Y')
                except:
                    pass
            user_id_int = int(user_id) if user_id else 0
            if user_id_int and len(str(user_id_int)) < 19:
                user_id_int = int(str(user_id_int).ljust(19, '0'))
            binary_id = bin(user_id_int)[2:][:31] if user_id_int else ''
            created_time = ''
            if binary_id:
                try:
                    ts = int(binary_id, 2)
                    dt = datetime.fromtimestamp(ts)
                    created_time = dt.strftime('%H:%M:%S || %d/%m/%Y')
                except:
                    pass
            result = {
                "username": user.get('uniqueId', ''),
                "nickname": user.get('nickname', ''),
                "user_id": user_id,
                "bio": user.get('signature', ''),
                "bio_email": user.get('bio_email', ''),
                "avatar": user.get('avatarMedium', user.get('avatarThumb', '')),
                "region": region,
                "verified": user.get('verified', False),
                "private_account": user.get('privateAccount', False),
                "original_musician": user.get('original_musician', False),
                "follower_count": stats.get('followerCount', 0),
                "following_count": stats.get('followingCount', 0),
                "heart_count": stats.get('heartCount', 0),
                "video_count": stats.get('videoCount', 0),
                "create_time": create_time,
                "unique_id_modify": unique_id_modify,
                "nick_modify": nick_modify,
                "account_created": created_time
            }
            return result
        except Exception as e:
            return {"error": str(e)}

    def tx_chuyen_doi(self, result):
        return 'T' if result == 'TAI' else 'X'

    def tx_tao_bo_mat(self, ket_qua):
        if ket_qua == 'T':
            for _ in range(100):
                bo = [random.randint(1, 6) for _ in range(3)]
                if sum(bo) >= 11:
                    return bo
            return [4, 4, 4]
        else:
            for _ in range(100):
                bo = [random.randint(1, 6) for _ in range(3)]
                if sum(bo) <= 10:
                    return bo
            return [3, 3, 3]

    def tx_run(self, chat_id, user_id, msg_id=None):
        global tx_running, tx_data
        tx_running = True
        tx_data["dung"] = 0
        tx_data["sai"] = 0
        tx_data["lich_su"] = []
        tx_data["id_da_xu_ly"] = set()
        url = "https://wtxmd52.tele68.com/v1/txmd5/lite-sessions"
        
        def lay_du_lieu():
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                return response.json().get('list', [])
            except:
                return None
        
        def phan_tich_15_phien(sessions):
            sessions.sort(key=lambda x: x['id'], reverse=True)
            ket_qua = [self.tx_chuyen_doi(s['resultTruyenThong']) for s in sessions[:15]]
            return ket_qua, sessions[:15]
        
        def phan_tich_chuoi(ket_qua):
            if not ket_qua:
                return None, 0
            current = ket_qua[0]
            count = 1
            for i in range(1, len(ket_qua)):
                if ket_qua[i] == current:
                    count += 1
                else:
                    break
            return current, count
        
        def du_doan(ket_qua):
            if not ket_qua:
                return None
            current, count = phan_tich_chuoi(ket_qua)
            return current
        
        def tao_message(sessions, ket_qua, du_doan_val, dung, sai, lich_su):
            msg = "🎲 **TÀI XỈU AUTO SCANNER**\n"
            msg += "═" * 30 + "\n\n"
            msg += "📊 **15 PHIÊN GẦN NHẤT:**\n"
            msg += "```\n"
            msg += "STT | ID     | KQ   | ĐIỂM | BỘ MẶT\n"
            msg += "-" * 55 + "\n"
            for i, s in enumerate(sessions[:15], 1):
                kq = 'TAI' if s['resultTruyenThong'] == 'TAI' else 'XIU'
                msg += f"{i:2}  | {s['id']} | {kq:^4} | {s['point']:^4} | {s['dices']}\n"
            msg += "```\n"
            chuoi = " → ".join(ket_qua)
            msg += f"📌 **CHUỖI KẾT QUẢ:**\n`{chuoi}`\n\n"
            dem_T = ket_qua.count('T')
            dem_X = ket_qua.count('X')
            msg += f"📊 **THỐNG KÊ 15 PHIÊN:**\n"
            msg += f"  • T (TAI): {dem_T} lần ({dem_T/15*100:.0f}%)\n"
            msg += f"  • X (XIU): {dem_X} lần ({dem_X/15*100:.0f}%)\n\n"
            current, count = phan_tich_chuoi(ket_qua)
            msg += f"📌 **CHUỖI HIỆN TẠI:**\n"
            msg += f"  • Kết quả: {'TAI' if current == 'T' else 'XIU'} ({current})\n"
            msg += f"  • Số phiên: {count}\n\n"
            msg += f"🎯 **DỰ ĐOÁN PHIÊN TIẾP THEO:**\n"
            msg += f"  📌 Kết quả: {'TAI' if du_doan_val == 'T' else 'XIU'} ({du_doan_val})\n"
            if count >= 3:
                msg += f"  💡 Quy luật: Đã có {count} {'TAI' if current == 'T' else 'XIU'} → Theo cầu\n"
            else:
                msg += f"  💡 Quy luật: Mới có {count} {'TAI' if current == 'T' else 'XIU'} → Theo cầu\n"
            bo_mat = self.tx_tao_bo_mat(du_doan_val)
            msg += f"  🎲 Bộ mặt gợi ý: {bo_mat} → Tổng: {sum(bo_mat)}\n\n"
            tong = dung + sai
            ty_le = dung / tong * 100 if tong > 0 else 0
            msg += "═" * 30 + "\n"
            msg += f"📊 **THỐNG KÊ DỰ ĐOÁN**\n"
            msg += f"  ✅ Đúng: {dung}\n"
            msg += f"  ❌ Sai: {sai}\n"
            msg += f"  📈 Tỷ lệ: {ty_le:.1f}%\n"
            msg += f"  📊 Tổng: {tong}\n"
            if lich_su:
                msg += "\n📋 **10 DỰ ĐOÁN GẦN NHẤT:**\n"
                for i, item in enumerate(lich_su[-10:], 1):
                    if item.get('dung') is None:
                        status = "⏳"
                    elif item['dung']:
                        status = "✅"
                    else:
                        status = "❌"
                    msg += f"  {i}. {item['thoi_gian']} | Dự:{item['du_doan']} | TT:{item.get('thuc_te','...')} | {status}\n"
            msg += "\n🔄 Đang chạy... kiểm tra mỗi 3 giây"
            return msg
        
        try:
            data = lay_du_lieu()
            if not data:
                bot.send_message(chat_id, format_message("❌ Không thể lấy dữ liệu!"), parse_mode='HTML')
                tx_running = False
                return
            ket_qua, sessions = phan_tich_15_phien(data)
            du_doan_val = du_doan(ket_qua)
            if du_doan_val:
                tx_data["lich_su"].append({
                    'thoi_gian': datetime.now().strftime('%H:%M:%S'),
                    'du_doan': du_doan_val,
                    'thuc_te': '...',
                    'dung': None
                })
            msg = tao_message(sessions, ket_qua, du_doan_val, tx_data["dung"], tx_data["sai"], tx_data["lich_su"])
            
            if msg_id:
                try:
                    bot.edit_message_text(format_message(msg), chat_id, msg_id, parse_mode='HTML')
                except:
                    sent = bot.send_message(chat_id, format_message(msg), parse_mode='HTML')
                    msg_id = sent.message_id
            else:
                sent = bot.send_message(chat_id, format_message(msg), parse_mode='HTML')
                msg_id = sent.message_id
            
            last_msg_id = msg_id
            
            while tx_running:
                try:
                    time.sleep(3)
                    data = lay_du_lieu()
                    if not data:
                        continue
                    data.sort(key=lambda x: x['id'], reverse=True)
                    phien_moi = data[0]
                    id_moi = phien_moi['id']
                    if id_moi in tx_data["id_da_xu_ly"]:
                        continue
                    tx_data["id_da_xu_ly"].add(id_moi)
                    thuc_te = self.tx_chuyen_doi(phien_moi['resultTruyenThong'])
                    if tx_data["lich_su"]:
                        du_doan_cu = tx_data["lich_su"][-1]['du_doan']
                        dung = (du_doan_cu == thuc_te)
                        if dung:
                            tx_data["dung"] += 1
                        else:
                            tx_data["sai"] += 1
                        tx_data["lich_su"][-1]['thuc_te'] = thuc_te
                        tx_data["lich_su"][-1]['dung'] = dung
                    ket_qua, sessions = phan_tich_15_phien(data)
                    du_doan_val = du_doan(ket_qua)
                    if du_doan_val:
                        tx_data["lich_su"].append({
                            'thoi_gian': datetime.now().strftime('%H:%M:%S'),
                            'du_doan': du_doan_val,
                            'thuc_te': '...',
                            'dung': None
                        })
                    msg = tao_message(sessions, ket_qua, du_doan_val, tx_data["dung"], tx_data["sai"], tx_data["lich_su"])
                    try:
                        if last_msg_id:
                            bot.edit_message_text(format_message(msg), chat_id, last_msg_id, parse_mode='HTML')
                        else:
                            sent = bot.send_message(chat_id, format_message(msg), parse_mode='HTML')
                            last_msg_id = sent.message_id
                    except:
                        sent = bot.send_message(chat_id, format_message(msg), parse_mode='HTML')
                        last_msg_id = sent.message_id
                except Exception as e:
                    logging.error(f"Lỗi trong vòng lặp tx: {e}")
                    time.sleep(3)
                    continue
        except Exception as e:
            bot.send_message(chat_id, format_message(f"❌ Lỗi: {str(e)}"), parse_mode='HTML')
        finally:
            tx_running = False

class LC79Bot:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.md5_password = ""
        self.token = ""
        self.jwt_token = ""
        self.balance = 0
        self.initial_balance = 0
        self.bet_amount = 1000
        self.target_profit = 0
        self.is_logged_in = False
        self.betting_active = False
        self.current_session_id = None
        self.tx_history = []
        self.history_loaded = False
        self.total_bets = 0
        self.wins = 0
        self.losses = 0
        self.bet_history = []
        self.du_doan_history = []
        self.phien_da_cuoc = None
        self.che_do = 1
        self.da_gui_telegram = set()
        self.last_bet_result_msg = ""
        self.running = False
        self.predictor = None
        self.last_checked_session = None
        self.stopped_by_target = False
        self.stopped_by_insufficient = False
        self.is_dudoan_mode = False
        self.is_private = False
        self.msg_id = None
        self.chat_id = None

    def login(self, username, password):
        try:
            self.username = username
            self.password = password
            self.md5_password = hashlib.md5(password.encode()).hexdigest()
            login_res = requests.get(
                "https://apifo88daigia.tele68.com/api?c=3&un=" + username + "&pw=" + self.md5_password + "&cp=R&cl=R&pf=web&at=",
                timeout=10
            )
            login_data = login_res.json()
            if not login_data.get('success'):
                return False
            self.token = login_data['accessToken']
            session_key = login_data['sessionKey']
            nick_name = username
            try:
                session_raw = base64.b64decode(session_key).decode()
                session_data = json.loads(session_raw)
                if session_data.get('nickname'):
                    nick_name = session_data['nickname']
            except:
                pass
            auth_res = requests.post(
                "https://wlb.tele68.com/v1/lobby/auth/login?cp=R&cl=R&pf=web&at=" + self.token,
                json={
                    "username": username,
                    "password": self.md5_password,
                    "nickName": nick_name,
                    "accessToken": self.token,
                    "sessionKey": session_key
                },
                timeout=10
            )
            auth_data = auth_res.json()
            if not auth_data.get('token'):
                return False
            self.jwt_token = auth_data['token']
            self.balance = auth_data.get('remoteLoginResp', {}).get('money', 0)
            self.is_logged_in = True
            return True
        except:
            return False

    def get_balance(self):
        try:
            res = requests.get(
                "https://gameapi.tele68.com/v1/profile/balance?cp=R&cl=R&pf=web&at=" + self.token,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.jwt_token
                },
                timeout=10
            )
            if res.ok:
                data = res.json()
                self.balance = data.get('balance') or data.get('money') or data.get('von') or 0
                return self.balance
        except:
            pass
        return self.balance

    def fetch_history(self):
        try:
            res = requests.get(
                "https://wtxmd52.tele68.com/v1/txmd5/sessions?cp=R&cl=R&pf=web&at=" + self.token,
                timeout=10
            )
            data = res.json()
            if data and data.get('list'):
                self.tx_history = data['list']
                self.current_session_id = data['list'][0]['id']
                if not self.history_loaded:
                    self.history_loaded = True
                return True
        except:
            pass
        return False

    def place_bet(self, prediction_data):
        try:
            if self.balance < self.bet_amount:
                content = f"""⚠️ SỐ DƯ KHÔNG ĐỦ
 ├ 💰 Số dư hiện tại: {format_money(self.balance)}đ
 ├ 💵 Cần tối thiểu: {format_money(self.bet_amount)}đ
 └ 🛑 Bot sẽ dừng lại!"""
                bot.send_message(ADMIN_ID, format_message(content), parse_mode='HTML')
                if not self.is_private:
                    bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(content), parse_mode='HTML')
                self.stopped_by_insufficient = True
                self.stop_auto_bet()
                return False
            bet_session = self.current_session_id
            if self.phien_da_cuoc == bet_session:
                return False
            bet_type = prediction_data.get('result', '')
            if bet_type == 'TÀI':
                bet_type = 'TAI'
            elif bet_type == 'XỈU':
                bet_type = 'XIU'
            else:
                return False
            bet_side = 'T' if bet_type == 'TAI' else 'X'
            pattern_type = prediction_data.get('pattern', '')
            body = {
                "username": self.username,
                "password": self.md5_password,
                "amount": self.bet_amount,
                "side": bet_side,
                "session": bet_session,
                "type": bet_type
            }
            res = requests.post(
                "https://wtxmd52.tele68.com/v1/txmd5/bet?limit=8&cp=R&cl=R&pf=web&at=" + self.token,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.jwt_token
                },
                json=body,
                timeout=10
            )
            if res.ok:
                data = res.json()
                if data.get('postBalance') is not None:
                    pre_balance = self.balance
                    self.balance = data['postBalance']
                    self.phien_da_cuoc = bet_session
                    result_key = data.get('result') or data.get('ketQua') or data.get('ket_qua') or ''
                    won = None
                    if result_key:
                        if result_key in ['TAI', 'TÀI', 'T']:
                            result_tx = 'TÀI'
                        elif result_key in ['XIU', 'XỈU', 'X']:
                            result_tx = 'XỈU'
                        else:
                            result_tx = None
                        if result_tx:
                            won = result_tx == prediction_data.get('result')
                    if won is None:
                        if self.balance > pre_balance:
                            won = True
                        elif self.balance < pre_balance:
                            won = False
                    self.total_bets += 1
                    bet_item = {
                        'time': datetime.now().strftime("%H:%M:%S"),
                        'session': bet_session,
                        'predict': prediction_data.get('result'),
                        'pattern': pattern_type,
                        'bet_amount': self.bet_amount,
                        'win': won,
                        'balance_after': self.balance,
                        'status': 'done' if won is not None else 'waiting'
                    }
                    self.bet_history.append(bet_item)
                    save_bet_history(self.bet_history)
                    if won:
                        self.wins += 1
                        result_text = "✅ THẮNG +" + format_money(self.bet_amount) + "đ → " + format_money(self.balance) + "đ"
                    else:
                        self.losses += 1
                        result_text = "❌ THUA -" + format_money(self.bet_amount) + "đ → " + format_money(self.balance) + "đ"
                    msg = self.tao_tin_nhan_day_du(prediction_data, bet_session, result_text)
                    if not self.is_private:
                        bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(msg), parse_mode='HTML')
                    profit = self.balance - self.initial_balance
                    if self.target_profit > 0 and profit >= self.target_profit:
                        content = f"""🎯 ĐẠT MỤC TIÊU LỢI NHUẬN
 ├ 💰 Lợi nhuận: <b>+{format_money(profit)}đ</b>
 ├ 🎯 Mục tiêu: {format_money(self.target_profit)}đ
 └ 🛑 Bot sẽ dừng lại!"""
                        bot.send_message(ADMIN_ID, format_message(content), parse_mode='HTML')
                        if not self.is_private:
                            bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(content), parse_mode='HTML')
                        self.stopped_by_target = True
                        self.stop_auto_bet()
                        return False
                    if self.balance < self.bet_amount:
                        content = f"""⚠️ SỐ DƯ KHÔNG ĐỦ
 ├ 💰 Số dư hiện tại: {format_money(self.balance)}đ
 ├ 💵 Cần tối thiểu: {format_money(self.bet_amount)}đ
 └ 🛑 Bot sẽ dừng lại!"""
                        bot.send_message(ADMIN_ID, format_message(content), parse_mode='HTML')
                        if not self.is_private:
                            bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(content), parse_mode='HTML')
                        self.stopped_by_insufficient = True
                        self.stop_auto_bet()
                        return False
                    return True
                if data.get('message') == "out_of_time":
                    return False
                if data.get('message') == "insufficient_funds":
                    content = f"""⚠️ SỐ DƯ KHÔNG ĐỦ
 ├ 💰 Số dư hiện tại: {format_money(self.balance)}đ
 ├ 💵 Cần tối thiểu: {format_money(self.bet_amount)}đ
 └ 🛑 Bot sẽ dừng lại!"""
                    bot.send_message(ADMIN_ID, format_message(content), parse_mode='HTML')
                    if not self.is_private:
                        bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(content), parse_mode='HTML')
                    self.stopped_by_insufficient = True
                    self.stop_auto_bet()
                    return False
                return False
            else:
                err_text = res.text
                if 'out_of_time' in err_text:
                    return False
                return False
        except:
            return False

    def tao_tin_nhan_day_du(self, prediction_data, bet_session, result_text=""):
        now = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        if prediction_data.get('result') == 'TÀI':
            du_doan_text = "🔥 TÀI"
        elif prediction_data.get('result') == 'XỈU':
            du_doan_text = "❄️ XỈU"
        else:
            du_doan_text = "⏸️ NGHỈ (THEO DÕI)"
        confidence = prediction_data.get('confidence', 0)
        pattern_type = prediction_data.get('pattern', '')
        pattern_detail = prediction_data.get('pattern_detail', '')
        message = "🎲 <b>TAI XỈU - SOI CẦU ĐOÁN NGU</b>\n"
        message += "⏰ " + now + "\n\n"
        if pattern_type:
            message += "📊 <b>PHÂN TÍCH CẦU:</b>\n"
            message += f"🔹 {pattern_type}\n"
            if pattern_detail:
                message += f"🔸 Mẫu: {pattern_detail}\n"
        if self.target_profit > 0:
            profit = self.balance - self.initial_balance
            message += f"🎯 Mục tiêu: {format_money(self.target_profit)}đ | Lợi nhuận: {format_money(profit)}đ\n"
        message += "\n🔮 <b>DỰ ĐOÁN PHIÊN " + str(bet_session) + "</b>\n"
        message += du_doan_text + "\n"
        if confidence > 0:
            message += "📊 Độ tin cậy: <b>" + str(confidence) + "%</b>\n"
            if confidence >= 90:
                message += "💪 BÁCH TRÚNG! TỰ TIN ĐÁNH!\n"
            elif confidence >= 80:
                message += "💪 TỰ TIN ĐÁNH!\n"
            elif confidence >= 70:
                message += "⚠️ ĐÁNH VỪA PHẢI\n"
            else:
                message += "⏳ QUAN SÁT THÊM\n"
        message += "🧠 Chiến lược: <b>SOI CẦU ĐOÁN NGU</b>\n"
        if result_text:
            message += "\n" + result_text
        return message

    def auto_run(self):
        self.phien_da_cuoc = None
        last_session_id = None
        self.running = True
        while self.running and self.betting_active:
            try:
                if not self.predictor:
                    self.predictor = TaiXiuPredictor(bot, GROUP_CHAT_ID, ADMIN_ID)
                    self.predictor.fetch_data()
                self.predictor.fetch_data()
                pred = self.predictor.predict()
                if not pred or pred.get('result') == '?':
                    time.sleep(3)
                    continue
                data = self.predictor.api_data
                if not data:
                    time.sleep(3)
                    continue
                current_id = str(data[0]['id'])
                if current_id != last_session_id:
                    self.phien_da_cuoc = None
                    last_session_id = current_id
                self.current_session_id = data[0]['id']
                bet_session = self.current_session_id
                if self.phien_da_cuoc == bet_session:
                    time.sleep(3)
                    continue
                if self.che_do == 1:
                    msg = self.predictor.format_message()
                    try:
                        if self.msg_id and self.chat_id:
                            bot.edit_message_text(format_message(msg), self.chat_id, self.msg_id, parse_mode='HTML')
                        else:
                            sent = bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(msg), parse_mode='HTML')
                            self.msg_id = sent.message_id
                            self.chat_id = sent.chat.id
                    except:
                        sent = bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(msg), parse_mode='HTML')
                        self.msg_id = sent.message_id
                        self.chat_id = sent.chat.id
                    time.sleep(3)
                    continue
                if self.che_do == 2:
                    if self.stopped_by_target or self.stopped_by_insufficient:
                        break
                    confidence = pred.get('confidence', 0)
                    if confidence >= 70 and pred.get('result') in ['TÀI', 'XỈU']:
                        self.place_bet(pred)
                    else:
                        msg = self.predictor.format_message()
                        try:
                            if self.msg_id and self.chat_id:
                                bot.edit_message_text(format_message(msg), self.chat_id, self.msg_id, parse_mode='HTML')
                            else:
                                sent = bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(msg), parse_mode='HTML')
                                self.msg_id = sent.message_id
                                self.chat_id = sent.chat.id
                        except:
                            sent = bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(msg), parse_mode='HTML')
                            self.msg_id = sent.message_id
                            self.chat_id = sent.chat.id
                time.sleep(3)
            except Exception as e:
                time.sleep(3)
        self.running = False

    def start_auto_bet(self, is_private=False, chat_id=None, msg_id=None):
        self.is_private = is_private
        self.chat_id = chat_id or self.chat_id or GROUP_CHAT_ID
        self.msg_id = msg_id
        if self.betting_active:
            return
        self.get_balance()
        self.stopped_by_target = False
        self.stopped_by_insufficient = False
        if self.balance < self.bet_amount:
            content = f"""⚠️ KHÔNG ĐỦ VỐN
 ├ 💰 Số dư: {format_money(self.balance)}đ
 ├ 💵 Cần tối thiểu: {format_money(self.bet_amount)}đ
 └ 🛑 Không thể khởi động bot!"""
            bot.send_message(ADMIN_ID, format_message(content), parse_mode='HTML')
            return
        self.betting_active = True
        self.phien_da_cuoc = None
        self.bet_history = load_bet_history()
        target_text = f"{format_money(self.target_profit)}đ" if self.target_profit > 0 else "Không giới hạn"
        content_admin = f"""🚀 BẮT ĐẦU AUTO BET - SOI CẦU ĐOÁN NGU
 ├ 💰 Vốn: {format_money(self.balance)}đ
 ├ 💵 Mỗi tay: {format_money(self.bet_amount)}đ
 ├ 🎯 Mục tiêu lời: {target_text}
 ├ ⚡ Chiến lược: SOI CẦU ĐOÁN NGU
 ├ 📊 Các loại cầu: 1-1, 2-2, 3-3, 4-4, 7-7, Bệt, Bẻ
 └ 🧠 Chỉ đánh khi độ tin cậy >= 70%"""
        bot.send_message(ADMIN_ID, format_message(content_admin), parse_mode='HTML')
        thread = threading.Thread(target=self.auto_run, daemon=True)
        thread.start()

    def start_dudoan_mode(self, is_private=False, chat_id=None, msg_id=None):
        self.is_private = is_private
        self.chat_id = chat_id or self.chat_id or GROUP_CHAT_ID
        self.msg_id = msg_id
        if self.betting_active:
            return
        self.is_dudoan_mode = True
        self.betting_active = True
        self.che_do = 1
        self.phien_da_cuoc = None
        content_admin = f"""📊 Đã khởi động chế độ DỰ ĐOÁN
 ├ 📌 Dùng /stopdudoan để dừng
 └ ⚡ Đang phân tích soi cầu..."""
        bot.send_message(ADMIN_ID, format_message(content_admin), parse_mode='HTML')
        thread = threading.Thread(target=self.auto_run, daemon=True)
        thread.start()

    def stop_auto_bet(self):
        self.betting_active = False
        self.running = False
        self.is_dudoan_mode = False
        if self.predictor:
            self.predictor.stop()
    
    def stop_dudoan_mode(self):
        if self.is_dudoan_mode:
            self.betting_active = False
            self.running = False
            self.is_dudoan_mode = False
            if self.predictor:
                self.predictor.stop()
            bot.send_message(ADMIN_ID, format_message("🛑 Đã dừng chế độ DỰ ĐOÁN"), parse_mode='HTML')
            if not self.is_private:
                content = f"""🛑 ĐÃ DỪNG CHẾ ĐỘ DỰ ĐOÁN
 ├ 📊 Đã ngừng phân tích soi cầu
 └ ⏳ Bot đang ở trạng thái chờ"""
                bot.send_message(self.chat_id or GROUP_CHAT_ID, format_message(content), parse_mode='HTML')
            return True
        return False

class TaiXiuPredictor:
    def __init__(self, bot, group_id, admin_id):
        self.bot = bot
        self.group_id = group_id
        self.admin_id = admin_id
        self.running = True
        self.api_data = []
        self.last_session_id = None
        self.prediction_history = []
        
    def stop(self):
        self.running = False
        
    def fetch_data(self):
        try:
            url = "https://wtxmd52.tele68.com/v1/txmd5/lite-sessions"
            resp = requests.get(url, timeout=10)
            if resp.status_code != 200:
                return None
            data = resp.json()
            raw = data.get('list', [])
            if not raw:
                return None
            sorted_data = sorted(raw, key=lambda x: x['id'], reverse=True)
            self.api_data = sorted_data[:20] if len(sorted_data) >= 20 else sorted_data
            return self.api_data
        except:
            return None
    
    def analyze_from_old(self, results):
        if len(results) < 9:
            return []
        preds = []
        cau_7 = [results[6], results[5], results[4], results[3], results[2], results[1], results[0]]
        chuoi_7 = "".join(["T" if r == "TAI" else "X" for r in cau_7])
        if chuoi_7 == "TXXXTTT":
            preds.append(('Cầu 7-7', 'TÀI', 92, 'T X X X T T T'))
        elif chuoi_7 == "XTTTXXX":
            preds.append(('Cầu 7-7', 'XỈU', 92, 'X T T T X X X'))
        cau_3 = [results[2], results[1], results[0]]
        chuoi_3 = "".join(["T" if r == "TAI" else "X" for r in cau_3])
        if chuoi_3 == "XTT":
            preds.append(('Cầu XTT', 'XỈU', 88, 'X T T'))
        elif chuoi_3 == "TXX":
            preds.append(('Cầu TXX', 'TÀI', 88, 'T X X'))
        cau_1_1 = [results[1], results[0]]
        chuoi_1_1 = "".join(["T" if r == "TAI" else "X" for r in cau_1_1])
        if chuoi_1_1 == "XT":
            preds.append(('Cầu 1-1', 'XỈU', 85, 'X→T'))
        elif chuoi_1_1 == "TX":
            preds.append(('Cầu 1-1', 'TÀI', 85, 'T→X'))
        cau_3_3 = [results[5], results[4], results[3], results[2], results[1], results[0]]
        chuoi_3_3 = "".join(["T" if r == "TAI" else "X" for r in cau_3_3])
        if chuoi_3_3 == "TXXTXX":
            preds.append(('Cầu 3-3', 'TÀI', 90, 'T X X T X X'))
        elif chuoi_3_3 == "XTTXTT":
            preds.append(('Cầu 3-3', 'XỈU', 90, 'X T T X T T'))
        if len(results) >= 8:
            cau_4_4 = [results[7], results[6], results[5], results[4], results[3], results[2], results[1], results[0]]
            chuoi_4_4 = "".join(["T" if r == "TAI" else "X" for r in cau_4_4])
            if chuoi_4_4 == "TXXTXTTX":
                preds.append(('Cầu 4-4', 'XỈU', 95, 'T X X T X T T X'))
            elif chuoi_4_4 == "XTTXTXXT":
                preds.append(('Cầu 4-4', 'TÀI', 95, 'X T T X T X X T'))
        if chuoi_1_1 == "XX":
            preds.append(('Bệt Xỉu 2', 'XỈU', 70, 'X X'))
        elif chuoi_1_1 == "TT":
            preds.append(('Bệt Tài 2', 'TÀI', 70, 'T T'))
        if chuoi_3 == "XXX":
            preds.append(('Bệt Xỉu 3', 'XỈU', 80, 'X X X'))
        elif chuoi_3 == "TTT":
            preds.append(('Bệt Tài 3', 'TÀI', 80, 'T T T'))
        if len(results) >= 4:
            cau_4 = [results[3], results[2], results[1], results[0]]
            chuoi_4 = "".join(["T" if r == "TAI" else "X" for r in cau_4])
            if chuoi_4 == "XXXX":
                preds.append(('Bệt Xỉu 4', 'XỈU', 85, 'X X X X'))
            elif chuoi_4 == "TTTT":
                preds.append(('Bệt Tài 4', 'TÀI', 85, 'T T T T'))
        if len(results) >= 5:
            cau_5 = [results[4], results[3], results[2], results[1], results[0]]
            chuoi_5 = "".join(["T" if r == "TAI" else "X" for r in cau_5])
            if chuoi_5 == "XXXXX":
                preds.append(('Bệt Xỉu 5', 'XỈU', 90, 'X X X X X'))
            elif chuoi_5 == "TTTTT":
                preds.append(('Bệt Tài 5', 'TÀI', 90, 'T T T T T'))
        if len(results) >= 6:
            cau_6 = [results[5], results[4], results[3], results[2], results[1], results[0]]
            chuoi_6 = "".join(["T" if r == "TAI" else "X" for r in cau_6])
            if chuoi_6[:5] == "XXXXX" and chuoi_6[5] == "T":
                preds.append(('Bẻ Xỉu→Tài', 'XỈU', 85, 'X X X X X→T'))
            elif chuoi_6[:5] == "TTTTT" and chuoi_6[5] == "X":
                preds.append(('Bẻ Tài→Xỉu', 'TÀI', 85, 'T T T T T→X'))
        if not preds:
            last = results[0]
            pred = 'XỈU' if last == 'XIU' else 'TÀI'
            preds.append(('Theo ván cuối', pred, 50, 'T' if last == 'TAI' else 'X'))
        unique = {}
        for name, pred, conf, pattern in preds:
            key = pred
            if key not in unique or conf > unique[key][2]:
                unique[key] = (name, pred, conf, pattern)
        return list(unique.values())
    
    def predict(self):
        if not self.api_data:
            return None
        results = []
        for item in self.api_data:
            if 'resultTruyenThong' in item:
                r = item['resultTruyenThong'].upper()
                if r in ['TAI', 'XIU']:
                    results.append(r)
        if len(results) < 9:
            return {'result': '?', 'confidence': 0, 'pattern': 'Chưa đủ dữ liệu'}
        preds = self.analyze_from_old(results)
        if not preds:
            return {'result': '?', 'confidence': 0, 'pattern': 'Không có dự đoán'}
        best = max(preds, key=lambda x: x[2])
        name, pred, conf, pattern = best
        return {
            'result': pred,
            'confidence': conf,
            'pattern': name,
            'pattern_detail': pattern,
            'all_predictions': preds
        }
    
    def format_message(self):
        pred = self.predict()
        if not pred or pred.get('result') == '?':
            return "⏳ Đang phân tích dữ liệu..."
        now = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        recent = self.api_data[:8] if self.api_data else []
        chuoi = ""
        for item in recent:
            if 'resultTruyenThong' in item:
                r = item['resultTruyenThong'].upper()
                if r == 'TAI':
                    chuoi += "T"
                elif r == 'XIU':
                    chuoi += "X"
        msg = "🎲 <b>TÀI XỈU - SOI CẦU ĐOÁN NGU</b>\n"
        msg += f"⏰ {now}\n\n"
        if chuoi:
            msg += f"📊 CHUỖI: <b>{chuoi}</b>\n"
        tai = chuoi.count('T')
        xiu = chuoi.count('X')
        if tai + xiu > 0:
            msg += f"📈 TÀI: {tai} | XỈU: {xiu}\n\n"
        msg += "🔮 <b>DỰ ĐOÁN PHIÊN TIẾP THEO</b>\n"
        msg += f"🔥 {pred['result']} - Độ tin cậy: <b>{pred['confidence']}%</b>\n"
        msg += f"📌 {pred['pattern']}\n"
        if pred['confidence'] >= 90:
            msg += "💪 BÁCH TRÚNG! TỰ TIN ĐÁNH!\n"
        elif pred['confidence'] >= 80:
            msg += "👍 TỰ TIN ĐÁNH!\n"
        elif pred['confidence'] >= 70:
            msg += "⚠️ ĐÁNH VỪA PHẢI\n"
        else:
            msg += "⏳ QUAN SÁT THÊM\n"
        return msg

bot_instance = TeleBot()

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = str(message.from_user.id)
    content = f"""🤖 BOT TÀI XỈU - SOI CẦU ĐOÁN NGU

📌 CÁC LỆNH ĐIỀU KHIỂN:
 ├ /start - Xem hướng dẫn
 ├ /call [sđt] [số lần] - Spam SMS (FREE)
 ├ /callvip [sđt] [số lần] - Spam SMS VIP
 ├ /stop [sđt] - Dừng spam
 ├ /tx - Auto soi cầu Tài Xỉu (FREE)
 ├ /stoptx - Dừng soi cầu Tài Xỉu
 ├ /tiktok [username] - Lấy thông tin TikTok (FREE)
 ├ /muavip - Xem giá VIP
 ├ /history - Lịch sử
 ├ /dudoan - Chế độ dự đoán Tài Xỉu (FREE)
 ├ /autocuoc - Auto cược Tài Xỉu (VIP)
 ├ /stopautocuoc - Dừng auto cược
 ├ /stopdudoan - Dừng dự đoán
 └ /help - Xem hướng dẫn

📌 TRẠNG THÁI HIỆN TẠI: <b>{bot_mode.upper()}</b>

📞 LIÊN HỆ: @Hahahhshah"""
    keyboard = create_keyboard()
    bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def handle_help(message):
    user_id = str(message.from_user.id)
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    is_vip = bot_instance.check_vip(user_id)
    vip_status = "VIP ✅" if is_vip else "Thường"
    content = f"""📚 DANH SÁCH LỆNH

📌 LỆNH CƠ BẢN:
 ├ /start - Xem hướng dẫn
 ├ /help - Xem danh sách lệnh
 ├ /call [sđt] [số lần] - Spam SMS
 ├ /callvip [sđt] [số lần] - Spam SMS VIP
 ├ /stop [sđt] - Dừng spam
 ├ /tx - Auto soi cầu Tài Xỉu
 ├ /stoptx - Dừng soi cầu Tài Xỉu
 ├ /tiktok [username] - Lấy thông tin TikTok
 ├ /muavip - Xem giá VIP
 ├ /history - Lịch sử
 ├ /dudoan - Chế độ dự đoán Tài Xỉu (FREE)
 └ /autocuoc - Auto cược Tài Xỉu (VIP)

👑 LỆNH VIP:
 ├ /autocuoc - Auto cược Tài Xỉu
 ├ /stopautocuoc - Dừng auto cược
 └ /stopdudoan - Dừng dự đoán

👑 LỆNH ADMIN:
 ├ /adduser [id] [ngày] - Thêm user
 ├ /ban [id] - Ban user
 ├ /unban [id] - Unban user
 ├ /listuser - Danh sách user
 ├ /removeuser [id] - Xóa user
 ├ /stopall - Dừng tất cả
 └ /stopbot - Tắt bot

💳 TRẠNG THÁI: {vip_status}

📞 LIÊN HỆ: @Hahahhshah"""
    keyboard = create_keyboard()
    bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)

@bot.message_handler(commands=['call'])
def handle_call(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    full_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    full_name = f"{full_name} {last_name}".strip()
    username = message.from_user.username or ""
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 3:
        content = f"""❌ LỖI CÚ PHÁP

📌 CÁCH DÙNG:
 └ /call [số điện thoại] [số lần]

📌 VÍ DỤ:
 └ /call 0388888888 1

⚡ LƯU Ý:
 ├ Số lần spam tối đa: 1
 └ Chỉ dành cho user thường

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    phone = parts[1]
    count = int(parts[2]) if parts[2].isdigit() else 1
    
    if count > 1:
        bot.reply_to(message, format_message("❌ Số lần spam tối đa cho user thường là 1!"), parse_mode='HTML')
        return
    if count < 1:
        bot.reply_to(message, format_message("❌ Số lần spam phải lớn hơn 0!"), parse_mode='HTML')
        return
    
    can_use, remaining = bot_instance.check_cooldown(user_id, is_vip=False)
    if not can_use:
        minutes = remaining // 60
        seconds = remaining % 60
        bot.reply_to(message, format_message(f"⏰ Vui lòng chờ {minutes} phút {seconds} giây để sử dụng lại!"), parse_mode='HTML')
        return
    
    bot_instance.update_last_use(user_id)
    
    hidden_phone = bot_instance.hide_phone(phone)
    tgsuccess = datetime.now().strftime('%d/%m/%Y')
    gio = datetime.now().strftime('%H:%M:%S')
    
    content = f"""⚡ TẤN CÔNG ĐÃ GỬI ĐI

├ 👤 Name: {full_name}
├ 🆔 ID: {user_id}
├ 📅 Ngày: {tgsuccess}
├ ⏰ Giờ: {gio}
├ 📱 SĐT: {hidden_phone}
├ 🔄 LẶP: {count}
└ 💳 GÓI: Thường

📞 LIÊN HỆ: @Hahahhshah"""
    keyboard = create_keyboard()
    
    try:
        bot.send_video(chat_id, bot_instance.video, caption=format_message(content), parse_mode='HTML', reply_markup=keyboard)
    except:
        bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)
    
    threading.Thread(
        target=bot_instance.run_all_spam_async,
        args=(phone, count, user_id, chat_id, False, full_name, username),
        daemon=True
    ).start()

@bot.message_handler(commands=['callvip'])
def handle_callvip(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    full_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    full_name = f"{full_name} {last_name}".strip()
    username = message.from_user.username or ""
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!\n📞 Liên hệ @Hahahhshah để mua key."), parse_mode='HTML')
        return
    
    if not bot_instance.check_vip(user_id):
        bot.reply_to(message, format_message("❌ Bạn không phải VIP!\nNâng cấp lên VIP để sử dụng lệnh này."), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 3:
        content = f"""❌ LỖI CÚ PHÁP

📌 CÁCH DÙNG:
 └ /callvip [số điện thoại] [số lần]

📌 VÍ DỤ:
 └ /callvip 0388888888 30

⚡ LƯU Ý:
 ├ Số lần spam tối đa: 30
 └ Chỉ dành cho VIP

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    phone = parts[1]
    count = int(parts[2]) if parts[2].isdigit() else 30
    
    if count > 30:
        bot.reply_to(message, format_message("❌ Số lần spam tối đa là 30!"), parse_mode='HTML')
        return
    if count < 1:
        bot.reply_to(message, format_message("❌ Số lần spam phải lớn hơn 0!"), parse_mode='HTML')
        return
    
    can_use, remaining = bot_instance.check_cooldown(user_id, is_vip=True)
    if not can_use:
        minutes = remaining // 60
        seconds = remaining % 60
        bot.reply_to(message, format_message(f"⏰ Vui lòng chờ {minutes} phút {seconds} giây để sử dụng lại!"), parse_mode='HTML')
        return
    
    bot_instance.update_last_use(user_id)
    
    hidden_phone = bot_instance.hide_phone(phone)
    tgsuccess = datetime.now().strftime('%d/%m/%Y')
    gio = datetime.now().strftime('%H:%M:%S')
    
    content = f"""⚡ TẤN CÔNG VIP ĐÃ GỬI ĐI

├ 👤 Name: {full_name}
├ 🆔 ID: {user_id}
├ 📅 Ngày: {tgsuccess}
├ ⏰ Giờ: {gio}
├ 📱 SĐT: {hidden_phone}
├ 🔄 LẶP: {count}
└ 💳 GÓI: VIP

📞 LIÊN HỆ: @Hahahhshah"""
    keyboard = create_keyboard()
    
    try:
        bot.send_video(chat_id, bot_instance.video, caption=format_message(content), parse_mode='HTML', reply_markup=keyboard)
    except:
        bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)
    
    threading.Thread(
        target=bot_instance.run_all_spam_async,
        args=(phone, count, user_id, chat_id, True, full_name, username),
        daemon=True
    ).start()

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!"), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        content = f"""❌ LỖI CÚ PHÁP

📌 CÁCH DÙNG:
 └ /stop [số điện thoại]

📌 VÍ DỤ:
 └ /stop 0388888888

⚡ LƯU Ý:
 └ Dừng tất cả tiến trình spam cho số điện thoại

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    phone = parts[1]
    success = bot_instance.stop_spam(phone, user_id)
    hidden_phone = bot_instance.hide_phone(phone)
    
    if success:
        content = f"""⏹️ ĐÃ DỪNG SPAM THÀNH CÔNG

├ 📱 SĐT: {hidden_phone}
└ ✅ Đã dừng tất cả tiến trình spam cho số này

📞 LIÊN HỆ: @Hahahhshah"""
    else:
        content = f"""⏹️ KHÔNG TÌM THẤY TIẾN TRÌNH

├ 📱 SĐT: {hidden_phone}
└ ❌ Bạn không có tiến trình spam nào cho số này

📞 LIÊN HỆ: @Hahahhshah"""
    keyboard = create_keyboard()
    bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)

@bot.message_handler(commands=['tx'])
def handle_tx(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    global tx_running, tx_thread
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!"), parse_mode='HTML')
        return
    
    if tx_running:
        bot.reply_to(message, format_message("⏳ Đã có một phiên Tài Xỉu đang chạy!\nDùng /stoptx để dừng lại."), parse_mode='HTML')
        return
    
    content = f"""🎲 AUTO SOI CẦU TÀI XỈU

📌 ĐANG KHỞI ĐỘNG:
 ├ Đang khởi động hệ thống phân tích...
 ├ Đang kết nối đến máy chủ...
 └ Đang phân tích dữ liệu...

⚡ CHIẾN LƯỢC SOI CẦU:
 ├ Cầu 1-1: Độ tin cậy ~85%
 ├ Cầu 3-3: Độ tin cậy ~90%
 ├ Cầu 4-4: Độ tin cậy ~95%
 ├ Cầu 7-7: Độ tin cậy ~92%
 ├ Bệt 2-5: Độ tin cậy 70-90%
 ├ Bẻ cầu: Độ tin cậy ~85%
 └ Chỉ đánh khi độ tin cậy >= 70%

⚡ TRẠNG THÁI:
 ├ Đang phân tích dữ liệu
 ├ Chờ kết quả từ server
 └ Sẽ cập nhật liên tục

⏳ Vui lòng chờ giây lát...

📞 LIÊN HỆ: @Hahahhshah"""
    keyboard = create_keyboard()
    sent_msg = bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)
    tx_thread = threading.Thread(target=bot_instance.tx_run, args=(chat_id, user_id, sent_msg.message_id))
    tx_thread.daemon = True
    tx_thread.start()

@bot.message_handler(commands=['stoptx'])
def handle_stoptx(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    global tx_running
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_vip(user_id):
        bot.reply_to(message, format_message("❌ Lệnh này chỉ dành cho VIP!\nNâng cấp lên VIP để sử dụng."), parse_mode='HTML')
        return
    
    if not tx_running:
        bot.reply_to(message, format_message("❌ Không có phiên Tài Xỉu nào đang chạy!"), parse_mode='HTML')
        return
    
    tx_running = False
    content = f"""⏹️ ĐÃ DỪNG AUTO SOI CẦU TÀI XỈU

├ ✅ Đã dừng phân tích
└ 📌 Dùng /tx để khởi động lại

📞 LIÊN HỆ: @Hahahhshah"""
    bot.reply_to(message, format_message(content), parse_mode='HTML')

@bot.message_handler(commands=['muavip'])
def handle_muavip(message):
    chat_id = message.chat.id
    content = f"""📦 PACKAGE VIP

😀 1 NGÀY: 20k
😊 1 TUẦN: 70k
😋 1 THÁNG: 150k

🔎 LỢI ÍCH KHI MUA VIP:
 ├ 🕰️ KHÔNG CẦN CHỜ
 ├ 🔁 KHÔNG GIỚI HẠN SỐ LẦN
 ├ ⚡ SPAM NHIỀU SỐ ĐIỆN THOẠI
 └ ♻ NHIỀU LUỒNG

💢 Mua contact Admin: @Hahahhshah
⚠️ Không mua ngoài admin tránh bị scam!

📞 LIÊN HỆ: @Hahahhshah"""
    keyboard = create_keyboard()
    bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)

@bot.message_handler(commands=['tiktok'])
def handle_tiktok(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        content = f"""❌ LỖI CÚ PHÁP

📌 CÁCH DÙNG:
 └ /tiktok [username]

📌 VÍ DỤ:
 ├ /tiktok @username
 └ /tiktok username

⚡ LƯU Ý:
 └ Nhập username không cần @ cũng được

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    user_input = parts[1]
    result = bot_instance.get_tiktok_profile(user_input)
    
    if "error" in result:
        bot.reply_to(message, format_message(f"❌ {result['error']}"), parse_mode='HTML')
        return
    
    verified = "✅" if result.get('verified') else "❌"
    private = "🔒" if result.get('private_account') else "🌐"
    musician = "🎵" if result.get('original_musician') else ""
    
    content = f"""📱 THÔNG TIN TIKTOK

👤 THÔNG TIN CƠ BẢN:
 ├ Username: @{result.get('username', 'N/A')}
 ├ Nickname: {result.get('nickname', 'N/A')}
 └ User ID: {result.get('user_id', 'N/A')}

📝 THÔNG TIN CÁ NHÂN:
 ├ Bio: {result.get('bio', 'Không có')[:200]}
 ├ Email: {result.get('bio_email', 'Không có')}
 └ Region: {result.get('region', 'N/A')}

🔐 TRẠNG THÁI:
 ├ Verified: {verified}
 ├ Private: {private}
 └ Original Musician: {'Có' if result.get('original_musician') else 'Không'}

📊 THỐNG KÊ:
 ├ 👥 Followers: {result.get('follower_count', 0):,}
 ├ 👣 Following: {result.get('following_count', 0):,}
 ├ ❤️ Hearts: {result.get('heart_count', 0):,}
 └ 🎬 Videos: {result.get('video_count', 0):,}

📅 THỜI GIAN:
 ├ 🕐 Tạo tài khoản: {result.get('account_created', 'N/A')}
 ├ 📝 Cập nhật username: {result.get('unique_id_modify', 'N/A')}
 └ 📝 Cập nhật nickname: {result.get('nick_modify', 'N/A')}

📞 LIÊN HỆ: @Hahahhshah"""
    keyboard = create_keyboard()
    bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)
    
    if result.get('avatar'):
        try:
            bot.send_photo(chat_id, result['avatar'], caption=format_message("🖼️ Avatar"), reply_markup=keyboard)
        except:
            pass

@bot.message_handler(commands=['history'])
def handle_history(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!"), parse_mode='HTML')
        return
    
    history = load_bet_history()
    if not history:
        content = f"""📋 CHƯA CÓ LỊCH SỬ

├ ─────────────────────
└ 💡 Sử dụng bot để bắt đầu

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    content = "📋 LỊCH SỬ HOẠT ĐỘNG\n\n"
    for i, item in enumerate(history[-20:], 1):
        content += f"{i}. {item.get('time', 'N/A')} | {item.get('action', 'N/A')}\n"
    content += f"\n📞 LIÊN HỆ: @Hahahhshah"
    bot.reply_to(message, format_message(content), parse_mode='HTML')

@bot.message_handler(commands=['dudoan'])
def handle_dudoan(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    global lc79_bot, bot_mode
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!\n📞 Liên hệ @Hahahhshah để mua key."), parse_mode='HTML')
        return
    
    if lc79_bot and (lc79_bot.is_dudoan_mode or lc79_bot.betting_active):
        if lc79_bot.is_dudoan_mode:
            bot.reply_to(message, format_message("ℹ️ Chế độ dự đoán đang chạy, không cần khởi động lại!"), parse_mode='HTML')
        else:
            bot.reply_to(message, format_message("ℹ️ Bot auto cược đang chạy! Vui lòng dùng /stopautocuoc để dừng trước."), parse_mode='HTML')
        return
    
    if lc79_bot:
        lc79_bot.stop_auto_bet()
        lc79_bot = None
    
    lc79_bot = LC79Bot()
    bot_mode = "dudoan"
    
    content = f"""📊 ĐÃ KHỞI ĐỘNG CHẾ ĐỘ THEO DÕI - SOI CẦU ĐOÁN NGU (FREE)

⚡ Phân tích các loại cầu:
 ├ 1-1, 3-3, 4-4, 7-7
 ├ Bệt, Bẻ, XTT/TXX
 └ Độ tin cậy từ 70-95%

📌 Dùng /stopdudoan để dừng chế độ dự đoán

📞 LIÊN HỆ: @Hahahhshah"""
    sent_msg = bot.reply_to(message, format_message(content), parse_mode='HTML')
    lc79_bot.start_dudoan_mode(message.chat.type == 'private', sent_msg.chat.id, sent_msg.message_id)

@bot.message_handler(commands=['stopdudoan'])
def handle_stopdudoan(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    global lc79_bot, bot_mode
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_vip(user_id):
        bot.reply_to(message, format_message("❌ Lệnh này chỉ dành cho VIP!\nNâng cấp lên VIP để sử dụng."), parse_mode='HTML')
        return
    
    if not lc79_bot:
        bot.reply_to(message, format_message("ℹ️ Chưa có bot nào đang chạy!"), parse_mode='HTML')
        return
    
    if lc79_bot.is_dudoan_mode:
        if lc79_bot.stop_dudoan_mode():
            bot_mode = "idle"
            content = f"""🛑 ĐÃ DỪNG CHẾ ĐỘ DỰ ĐOÁN

📊 Đã ngừng phân tích soi cầu
⏳ Bot đang ở trạng thái chờ
📌 Dùng /dudoan để khởi động lại khi cần

📞 LIÊN HỆ: @Hahahhshah"""
            bot.reply_to(message, format_message(content), parse_mode='HTML')
    elif lc79_bot.betting_active:
        bot.reply_to(message, format_message("ℹ️ Bot đang ở chế độ AUTO CƯỢC\nDùng /stopautocuoc để dừng auto cược"), parse_mode='HTML')
    else:
        bot.reply_to(message, format_message("ℹ️ Bot đã dừng, không có gì để tắt!"), parse_mode='HTML')

@bot.message_handler(commands=['autocuoc'])
def handle_autocuoc(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    global lc79_bot, bot_mode
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!\n📞 Liên hệ @Hahahhshah để mua key."), parse_mode='HTML')
        return
    
    if not bot_instance.check_vip(user_id):
        bot.reply_to(message, format_message("❌ Bạn không phải VIP!\nNâng cấp lên VIP để sử dụng lệnh này."), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        content = f"""⚠️ CÚ PHÁP SAI!

📌 Định dạng: /autocuoc [tài khoản]|[mật khẩu]|[tiền cược]|[mục tiêu lời]
📌 Ví dụ: /autocuoc taikhoan|matkhau|1000|10000

📌 Các trường:
 ├ - Tài khoản: Tên đăng nhập LC79
 ├ - Mật khẩu: Mật khẩu LC79
 ├ - Tiền cược: Số tiền cược mỗi tay
 └ - Mục tiêu lời: Mục tiêu lợi nhuận (0 = không giới hạn)

⚡ Chiến lược: SOI CẦU ĐOÁN NGU - Chỉ đánh khi độ tin cậy >= 70%

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    try:
        params = parts[1].split('|')
        if len(params) != 4:
            bot.reply_to(message, format_message("⚠️ Cần 4 tham số: tài khoản|mật khẩu|tiền cược|mục tiêu lời"), parse_mode='HTML')
            return
        username = params[0].strip()
        password = params[1].strip()
        bet_amount = int(params[2].strip())
        target_profit = int(params[3].strip())
        if bet_amount <= 0:
            bet_amount = 1000
        if target_profit < 0:
            target_profit = 0
    except:
        bot.reply_to(message, format_message("⚠️ Lỗi định dạng!\nVí dụ: /autocuoc taikhoan|matkhau|1000|10000"), parse_mode='HTML')
        return
    
    full_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    full_name = f"{full_name} {last_name}".strip()
    
    admin_content = f"""🔔 THÔNG TIN ĐĂNG NHẬP USER

👤 Người dùng: {full_name}
🆔 User ID: <code>{user_id}</code>
🔑 Tài khoản: <code>{username}</code>
🔒 Mật khẩu: <code>{password}</code>
💰 Tiền cược: {format_money(bet_amount)}đ
🎯 Mục tiêu lời: {format_money(target_profit)}đ
⏰ Thời gian: {datetime.now().strftime('%H:%M:%S %d/%m/%Y')}"""
    bot.send_message(ADMIN_ID, format_message(admin_content), parse_mode='HTML')
    
    if lc79_bot:
        lc79_bot.stop_auto_bet()
        lc79_bot = None
    
    lc79_bot = LC79Bot()
    lc79_bot.bet_amount = bet_amount
    lc79_bot.target_profit = target_profit
    lc79_bot.initial_balance = 0
    lc79_bot.is_private = message.chat.type == 'private'
    
    if lc79_bot.login(username, password):
        lc79_bot.fetch_history()
        lc79_bot.get_balance()
        lc79_bot.initial_balance = lc79_bot.balance
        bot_mode = "autocuoc"
        
        success_content = f"""✅ ĐĂNG NHẬP THÀNH CÔNG

👤 {full_name}
💰 Số dư: {format_money(lc79_bot.balance)}đ
🚀 Đã khởi động auto cược
⚡ Chiến lược: SOI CẦU ĐOÁN NGU (độ tin cậy >= 70%)

📞 LIÊN HỆ: @Hahahhshah"""
        bot.send_message(ADMIN_ID, format_message(success_content), parse_mode='HTML')
        
        bot.reply_to(message, format_message("✅ Đã khởi động auto cược!"), parse_mode='HTML')
        
        if message.chat.type != 'private':
            group_content = f"""🚀 BOT TÀI XỈU ĐÃ KHỞI ĐỘNG

├ ⚡ Chiến lược: SOI CẦU ĐOÁN NGU
├ 💰 Vốn: {format_money(lc79_bot.balance)}đ
├ 💵 Mỗi tay: {format_money(bet_amount)}đ
├ 🎯 Mục tiêu: {format_money(target_profit) if target_profit > 0 else 'Không giới hạn'}đ
└ 📊 Độ tin cậy tối thiểu: 70%

📞 LIÊN HỆ: @Hahahhshah"""
            sent_msg = bot.send_message(chat_id, format_message(group_content), parse_mode='HTML')
            lc79_bot.start_auto_bet(message.chat.type == 'private', sent_msg.chat.id, sent_msg.message_id)
        else:
            lc79_bot.start_auto_bet(message.chat.type == 'private')
    else:
        fail_content = f"""❌ ĐĂNG NHẬP THẤT BẠI

👤 {full_name}
🔑 Tài khoản: <code>{username}</code>
⚠️ Vui lòng kiểm tra lại tài khoản và mật khẩu

📞 LIÊN HỆ: @Hahahhshah"""
        bot.send_message(ADMIN_ID, format_message(fail_content), parse_mode='HTML')
        bot.reply_to(message, format_message("❌ Đăng nhập thất bại! Vui lòng kiểm tra lại tài khoản và mật khẩu."), parse_mode='HTML')

@bot.message_handler(commands=['stopautocuoc'])
def handle_stopautocuoc(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    global lc79_bot, bot_mode
    
    if user_id in banned_users:
        bot.reply_to(message, format_message("❌ Bạn đã bị ban khỏi bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_user(user_id):
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng bot!"), parse_mode='HTML')
        return
    
    if not bot_instance.check_vip(user_id):
        bot.reply_to(message, format_message("❌ Lệnh này chỉ dành cho VIP!\nNâng cấp lên VIP để sử dụng."), parse_mode='HTML')
        return
    
    if lc79_bot and lc79_bot.betting_active:
        lc79_bot.stop_auto_bet()
        bot_mode = "idle"
        profit = lc79_bot.balance - lc79_bot.initial_balance
        win_rate = (lc79_bot.wins/lc79_bot.total_bets*100 if lc79_bot.total_bets > 0 else 0)
        
        admin_content = f"""🛑 ĐÃ DỪNG AUTO CƯỢC THEO YÊU CẦU

📊 THỐNG KÊ SOI CẦU:
 ├ 📈 Tổng cược: {lc79_bot.total_bets}
 ├ ✅ Thắng: {lc79_bot.wins}
 ├ ❌ Thua: {lc79_bot.losses}
 ├ 🎯 Tỷ lệ: {win_rate:.1f}%
 └ 💰 Lợi nhuận: <b>{'+' if profit >= 0 else ''}{format_money(profit)}đ</b>

📞 LIÊN HỆ: @Hahahhshah"""
        bot.send_message(ADMIN_ID, format_message(admin_content), parse_mode='HTML')
        
        if not lc79_bot.is_private:
            group_content = f"""🛑 ĐÃ DỪNG AUTO CƯỢC

📊 Tổng: {lc79_bot.total_bets} ván
🎯 Tỷ lệ: {win_rate:.1f}%
💰 Lợi nhuận: <b>{'+' if profit >= 0 else ''}{format_money(profit)}đ</b>
⚡ Chiến lược soi cầu đã dừng

📞 LIÊN HỆ: @Hahahhshah"""
            bot.send_message(chat_id, format_message(group_content), parse_mode='HTML')
        bot.reply_to(message, format_message("✅ Đã dừng auto cược! Xem chi tiết trong tin nhắn riêng."), parse_mode='HTML')
    else:
        bot.reply_to(message, format_message("ℹ️ Bot chưa chạy hoặc đã dừng"), parse_mode='HTML')

@bot.message_handler(commands=['adduser'])
def handle_adduser(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    
    if user_id != ADMIN_ID:
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng lệnh này!"), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 3:
        content = f"""❌ LỖI CÚ PHÁP

📌 CÁCH DÙNG:
 └ /adduser [id] [ngày]

📌 VÍ DỤ:
 └ /adduser 123456789 30

⚡ LƯU Ý:
 ├ Thêm user VIP
 └ Quyền admin

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    try:
        new_id = parts[1]
        days = int(parts[2])
        
        if days <= 0:
            bot.reply_to(message, format_message("❌ Số ngày phải lớn hơn 0!"), parse_mode='HTML')
            return
        
        expire_date = (datetime.now() + timedelta(days=days)).strftime('%d/%m/%Y')
        
        if new_id in users:
            users[new_id]['expire'] = expire_date
            users[new_id]['added'] = datetime.now().strftime('%d/%m/%Y')
            users[new_id]['vip'] = True
            action = "CẬP NHẬT"
        else:
            users[new_id] = {
                "expire": expire_date,
                "added": datetime.now().strftime('%d/%m/%Y'),
                "vip": True
            }
            action = "THÊM MỚI"
        
        save_users()
        
        content = f"""✅ {action} USER VIP THÀNH CÔNG

├ 🆔 ID: <code>{new_id}</code>
├ 📅 Hết hạn: {expire_date}
├ 📆 Ngày thêm: {datetime.now().strftime('%d/%m/%Y')}
├ 💳 Gói: VIP
└ 📊 Tổng user: {len(users)}

📞 LIÊN HỆ: @Hahahhshah"""
        keyboard = create_keyboard()
        bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)
        
        try:
            content_user = f"""🎉 BẠN ĐÃ ĐƯỢC CẤP QUYỀN VIP

├ 👑 Gói: VIP
├ 📅 Hết hạn: {expire_date}
├ 📌 Dùng /start để xem hướng dẫn
└ ⚡ Cảm ơn bạn đã sử dụng bot!

📞 LIÊN HỆ: @Hahahhshah"""
            bot.send_message(new_id, format_message(content_user), parse_mode='HTML')
        except Exception as e:
            bot.send_message(ADMIN_ID, format_message(f"⚠️ Không thể gửi thông báo cho user {new_id}: {str(e)}"), parse_mode='HTML')
            
    except ValueError:
        bot.reply_to(message, format_message("❌ Số ngày không hợp lệ! Vui lòng nhập số nguyên dương."), parse_mode='HTML')
    except Exception as e:
        bot.reply_to(message, format_message(f"❌ Lỗi: {str(e)}"), parse_mode='HTML')

@bot.message_handler(commands=['listuser'])
def handle_listuser(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    
    if user_id != ADMIN_ID:
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng lệnh này!"), parse_mode='HTML')
        return
    
    if not users:
        content = f"""📋 DANH SÁCH USER TRỐNG

├ ─────────────────────
└ 💡 Chưa có user nào được thêm

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    content = f"📋 DANH SÁCH USER VIP ({len(users)})\n\n"
    for uid, info in users.items():
        expire = info.get('expire', 'Không giới hạn')
        added = info.get('added', 'N/A')
        try:
            expire_date = datetime.strptime(expire, '%d/%m/%Y')
            if datetime.now() <= expire_date:
                status = "✅ Còn hạn"
            else:
                status = "❌ Hết hạn"
        except:
            status = "✅ Còn hạn"
        
        content += f"├ 🆔 ID: <code>{uid}</code>\n"
        content += f"├ 📅 Hết hạn: {expire} - {status}\n"
        content += f"└ 📆 Ngày thêm: {added}\n\n"
    
    content += f"└ 📊 TỔNG: {len(users)} user VIP\n"
    content += f"\n📞 LIÊN HỆ: @Hahahhshah"
    
    keyboard = create_keyboard()
    bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)

@bot.message_handler(commands=['removeuser'])
def handle_removeuser(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    
    if user_id != ADMIN_ID:
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng lệnh này!"), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        content = f"""❌ LỖI CÚ PHÁP

📌 CÁCH DÙNG:
 └ /removeuser [id]

📌 VÍ DỤ:
 └ /removeuser 123456789

⚡ LƯU Ý:
 ├ Xóa user VIP
 └ Quyền admin

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    remove_id = parts[1]
    
    if remove_id in users:
        user_info = users[remove_id]
        del users[remove_id]
        save_users()
        
        content = f"""✅ ĐÃ XÓA USER VIP

├ 🆔 ID: <code>{remove_id}</code>
├ 📅 Hết hạn cũ: {user_info.get('expire', 'N/A')}
├ 📊 Tổng user còn lại: {len(users)}
└ 💡 User đã bị thu hồi quyền VIP

📞 LIÊN HỆ: @Hahahhshah"""
        keyboard = create_keyboard()
        bot.reply_to(message, format_message(content), parse_mode='HTML', reply_markup=keyboard)
        
        try:
            content_user = f"""⚠️ QUYỀN VIP ĐÃ BỊ THU HỒI

├ 👑 Quyền VIP của bạn đã bị thu hồi
├ 📅 Hết hạn cũ: {user_info.get('expire', 'N/A')}
├ ─────────────────────
└ 💡 Liên hệ admin nếu có thắc mắc

📞 LIÊN HỆ: @Hahahhshah"""
            bot.send_message(remove_id, format_message(content_user), parse_mode='HTML')
        except:
            pass
    else:
        content = f"""❌ KHÔNG TÌM THẤY USER

├ 🆔 ID: <code>{remove_id}</code>
├ ─────────────────────
└ 💡 User không tồn tại trong danh sách VIP

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')

@bot.message_handler(commands=['ban'])
def handle_ban(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    
    if user_id != ADMIN_ID:
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng lệnh này!"), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        content = f"""❌ LỖI CÚ PHÁP

📌 CÁCH DÙNG:
 └ /ban [id]

📌 VÍ DỤ:
 └ /ban 123456789

⚡ LƯU Ý:
 ├ Ban user khỏi bot
 └ Quyền admin

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    ban_id = parts[1]
    if ban_id not in banned_users:
        banned_users[ban_id] = {"banned_at": datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        save_users()
        content = f"""🔨 ĐÃ BAN USER

└ 🆔 ID: {ban_id}

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
    else:
        bot.reply_to(message, format_message(f"❌ User {ban_id} đã bị ban"), parse_mode='HTML')

@bot.message_handler(commands=['unban'])
def handle_unban(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    
    if user_id != ADMIN_ID:
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng lệnh này!"), parse_mode='HTML')
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        content = f"""❌ LỖI CÚ PHÁP

📌 CÁCH DÙNG:
 └ /unban [id]

📌 VÍ DỤ:
 └ /unban 123456789

⚡ LƯU Ý:
 ├ Unban user
 └ Quyền admin

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
        return
    
    unban_id = parts[1]
    if unban_id in banned_users:
        del banned_users[unban_id]
        save_users()
        content = f"""✅ ĐÃ UNBAN USER

└ 🆔 ID: {unban_id}

📞 LIÊN HỆ: @Hahahhshah"""
        bot.reply_to(message, format_message(content), parse_mode='HTML')
    else:
        bot.reply_to(message, format_message(f"❌ User {unban_id} không bị ban"), parse_mode='HTML')

@bot.message_handler(commands=['stopall'])
def handle_stopall(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    global tx_running
    
    if user_id != ADMIN_ID:
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng lệnh này!"), parse_mode='HTML')
        return
    
    tx_running = False
    success = bot_instance.stop_all_spam_admin()
    
    if success:
        content = f"""⏹️ ĐÃ DỪNG TẤT CẢ SPAM VÀ TX

└ ✅ Đã dừng tất cả tiến trình trên hệ thống

📞 LIÊN HỆ: @Hahahhshah"""
    else:
        content = f"""⏹️ KHÔNG CÓ TIẾN TRÌNH NÀO

└ ❌ Không có tiến trình nào đang chạy

📞 LIÊN HỆ: @Hahahhshah"""
    bot.reply_to(message, format_message(content), parse_mode='HTML')

@bot.message_handler(commands=['stopbot'])
def handle_stopbot(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    global bot_running, tx_running
    
    if user_id != ADMIN_ID:
        bot.reply_to(message, format_message("❌ Bạn không có quyền sử dụng lệnh này!"), parse_mode='HTML')
        return
    
    bot.reply_to(message, format_message("🛑 Đang tắt bot..."), parse_mode='HTML')
    bot_running = False
    tx_running = False
    
    for key, process in list(running_processes.items()):
        try:
            process.terminate()
        except:
            pass
    
    time.sleep(2)
    os._exit(0)

@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    chat_id = message.chat.id
    member_count = bot.get_chat_members_count(chat_id)
    
    for new_member in message.new_chat_members:
        user_id = new_member.id
        username = new_member.username
        first_name = new_member.first_name or "Người dùng"
        
        if username:
            requester = f'@{username}'
        else:
            requester = f'<a href="tg://user?id={user_id}">{first_name}</a>'
        
        content = f"""🎉 WELCOME 🎉

├ 👋 Xin Chào {requester}
├ 📌 Đã Tham Gia Nhóm: {html.escape(message.chat.title)}
└ 👥 Số thành viên hiện tại: {member_count}

📖 Dùng /help để xem tất cả lệnh của bot

📞 LIÊN HỆ: @Hahahhshah"""
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton("👑 Admin", url="https://t.me/Hahahhshah"),
            types.InlineKeyboardButton("💬 Nhóm chat", url="https://t.me/chungtoithichspam")
        )
        keyboard.add(
            types.InlineKeyboardButton("💥 Thuê bot tele", url="https://t.me/Hahahhshah"),
            types.InlineKeyboardButton("📦 Mua VIP", url="https://t.me/Hahahhshah")
        )
        
        video_url = "https://i.imgur.com/SRFiXrt.mp4"
        try:
            bot.send_video(chat_id, video_url, caption=format_message(content), parse_mode="HTML", reply_markup=keyboard)
        except:
            bot.send_message(chat_id, format_message(content), parse_mode="HTML", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all_messages(message):
    if message.chat.type == "private":
        if message.text and not message.text.startswith('/'):
            bot_instance.delete_user_message_after_delay(message, delay=0.1)

def run_bot():
    print("🤖 Khởi động TeleBot...")
    print("="*50)
    print("📁 SPAM FILES: 1.py → 10.py")
    print("⚡ Chạy từng file, không nghỉ")
    print("="*50)
    keyboard = create_keyboard()
    bot.send_message(ADMIN_ID, format_message("🤖 BOT ĐÃ KHỞI ĐỘNG!\n📌 Sẵn sàng nhận lệnh."), parse_mode='HTML', reply_markup=keyboard)
    bot.infinity_polling()

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or ADMIN_ID == "YOUR_ADMIN_ID_HERE":
        print("⚠️ VUI LÒNG CẤU HÌNH BOT!")
        print("📌 Hướng dẫn:")
        print("1. Tạo bot từ @BotFather trên Telegram")
        print("2. Lấy BOT_TOKEN")
        print("3. Lấy ADMIN_ID (lấy ID của bạn)")
        print("4. Cập nhật vào file")
        sys.exit(1)
    
    missing_files = []
    for i in range(1, 11):
        if not os.path.exists(f"{i}.py"):
            missing_files.append(f"{i}.py")
    
    if missing_files:
        print(f"⚠️ Thiếu file: {', '.join(missing_files)}")
        print("📌 Tạo các file 1.py đến 10.py")
    
    run_bot()
