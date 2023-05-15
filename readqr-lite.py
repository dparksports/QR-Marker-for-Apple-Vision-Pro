import cv2
import zxingcpp
import hashlib

vid = cv2.VideoCapture(0)
while (True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    results = zxingcpp.read_barcodes(frame)
    strs = []
    for result in results:
        strs.append(result.text)
    restored = "".join(strs)
    print(len(restored))
    if len(restored) > 1:
        hashlib.sha256(restored.encode()).hexdigest()
        with open('restored.txt', 'w') as f:
            f.write(restored)

        break
           
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()