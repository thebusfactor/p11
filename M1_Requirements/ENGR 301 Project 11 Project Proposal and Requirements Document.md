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

One page defining the system's relationship to other related products
(9.5.3. but not the subsections in the standard.)

#### 1.3.2 Product functions

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

see 9.5.15 and 9.5.16. for most systems, this will be around one page.

### 3.7 Software system attributes

Present the systemic (aka non-functional) requirements of the product
(see ISO/IEC 25010).
List up to twenty systemic requirements / attributes.
Write a short natural language description of the top nonfunctional
requirements (approx. five pages).


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

Identify dates for key project deliverables: 
1. architectural prototype
1. minimum viable product
1. further releases

(1 page).

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
