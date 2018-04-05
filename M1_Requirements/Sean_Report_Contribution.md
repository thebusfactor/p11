for at least top ten focal use cases, write a short goal statement and
use case body (up to seven pages).  Identify the use cases that
comprise a minimum viable product.


### 3.2 Functions
 
Basic functionality of our system comprises imited user interaction. It involves a camera being set-up at a suitable intersection that provides sufficient view
for detecting the traffic light that controls said intersection and any busses that may travel through the light controlled lane, thus being able to see when one does not obey
the road rules. From here we can extend the function and user interaction by offering auto-detection of the scene and the ability for the user to define what actions should take place upon the event.

As part of our system we will have these inputs and outputs.
Input:
* Camera feed, video of scene (MVP)
* GUI input for selecting lights (MVP)
* User defined actions (END)
* Training data; images (END)

Output: 
* Alert; Box + red light (MVP)
* Training data weights (MVP)
* Info of scene (END)
    * Time/Date
    * License plate
    * Image/video of moment

MVP Use Case Diagram
!url thing 

Minimum Viable Product Use Cases
###### 1. User sets up camera
###### 2. Requires MVP Use Case 1, boots software, selects and adds traffic light area of detection
###### 3. Requires MVP Use Case 1, boots software, selects and deletes traffic light area of detection
###### 4. Requires MVP Use Case 1, boots software, selects and updates traffic light area of detection
###### 5. Requires MVP Use Case 1, boots software, selects and adds bus line of detection
###### 6. Requires MVP Use Case 1, boots software, selects and deletes bus line of detection
###### 7. Requires MVP Use Case 1, boots software, selects and updates bus line of detection



*Actions of actors:* | *Actions of system:* 
--- | ---
*Still* | `renders` 
1 | 2 

End Goal(s) Use Cases
###### 1. User sets up camera, boots software and user will automatically get alerted when a bus has ran a red light
Description: For our first end goal use case where the user should have no interaction or intervention with the system other than checking the video feed is suitable for detection.
What this involves is the software to have used machine learning to be able to scan and detect a video feed for the location on the image of the bus and the lights. This
extracts the user and allows the system to run external to any prior input required in the MVP.
Validity check: Predominantly done through user checking video feed, in the case where it doesn't detect a light and/or bus upon start up, the user will be alerted that no point of interest was detected and realignment is required. 
Exact sequence: Set up of camera -> Run software -> Software auto-detects the environmental interest points -> Runs and alerts user when event triggers
Effect of Parameters: If an obstruction interferes with the camera the software should alert it has lost the points of interest.
Relationship of input and output: Video feed input is scanned for points of interest -> Alert is outputted when event triggered.
 
###### 2. Requires End Goal Use Case 1, Upon booting of software user can define output upon event trigger
Description: An extension of the first End Goal Use Case, upon detection of bus running red light the user can define what the output should be. This could be an email or computer alert event has been triggered.
Exact sequence: Run software -> User defines what output should be -> Output is delivered when event triggers.
Effect of Parameters: Depending on the level of sophistication of system, user may define output to only occur after X amount of buses have ran a red light or any other aspect they deem appropriate.
Relationship of input and output: Video feed input is scanned for points of interest -> User defined alert is outputted when event triggered.

Extension Goal(s) Use Cases (Should I flesh out?)
###### 1. Requires End Goal Use Case 1, Upon booting of software user can define additional points of interest to keep track of
Description: As part of the possible extension to this project, 
Validity check: Since these events like License plate detection, police interfention, speed detection validity checks would need to occur to make sure the values and assumptions made are performing above an expected
correctness threshold (Assuming a baseline of 90%).
Exact sequence: Run software -> Software auto-detects the environmental interest points -> Runs and logs additional event, alerts user
Effect of Parameters: If an obstruction interferes with the camera the software should alert it has lost the points of interest. Instances of each event need to be recorded to perform statistical analysis.
Relationship of input and output: Video feed input is scanned for points of interest -> Additional event is logged and user alerted.

 


### 3.10 Supporting information

Dylan's section 

a) Training data weight output
b) If machine learning is required we will be gathering output from the training in the form of weights and biases that will influence and classify future input.
This will be used to set up the camera and it will autodetect the intersection layout from a variety of angles. If the weights and biases
are fine tuned enough we should have a good system for detection. 
c) Program will be the recipient of the output, as the output is fed back in for more training and testing.
d) 90% tolerance for how accurately the output is used to detect whether the bus has passed a red light.
e) Measure against a test set and judge prediction percentage.
g) For our end goal and extension goal this output is related to both aspects as this governs how well a bus is detected and thus when an alert triggers.
j) The format should be whatever data type we use for our weights (float, double, int).

a) Alert from trigger
b) An alert should be issued via email, push notification or through the software when a bus runs a red light. 
c) User of system should recieve an alert when the issue occurs.
d) Every instance of detection the alert should send.
e) If we provide it false positives and see if it detects a static image of the offense, and issues the email to the user.
f) ***what we deem***
g) This is the key output from our system and relies on every other input functioning correctly.
h) The output of the alert may be a simple ping on the computer that is running the software, to an email and digital log of the trigger.

a) Info of scene
b) The moment of the red light breach there should be data taken of the time, data and a visual of the scene (image or video)
c) Emailed or provided to the user via a server which would host the images.
d) Every instance of detection the info should be captured.
e) Visually inspecting the data vs real time and see if there are any discrepancies of when it is and is not outputting the signal.
f) This output relies on the camera feed especially as it needs to accurately capture the scene upon the event triggering. 
j) The data format for the image of the scene will most likely be a .png, 








