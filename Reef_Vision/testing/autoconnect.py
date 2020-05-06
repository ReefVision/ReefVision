import sys
sys.path.append("..")
from CameraManager.TPUCameraManager import CameraManager, GStreamerPipelines
import os

camMan = CameraManager() #Creates new camera manager object

CSICam = camMan.newCam(1)
RGB = CSICam.addPipeline(GStreamerPipelines.RGB,(640,480),30,"rgb")

# pipelineStarted = False
# i=0
# while True:
#     if os.path.exists('/dev/video1'):
#         if(pipelineStarted):
#             if(RGB):
#                 i+=1
#                 print(i)
#                 data = bytes(RGB)
#         else:
#             CSICam.startPipeline()
#             pipelineStarted = True
#     else:
#         if(pipelineStarted):
#             CSICam.stopPipeline()
#             pipelineStarted = False
#         print("Disconnected")
while True:
    if(RGB):
        data = bytes(RGB)
        print(data[1])
# if self.set_ai:
    
#     self.AI = self.CSICam.addPipeline(GStreamerPipelines.RGB, self.model_res,30,"AI")

# self.CSICam.startPipeline() 

# if os.path.exists('/dev/video1'):
#     self.USBCam = self.camMan.newCam(1) #Creates new RGB CSI-camera
#     self.SB = self.USBCam.addPipeline(GStreamerPipelines.H264,(640,480),30,"usb_cam") #Creates an RGB stream at 30 fps and 640x480 for openCV
#     self.USBCam.startPipeline()
# else:
#     self.USBCam = None