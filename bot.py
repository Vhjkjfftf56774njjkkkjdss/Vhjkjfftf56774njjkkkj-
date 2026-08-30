import subprocess
import sys
import importlib

def _auto_install():
    required = {
        'telebot': 'pyTelegramBotAPI',
        'requests': 'requests',
        'psutil': 'psutil',
        'httpx': 'httpx',
        'aiohttp': 'aiohttp',
        'aiohttp_socks': 'aiohttp_socks',
        'Crypto': 'pycryptodome',
        'PIL': 'Pillow',
        'ddddocr': 'ddddocr',
        'bs4': 'beautifulsoup4',
        'fake_useragent': 'fake-useragent',
        'stem': 'stem',
        'urllib3': 'urllib3',
        'colorama': 'colorama',
    }
    for module, package in required.items():
        try:
            importlib.import_module(module)
        except ImportError:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            except Exception:
                pass
_auto_install()
import json
import telebot
import datetime
import time
import os, sys, re
import subprocess
import requests
import threading
import psutil
import platform
import socket
import random
from collections import defaultdict
from telebot import types
from urllib.parse import quote
bot_token = '7845936454:AAHGrld1WgMgYuPI_HM0hGr5OQp-ilus9Wc'
bot = telebot.TeleBot(bot_token)
processes = []
process_phones = {}
process_logs = {}        # pid -> đường dẫn file log
running_scripts = {}     # (script, phone) -> pid (chống launch trùng)
VIP_FILE = 'vip_users.json'
vip_users = {}

def _git_push(file_path, label):
    """Push git trong thread riêng để không block polling của bot."""
    def _worker():
        try:
            subprocess.run(['git', 'add', file_path], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'Update {label}: {datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")} [skip ci]'], check=True, capture_output=True)
            subprocess.run(['git', 'push', 'origin', 'main', '--force'], check=True, capture_output=True)
            print(f'<tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã commit {file_path} lên repo')
        except Exception as e:
            print(f'<tg-emoji emoji-id="6129782440157256336">⚠️</tg-emoji> Lỗi push {file_path}: {e}')
    threading.Thread(target=_worker, daemon=True).start()

def save_vip_users():
    try:
        with open(VIP_FILE, 'w', encoding='utf-8') as f:
            json.dump(vip_users, f, indent=2, ensure_ascii=False)
        _git_push(VIP_FILE, 'VIP Users')
    except Exception as e:
        print(f'<tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi lưu vip_users.json: {e}')

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

FREE_KEYS_FILE = 'free_keys.json'

def load_free_keys():
    try:
        if os.path.exists(FREE_KEYS_FILE):
            with open(FREE_KEYS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        pass
    return {}

def save_free_keys(data):
    try:
        with open(FREE_KEYS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f'<tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi lưu free_keys.json: {e}')

def has_free_key(user_id):
    today = str(datetime.date.today())
    data = load_free_keys()
    return str(user_id) in data.get(today, [])

def set_free_key(user_id):
    today = str(datetime.date.today())
    data = load_free_keys()
    today_list = data.get(today, [])
    uid = str(user_id)
    if uid not in today_list:
        today_list.append(uid)
        data[today] = today_list
        save_free_keys(data)

def get_vip_info(user_id):
    info = vip_users.get(str(user_id))
    if not info:
        return None
    try:
        start = datetime.datetime.strptime(info.get('start', ''), '%Y-%m-%d').date()
        days = int(info.get('days', 0))
        end = start + datetime.timedelta(days=days)
        if datetime.date.today() > end:
            del vip_users[str(user_id)]
            save_vip_users()
            return None
        return {'start': start, 'days': days, 'end': end}
    except:
        return None

def is_vip_user(user_id):
    return get_vip_info(user_id) is not None

def set_vip_user(user_id, days):
    today = datetime.date.today()
    uid = str(user_id)
    existing = get_vip_info(uid)
    if existing:
        total_days = (existing['end'] - today).days + int(days)
    else:
        total_days = int(days)
    vip_users[uid] = {'start': today.strftime('%Y-%m-%d'), 'days': total_days}
    save_vip_users()
    return (today.strftime('%Y-%m-%d'), total_days, (today + datetime.timedelta(days=total_days)).strftime('%Y-%m-%d'))

load_vip_users()

BANNED_FILE = 'banned_users.json'
banned_users = []

def save_banned_users():
    try:
        with open(BANNED_FILE, 'w', encoding='utf-8') as f:
            json.dump(banned_users, f, indent=2, ensure_ascii=False)
        _git_push(BANNED_FILE, 'Banned Users')
    except Exception as e:
        print(f'<tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi lưu banned_users.json: {e}')

def load_banned_users():
    global banned_users
    try:
        if os.path.exists(BANNED_FILE):
            with open(BANNED_FILE, 'r', encoding='utf-8') as f:
                banned_users = [str(u) for u in json.load(f)]
        else:
            banned_users = []
            save_banned_users()
    except:
        banned_users = []

def is_banned(user_id):
    return str(user_id) in banned_users

load_banned_users()
ADMIN_ID = '7235906278'
user_cooldown_free = defaultdict(lambda: 0)
user_cooldown_vip = defaultdict(lambda: 0)
user_tokens = defaultdict(lambda: '')
FREE_MAX_COUNT = 10
VIP_MAX_COUNT = 30
COOLDOWN_FREE_SECONDS = 300
COOLDOWN_VIP_SECONDS = 250

def TimeStamp():
    now = str(datetime.date.today())
    return now

def generate_token():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join((random.choice(characters) for _ in range(4)))

BLACKLIST_FILE = 'blacklist.json'

def save_blacklist(blacklist):
    try:
        with open(BLACKLIST_FILE, 'w', encoding='utf-8') as f:
            json.dump(blacklist, f, indent=2, ensure_ascii=False)
        _git_push(BLACKLIST_FILE, 'Blacklist')
    except Exception as e:
        print(f'<tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi lưu blacklist.json: {e}')

def load_blacklist():
    if os.path.exists(BLACKLIST_FILE):
        try:
            with open(BLACKLIST_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return []

REDEEM_FILE = 'redeem_codes.json'

def load_redeem_codes():
    if os.path.exists(REDEEM_FILE):
        try:
            with open(REDEEM_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {}

def save_redeem_codes(codes):
    try:
        with open(REDEEM_FILE, 'w', encoding='utf-8') as f:
            json.dump(codes, f, indent=2, ensure_ascii=False)
        _git_push(REDEEM_FILE, 'Redeem Codes')
    except Exception as e:
        print(f'<tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi lưu redeem_codes.json: {e}')

def get_cpu_disk_info():
    try:
        cpu_usage = psutil.cpu_percent(interval=0.5)
        disk = psutil.disk_usage('/')
        return f'CPU: {cpu_usage}% | Disk: {disk.percent}%'
    except:
        return 'CPU: N/A | Disk: N/A'

def get_system_info():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        info = {'cpu': f'{cpu_usage}%', 'memory': f'{memory.percent}% ({memory.used // 1024 ** 3}GB/{memory.total // 1024 ** 3}GB)', 'disk': f'{disk.percent}% ({disk.used // 1024 ** 3}GB/{disk.total // 1024 ** 3}GB)', 'os': f'{platform.system()} {platform.release()}', 'python': platform.python_version(), 'hostname': socket.gethostname(), 'ip': socket.gethostbyname(socket.gethostname()), 'process_count': len(processes), 'uptime': time.time() - psutil.boot_time()}
        return info
    except:
        return None

def format_uptime(seconds):
    days = int(seconds // (24 * 3600))
    seconds = seconds % (24 * 3600)
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    parts = []
    if days > 0:
        parts.append(f'{days} ngày')
    if hours > 0:
        parts.append(f'{hours} giờ')
    if minutes > 0:
        parts.append(f'{minutes} phút')
    if seconds > 0 or not parts:
        parts.append(f'{seconds} giây')
    return ' '.join(parts)

def check_cooldown(user_id, cooldown_seconds, bucket):
    current_time = time.time()
    last_spam_time = bucket.get(user_id, 0)
    if current_time - last_spam_time < cooldown_seconds:
        remaining = int(cooldown_seconds - (current_time - last_spam_time))
        return (False, remaining)
    return (True, 0)

def update_cooldown(user_id, bucket):
    bucket[user_id] = time.time()

def validate_phone_number(phone):
    phone = re.sub('\\s+', '', phone)
    patterns = ['^(0|\\+84)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$', '^(84)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$', '^(03[2-9]|05[6|8|9]|07[0|6-9]|08[0-6|8|9]|09[0-4|6-9])[0-9]{7}$']
    for pattern in patterns:
        if re.match(pattern, phone):
            return True
    return False

def format_phone_number(phone):
    phone = re.sub('\\s+', '', phone)
    if phone.startswith('+84'):
        phone = '0' + phone[3:]
    elif phone.startswith('84'):
        phone = '0' + phone[2:]
    return phone

def mask_phone_number(phone):
    if len(phone) >= 10:
        return f'{phone[:4]}xxxx{phone[-2:]}'
    return phone

def get_user_info(message):
    user = message.from_user
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip() or 'Không có tên'
    username = f'@{user.username}' if user.username else 'Không có username'
    user_id = user.id
    return {'name': full_name, 'username': username, 'id': user_id}

def launch_script(fname, phone, laps, log_dir='logs'):
    """Chạy script spam TÁCH RIÊNG khỏi bot (detached, non-blocking).

    - Dùng sys.executable (cùng interpreter với bot).
    - start_new_session=True: tách session, không bị treo theo bot.
    - stdout/stderr ghi vào file log (không DEVNULL) để dễ debug.
    - Chống launch trùng: nếu (script, phone) đang chạy thì trả về process hiện có.
    """
    key = (fname, phone)
    if key in running_scripts:
        old_pid = running_scripts[key]
        try:
            p = psutil.Process(old_pid)
            if p.is_running():
                for proc in processes:
                    if proc.pid == old_pid:
                        return proc
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            running_scripts.pop(key, None)
    try:
        os.makedirs(log_dir, exist_ok=True)
        script_path = os.path.join(os.getcwd(), fname)
        log_path = os.path.join(log_dir, f'{os.path.splitext(fname)[0]}_{phone}.log')
        logf = open(log_path, 'a', encoding='utf-8')
        proc = subprocess.Popen(
            [sys.executable, script_path, phone, str(laps)],
            stdin=subprocess.DEVNULL,
            stdout=logf,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        processes.append(proc)
        process_phones[proc.pid] = phone
        process_logs[proc.pid] = log_path
        running_scripts[key] = proc.pid
        return proc
    except Exception as e:
        print(f'[LAUNCH] Lỗi chạy {fname}: {e}')
        return None

def monitor_process(pid, phone, count, chat_id, user_info=None, is_vip=False):
    try:
        process = psutil.Process(pid)
        while True:
            try:
                if not process.is_running() or process.status() == psutil.STATUS_ZOMBIE:
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                break
            time.sleep(2)
        for i, p in enumerate(processes):
            if p.pid == pid:
                processes.pop(i)
                process_phones.pop(pid, None)
                break
        for key, rpid in list(running_scripts.items()):
            if rpid == pid:
                running_scripts.pop(key, None)
        process_logs.pop(pid, None)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    except Exception as e:
        print(f'Lỗi khi giám sát tiến trình: {e}')

def delete_message_after_delay(chat_id, message_id, delay_seconds):

    def delete_message():
        time.sleep(delay_seconds)
        try:
            bot.delete_message(chat_id, message_id)
        except Exception as e:
            print(f'Không thể xóa tin nhắn: {e}')
    thread = threading.Thread(target=delete_message)
    thread.daemon = True
    thread.start()

def auto_delete(func):
    def wrapper(message, *args, **kwargs):
        try:
            result = func(message, *args, **kwargs)
        finally:
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except Exception:
                pass
        return result
    return wrapper

def is_private_chat(message):
    return message.chat.type == 'private'

ALLOWED_GROUP_ID = -1004420189760

def should_respond(message):
    if is_private_chat(message):
        return True
    return message.chat.id == ALLOWED_GROUP_ID

def private_only(func):

    def wrapper(message, *args, **kwargs):
        if not should_respond(message):
            return
        return func(message, *args, **kwargs)
    return wrapper

@bot.message_handler(commands=['mua'])
@auto_delete
@private_only
def mua(message):
    reply_text = '''<blockquote>
<tg-emoji emoji-id="6129509499280563691">💎</tg-emoji> <b>BẢNG GIÁ PLAN</b>

<b>VIP PREMIUM:</b>
⭐ <b>1 NGÀY</b> - 10K
⭐ <b>1 TUẦN</b> - 50K
⭐ <b>1 THÁNG</b> - 140K
⭐ <b>2 THÁNG</b> - 170K
<tg-emoji emoji-id="6129792056589031358">🔥</tg-emoji> <b>3 THÁNG</b> - 210K
<tg-emoji emoji-id="6129792056589031358">🔥</tg-emoji> <b>6 THÁNG</b> - 360K

<tg-emoji emoji-id="6129732880529628243">💵</tg-emoji> <b>Mua VIP:</b>
• <b>Telegram:</b> @Hahahhshah
• <b>Support:</b> @Hahahhshah
</blockquote>'''
    bot.send_message(chat_id=message.chat.id, text=reply_text, parse_mode='HTML')

@bot.message_handler(commands=['giftcode'])
@auto_delete
@private_only
def redeem(message):
    user_id = message.from_user.id
    if len(message.text.split()) < 2:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Vui lòng nhập mã redeem!</b></blockquote>', parse_mode='HTML')
        return
    code = message.text.split()[1].upper()
    codes = load_redeem_codes()
    if code not in codes:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Mã redeem không hợp lệ hoặc không tồn tại!</b></blockquote>', parse_mode='HTML')
        return
    if codes[code]['used']:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Mã redeem đã được sử dụng!</b></blockquote>', parse_mode='HTML')
        return
    days = codes[code]['days']
    ngay, total_days, new_end_str = set_vip_user(user_id, days)
    bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6131660826924292492">🎁</tg-emoji> <i>GiftCode Entered Successfully.</i></b>\n• <b>Start Time:</b> {ngay}\n• <b>Validity:</b> {total_days} day\n• <b>Expire Time:</b> {new_end_str}</blockquote>', parse_mode='HTML')
    codes[code]['used'] = True
    save_redeem_codes(codes)

@bot.message_handler(commands=['fbid'])
@auto_delete
@private_only
def get_fbid(message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji> SAI ĐỊNH DẠNG <tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji></b>\n\n<b><tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> Ví Dụ:</b> <code>/fbid https://www.facebook.com/givaybeiu</code>\n<i><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Vui lòng nhập đúng định dạng link.</i></blockquote>', parse_mode='HTML')
            return
        fb_link = args[1].strip()
        encoded_link = quote(fb_link, safe='')
        api_url = f'https://ffb.vn/api/tool/get-id-fb?idfb={encoded_link}'
        res = requests.get(api_url, timeout=10)
        data = res.json()
        if data.get('error') != 0:
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Không lấy được Facebook ID!</b></blockquote>', parse_mode='HTML')
            return
        fb_id = data.get('id', 'Không rõ')
        name = data.get('name', 'Không rõ')
        bot.reply_to(message, f'<blockquote>• <b>Successfully Get Facebook UID.</b>\n\n• <b>NAME:</b> <b>{name}</b>\n• <b>UID:</b> <code>{fb_id}</code></blockquote>', parse_mode='HTML')
    except Exception as e:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129782440157256336">⚠️</tg-emoji> API UPDATE.</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['addredeem'])
@auto_delete
@private_only
def addredeem(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    parts = message.text.split()
    if len(parts) < 4:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Thiếu tham số!</b>\n<b>Cú pháp:</b> <code>/addredeem [ngày] [số_lần_dùng] [mã_redeem]</code>\n<b>Ví dụ:</b> <code>/addredeem 30 5 Beiu123</code></blockquote>', parse_mode='HTML')
        return
    if not parts[1].isdigit() or not parts[2].isdigit():
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số ngày và số lần dùng phải là số!</b></blockquote>', parse_mode='HTML')
        return
    days = int(parts[1])
    count = int(parts[2])
    redeem_prefix = parts[3].upper()
    if days <= 0 or count <= 0:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số ngày và số lần dùng phải lớn hơn 0!</b></blockquote>', parse_mode='HTML')
        return
    if count > 1000:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần dùng tối đa là 1000!</b></blockquote>', parse_mode='HTML')
        return
    if len(redeem_prefix) > 20:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Mã redeem prefix quá dài (tối đa 20 ký tự)!</b></blockquote>', parse_mode='HTML')
        return
    codes = load_redeem_codes()
    generated_codes = []
    for i in range(count):
        while True:
            code = f'{redeem_prefix}{i + 1:03d}'
            if code not in codes:
                codes[code] = {'days': days, 'used': False}
                generated_codes.append(code)
                break
            else:
                code = f'{redeem_prefix}{random.randint(100, 999)}'
                if code not in codes:
                    codes[code] = {'days': days, 'used': False}
                    generated_codes.append(code)
                    break
    save_redeem_codes(codes)
    code_list = '\n'.join(generated_codes)
    bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã tạo {count} mã redeem {days} ngày:</b>\n\n{code_list}\n\n<b><tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> Tổng số mã redeem hiện có: {len(codes)}</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['listredeem'])
@auto_delete
@private_only
def listredeem(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    codes = load_redeem_codes()
    if not codes:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129432481927010933">✉️</tg-emoji> Không có mã redeem nào trong hệ thống!</b></blockquote>', parse_mode='HTML')
        return
    active_codes = []
    used_codes = []
    for code, data in codes.items():
        if data['used']:
            used_codes.append((code, data['days']))
        else:
            active_codes.append((code, data['days']))
    response = f'<tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> DANH SÁCH MÃ REDEEM\n\n'
    response += f'• Tổng số mã: {len(codes)}\n'
    response += f'• Chưa sử dụng: {len(active_codes)}\n'
    response += f'• Đã sử dụng: {len(used_codes)}\n\n'
    if active_codes:
        response += '<tg-emoji emoji-id="6129736819014639296">🔸</tg-emoji> MÃ CHƯA SỬ DỤNG:\n'
        for code, days in active_codes[:20]:
            response += f'  {code} - {days} ngày\n'
        if len(active_codes) > 20:
            response += f'  ... và {len(active_codes) - 20} mã khác\n'
        response += '\n'
    if used_codes:
        response += '<tg-emoji emoji-id="6129736819014639296">🔸</tg-emoji> MÃ ĐÃ SỬ DỤNG:\n'
        for code, days in used_codes[:10]:
            response += f'  {code} - {days} ngày (đã dùng)\n'
        if len(used_codes) > 10:
            response += f'  ... và {len(used_codes) - 10} mã khác\n'
    bot.reply_to(message, f'<blockquote><b>{response}</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['blacklist'])
@auto_delete
@private_only
def blacklist(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    parts = message.text.split()
    if len(parts) < 2:
        blacklist_numbers = load_blacklist()
        if not blacklist_numbers:
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> Danh sách blacklist trống!</b></blockquote>', parse_mode='HTML')
        else:
            bl_list = '\n'.join([f'{i + 1}. {num}' for i, num in enumerate(blacklist_numbers)])
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> Danh sách số điện thoại bị cấm ({len(blacklist_numbers)} số):</b>\n\n{bl_list}</blockquote>', parse_mode='HTML')
        return
    subcommand = parts[1].lower()
    if subcommand == 'add' and len(parts) >= 3:
        phone = parts[2]
        if not validate_phone_number(phone):
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số điện thoại không hợp lệ!</b></blockquote>', parse_mode='HTML')
            return
        formatted_phone = format_phone_number(phone)
        blacklist_numbers = load_blacklist()
        if formatted_phone in blacklist_numbers:
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số {formatted_phone} đã có trong blacklist!</b></blockquote>', parse_mode='HTML')
            return
        blacklist_numbers.append(formatted_phone)
        try:
            save_blacklist(blacklist_numbers)
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã thêm {formatted_phone} vào blacklist!</b></blockquote>', parse_mode='HTML')
        except Exception as e:
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi thêm vào blacklist: {str(e)}</b></blockquote>', parse_mode='HTML')
    elif subcommand == 'remove' and len(parts) >= 3:
        phone = parts[2]
        formatted_phone = format_phone_number(phone)
        blacklist_numbers = load_blacklist()
        if formatted_phone not in blacklist_numbers:
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số {formatted_phone} không có trong blacklist!</b></blockquote>', parse_mode='HTML')
            return
        blacklist_numbers.remove(formatted_phone)
        try:
            save_blacklist(blacklist_numbers)
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã xóa {formatted_phone} khỏi blacklist!</b></blockquote>', parse_mode='HTML')
        except Exception as e:
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi xóa khỏi blacklist: {str(e)}</b></blockquote>', parse_mode='HTML')
    elif subcommand == 'clear':
        try:
            save_blacklist([])
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã xóa toàn bộ blacklist!</b></blockquote>', parse_mode='HTML')
        except Exception as e:
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi xóa blacklist: {str(e)}</b></blockquote>', parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Cú pháp không hợp lệ!</b>\n\n<b>Các lệnh blacklist:</b>\n• <code>/blacklist</code> - Xem danh sách\n• <code>/blacklist add [số]</code> - Thêm số\n• <code>/blacklist remove [số]</code> - Xóa số\n• <code>/blacklist clear</code> - Xóa toàn bộ</blockquote>', parse_mode='HTML')

def TimeStamp():
    now = datetime.datetime.now()
    return now.strftime('%d-%m-%Y %H:%M:%S')


@bot.message_handler(commands=['getkey'])
@auto_delete
@private_only
def startkey(message):
    user_id = message.from_user.id
    name = message.from_user.full_name
    time_now = TimeStamp()
    if is_vip_user(user_id):
        vip_gif_url = 'https://static.tumblr.com/e0ddbcad98f365cdbeb5a257a4acee18/nezqmod/rZBptd8bh/tumblr_static_ot20qyb2yqsw8sgcc8ww84gc_2048_v2.gif'
        
        vip_caption = f'\n<tg-emoji emoji-id="6129705083501293112">👑</tg-emoji> {name}\n\n<tg-emoji emoji-id="6129579803600231171">🎉</tg-emoji> Bạn đã là VIP PREMIUM!\n\n<tg-emoji emoji-id="6129479035077531636">✨</tg-emoji> Quyền lợi VIP:\n• Dùng /smsvip - Premium (tối đa {VIP_MAX_COUNT} lượt)\n• Dùng /sms - Free (tối đa {FREE_MAX_COUNT} lượt)\n• Không cần getkey hàng ngày\n• Ưu tiên hỗ trợ\n\n<tg-emoji emoji-id="6129639980387015660">🚀</tg-emoji> Hãy bắt đầu spam ngay!\n• /smsvip 0346091524 30 - Premium\n• /sms 0346091524 10 - Free\n\n<tg-emoji emoji-id="6129509499280563691">💎</tg-emoji> VIP Status: Đang hoạt động\n'
        bot.send_animation(chat_id=message.chat.id, animation=vip_gif_url, caption=vip_caption, parse_mode='HTML')
        return
    waiting_msg = bot.reply_to(message, '<tg-emoji emoji-id="6129802875611651951">⏩</tg-emoji> VUI LÒNG ĐỢI TRONG GIÂY LÁT!', parse_mode='HTML')
    delete_message_after_delay(message.chat.id, waiting_msg.message_id, 1)


    key_raw = 'xintatcachungsinhdungcooantrailannhau_' + str(int(user_id) * int(datetime.date.today().day) - 12666)

    key_url = 'https://www.google.com/search?q=' + quote(key_raw, safe='')

    api_token = '65b7b764eff4e751576356dd'
    url = requests.get(f'https://link4m.co/api-shorten/v2?api={api_token}&url={key_url}').json()
    url_key = url['shortenedUrl']

    free_gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWttdWVneGd0a2NpejMzc3ltYnF4MDIwa2xoOWtwa2tpMGZ5NXR0MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hB0CNWqJfn1eg9gHKU/giphy.gif'
    free_caption = f'\n• Use By: {name}\n• ID: {user_id}\n• Time: {time_now}\n\n• LINK LẤY KEY: {url_key}\n<tg-emoji emoji-id="6129477982810545152">‼️</tg-emoji> Sau Khi Lấy Key Xong Dùng Lệnh /key [KEY] Để Xác Thực Key.\n'
    bot.send_animation(chat_id=message.chat.id, animation=free_gif_url, caption=free_caption, parse_mode='HTML')


@bot.message_handler(commands=['key'])
@auto_delete
@private_only
def key(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129731845442510016">🔐</tg-emoji> VUI LÒNG NHẬP KEY.</b></blockquote>', parse_mode='HTML')
        return
    user_id = message.from_user.id
    key = message.text.split()[1]
    username = message.from_user.username
    expected_key = 'xintatcachungsinhdungcooantrailannhau_' + str(int(message.from_user.id) * int(datetime.date.today().day) - 12666)
    if key == expected_key:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> KEY HỢP LỆ.</b> Bạn đã được phép sử dụng lệnh <code>/sms</code> (FREE)!</blockquote>', parse_mode='HTML')
        set_free_key(user_id)
    else:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> KEY KHÔNG HỢP LỆ.</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['profile'])
@auto_delete
@private_only
def profile(message):
    user = message.from_user
    user_id = user.id
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip() or 'Không có tên'
    now = datetime.datetime.now()
    today_str = now.strftime('%d-%m-%Y %H:%M:%S')
    token = generate_token()
    user_tokens[user_id] = token
    plan_text = '<tg-emoji emoji-id="6131660826924292492">🎁</tg-emoji> FREE'
    start_time_str = 'N/A'
    expire_time_str = 'N/A'
    vip_info = get_vip_info(user_id)
    if vip_info:
        plan_text = '<tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> PREMIUM (Online)'
        start_time_str = vip_info['start'].strftime('%d-%m-%Y')
        expire_time_str = vip_info['end'].strftime('%d-%m-%Y')
    elif str(user_id) in vip_users:
        plan_text = '<tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> PREMIUM (Offline)'
    profile_text = f'<blockquote>\n<b>• Name:</b> {full_name}\n<b>• ID:</b> <code>{user_id}</code>\n<b>• Token:</b> <code>{token}</code>\n<b>• Plan:</b> {plan_text}\n<b>• Start Time:</b> {start_time_str}\n<b>• Expire Time:</b> {expire_time_str}\n<b>• Today:</b> {today_str}\n\n<b>Token Update Sau Mỗi 3s</b></blockquote>\n'
    bot.reply_to(message, profile_text, parse_mode='HTML')

@bot.message_handler(commands=['sms'])
@auto_delete
@private_only
def sms_free(message):
    user_id = message.from_user.id
    if is_banned(user_id):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn đã bị cấm sử dụng bot!</b></blockquote>', parse_mode='HTML')
        return
    cooldown_ok, remaining = check_cooldown(user_id, COOLDOWN_FREE_SECONDS, user_cooldown_free)
    if not cooldown_ok:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129802875611651951">⏩</tg-emoji> Vui lòng đợi {remaining} giây trước khi spam tiếp!</b></blockquote>', parse_mode='HTML')
        return
    is_vip = is_vip_user(user_id)
    if not is_vip:
        if not has_free_key(user_id):
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn chưa có quyền spam FREE!</b>\nDùng <code>/getkey</code> để lấy key và dùng <code>/key</code> để nhập key hôm nay\n<b>Ví dụ:</b> <code>/key xintatcachungsinhdungcooantrailannhau_12345</code></blockquote>', parse_mode='HTML')
            return
    if len(message.text.split()) < 3:
        bot.reply_to(message, '<blockquote><tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji> <b><u>SAI ĐỊNH DẠNG</u></b> <tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji>\n\n⭕️ <b>Vui Lòng Nhập [Phone] [Count]</b>\n<tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> <b>Ví Dụ:</b> <code>/sms 0982774812 10</code> \n\n<b><i><u><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Vui lòng nhập đúng định dạng và phone phải đủ 10 số.</u></i></b></blockquote>', parse_mode='HTML')
        return
    phone_number = message.text.split()[1]
    lap = message.text.split()[2]
    if not validate_phone_number(phone_number):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ!</b>\n<b>Định dạng hợp lệ:</b>\n• <code>0xxxxxxxxx</code> (10 số)\n• <code>+84xxxxxxxxx</code>\n• <code>84xxxxxxxxx</code>\n<b>Ví dụ:</b> <code>0938817263</code>, <code>+84938817263</code>, <code>84938817263</code></blockquote>', parse_mode='HTML')
        return
    formatted_phone = format_phone_number(phone_number)
    blacklist_numbers = load_blacklist()
    if formatted_phone in blacklist_numbers:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số điện thoại {formatted_phone} đã bị cấm spam!</b></blockquote>', parse_mode='HTML')
        return
    if not lap.isnumeric():
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần phải là số nguyên dương!</b>\n<b>Ví dụ:</b> <code>/sms 0938817263 5</code></blockquote>', parse_mode='HTML')
        return
    lap_int = int(lap)
    if lap_int <= 0:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần phải lớn hơn 0!</b></blockquote>', parse_mode='HTML')
        return
    if lap_int > FREE_MAX_COUNT:
        lap_int = FREE_MAX_COUNT
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129782440157256336">⚠️</tg-emoji> FREE chỉ được spam tối đa {FREE_MAX_COUNT} lượt/lần!</b> Đã tự động điều chỉnh về {FREE_MAX_COUNT} lượt.</blockquote>', parse_mode='HTML')
    if formatted_phone in ['0938817263']:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129593109408913890">😠</tg-emoji> Spam cái đầu buồi tao huhu</b></blockquote>', parse_mode='HTML')
        return
    scripts = ['callsms9.py']
    try:
        process = None
        for fname in scripts:
            process = launch_script(fname, formatted_phone, lap_int)
        update_cooldown(user_id, user_cooldown_free)
        user_info = get_user_info(message)
        thread = threading.Thread(target=monitor_process, args=(process.pid, formatted_phone, lap_int, message.chat.id, user_info, is_vip))
        thread.daemon = True
        thread.start()
        user_info = get_user_info(message)
        masked_phone = mask_phone_number(formatted_phone)
        plan = 'Premium' if is_vip else 'Free'
        response_text = f"<blockquote>\n<b>Attacking Spam Success</b>\n\n• <b>AttackBy:</b> <u>{user_info['name']}</u>\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Count:</b> <b><i>{lap_int}</i></b>\n• <b>Plan:</b> {plan}\n• <b>List:</b> <u>Phone</u>\n• <b>Phone:</b> <code>{masked_phone}</code>\n</blockquote>"
        gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUybzBucjI5MmV0cmRoZm9yb2YzYWdvc2oydjVqZm1aMGRmODZxdTJidSZlcD12MV9naWZzX3NlYXJjaCZjdT1n/dmFXUZ5up1T896HP8B/source.gif'
        bot.send_animation(chat_id=message.chat.id, animation=gif_url, caption=response_text, parse_mode='HTML')
        try:
            cmd_name = message.text.split()[0]
            admin_text = f"<blockquote>\n<b><tg-emoji emoji-id='6129577213734952104'>🔔</tg-emoji> LỆNH MỚI: {cmd_name}</b>\n\n• <b>ID:</b> <code>{user_id}</code>\n• <b>Name:</b> {user_info['name']}\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Số Điện Thoại:</b> <code>{formatted_phone}</code>\n• <b>Số Lượt:</b> {lap_int}\n• <b>Time:</b> {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n</blockquote>"
            bot.send_message(ADMIN_ID, admin_text, parse_mode='HTML')
        except:
            pass
    except Exception as e:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi khởi động tấn công: {str(e)}</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['smsvip'])
@auto_delete
@private_only
def spam_premium(message):
    user_id = message.from_user.id
    if is_banned(user_id):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn đã bị cấm sử dụng bot!</b></blockquote>', parse_mode='HTML')
        return
    cooldown_ok, remaining = check_cooldown(user_id, COOLDOWN_VIP_SECONDS, user_cooldown_vip)
    if not cooldown_ok:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129802875611651951">⏩</tg-emoji> Vui lòng đợi {remaining} giây trước khi spam tiếp!</b></blockquote>', parse_mode='HTML')
        return
    if not is_vip_user(user_id):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lệnh <code>/smsvip</code> chỉ dành cho VIP PREMIUM!</b>\nBạn có thể dùng <code>/sms</code> (FREE) hoặc mua VIP bằng lệnh <code>/mua</code></blockquote>', parse_mode='HTML')
        return
    if len(message.text.split()) < 3:
        bot.reply_to(message, '<blockquote><tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji> <b><u>SAI ĐỊNH DẠNG</u></b> <tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji>\n\n⭕️ <b>Vui Lòng Nhập [Phone] [Count]</b>\n<tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> <b>Ví Dụ:</b> <code>/smsvip 0982774812 30</code> \n\n<b><i><u><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Vui lòng nhập đúng định dạng và phone phải đủ 10 số.</u></i></b></blockquote>', parse_mode='HTML')
        return
    phone_number = message.text.split()[1]
    lap = message.text.split()[2]
    if not validate_phone_number(phone_number):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ!</b>\n<b>Định dạng hợp lệ:</b>\n• <code>0xxxxxxxxx</code> (10 số)\n• <code>+84xxxxxxxxx</code>\n• <code>84xxxxxxxxx</code>\n<b>Ví dụ:</b> <code>0938817263</code>, <code>+84938817263</code>, <code>84938817263</code></blockquote>', parse_mode='HTML')
        return
    formatted_phone = format_phone_number(phone_number)
    blacklist_numbers = load_blacklist()
    if formatted_phone in blacklist_numbers:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số điện thoại {formatted_phone} đã bị cấm spam!</b></blockquote>', parse_mode='HTML')
        return
    if not lap.isnumeric():
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần phải là số nguyên dương!</b>\n<b>Ví dụ:</b> <code>/smsvip 0938817263 30</code></blockquote>', parse_mode='HTML')
        return
    lap_int = int(lap)
    if lap_int <= 0:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần phải lớn hơn 0!</b></blockquote>', parse_mode='HTML')
        return
    if lap_int > VIP_MAX_COUNT:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> VIP chỉ được spam tối đa {VIP_MAX_COUNT} lượt/lần!</b></blockquote>', parse_mode='HTML')
        return
    if formatted_phone in ['0938817263']:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129593109408913890">😠</tg-emoji> Spam cái đầu buồi tao huhu</b></blockquote>', parse_mode='HTML')
        return
    scripts = ['callsms.py'] + [f'callsms{i}.py' for i in range(2, 12)]
    try:
        process = None
        for fname in scripts:
            process = launch_script(fname, formatted_phone, lap_int)
        update_cooldown(user_id, user_cooldown_vip)
        user_info = get_user_info(message)
        thread = threading.Thread(target=monitor_process, args=(process.pid, formatted_phone, lap_int, message.chat.id, user_info, True))
        thread.daemon = True
        thread.start()
        user_info = get_user_info(message)
        masked_phone = mask_phone_number(formatted_phone)
        response_text = f"<blockquote>\n<b>Attacking Spam Success</b>\n\n• <b>AttackBy:</b> <u>{user_info['name']}</u>\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Count:</b> <b><i>{lap_int}</i></b>\n• <b>Plan:</b> Premium\n• <b>List:</b> <u>Phone</u>\n• <b>Phone:</b> <code>{masked_phone}</code>\n</blockquote>"
        gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUybzBucjI5MmV0cmRoZm9yb2YzYWdvc2oydjVqZm1aMGRmODZxdTJidSZlcD12MV9naWZzX3NlYXJjaCZjdT1n/dmFXUZ5up1T896HP8B/source.gif'
        bot.send_animation(chat_id=message.chat.id, animation=gif_url, caption=response_text, parse_mode='HTML')
        try:
            cmd_name = message.text.split()[0]
            admin_text = f"<blockquote>\n<b><tg-emoji emoji-id='6129577213734952104'>🔔</tg-emoji> LỆNH MỚI: {cmd_name}</b>\n\n• <b>ID:</b> <code>{user_id}</code>\n• <b>Name:</b> {user_info['name']}\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Số Điện Thoại:</b> <code>{formatted_phone}</code>\n• <b>Số Lượt:</b> {lap_int}\n• <b>Time:</b> {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n</blockquote>"
            bot.send_message(ADMIN_ID, admin_text, parse_mode='HTML')
        except:
            pass
    except Exception as e:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi khởi động tấn công: {str(e)}</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['call'])
@auto_delete
@private_only
def call_free(message):
    user_id = message.from_user.id
    if is_banned(user_id):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn đã bị cấm sử dụng bot!</b></blockquote>', parse_mode='HTML')
        return
    cooldown_ok, remaining = check_cooldown(user_id, COOLDOWN_FREE_SECONDS, user_cooldown_free)
    if not cooldown_ok:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129802875611651951">⏩</tg-emoji> Vui lòng đợi {remaining} giây trước khi spam tiếp!</b></blockquote>', parse_mode='HTML')
        return
    is_vip = is_vip_user(user_id)
    if not is_vip:
        if not has_free_key(user_id):
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn chưa có quyền spam FREE!</b>\nDùng <code>/getkey</code> để lấy key và dùng <code>/key</code> để nhập key hôm nay\n<b>Ví dụ:</b> <code>/key xintatcachungsinhdungcooantrailannhau_12345</code></blockquote>', parse_mode='HTML')
            return
    if len(message.text.split()) < 3:
        bot.reply_to(message, '<blockquote><tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji> <b><u>SAI ĐỊNH DẠNG</u></b> <tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji>\n\n⭕️ <b>Vui Lòng Nhập [Phone] [Count]</b>\n<tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> <b>Ví Dụ:</b> <code>/call 0982774812 10</code> \n\n<b><i><u><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Vui lòng nhập đúng định dạng và phone phải đủ 10 số.</u></i></b></blockquote>', parse_mode='HTML')
        return
    phone_number = message.text.split()[1]
    lap = message.text.split()[2]
    if not validate_phone_number(phone_number):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ!</b>\n<b>Định dạng hợp lệ:</b>\n• <code>0xxxxxxxxx</code> (10 số)\n• <code>+84xxxxxxxxx</code>\n• <code>84xxxxxxxxx</code>\n<b>Ví dụ:</b> <code>0938817263</code>, <code>+84938817263</code>, <code>84938817263</code></blockquote>', parse_mode='HTML')
        return
    formatted_phone = format_phone_number(phone_number)
    blacklist_numbers = load_blacklist()
    if formatted_phone in blacklist_numbers:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số điện thoại {formatted_phone} đã bị cấm spam!</b></blockquote>', parse_mode='HTML')
        return
    if not lap.isnumeric():
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần phải là số nguyên dương!</b>\n<b>Ví dụ:</b> <code>/call 0938817263 5</code></blockquote>', parse_mode='HTML')
        return
    lap_int = int(lap)
    if lap_int <= 0:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần phải lớn hơn 0!</b></blockquote>', parse_mode='HTML')
        return
    if lap_int > FREE_MAX_COUNT:
        lap_int = FREE_MAX_COUNT
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129782440157256336">⚠️</tg-emoji> FREE chỉ được spam tối đa {FREE_MAX_COUNT} lượt/lần!</b> Đã tự động điều chỉnh về {FREE_MAX_COUNT} lượt.</blockquote>', parse_mode='HTML')
    if formatted_phone in ['0938817263']:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129593109408913890">😠</tg-emoji> Spam cái đầu buồi tao huhu</b></blockquote>', parse_mode='HTML')
        return
    scripts = ['callsms9.py', 'call2.py']
    try:
        process = None
        for fname in scripts:
            process = launch_script(fname, formatted_phone, lap_int)
        update_cooldown(user_id, user_cooldown_free)
        user_info = get_user_info(message)
        thread = threading.Thread(target=monitor_process, args=(process.pid, formatted_phone, lap_int, message.chat.id, user_info, is_vip))
        thread.daemon = True
        thread.start()
        user_info = get_user_info(message)
        masked_phone = mask_phone_number(formatted_phone)
        plan = 'Premium' if is_vip else 'Free'
        response_text = f"<blockquote>\n<b>Attacking Spam Success</b>\n\n• <b>AttackBy:</b> <u>{user_info['name']}</u>\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Count:</b> <b><i>{lap_int}</i></b>\n• <b>Plan:</b> {plan}\n• <b>List:</b> <u>Phone</u>\n• <b>Phone:</b> <code>{masked_phone}</code>\n</blockquote>"
        gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUybzBucjI5MmV0cmRoZm9yb2YzYWdvc2oydjVqZm1aMGRmODZxdTJidSZlcD12MV9naWZzX3NlYXJjaCZjdT1n/dmFXUZ5up1T896HP8B/source.gif'
        bot.send_animation(chat_id=message.chat.id, animation=gif_url, caption=response_text, parse_mode='HTML')
        try:
            cmd_name = message.text.split()[0]
            admin_text = f"<blockquote>\n<b><tg-emoji emoji-id='6129577213734952104'>🔔</tg-emoji> LỆNH MỚI: {cmd_name}</b>\n\n• <b>ID:</b> <code>{user_id}</code>\n• <b>Name:</b> {user_info['name']}\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Số Điện Thoại:</b> <code>{formatted_phone}</code>\n• <b>Số Lượt:</b> {lap_int}\n• <b>Time:</b> {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n</blockquote>"
            bot.send_message(ADMIN_ID, admin_text, parse_mode='HTML')
        except:
            pass
    except Exception as e:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi khởi động tấn công: {str(e)}</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['callvip'])
@auto_delete
@private_only
def callvip(message):
    user_id = message.from_user.id
    if is_banned(user_id):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn đã bị cấm sử dụng bot!</b></blockquote>', parse_mode='HTML')
        return
    cooldown_ok, remaining = check_cooldown(user_id, COOLDOWN_VIP_SECONDS, user_cooldown_vip)
    if not cooldown_ok:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129802875611651951">⏩</tg-emoji> Vui lòng đợi {remaining} giây trước khi spam tiếp!</b></blockquote>', parse_mode='HTML')
        return
    if not is_vip_user(user_id):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lệnh <code>/callvip</code> chỉ dành cho VIP PREMIUM!</b>\nBạn có thể dùng <code>/sms</code> (FREE) hoặc mua VIP bằng lệnh <code>/mua</code></blockquote>', parse_mode='HTML')
        return
    if len(message.text.split()) < 3:
        bot.reply_to(message, '<blockquote><tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji> <b><u>SAI ĐỊNH DẠNG</u></b> <tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji>\n\n⭕️ <b>Vui Lòng Nhập [Phone] [Count]</b>\n<tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> <b>Ví Dụ:</b> <code>/callvip 0982774812 30</code> \n\n<b><i><u><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Vui lòng nhập đúng định dạng và phone phải đủ 10 số.</u></i></b></blockquote>', parse_mode='HTML')
        return
    phone_number = message.text.split()[1]
    lap = message.text.split()[2]
    if not validate_phone_number(phone_number):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ!</b>\n<b>Định dạng hợp lệ:</b>\n• <code>0xxxxxxxxx</code> (10 số)\n• <code>+84xxxxxxxxx</code>\n• <code>84xxxxxxxxx</code>\n<b>Ví dụ:</b> <code>0938817263</code>, <code>+84938817263</code>, <code>84938817263</code></blockquote>', parse_mode='HTML')
        return
    formatted_phone = format_phone_number(phone_number)
    blacklist_numbers = load_blacklist()
    if formatted_phone in blacklist_numbers:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số điện thoại {formatted_phone} đã bị cấm spam!</b></blockquote>', parse_mode='HTML')
        return
    if not lap.isnumeric():
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần phải là số nguyên dương!</b>\n<b>Ví dụ:</b> <code>/callvip 0938817263 30</code></blockquote>', parse_mode='HTML')
        return
    lap_int = int(lap)
    if lap_int <= 0:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số lần phải lớn hơn 0!</b></blockquote>', parse_mode='HTML')
        return
    if lap_int > VIP_MAX_COUNT:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> VIP chỉ được spam tối đa {VIP_MAX_COUNT} lượt/lần!</b></blockquote>', parse_mode='HTML')
        return
    if formatted_phone in ['0938817263']:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129593109408913890">😠</tg-emoji> Spam cái đầu buồi tao huhu</b></blockquote>', parse_mode='HTML')
        return
    scripts = ['call.py'] + [f'call{i}.py' for i in range(2, 6)] + ['callsms.py'] + [f'callsms{i}.py' for i in range(2, 12)]
    try:
        process = None
        for fname in scripts:
            process = launch_script(fname, formatted_phone, lap_int)
        update_cooldown(user_id, user_cooldown_vip)
        user_info = get_user_info(message)
        thread = threading.Thread(target=monitor_process, args=(process.pid, formatted_phone, lap_int, message.chat.id, user_info, True))
        thread.daemon = True
        thread.start()
        user_info = get_user_info(message)
        masked_phone = mask_phone_number(formatted_phone)
        response_text = f"<blockquote>\n<b>Attacking Spam Success</b>\n\n• <b>AttackBy:</b> <u>{user_info['name']}</u>\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Count:</b> <b><i>{lap_int}</i></b>\n• <b>Plan:</b> Premium\n• <b>List:</b> <u>Phone</u>\n• <b>Phone:</b> <code>{masked_phone}</code>\n</blockquote>"
        gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUybzBucjI5MmV0cmRoZm9yb2YzYWdvc2oydjVqZm1aMGRmODZxdTJidSZlcD12MV9naWZzX3NlYXJjaCZjdT1n/dmFXUZ5up1T896HP8B/source.gif'
        bot.send_animation(chat_id=message.chat.id, animation=gif_url, caption=response_text, parse_mode='HTML')
        try:
            cmd_name = message.text.split()[0]
            admin_text = f"<blockquote>\n<b><tg-emoji emoji-id='6129577213734952104'>🔔</tg-emoji> LỆNH MỚI: {cmd_name}</b>\n\n• <b>ID:</b> <code>{user_id}</code>\n• <b>Name:</b> {user_info['name']}\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Số Điện Thoại:</b> <code>{formatted_phone}</code>\n• <b>Số Lượt:</b> {lap_int}\n• <b>Time:</b> {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n</blockquote>"
            bot.send_message(ADMIN_ID, admin_text, parse_mode='HTML')
        except:
            pass
    except Exception as e:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi khởi động tấn công: {str(e)}</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['treosmscall'])
@auto_delete
@private_only
def treosmscall(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, '<blockquote><tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji> <b><u>SAI ĐỊNH DẠNG</u></b> <tg-emoji emoji-id="6129909635613726974">⭐</tg-emoji>\n\n⭕️ <b>Vui Lòng Nhập [Phone]</b>\n<tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji> <b>Ví Dụ:</b> <code>/treosmscall 0982774812</code>\n\n<b><i><u><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Lệnh Admin - Không Giới Hạn, Tự Động Chạy Tất Cả File.</u></i></b></blockquote>', parse_mode='HTML')
        return
    phone_number = parts[1]
    if not validate_phone_number(phone_number):
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ!</b>\n<b>Định dạng hợp lệ:</b>\n• <code>0xxxxxxxxx</code> (10 số)\n• <code>+84xxxxxxxxx</code>\n• <code>84xxxxxxxxx</code>\n<b>Ví dụ:</b> <code>0938817263</code>, <code>+84938817263</code>, <code>84938817263</code></blockquote>', parse_mode='HTML')
        return
    formatted_phone = format_phone_number(phone_number)
    lap_int = 999999999
    scripts = sorted(f for f in os.listdir(os.getcwd()) if re.match(r'^(call|callsms)\d*\.py$', f))
    try:
        started = 0
        for fname in scripts:
            proc = launch_script(fname, formatted_phone, lap_int)
            if proc is not None:
                process = proc
                started += 1
        if started == 0:
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Không tìm thấy file script nào (call*.py / callsms*.py)!</b></blockquote>', parse_mode='HTML')
            return
        user_info = get_user_info(message)
        thread = threading.Thread(target=monitor_process, args=(process.pid, formatted_phone, lap_int, message.chat.id, user_info, True))
        thread.daemon = True
        thread.start()
        masked_phone = mask_phone_number(formatted_phone)
        response_text = f"<blockquote>\n<b><tg-emoji emoji-id='6235628846855492222'>🔥</tg-emoji> TREO SMS + CALL THÀNH CÔNG</b>\n\n• <b>AttackBy:</b> <u>{user_info['name']}</u>\n• <b>Username:</b> <code>{user_info['username']}</code>\n• <b>Count:</b> <b><i>∞ Không giới hạn</i></b>\n• <b>Plan:</b> Admin\n• <b>Số File Chạy:</b> <code>{started} file</code>\n• <b>Phone:</b> <code>{masked_phone}</code>\n\n<tg-emoji emoji-id='6242510612824332116'>⏳</tg-emoji> Dùng <code>/stop {formatted_phone}</code> để dừng\n</blockquote>"
        gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUybzBucjI5MmV0cmRoZm9yb2YzYWdvc2oydjVqZm1aMGRmODZxdTJidSZlcD12MV9naWZzX3NlYXJjaCZjdT1n/dmFXUZ5up1T896HP8B/source.gif'
        bot.send_animation(chat_id=message.chat.id, animation=gif_url, caption=response_text, parse_mode='HTML')
    except Exception as e:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi khởi động tấn công: {str(e)}</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['help'])
@auto_delete
@private_only
def help(message):
    user = message.from_user
    user_id = user.id
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip() or 'Không có tên'
    help_gif = 'https://i.pinimg.com/originals/c2/ce/2d/c2ce2d82a11c90b05ad4abd796ef2fff.gif'
    help_text = f'<blockquote>\n<b>Welcome {full_name}<tg-emoji emoji-id="6129523887421006760">👆</tg-emoji></b>\n\n  | <b><u>Member</u></b> <tg-emoji emoji-id="6129746001654718223">🔖</tg-emoji>\n  \n• /profile - <b>Xem Thông Tin Plan</b>\n• /getkey - <b>GetKey Miễn Phí</b>\n• /key <i>[Key]</i> - <b>Xác Thực Key</b>\n   •Ex: <code>/key xintatcachungsinhdungcooantrailannhau_abcxyv</code>\n• /sms <i>[Phone] [Count]</i> - <b>Spam SMS FREE</b>\n   •Ex: <code>/sms 0999999999 10</code>\n• /smsvip <i>[Phone] [Count]</i> - <b>Spam SMS PREMIUM</b>\n   •Ex: <code>/smsvip 0999999999 30</code>\n• /call <i>[Phone] [Count]</i> - <b>Spam CALL FREE</b>\n   •Ex: <code>/call 0999999999 10</code>\n• /callvip <i>[Phone] [Count]</i> - <b>Spam CALL PREMIUM</b>\n   •Ex: <code>/callvip 0999999999 30</code>\n• /giftcode <i>[Code]</i> - <b>Nhập GiftCode</b>\n   •Ex: <code>/giftcode abcxyz</code>\n• /mua - <b>Mua Plan VIP</b>\n\n  | <b><u>Lệnh Khác</u></b> <tg-emoji emoji-id="6129805465476929485">⚡</tg-emoji>\n\n• /stickerid - <b>Lấy ID Sticker</b>\n• /fbid - <b>Lấy ID Facebook</b>\n   •Ex: <code>/fbid https://facebook.com/zuck</code>\n</blockquote>'
    bot.send_animation(chat_id=message.chat.id, animation=help_gif, caption=help_text, parse_mode='HTML')

@bot.message_handler(commands=['admin'])
@auto_delete
@private_only
def admin(message):
    user = message.from_user
    user_id = user.id
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip() or 'Không có tên'
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    admin_gif = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDdzdnNqMms4aDZ2NGU4ZTNhYWFhY2EzOHF5ODlkYzN0aG92bG11ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYt5jPR6QX5pnqM/giphy.gif'
    help_text = f'<blockquote>\n<b>Welcome {full_name}<tg-emoji emoji-id="6129523887421006760">👆</tg-emoji></b>\n\n  | <b><u>Admin</u></b> <tg-emoji emoji-id="6129509499280563691">💎</tg-emoji>\n\n• /them <code>[ID] [Ngày]</code> - Thêm/Gia hạn VIP\n• /removip <code>[ID]</code> - Xóa VIP\n• /ban <code>[ID]</code> - Cấm user dùng bot\n• /unban <code>[ID]</code> - Gỡ cấm user\n• /addredeem <code>[Ngày] [Số lượng] [Mã]</code> - Tạo giftcode\n• /listredeem - Danh sách giftcode\n• /blacklist - Quản lý blacklist\n• /status - Trạng thái bot\n• /restart - Khởi động lại bot\n• /stop - Dừng tất cả + tắt bot\n• /stop <code>[SĐT]</code> - Dừng spam theo số điện thoại\n• /treosmscall <code>[SĐT]</code> - Treo SMS + CALL không giới hạn (tất cả file)\n</blockquote>'
    bot.send_animation(chat_id=message.chat.id, animation=admin_gif, caption=help_text, parse_mode='HTML')

@bot.message_handler(commands=['status'])
@auto_delete
@private_only
def status(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    system_info = get_system_info()
    if system_info:
        uptime_formatted = format_uptime(system_info['uptime'])
        status_text = f"\n<blockquote><b><tg-emoji emoji-id='6129801569941592173'>📊</tg-emoji> STATUS BOT\n\n├─<tg-emoji emoji-id='6129873536413605540'>🤖</tg-emoji> Bot: Đang hoạt động\n├─<tg-emoji emoji-id='6244678063775289843'>⚙️</tg-emoji> Tiến trình: {system_info['process_count']}\n├─<tg-emoji emoji-id='6300937964939645617'>💻</tg-emoji> CPU: {system_info['cpu']}\n├─<tg-emoji emoji-id='6129746001654718223'>💾</tg-emoji> RAM: {system_info['memory']}\n├─<tg-emoji emoji-id='6242510612824332116'>⏱️</tg-emoji> Uptime: {uptime_formatted}\n"
        vip_count = len(vip_users)
        today_users = len(load_free_keys().get(str(datetime.date.today()), []))
        codes = load_redeem_codes()
        active_codes = sum((1 for data in codes.values() if not data['used']))
        used_codes = sum((1 for data in codes.values() if data['used']))
        blacklist_numbers = load_blacklist()
        status_text += f'\n├─<tg-emoji emoji-id="6129705083501293112">👑</tg-emoji> VIP: {vip_count} tài khoản'
        status_text += f'\n├─<tg-emoji emoji-id="6129879029676776924">👀</tg-emoji> User hôm nay: {today_users}'
        status_text += f'\n├─<tg-emoji emoji-id="6129779562529168023">🗓</tg-emoji> Ngày: {datetime.date.today()}'
        status_text += f'\n├─<tg-emoji emoji-id="6129802875611651951">⏩</tg-emoji> Cooldown: {COOLDOWN_FREE_SECONDS}s (Free) / {COOLDOWN_VIP_SECONDS}s (VIP)'
        status_text += f'\n├─<tg-emoji emoji-id="6129509499280563691">💎</tg-emoji> VIP max: {VIP_MAX_COUNT} lượt'
        status_text += f'\n├─<tg-emoji emoji-id="6131660826924292492">🎁</tg-emoji> FREE max: {FREE_MAX_COUNT} lượt'
        status_text += f'\n├─<tg-emoji emoji-id="6129731845442510016">🔐</tg-emoji> Mã redeem: {active_codes} chưa dùng, {used_codes} đã dùng'
        status_text += f'\n├─<tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Blacklist: {len(blacklist_numbers)} số</b></blockquote>'
    else:
        status_text = '<blockquote><b><tg-emoji emoji-id="6129782440157256336">⚠️</tg-emoji> Không thể lấy thông tin hệ thống</b></blockquote>'
    bot.reply_to(message, status_text, parse_mode='HTML')

@bot.message_handler(commands=['restart'])
@auto_delete
@private_only
def restart(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129589862413638401">🔗</tg-emoji> Bot sẽ được khởi động lại trong giây lát...</b></blockquote>', parse_mode='HTML')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.message_handler(commands=['stop'])
@auto_delete
@private_only
def stop(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    parts = message.text.split()
    if len(parts) >= 2:
        phone = parts[1]
        if not validate_phone_number(phone):
            bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số điện thoại không hợp lệ!</b>\n<b>Cú pháp:</b> <code>/stop [sdt]</code> hoặc <code>/stop</code> để dừng tất cả</blockquote>', parse_mode='HTML')
            return
        target = format_phone_number(phone)
        killed = 0
        for process in list(processes):
            if process_phones.get(process.pid) == target:
                try:
                    process.terminate()
                    killed += 1
                except:
                    pass
                processes.remove(process)
                process_phones.pop(process.pid, None)
        if killed:
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã dừng {killed} tiến trình đang tấn công số {target}</b></blockquote>', parse_mode='HTML')
        else:
            bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Không có tiến trình nào đang chạy với số {target}</b></blockquote>', parse_mode='HTML')
        return
    for process in processes:
        try:
            process.terminate()
        except:
            pass
    processes.clear()
    process_phones.clear()
    bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Đã dừng tất cả các cuộc tấn công và bot sẽ dừng lại...</b></blockquote>', parse_mode='HTML')
    time.sleep(2)
    bot.stop_polling()

@bot.message_handler(commands=['them'])
@auto_delete
@private_only
def them(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    parts = message.text.split()
    if len(parts) < 3:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Cú pháp:</b> <code>/them [id_user] [số_ngày_hiệu_lực]</code>\n<b>Ví dụ:</b> <code>/them 12345678 30</code></blockquote>', parse_mode='HTML')
        return
    idvip = parts[1]
    hethan = parts[2]
    if not hethan.isdigit():
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Số ngày hiệu lực phải là số!</b></blockquote>', parse_mode='HTML')
        return
    try:
        ngay, total_days, new_end_str = set_vip_user(idvip, int(hethan))
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Thêm/Gia Hạn VIP Thành Công Cho {idvip}</b>\n<tg-emoji emoji-id="6129779562529168023">🗓</tg-emoji> Ngày bắt đầu: {ngay}\n<tg-emoji emoji-id="6129802875611651951">⏩</tg-emoji> Hiệu lực: {total_days} ngày\n<tg-emoji emoji-id="6129779562529168023">🗓</tg-emoji> Hết hạn: {new_end_str}</blockquote>', parse_mode='HTML')
    except Exception as e:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Lỗi khi thêm VIP: {str(e)}</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['ban'])
@auto_delete
@private_only
def ban_user(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Cú pháp:</b> <code>/ban [id_user]</code>\n<b>Ví dụ:</b> <code>/ban 12345678</code></blockquote>', parse_mode='HTML')
        return
    target = parts[1]
    if not target.isdigit():
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> ID user phải là số!</b></blockquote>', parse_mode='HTML')
        return
    if target == ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Không thể ban admin!</b></blockquote>', parse_mode='HTML')
        return
    if target in banned_users:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> User {target} đã bị ban trước đó!</b></blockquote>', parse_mode='HTML')
        return
    banned_users.append(target)
    save_banned_users()
    bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã BAN user {target}</b>\n<tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> User này không thể dùng <code>/sms</code> <code>/smsvip</code> <code>/call</code> <code>/callvip</code> nữa.</blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['unban'])
@auto_delete
@private_only
def unban_user(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Cú pháp:</b> <code>/unban [id_user]</code>\n<b>Ví dụ:</b> <code>/unban 12345678</code></blockquote>', parse_mode='HTML')
        return
    target = parts[1]
    if target not in banned_users:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> User {target} không có trong danh sách ban!</b></blockquote>', parse_mode='HTML')
        return
    banned_users.remove(target)
    save_banned_users()
    bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã UNBAN user {target}</b>\n<tg-emoji emoji-id="6129906126625447892">🔒</tg-emoji> User này có thể dùng bot lại bình thường.</blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['start'])
@auto_delete
@private_only
def start_cmd(message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = f'\n<blockquote>\n<b>Hello <a href="tg://user?id={user_id}">{user_name}</a></b> <tg-emoji emoji-id="6129523887421006760">👆</tg-emoji>\n\n<i>Chào mừng bạn đến với bot.</i>\n\n<b>Để xem danh sách lệnh và cách sử dụng, vui lòng nhập:</b> <code>/help</code>\n\n<i>Hỗ Trợ</i>\n• <b>Admin:</b> @Hahahhshah\n• <b>Support:</b> @Hahahhshah\n\n<tg-emoji emoji-id="6129873536413605540">🤖</tg-emoji><i> Gặp vấn đề gì vui lòng liên hệ cskh ở trên để được hỗ trợ sớm nhất!</i>\n\n</blockquote>\n'
    bot.reply_to(message, text, parse_mode='HTML', disable_web_page_preview=True)

@bot.message_handler(commands=['stickerid'])
@auto_delete
@private_only
def stickerid(message):
    reply = message.reply_to_message
    if reply and reply.sticker:
        st = reply.sticker
        st_type = '<tg-emoji emoji-id="6129544215501216365">🎚</tg-emoji> Video' if getattr(st, 'is_video', False) else ('<tg-emoji emoji-id="6129650399977675538">🎩</tg-emoji> Animated' if getattr(st, 'is_animated', False) else '<tg-emoji emoji-id="6129760505759276442">💠</tg-emoji> Tĩnh')
        info = ('<blockquote><b><tg-emoji emoji-id="6129760505759276442">💠</tg-emoji> STICKER INFO</b>\n'
                '• <b>File ID:</b> <code>' + str(st.file_id) + '</code>\n'
                '• <b>Unique ID:</b> <code>' + str(st.file_unique_id) + '</code>\n'
                '• <b>Set Name:</b> <code>' + str(st.set_name or 'Không có') + '</code>\n'
                '• <b>Emoji:</b> ' + str(st.emoji or 'Không có') + '\n'
                '• <b>Loại:</b> ' + st_type + '\n'
                '</blockquote>')
        bot.reply_to(message, info, parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129782440157256336">⚠️</tg-emoji> Vui lòng trả lời lại tin nhắn chứa sticker.</b></blockquote>', parse_mode='HTML')

@bot.message_handler(commands=['removip'])
@auto_delete
@private_only
def removip(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> Bạn không có quyền sử dụng lệnh này.</b></blockquote>', parse_mode='HTML')
        return
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, '<blockquote><b><tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Cú pháp:</b> <code>/removip [id_user]</code>\n<b>Ví dụ:</b> <code>/removip 12345678</code></blockquote>', parse_mode='HTML')
        return
    id_to_remove = parts[1]
    if id_to_remove in vip_users:
        del vip_users[id_to_remove]
        save_vip_users()
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã xóa VIP của user {id_to_remove}</b></blockquote>', parse_mode='HTML')
    else:
        bot.reply_to(message, f'<blockquote><b><tg-emoji emoji-id="6129840374971112593">🚫</tg-emoji> User {id_to_remove} không có VIP</b></blockquote>', parse_mode='HTML')

@bot.message_handler(content_types=['sticker'])
@private_only
def sticker_info(message):
    st = message.sticker
    st_type = '<tg-emoji emoji-id="6129544215501216365">🎚</tg-emoji> Video' if getattr(st, 'is_video', False) else ('<tg-emoji emoji-id="6129650399977675538">🎩</tg-emoji> Animated' if getattr(st, 'is_animated', False) else '<tg-emoji emoji-id="6129760505759276442">💠</tg-emoji> Tĩnh')
    info = ('<blockquote><b><tg-emoji emoji-id="6129760505759276442">💠</tg-emoji> STICKER INFO</b>\n'
            '• <b>File ID:</b> <code>' + str(st.file_id) + '</code>\n'
            '• <b>Unique ID:</b> <code>' + str(st.file_unique_id) + '</code>\n'
            '• <b>Set Name:</b> <code>' + str(st.set_name or 'Không có') + '</code>\n'
            '• <b>Emoji:</b> ' + str(st.emoji or 'Không có') + '\n'
            '• <b>Loại:</b> ' + st_type + '\n'
            '</blockquote>')
    bot.reply_to(message, info, parse_mode='HTML')

@bot.message_handler(content_types=['new_chat_members'])
def handle_new_chat_members(message):
    for member in message.new_chat_members:
        if member.id == bot.get_me().id:
            welcome = ('<blockquote><b><tg-emoji emoji-id="6129873536413605540">🤖</tg-emoji> CẢM ƠN ĐÃ THÊM TÔI</b>\n\n'
                       '<tg-emoji emoji-id="6129479035077531636">✨</tg-emoji> <b>Bot hỗ trợ SMS + CALL</b>\n'
                       '<tg-emoji emoji-id="6129694470637100146">📌</tg-emoji> Dùng <code>/help</code> để xem danh sách lệnh\n'
                       '<tg-emoji emoji-id="6129509499280563691">💎</tg-emoji> Dùng <code>/mua</code> để xem bảng giá VIP\n\n'
                       '<tg-emoji emoji-id="6129639980387015660">🚀</tg-emoji> <b>Chúc nhóm hoạt động vui vẻ!</b></blockquote>')
            bot.send_message(message.chat.id, welcome, parse_mode='HTML')
            return
        fname = (member.first_name or '') + (' ' + (member.last_name or '') if member.last_name else '')
        fname = fname.strip() or 'Bạn'
        greet = ('<blockquote><b><tg-emoji emoji-id="6129523887421006760">👆</tg-emoji> Chào mừng ' + fname + ' <tg-emoji emoji-id="6129579803600231171">🎉</tg-emoji></b>\n'
                 '<tg-emoji emoji-id="6129579597441801084">💬</tg-emoji> Nhớ đọc <code>/help</code> để biết cách dùng bot nhé!</blockquote>')
        bot.send_message(message.chat.id, greet, parse_mode='HTML')

@bot.message_handler(content_types=['left_chat_member'])
def handle_left_chat_member(message):
    if message.left_chat_member.id == bot.get_me().id:
        pass

if __name__ == '__main__':
    print('Telegram: @Hahahhshah')
    for jf, default in [(BLACKLIST_FILE, []), (REDEEM_FILE, {}), (VIP_FILE, {}), (BANNED_FILE, []), (FREE_KEYS_FILE, {})]:
        if not os.path.exists(jf):
            with open(jf, 'w', encoding='utf-8') as f:
                json.dump(default, f)
            print(f'<tg-emoji emoji-id="6129812419028982717">✅</tg-emoji> Đã tạo: {jf}')
    while True:
        try:
            bot.delete_webhook()
            bot.polling(non_stop=True, skip_pending=True, timeout=25, long_polling_timeout=25)
        except Exception as e:
            print(f'[BOT] Lỗi polling: {e}')
            print('[BOT] Restart polling sau 5 giây...')
            time.sleep(5)
