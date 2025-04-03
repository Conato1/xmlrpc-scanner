import argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import re
import os
from colorama import Fore, Style, init
import urllib3

# Disable InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)  # Initialize colorama for colored output

# Define output file
OUTPUT_FILE = os.path.join(os.getcwd(), "output.txt")

# Thread-safe file writing
def write_to_file(data):
    try:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(data + "\n")
    except Exception as e:
        print(f"{Fore.RED}❌ [ERROR] Gagal menulis ke file: {e}{Style.RESET_ALL}")

# Print banner
def print_banner():
    banner = f"""
    {Fore.CYAN}🔍 XML-RPC Scanner v1.0 🔍{Style.RESET_ALL}
    --------------------------------
    {Fore.GREEN}🚀 Scan XML-RPC accessibility on websites{Style.RESET_ALL}
    {Fore.YELLOW}📌 Detects if 'xmlrpc.php' is accessible{Style.RESET_ALL}
    {Fore.RED}⚠️  Handles redirect, forbidden, and server errors{Style.RESET_ALL}
    --------------------------------
    {Fore.BLUE}Usage:{Style.RESET_ALL}
      python script.py --base_url https://example.com
      python script.py --mas_url urls.txt --threads 10 --delay 0.3
    --------------------------------
    {Fore.MAGENTA}© 2025 XML-RPC Scanner by Muhammad Thoriq. All rights reserved.{Style.RESET_ALL}
    """
    print(banner)

# Validate URL
def is_valid_url(url):
    regex = re.compile(
        r'^(https?://)?'  # http:// or https:// (optional)
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6}|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}(\.\d{1,3}){3})'  # or IP
        r'(:\d+)?'  # optional port
        r'(/.*)?$',  # optional path
        re.IGNORECASE)
    return re.match(regex, url) is not None

# Check XML-RPC accessibility
def check_xmlrpc(url):
    if not is_valid_url(url):
        print(f"{Fore.RED}❌ [INVALID URL] {url} is not a valid URL.{Style.RESET_ALL}")
        return None
    
    try:
        full_url = url.rstrip('/') + '/xmlrpc.php'
        headers = {'User-Agent': 'Mozilla/5.0'}
        #print(f"{Fore.YELLOW}🔍 [DEBUG] Checking: {full_url}{Style.RESET_ALL}")
        pass
    
        response = requests.get(full_url, headers=headers, timeout=10, allow_redirects=True, verify=False)
        
        if response.status_code == 405 and "XML-RPC server accepts POST requests only." in response.text:
            result = f"✅ [SUCCESS] {url} is accessible: {full_url}"
            print(f"{Fore.GREEN}✅ [RESULT] {result}{Style.RESET_ALL}")
            write_to_file(result)  # Hanya menulis jika SUCCESS
            return result
        else:
            #print(f"{Fore.RED}❌ [SKIPPED] {url} did not return expected response.{Style.RESET_ALL}")
            pass
        
    except requests.RequestException as e:
        #print(f"{Fore.RED}❌ [ERROR] Failed to check {url}: {e}{Style.RESET_ALL}")
        pass
    
    return None  # Jika tidak SUCCESS, tidak menulis apa pun ke file

# Main function
def main():
    print_banner()
    parser = argparse.ArgumentParser(description="🔍 Check if xmlrpc.php is accessible.")
    parser.add_argument('--base_url', help="🌐 Single URL to check.")
    parser.add_argument('--mas_url', help="📄 File containing multiple URLs (one per line).")
    parser.add_argument('--threads', type=int, default=5, help="🔄 Number of concurrent threads (default: 5).")
    parser.add_argument('--delay', type=float, default=0.5, help="⏳ Delay between requests in seconds (default: 0.5).")
    args = parser.parse_args()
    
    urls = []
    if args.base_url:
        urls.append(args.base_url)
    elif args.mas_url:
        try:
            with open(args.mas_url, 'r', encoding="utf-8") as f:
                urls = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"{Fore.RED}❌ [ERROR] File not found: {args.mas_url}{Style.RESET_ALL}")
            return
    
    if not urls:
        print(f"{Fore.YELLOW}⚠️ [WARNING] No URLs provided.{Style.RESET_ALL}")
        return
    
    print(f"{Fore.CYAN}🚀 Starting XML-RPC accessibility check...{Style.RESET_ALL}")
    
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(check_xmlrpc, url): url for url in urls}
        for future in as_completed(futures):
            result = future.result()
            if args.delay > 0:
                time.sleep(args.delay)
    
    print(f"{Fore.GREEN}✅ Scan completed! Results saved to output.txt{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
