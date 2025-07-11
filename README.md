# QR Code Generator

A simple Python script to generate QR codes.

## Features

- Generate QR codes from text, URLs, phone numbers, emails, WiFi credentials, and more.
- Save output as PNG, JPG, or WEBP images.
- Easy to use from the command line.

## Requirements

- Python 3.7+
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)

Install dependencies:
```sh
pip3 install pillow
pip3 install qrcode
```

## Usage

Run the script from your terminal:

```sh
python3 qr.py <data> [options]
```

### Options

- `-t`, `--type`  
  Type of QR code to generate. Options: `text`, `url`, `sms`, `email`, `tel`, `wifi`.  
  Default: `auto`
- `-s`, `--save`  
  Output image filename (supports `.png`, `.jpg`, `.webp`).  
  Default: `qrcode.png`

### Examples

```sh
python3 qr.py "hello world"
python3 qr.py "https://amicioespyy.eu" -s my_qr.webp
python3 qr.py "+49123456789:Hello" -t sms
python3 qr.py "user@example.com:Subject:Body" -t email
python3 qr.py "+49123456789" -t tel -s qr1.png
python3 qr.py "MySSID;WPA;password" -t wifi
```

### Get Help

To see all options and usage examples:

```sh
python3 qrcode.py --help
```

## License

MIT
