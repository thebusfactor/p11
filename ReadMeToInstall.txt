The virtual environment included with this release should handle most of the dependencies for you.
Running on windows, you will require some form of Bash emulator for the required scripts to work. Git Bash works well for us.

The program does require C++ Build Tools.
Download and install the visual build tools from this link. Leave the two optionals checked.
https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017

To run the project, you will need to use ManyCam.

Ensure that a functional webcam is available on the device.
Ensure ManyCam (The free version) is downloaded and installed locally
Run ManyCam
Open OBS, and add a Video Capture Device
Ensure that this video capture device is set for 'ManyCam Virtual Webcam'
Go to the Bus Factor code, ensure that in src/main.py, cam = Cam(None)
If there is a built in webcam, ensure that the open_cam method in src/externals/cam.py is video = cv2.VideoCapture(0)
Start the Bus Factor (run main.py)
Once these steps are completed, the bus factor software should be running a debug UI with classifications occuring on one window, and OBS should be capturing directly from the webcam, sans classifications. 
When you are done, make sure to Exit ManyCam. ManyCam leaves itself running in system tray unless forcibly closed.