## 1.3 Product Overview
### 1.3.1 Product Perspective

There have been multiple studies done on vehicles running red lights at intersections, with algorithms being created to detect whether a vehicle will run a red light, with accuracy over 90%. The Bus Factor project product can relate to systems currently in place in multiple countries – for example, the United States of America and India – where there are cameras stationed to catch motorists running red lights. While the Bus Factor product is not going to be developed for commercial or government use, such as traffic enforcement, the project still holds similar requirements that it needs to detect the traffic light state and vehicles' positions in relation to the intersection/crossing.

The system is being produced for a podcast called The Bus Factor that incorporates a live stream video showing the intersection outside of the office building the hosts are situated. The angle that the camera is positioned at contrasts with the position the traffic cameras in countries around the world are – those of which the angle has been optimised for the detection and image capture of the vehicles traveling through the intersection. The way the camera used in the Bus Factor project is currently situated, the traffic light state is not easy to see – so the accuracy of the light and vehicle detection is unideal to be implemented on by image processing techniques. 
This lackluster setup poorly compares to the commercial/governmental uses in countries around the world such as throughout the United States of America and India.


The user interface (UI) for The Bus Factor project would be uniquely designed for this system, not based off an existing product's UI. However, as the team may be incorporating the OpenCV library, there may be some specifications of the library that the UI may be required to hold. 
This could result in some similarities to other products' designs without intention. 

### 1.3.2 Product Functions

The basic functionality for this product, as described by our Minimum Viable Product (MVP), is as follows:

1. The ability to detect the traffic light state and buses travelling through the video feed from a consumer webcam
2. Functionality for a User Interface so that a user can define areas of interest. Specified areas of interest include:
    - The bounding box of the traffic light and individual bounding boxes of each traffic light colour
    - The stopping line at the intersection for the system to detect when the bus passes over it

3. The ability to output a static image that has been created once the system detects a traffic violation by bus 
4. That the system works on a Windows operating system. 

A consumer webcam is defined as a readily available camera that one may commonly find in-built in laptops or as an external USB camera.
Certain basic functionality for the MVP will be extended for the final product such as the ability to output a static image when a traffic violation is detected. For the final product this will be extended to output a short video file of the instance the violation occurred - ideally capturing the licence plate too).
Another beneficial function to the system is for the user to input custom codes to specify certain events when they occur. At the beginning of the program the user should be able to modify said event codes to whatever is desired. This builds on top of the basic UI requirements to ensure the user gets as much information as desired. 
Part of the system may have machine learning incorporated for added functionality such as statistics predicting the likelihood of certain events occurring based on time or weather. These events may include traffic violations or collisions.


### 1.3.3 User Characteristics
identify traffic light, stop lines - intersection
setting up camera


### 1.3.4 Limitations
Initially the team would get the product working to the current setup the client has for their podcast. This setup has many limitations for the team to consider to fulfill the Minimum Viable Product (MVP).
The current setup for the client's podcast has a low quality camera setup to point out of their office window towards an intersection. The off-angle positioning of their office is unideal for the detection of objects.
Only one of the intersection's stop lines are visible, the licence plates are illegible and the video quality is sub-optimal. This requires the object detection software the team will utilise to be very accurate to correctly capture the desired vehicles.

The team will be using the OpenCV library for the object detection, that of which the accuracy of the object detection is very high (assuming the correct data has been used for the AI training). 
While the team would ideally use a high quality camera for the video feed the software should work for all levels of camera quality, camera angle and intersection layout (the visibility of the traffic light states and the stop lines).
In order for the software to meet these requirements to operate in all generic scenarios, the team would need to 

## 3.6 Design Constraints

This project does not have many constraints that would hinder the development of the project. Some of the only constraints that the team might need to consider when designing the system would be the hardware (cameras) used, and the requirement to output instances of traffic violation to image and video files.
The rest of the specifications for the project do not restrict the development and should not hinder any ability to fulfill the client's specifications. 

Some minor constraints for the system that the team needs to take into account are the following:
- The software runs on Windows operating systems (eventually the system should additionally be able to operate on Linux operating systems).
- The current operation only considers one angle of the intersection, we would need to create our system for a general case so it can be used at any intersection, at any angle.
- The basic version of the system allows the user to input certain key areas such as the traffic light and the stopping line at intersections. This project group would also need to ensure that the system can automatically detect these objects without the user having the specify their location on the video feed.

Some of the extra functionality that the team has considered to be part of an end product may also need to be taken into consideration.
Certain extra functions such as accurate licence plate detection, speed detection and identifying specific events of interest may become constraints that the team needs to take note of.
These specific events of interests include scenarios of police intervention, vehicle collisions with pedestrians and vehicle near misses with other objects (mainly pedestrians and other vehicles).
These events of interest could be quite difficult to integrate into an already existing version of the system and may result in a design constraint that the team would encounter. 










