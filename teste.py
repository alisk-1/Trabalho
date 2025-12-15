
def tirar_fotos(image):

    from camconnect import CaptureImage
    import cv2
    CaptureImage(cv2.VideoCapture(0),

                 width=480, height=320,

                 window_name="Capture Image",

                 filename="captured_image.jpg").run()
