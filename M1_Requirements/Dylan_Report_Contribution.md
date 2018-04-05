ENGR301:

Dylan Kumar: 5.2 Budget, 3.2 Functions, 6.1 Assumptions and Dependencies, 3.1 External interfaces (Total Page Count: 5-6 Pages)

This is typically the longest subsection in the document - see 9.5.11.
List up to fifty use cases (in order of priority for development), and
for at least top ten focal use cases, write a short goal statement and
use case body (up to seven pages).  Identify the use cases that
comprise a minimum viable product.

Functions:

Detecting red light, 
Detecting bus

Autodetect location of buses, lights, turning direction, number plate, speed, lanes/multilanes. Work on bad cameras. 
All in real time. 
Detect likelyhood of bus running red light/hitting somebody. Detecting person walking (pedestrian in danger detection). Timestamps and basic analytics data of as it runs the red light.
Work out the colours of the lights. Detect whether the vehicle is a bus and whether it runs the detected light colour. 

 More specifically, it should only identify traffic lights in the driving direction.

 -wait until sean has finished functions and then do it.


 5.2 Budget:

Present a budget for the project (table), and justify each budget item
(one paragraph per item, one page overall).

| Item        | Are           | Cost  |
| ------------- | --------------| ------|
| Camera/Webcam | In the situation where the bus factor webcam is not sufficiently high quality for accurate machine learning or image processing detection and classification. A new webcam will have to be purchased, whereby cost unlikely to exceed $100. | $100 |
| Processing Power      | For machine learning classification, sufficient processing power will be needed to test and train our algorithm. The cost of this may range from $0, if we are able to use the Universities Processing servers, or a few hundred dollars for AWS/Tensorflow servers. As our software may continue to be used with the Bus Factor Podcast live, it may be a better decision to invest in an expensive graphics card for a computer, ranging from $500 to $1000. |   $1000 |




6.1 Assumptions and dependencies

one page on assumptions and dependencies (9.5.7)




3.1 External interfaces 

See 9.5.10. for most systems this will be around one page.

Define all inputs into and outputs from the software system. The description should complement the interface
descriptions in 9.5.3.3.1 through 9.5.3.3.5, and should not repeat information there. 

Each interface defined should include the following content:
a) Name of item;
b) Description of purpose;
c) Source of input or destination of output;
d) Valid range, accuracy, and/or tolerance;
e) Units of measure;
f) Timing;
g) Relationships to other inputs/outputs;
h) Screen formats/organization;
i) Window formats/organization;
j) Data formats;
k) Command formats;
l) Endmessages. 


### Inputs:


#### Video Input
The purpose of the video input is to provide a feed of a street or intersection in order to visually see vehicles such as buses drive through the street/s and pass traffic lights. This input will be sourced from our clients at the Bus Factor. The video footage will be live from a mounted webcam/camera connected to computer. The video feed has to be accurate enough for machine learning techniques to be able to detect red lights and distinguish between the vehicles. A typical webcam (720p) should be sufficient for this. The video input will be intially passed in as a common video format (e.g. MP4) for testing/training the algorithm from pre-recordered sources. Later on, as we extend the video input to be live from the webcam, the input will depend on the particular webcam that the Bus Factor decides to use. Common webcam outputs (which will be our video input) include RGB, BGR, YUV, and many others. The final outcome will require the video footage to be live, and likely be around 24 frames per second for a standard webcam. It is likely that we will not need to analyze every frame of video, so may then only apply machine learning algorithm to specific frames from the video input. Hence having a lower FPS may also be sufficient, especially due to the slow movement of the vehicles through the intersection. Finally the footage will be fed into machine learning algorithm which will detect the colour of the lights, whether the vehicle bus or not, and other data. 


#### Training data input
The Purpose is to train the machine learning system to be able to distinguish between buses and other vehicles, as well as the colour of the red light, the stop/start light location, and location of bus in lane. Training data will simply be hours of video feed of the CBD, most likely in a common video format such as MP4 taken from the bus factor podcast or provided from our clients. Using bus factor videos as training data may help increase accuracy of classification for our expected input due to the input being at the same camera angle, time of day, and location as the desired use of the the software that we are building. However, also training our classifier on different camera feeds, angles and locations may provide a more well rounded algorithm and prevent overfitting.


#### Input of traffic light location
Having a tool whereby the user could indicate the location of the traffic lights through an interface would enable more accurate and faster to implement detection of the current colour of the traffic light. Locating the specific traffic light may also help combat the multi-lane problem of having multiple lights for multiple lanes resulting in confusion in classification. As the bus factor isn't at a multi-lane area this issue may not be of much concern, but may be useful for future use and if the bus factor decided to move their viewing location. The source of the bounding box will be through a user interface that allows the user to drag or click to select over the desired area.

#### Input for traffic line crossing line
Having a tool whereby the user could indicate the line where vehicles cross the traffic light could make the basic image processing of whether the vehicle is running the red light or not far easier. This line would be made up from two points that the user would place down through the user interface. This line would define the crossing point of the line.

### Outputs: 

--Written by Sean with mild edits by myself

* Training data weights
* Alert (Box + red light)
* Info of scene 
    * Time/Date
    * License plate
    * Image/video of moment

#### Training data weight output
If machine learning is required we will be gathering output from the training in the form of weights and biases that will influence and classify future input. This will be used to set up the camera and it will autodetect the intersection layout from a variety of angles. If the weights and biases are fine tuned enough we should have a good system for detection. The program will be the recipient of the output, as the output is fed back in for more training and testing. The output will need at least a 90% tolerance for how accurately the output is used to detect whether the bus has passed a red light.

#### Alert from trigger
An alert should be issued via email, push notification or through the software when a bus runs a red light. The user/s of the system should recieve an alert when this issue occurs. For every valid instance of detection the alert should be sent. To measure this we would provide the system with false positives and see if it detects a static image of the offense, and ergo issues the email/alert to the user.
	
#### Info of scene
The moment of the red light breach there should be data taken of the time, data and a visual of the scene (image or video). This data would be outputted (Emailed or provided) to the user via a server which would host the images and metadata. With every instance of detection, this information should be captured. Testing measurements would involve visually inspecting the data and comparing to real time to see if there are any discrepancies of when it is and is not outputting the signal.




FUNCTIONS:


###### 5. Requires MVP Use Case 1, boots software, selects and adds bus line of detection
Goal statement: For the user to be able to place down two points by clicking twice. The goal for this would be to provide the system with the two points for a line that can be shown both visually, and internally processed. 

Use Case Body
Summary: This use case describes the interactions between the user and the system when utilizing the line tool.
Actors: User (primary), System (secondary)
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
1. User navigates to software and opens/starts it. | 2. System boots software.
3. User navigates to line tool and clicks two times on the visual feed to place down points.  | 4. System updates screen to show line that is made from those two points. Line vector is internally added to system for later use with bus detection. 


Alternative Scenarios:

A1: User clicks on wrong point/s

*Actions of actors:* | *Actions of system:* 
--- | ---
3. User navigates to line tool and clicks two times on the visual feed to place down points. | 4. System updates screen to show line that is made from those two points. Line vector is internally added to system for later use with bus detection. 
5. User presses on refresh button, to remove any currently placed objects on screen.  | 6. System removes lines and any other placed objects.



###### 6. Requires MVP Use Case 1, boots software, selects and deletes bus line of detection
Goal statement:

Use Case Body
Summary:
Actors:
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
*Still* | `renders` 
1 | 2 

###### 7. Requires MVP Use Case 1, boots software, selects and updates bus line of detection
Goal statement:

Use Case Body
Summary:
Actors:
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
*Still* | `renders` 
1 | 2 




