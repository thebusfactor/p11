ENGR 301 Project *11* Project Proposal and Requirements Document
#### Brandon Scott-Hill, Dylan Kumar, James Magallanes, Kristen Tait, Nicholas Snellgrove, Sean Stevenson

## 1. Introduction
One page overall introduction including sections 1.1 and 1.2.

### Client

Identify the client and their contact details

### 1.1 Purpose

One sentence describing the purpose of the system (9.5.1)

### 1.2 Scope

One paragraph describing the scope of the system (9.5.2)

### 1.3 Product overview 
#### 1.3.1 Product perspective

There have been multiple studies done on vehicles running red lights at intersections, with algorithms being created to detect whether a vehicle will run a red light, with accuracy over 90%. The Bus Factor project product can relate to systems currently in place in multiple countries – for example the United States of America and India – where there are cameras stationed to catch motorists running red lights. While the Bus Factor product is not going to be developed for commercial or government use, such as traffic enforcement, the project still holds similar requirements that it needs to detect the traffic light state and vehicles' positions in relation to the intersection/crossing.

The product is being produced for a podcast called The Bus Factor that incorporates a live stream video showing the intersection outside of the office building the hosts are situated. The angle that the camera is positioned at contrasts with the position the traffic cameras in countries around the world are – those of which the angle has been optimised for the detection and image capture of the vehicles travelling through the intersection. The way the camera used in the Bus Factor project is currently situated, the traffic light state is not easy to see – so the accuracy of the light and vehicle detection is unideal to be implemented on by image processing techniques. 

This lacklustre setup poorly compares to the commercial/governmental uses in countries around the world 


and the ability to predict dangerous events occurring seconds in advance. 

In terms of our specific project - making for bus factor stream/podcast

One page defining the system's relationship to other related products
(9.5.3. but not the subsections in the standard.)

#### 1.3.2 Product functions

The basic functionality for this product, as described by our Minimum Viable Product (MVP), is as follows:

1. The ability to detect the traffic light state and buses travelling through the video feed from a consumer webcam
2. Functionality for a User Interface so that a user can define areas of interest. Specified areas of interest include:
    - The bounding box of the traffic light and individual bounding boxes of each traffic light colour
    - The stopping line at the intersection for the system to detect when the bus passes over it

3. The ability to output a static image that has been created once the system detects a traffic violation by bus 
4. That the system works on a Windows operating system. 

A consumer webcam is defined as a readily available camera that one may commonly find in-built in laptops or as an external USB camera.


One page summary of the main functions of the product (9.5.4),
briefly characterising the minimum viable product.

#### 1.3.3 User characteristics   

One page identifying the main classes of users and their
characteristics (9.5.5) 

#### 1.3.4 Limitations

One page on the limitations on the product (9.5.6)

## 2. References

References to other documents or standards. Follow the IEEE Citation Reference scheme, available from the [IEEE website](https://www.ieee.org/documents/ieeecitationref.pdf) (PDF; 451 KB).
(1 page, longer if required)

## 3. Specific requirements  

20 pages outlining the requirements of the system.
You should apportion these these pages across the following 
subsections to focus on the most important parts of your product.

### 3.1 External interfaces

See 9.5.10. for most systems this will be around one page.

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

Minimum Use Case Diagram

![MVP Use Case Diagram](https://gitlab.ecs.vuw.ac.nz/ENGR301-302-2018/Project-11/Bus-Factor/blob/master/M1_Requirements/mvpDiagram.png?raw=true "MVP Use Case Diagram")

Minimum Viable Product Use Cases
###### 1. User sets up camera, user navigates to software and runs it
This use case is the only non-functional case our system has, which involes no software but the user making sure the camera is set-up in a manner allows for an unempeded view of the intersection. The goal for this would be for a successful detection of the bus and lights.
Validity check: There is no input check that can be performed on this case due to the nature of it, as it requires the user to check the intersection is in view. 
Effect of Parameters: No parameters seem evident that would effect the input.
Relationship of input and output: This is the main source of input for the software and pertains to all output. 

**Use Case Body**
Summary: User acquiring camera, plugging it in and checking output
Actors: Client/General user
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
1. User acquires camera | 
2. User plugs in and angles camera at intersection | 

###### 2. Requires MVP Use Case 1, Selects and adds traffic light area of detection
User should define the area of decetion for the traffic lights. This is for the software to search purely in this area, to cut down on processing time and increase accuracy of the detection. 
Validity check: Due to the nature of traffic and lights, you may get an intersection that never sees any action, or the event doesn't trigger at all. In this case it may be good to have a validity check for when there is no action detected but that is yet to be determined.  
Exact sequence: Interface shows video feed of area, user inserts shape of detection.
Effect of Parameters: If the user doesn't not have a working mouse they cannot proceed past this point.
Relationship of input and output: 

**Use Case Body**
Summary: User acquiring camera, plugging it in and checking output
Actors: Client/General user
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
1. User acquires camera | 
2. User plugs in and angles camera at intersection | 

###### 3. Requires MVP Use Case 1, Selects and deletes traffic light area of detection
This use case is the only non-functional case our system has, which involes no software but the user making sure the camera is set-up in a manner allows for an unempeded view of the intersection. The goal for this would be for a successful detection of the bus and lights. 

Validity check:  
Exact sequence: 
Effect of Parameters: If the user does not have a working mouse they cannot proceed past this point.
Relationship of input and output: 

**Use Case Body**
Summary: User acquiring camera, plugging it in and checking output
Actors: Client/General user
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
1. User acquires camera | 
2. User plugs in and angles camera at intersection | 

###### 4. Requires MVP Use Case 1, Selects and updates traffic light area of detection
This use case is the only non-functional case our system has, which involes no software but the user making sure the camera is set-up in a manner allows for an unempeded view of the intersection. The goal for this would be for a successful detection of the bus and lights. 

Validity check:  
Exact sequence: 
Effect of Parameters: If the user does not have a working mouse they cannot proceed past this point.
Relationship of input and output: 

**Use Case Body**
Summary: User acquiring camera, plugging it in and checking output
Actors: Client/General user
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
1. User acquires camera | 
2. User plugs in and angles camera at intersection | 

###### 5. Requires MVP Use Case 1, Selects and adds bus line of detection
Goal statement:

Use Case Body
Summary:
Actors:
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
*Still* | `renders` 
1 | 2 

###### 6. Requires MVP Use Case 1, Selects and deletes bus line of detection
Goal statement:

Use Case Body
Summary:
Actors:
Main Success Scenario:

*Actions of actors:* | *Actions of system:* 
--- | ---
*Still* | `renders` 
1 | 2 

###### 7. Requires MVP Use Case 1, Selects and updates bus line of detection
Goal statement:

Use Case Body
Summary:
Actors:
Main Success Scenario:

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

Extension Goal(s) Use Cases
###### 1. Requires End Goal Use Case 1, Upon booting of software user can define additional points of interest to keep track of
Description: As part of the possible extension to this project, 
Validity check: Since these events like License plate detection, police interfention, speed detection validity checks would need to occur to make sure the values and assumptions made are performing above an expected
correctness threshold (Assuming a baseline of 90%).
Exact sequence: Run software -> Software auto-detects the environmental interest points -> Runs and logs additional event, alerts user
Effect of Parameters: If an obstruction interferes with the camera the software should alert it has lost the points of interest. Instances of each event need to be recorded to perform statistical analysis.
Relationship of input and output: Video feed input is scanned for points of interest -> Additional event is logged and user alerted.

### 3.3 Usability Requirements

See 9.5.12. for most systems this will be around one page.

### 3.4 Performance requirements

See 9.5.13. for most systems this will be around one page.
Hardware projects also see section 9.4.6.


### 3.5 Logical database requirements

See 9.5.14. for most systems, a focus on d) and e) is appropriate,
such as an object-oriented domain analysis. You should provide an
overview domain model (e.g.  a UML class diagram of approximately ten
classes) and write a brief description of the responsibilities of each
class in the model (3 pages).

### 3.6 Design constraints

There are not many constraints on our project, only some of the ones that might hinder our development of the system would be the hardware we use (cameras), and the requirement to output instances of traffic violation to image and video files.
The rest of the specifications for the project do not restrict our development 
- Runs on Windows operating system (no other operating system support required)
- Eventually the system should be able to operate on a Linux operating system 
- Detecting objects through consumer camera (not the best/highest quality)
- Recognising when a traffic violation occurs and outputting the instance it occurs as a static image (ideally capturing licence plate, full view of vehicle)
- The system should also be able to output the incidence of the violation into a video format (a short clip of when the offender performs the violation)
- The current operation only considers one angle of the intersection
- Software has feature for user to input areas to define the intersection (User can define the stop line, the trafic lights, and therefore the system can detect when a vehicle has illegaly passed the stop line)
- Software can also automatically detect intersection elements
- Functionality for the user to input custom codes to specify certain events when they occur. At the beginning of the program the user should be able to modify said event codes to whatever is desired. 

Extras
- Licence plate detection
- Specific events of interest: Police intervention, Bus collisions with pedestrians, Vehicle near misses with pedestrains/other vehicles
- Integration with Open Broadcaster Software (OBS) (System that the clients use to run their podcast)
- Statistics predicting likelihood of events occurring based on time, weather etc.
- Object detection extended from just buses to other vehicles such as motorbikes, cars, cyclists etc
- Ability to report traffic violation statistics of certain vehicles to external company (Traffic authority or parent bus company)
- Speed detection


see 9.5.15 and 9.5.16. for most systems, this will be around one page.

### 3.7 Software system attributes

##Product Requirements

In order to meet the expectations of the ZX Security clients, the product created 
throughout the Bus Factor project must meet a range of requirements. Such requirements
include the the usability, efficiency, usability and security of the product. 
By considering these factors when creating the product, we will be able to produce 
a programme which completes the specified goals to a high quality standard.

**Usability Requirements**

As with any software tool it is important for the Bus Factor programme to implement
a high level ease-of-use into the programme. The outputs of the programme will depend
on the traffic lights and intersections selected by the user. Therefore, to achieve
a satisfactory output it is important that the program can be easily manipulated by the
user. This means that a user should be able to easily select an intersection or light 
using their mouse and the programme will only select the wanted area. 
In order to increase ease of use, the team will implement a small amount of controls 
into our user interface (UI) which will be paired with sufficient instructions
on how to use these controls. The programme will also be responsible for providing a 
notification to the user when the "red-light running" event occurs. To increase usability 
in this aspect the user must be able to easily access information about the events 
after they have been notified. In order to do this, we must implement an easily accessible
storage space for this information. 

**Efficiency Requirements**

*Performance Requirements*

In order for the Bus Factor programme to meet its requirements it must completing 
its tasks at a high speed. The main functionality of the programme is to be able 
to detect when a bus runs a red light and to notify the user of this event. In 
order to maintain a high level of efficiency the programme must detect and report
on the event with a good response time. This is important as the time at which
the event occured must be accurate for the user. It is also important the the user
is notified of the event quickly in order for them to take further action as fast
as possible. These actions may include emailing the bus company to alert them of 
the event. The Bus Factor project must also perform with a high level of accuracy. 
herefore, it must accurately detect when an event occurs and identify the entity 
which performed it. It must also accurately report back to user in order to give 
them the correct information about the event. If the program does not fulfill these
requirements it has the potential to accuse the wrong entity of performing the event. 
This may had detrimental consequences when making this information known to the 
listeners of the podcast or bus company. 

*Flexibility*

As part of the product, the programme itself must be able to function across a range
of contexts. The final Bus Factor programme must have the ability to monitor different 
intersections, whilst only selecting one set of lights and stop line at a time.
Therefore, the programme must have the flexibilty to take a range of different 
inputs. The final product must also have the flexibilty to use live input files from 
a webcam as well as a video file. 

*Space Requirements*

The Bus Factor programme is planned to initially be set up by the user then run
in the background of the users device. As the amount of memory taken up by the 
programme will affect the speed at which a device is run, it is important for our 
programme to use as little memory as possible. In order to do so, we must consider
the amount of memory the features of our programme take up and how we can decrease
this where possible. Part of the features of our planned programme includes the 
ability to store static images and video clips of an event when it happens. Therefore, 
it is important for the programme to efficiently store these files in order to decrease
the amount of memory used. 

**Maintainabilty**

It is important for any software project to implement a high level of maintainability 
within its code. This allows future reviewers or users of the code to easily change, add 
or extract parts of it to use themselves. As this project contains open-source code
it is likely that it's uses will extend from the context of the Bus Factor. Therefore, 
it is important that this project has a high level of maintainability. This will 
also be beneficial to the team as we develop and improve on our code. After completing
the minimal viable product, the team plans to extend the programme to contain more
features. Keeping a maintainable code will allow for us to do this easily without 
having to change the code which has already been written.
To keep a maintainable code, the programme must display low coupling between it’s elements. 
Thi means the team must create classes which include little to no dependencies on other classes.
code must also be easily readable, therefore, using appropriate variable and method names and
Javadocs where necessary. Methods must also contain a small amount of code and only perform minimal
functionalities. 
The maintainabilty of the programme will also promote reusabilty. If the client wishes
to use parts of the programme in future projects the future programmer should have 
the abilty to easily extract parts of the code due to low coupling between it's 
elements.

**Security Requirements**

The security of the project and the information gathered from it is a functional requirement which the 
team must hold in high regard. The code of the programme we are developing will be open-source, therefore, 
the team will not have to worry about who can access our code when it is complete. 
As previously mentioned in section (Space Requirements), the programme will store video files and
static images of the events that occur. These video files will be filmed on public property, therefore
can legally be accesible by anyone who is not using such images for commercial use [2]. 

However, the team intends to take an ethical approach when dealing with such footage and information 
(*see Ethical Requirements Section*). Prior to completion the team must protect the privacy of the project 
information. This includes the information about or gathered from clients, discussions amongst the group
and any documents which are not included in the programmes source code. In order to protect this data, 
the team will only use protected discussion platforms which are monitored by ECS department members. 

**Availability**

The Bus Factor project will produce a programme which uses video files or live camera inputs to monitor intersections. 
Consequently, the programme should be available to users who can provide this requirement. 
As part of the features of the minimum viable product for our project, the team aims to have the programme 
run on a Windows system. As a feature of the final product, the programme will run on Linux based system as
well. Therefore, the Bus Factor programme will be available to all users who are using these operating system. 

###External Requirements

*WRITE INTRO*

**Ethical Requirements**

In order to meet the ethical requirements for software development, the team must act according to 
the best interests of the clients, the public and the team members [1]. This will create a project which 
complies with the clients needs and creates a team environment which will promote productivity and communication. 
In order to meet the clients wishes the team will remain in constant communication with the client and 
will not make any choices which will largely affect the final product without first consulting the clients. 
The main method of communication between the team members and the clients will be through email. If further 
discussion is needed we will meet up with the clients when we believe necessary.

As previously mentioned in section (*Space Requirements & Security Requirements*) our programme will 
involve storing footage and images of people around the intersection. This cannot be avoided as the
busses and intersections will be located in a highly public area. According to the NZ Privacy Act the 
collection and use of images of individuals in a public space is considered legal, as long as such images
are not used for commercial use without the individuals consent. 
Although filming other individuals in a public space is legal, the team will take precausions to avoid offending the public when 
this footage is reviewed or used. In order to do this the programme will not display the individuals 
in a mocking *review* or insulting way.  

Throughout our group project the team aims to use strong teamwork skills in order to produce a high 
quality product for our clients. To do this, the members will communicate their ideas to eachother 
when making decisions and will be respectful towards eachothers opinions. The team will also delegate
work fairly and produce their work in a timely manner, therefore, not having an effect on the overall 
team's performance. 

**Regulatory Requirements**

Similarly with any software related product, the Bus Factor project must comply
with a range of regulations and standards set by the clients, the team and other 
external rules.
As previously stated in section (*Ethical Requirements*), the project will require us 
to consider the New Zealand Privacy Act [2] when using footage or images collected. As 
our clients do not intend to use such files commercially, the users will not need to 
be concerned about gathering permission from the individuals. 
Part of our project will involve integrating open CV and other external libraries 
into our code. Therefore, our program must comply with the licenses supplied by 
these libraries. Such licenses include the Open CV license agreement [3].

**Management**

*COMPLETE*

#Bibliography for Section 3.7 (if needed)

[1] https://www.computer.org/web/education/code-of-ethics
[2] https://www.privacy.org.nz/the-privacy-act-and-codes/privacy-act-and-codes-introduction/
[3] https://opencv.org/license.html


### 3.8 Physical and Environmental Requirements 

For systems with hardware components, identify the physical
characteristics of that hardware (9.4.10) and environment conditions
in which it must operate (9.4.11).  Depending on the project, this
section may be from one page up to 5 pages.

### 3.10 Supporting information

see 9.5.19. 

## 4. Verification

5 pages outlining how you will verify that the product meets the
most important specific requirements. The format of this section
should parallel section 3 of your document (see 9.5.18).
Wherever possible (especially systemic requirements) you should
indicate testable acceptance criteria.

## 5. Development schedule.

### 5.1 Schedule

##Project Deadlines

The assigned project deadlines are as follows:

| Item                  | Description                                          | Date     |
| :--------------------:|:----------------------------------------------------:|:--------:|
| Architecture Prototype| Document and demonstration of make up of programme.  |14/05/18  |
| Essay                 | Essay describing MVP and current project status.     |10/06/18  |
| Minimum Viable Product| Presentation for the minimum product developed.      |15/06/18  |

##Organised Timetable

In order to complete the Bus Factor project to a high standard, the team have 
agreed to allocate at least 8 hours per week to work on it. This 8 hours does 
not include personal time which the team members may use to further work on 
the project to meet deadlines. 

The team will meet twice at week for two 4-hour long labs. These labs will be
used for group discussions and to work on project assignments. 

| Lab 1    | Lab 2 |
|----------|-------|
|Wednesdays|Fridays|
|9:00-     |9:00-  |
|13:00     |13:00  |

In order to meet product requirements the group will meet or be in contact with
the ZX security clients approximately once every 3 weeks. These discussions will 
be used to ensure that the product meets the clients requests and to ask additional 
questions about the product. 


### 5.2 Budget

Present a budget for the project (table), and justify each budget item
(one paragraph per item, one page overall). 

### 5.3 Risks 

Identify the ten most important project risks: their type, likelihood,
impact, and mitigation strategies (3 pages).


## 6. Appendices
### 6.1 Assumptions and dependencies 

one page on assumptions and dependencies (9.5.7) 

### 6.2 Acronyms and abbreviations

* Incident: Refers to a bus being observed running a red light, as captured by the software.

## 6. Contributions

* Brandon Scott-Hill: 3.3 Usability Requirements, 3.4 Performance Requirements, 3.5 Logical Database Requirements (Total Page Count: 4-5 Pages)
* Dylan Kumar: 5.2 Budget, 3.2 Functions, 6.1 Assumptions and Dependencies, 3.1 External interfaces (Total Page Count: 5-6 Pages)
* James Magallanes: 1.3 Product Overview, 3.6 Design constraints (Total Page Count: 5 Pages)
* Kristen Tait: 5.1 Schedule, 3.7 Software system attributes (Total Page Count: 5 Pages)
* Nicholas Snellgrove: 1.0-1.2 Introduction, 5.3 Risks (Total Page Count: 4 Pages)
* Sean Stevenson: 3.2 Functions (Total Page Count: 4 Pages)

---
