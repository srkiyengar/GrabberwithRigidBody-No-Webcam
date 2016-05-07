__author__ = 'srkiyengar'


import cv2
import os
import logging

LOG_LEVEL = logging.DEBUG



# Set up a logger with output level set to debug; Add the handler to the logger
my_logger = logging.getLogger("My_Logger")



# Open video device

os.system("v4l2-ctl -d /dev/video1 --set-ctrl focus_auto=0")
os.system("v4l2-ctl -d /dev/video1 --set-ctrl focus_absolute=1")

class webcam:
    def __init__( self, cam_identifier, focus_type, focus_value):

        if focus_type != 0 or focus_type != 1:
            focus_type = 0
        if cam_identifier !=0 and cam_identifier!=1:
            cam_identifier = 0;
        input_string = "v4l2-ctl -d /dev/video"+str(cam_identifier)+" --set-ctrl focus_auto="+str(focus_type)
        my_logger.info("Setting to manual-focus: {}".format(input_string))
        os.system(input_string)

        if focus_type == 0:
            input_string = "v4l2-ctl -d /dev/video"+str(cam_identifier)+" --set-ctrl focus_absolute="+str(1)
            my_logger.info("Focus value: {}".format(input_string))
            os.system(input_string)

        capture = cv2.VideoCapture(1)

        if not capture.isOpened():
            raise IOError("Unable to open/initialize the camera for video capture")

        self.camera = capture

    def capture_and_save_frame(self,object_id,my_dataset):
        ret, img = self.camera.read()
        if not ret:
            my_logger.info("Camera read failure - no frame")
            return 0;
        else:
            filename = str(object_id)+".png"
            success = cv2.imwrite(filename,img)
            if success:
                my_dataset.insert_image_filename(filename)
                return 1
            else:
                my_logger.info("Failure while writing image file {}".format(filename))
                return 0
    def close_video(self):
        cv2.destroyAllWindows() # Close window
        self.camera.release() # Release video device