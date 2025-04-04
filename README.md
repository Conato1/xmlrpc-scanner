# XML-RPC Scanner

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)](CONTRIBUTING.md)
[![Issues](https://img.shields.io/github/issues/yourusername/xmlrpc-scanner.svg)](https://github.com/Conato1/xmlrpc-scanner/issues)

---

## 🔍 Overview
XML-RPC Scanner is a fast and efficient tool for **detecting the accessibility of xmlrpc.php on websites.** It helps identify potential security risks, including open, restricted, or misconfigured XML-RPC endpoints. Featuring multi-threading, customizable delays, and structured output, it ensures accurate and comprehensive scanning for security analysis. 🚀

> Created by **Muhammad Thoriq**  
> Version: `v1.0.2a`

---

## ⚠️ Disclaimer
This tool is developed solely for educational and security research purposes. Unauthorized scanning of websites without proper consent may violate legal and ethical guidelines. The author assumes no responsibility for any misuse or illegal activities conducted using this tool. Use it responsibly and ethically. 🚀

## ✨ Features
✅ Scan a single URL or multiple URLs from a file  
✅ Multi-threaded scanning for fast results  
✅ Customizable request delay to avoid rate limiting  
✅ Detects forbidden access, redirects, and errors  
✅ Outputs results in a structured format  

---

## 🚀 Installation

```sh
# Clone this repository
git clone https://github.com/Conato1/xmlrpc-scanner.git
cd xmlrpc-scanner

# Install dependencies
pip install -r requirements.txt
```

## 🚀🚀 Installation Virtual Enviroment [Optional]

```
sudo apt update
sudo apt install python3-venv
sudo apt install virtualenv python3-virtualenv

python3 -m venv name_folder  
source name_folder/bin/activate  
virtualenv -p python3 nama_folder
```

---

## ⚡ Usage

### Scan a Single URL
```sh
python3 xml.py --base_url https://example.com
```

### Scan Multiple URLs from a File
```sh
python3 xml.py --mas_url urls.txt --threads 10 --delay 0.3
```

| Argument      | Description                                       |
|--------------|---------------------------------------------------|
| `--base_url` | Scan a single website for XML-RPC accessibility  |
| `--mas_url`  | Provide a file containing multiple URLs          |
| `--threads`  | Number of concurrent threads (default: 5)        |
| `--delay`    | Delay between requests in seconds (default: 0.5) |

---

## 📜 Example Output
```sh
✅ [SUCCESS] https://example.com/xmlrpc.php is accessible
⛔ [FORBIDDEN] https://test.com/xmlrpc.php is blocked (403)
➡️ [REDIRECT] https://site.com redirects to https://newsite.com
```

---

## 📁 Subdomain File
```sh
Scan using [Sudomy](https://github.com/screetsec/Sudomy) and use httprobe_subdomain.txt as the reference file for checking xmlrpc.php.
```

---

## 🛠️ Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🔗 Connect
- GitHub: [Conato1](https://github.com/Conato1)
- Linkedin: [@muhammadthoriq](https://www.linkedin.com/in/muhammadthoriq/)

