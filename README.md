# Wifi QR Code Reader

Reads a Wifi Password QR Code from a Mac, a Windows or a Linux, so you don't have to type a long wifi password

1) Point your laptop camera to the Wifi QR Code
2) Once it is scanned, it generates a text file called restored.txt


```sh
git clone https://github.com/dparksports/wifi_qrcode_reader/
cd wifi_qrcode_reader
pip install -r requirements.txt
python read_qr_marker.py
cat restored.txt
```

## Sample Wifi QRCode Scanned Result File

Here is the content of the text file "restored.txt" 

```sh
WIFI:T:WPA;S:Phacil;PWifiPasswordABC123;H:false;;
```

Copy "PWifiPasswordABC123" to the password field of your wifi


