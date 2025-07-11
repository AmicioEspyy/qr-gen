#!/usr/bin/env python3
import sys, os, argparse, qrcode
from PIL import Image

def sms(data):
    num, msg = data.split(':', 1)
    return f'sms:{num}?body={msg}'

def email(data):
    parts = data.split(':', 2)
    if len(parts) == 1: return f"mailto:{parts[0]}"
    if len(parts) == 2: return f"mailto:{parts[0]}?subject={parts[1]}"
    return f"mailto:{parts[0]}?subject={parts[1]}&body={parts[2]}"

def tel(data): return f"tel:{data}"

def wifi(data):
    ssid, typ, pwd, *h = data.split(';')
    return f'WIFI:S:{ssid};T:{typ};P:{pwd};' + (f'H:{h[0]};' if h else '') + ';'

def main():
    p = argparse.ArgumentParser(
        description="Generate a QR code from text, URL, SMS, email, phone, or WiFi credentials.",
        usage=(
            "./qrcode.py <data> [-t TYPE] [-s OUTPUT]\n"
            "Examples:\n"
            "  ./qrcode.py 'hello world'\n"
            "  ./qrcode.py https://amicioespyy.eu -s my_qr.webp\n"
            "  ./qrcode.py '+49123456789:Hello' -t sms\n"
            "  ./qrcode.py 'user@example.com:Subject:Body' -t email\n"
            "  ./qrcode.py '+49123456789' -t tel -s qr1.png\n"
            "  ./qrcode.py 'MySSID;WPA;password' -t wifi"
        )
    )

    p.add_argument('data', nargs='?', help="Data to encode.")
    p.add_argument('-t', '--type', default='auto', help="Type: text, url, sms, email, tel, wifi (default: auto)")
    p.add_argument('-s', '--save', help="Output image file (png, jpg, webp). Default: ./qrcode.png")

    if len(sys.argv) == 1:
        p.print_help(sys.stderr)
        sys.exit(0)

    a = p.parse_args()

    if not a.data:
        p.print_help(sys.stderr)
        sys.exit(1)

    d, t = a.data, a.type

    if t == 'sms': c = sms(d)
    elif t == 'email': c = email(d)
    elif t == 'tel': c = tel(d)
    elif t == 'wifi': c = wifi(d)
    elif t == 'url': c = d if d.startswith(('http://', 'https://')) else f"http://{d}"
    elif t == 'text': c = d
    else: 
        c = d if d.startswith(('http://', 'https://')) else d

    f = a.save or os.path.join(os.path.dirname(os.path.abspath(__file__)), "qrcode.png")

    if os.path.splitext(f)[1].lower() not in ['.png','.jpg','.jpeg','.webp']:
        sys.exit("File must end with .png, .jpg, .jpeg, or .webp")
        
    img = qrcode.make(c)
    img = img.resize((512, 512), Image.NEAREST)
    img.save(f)
    print(f"QR code saved to: {f}")

if __name__ == "__main__":
    main()