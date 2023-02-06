import cv2
from pyzbar import pyzbar

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Find QR and barcode in the frame
    decoded_objects = pyzbar.decode(frame)

    # Print results
    for obj in decoded_objects:
        print('Type : ', obj.type)
        print('Data : ', obj.data)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
