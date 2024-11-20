import wifi_qrcode_generator.generator

qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid='Home', hidden=False, authentication_type='WPA', password='o4XjFmz2j1Fph4V+PnD6JumY87K7AnVPpIkt9rai4xkoPFaygYIVq/J1GajdDYO'
)
qr_code.print_ascii()
qr_code.make_image().save('qr.png')
