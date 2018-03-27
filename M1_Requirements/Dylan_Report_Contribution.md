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

Amazon AWS 


Best case table:

1. Processing power (Graphics card)


Worst case table:





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


1.
a) Video Input
b) Purpose to view a feed of the CBD in order to view buses/vehicles drive through the streets and pass the lights. 
c) Input will be sourced from clients. This footage will be live from a mounted webcam/camera connected to computer.
d) Video feed has to be accurate enough for machine learning techniques to be able to detect red lights and distinguish between
vehicles.
e) 
f) Video footage will be live, 24 fps 
g) Footage will be fed into machine learning algorithm which will detect the colour of the lights, whether the vehicle bus or not,
and other data. 


2. 
a) Training data input
b) Purpose to train the machine learning system to be able to distinguish between buses and other vehicles, as well as the colour of the 
red light, the stop/start light location, and location of bus in lane. Training data will simply be hours of video feed of the CBD, most likely
taken from the bus factor podcast. Using bus factor videos as training data may help increase accuracy of classification for our expected input 
due to the input being at the same camera angle, time of day, and location as the desired use of the the software that we are building. However, 
also training our classifier on different camera feeds, angles and locations may provide a more well rounded algorithm.
b) Input training data will be provided from clients

3.
a) Input of traffic light location
b) Having a tool whereby the user could indicate the location of the traffic lights through an interface would enable more accurate and easier detection of the current colour of the traffic light, as well as help combat the multi-lane problem of multiple lights for multiple lanes.
As the bus factor isn't at a multi-lane area this may not be such a big issue, but may be useful for future use and if the bus factor ever moved their viewing location.
c) The source of the bounding box will be through a user interface that allows the user to drag or click to select over the desired area.
d) 

4. 
a) Input for traffic line crossing line
b) Having a tool whereby the user could indicate the line where vehicles cross the traffic light could make the basic image processing of whether
the is running the red light or not. 
c) This line would be made up from two points that the user would place down through the user interface. This line would define the crossing point of the line.




4.
a) Machine learning output
b) Should 

3. 
a) 



