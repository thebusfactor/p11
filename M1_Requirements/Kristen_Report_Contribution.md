#Project Proposal

# 5.1 Schedule

Identify dates for key project deliverables: 
1. architectural prototype
1. minimum viable product
1. further releases

(1 page).


# 3.7 Software system attributes

Present the systemic (aka non-functional) requirements of the product
(see ISO/IEC 25010).
List up to twenty systemic requirements / attributes.
Write a short natural language description of the top nonfunctional
requirements (approx. five pages).


###Brainstorm

Performance – for example Response Time, Throughput, Utilization, Static Volumetric
Scalability
Recoverability
Serviceability
Regulatory
Manageability
Environmental
Data Integrity
Usability
Interoperability

###External Requirements

1. Ethical Requirements 
   - Security of data. 
   - Protect peoples privacy; includes the bus drivers and the pedestrians on the bus or on the streets surrounding intersections.
   - Can't release data like license plates to the wrong people.
2. Legislative Requirements???
3. Regulatory Requirements
   - (Write everything that the client expects us to do??)


###Product Requirements

1. Usability Requirements
/   - Must be easy for the user to interact with the programme. 
/   - Done by opening a programme which is linked to a webcam. User must be able to easily select a features of an intersection 
     including drawing a circle around the lights, drawing a line where the crossing is.   
/   - User must be notified of running red light. 
   - Must be used across Windows for MVP and Linux for end goal. 
2. Efficiency Requirements
   1. Performance Requirements
      - Programme must be fast enough to detect a bus running a red light and notify the user within a matter of minutes. 
      - Must read video inputs at a fast speed so the detection isn't delayed and inaccurate. 
      - Must notify user quickly (good response time).
      - Accuracy; Must detect the correct lights, must detect the correct colour, must accurately detect when the bus is crossing and not when 
        it's finishing crossing as  the light turns red.
    2. Space Requirements
     - Programme can't use too must memory as there could be a lot of things stored??
3. Dependency Requirements
     - Must be maintainable, code can be easily changed in future for other users as this is an open source project??
     - Classes can't depend too much on each other so they can be easily separated and possibly independantly tested. 
     - Programme and information regarding red light running must be readily available to users. 
     - Must be reliable. This will give us accurate data about running red lights and make sure that the event isn't missed. 
     - Must be easy to change video input, programmw can be used across multiple intersections. 
4. Security Requirements
     - Data gathered from busses running red lights should only be released to the appropriate users. 
     - When sending out emails to bus company after running red light (which will be an extra feature), need to make sure that the correct 
       information is sent to the correct people. 
     - Can't release data like license plates to the wrong people.

###Organizational Requirements

1. Environmental Requirements
   - (N/A)
2. Operational Requirements 
   - Must be able to run on Windows and Linux. (MVP Windows). 
   - Uses a commercial webcam as video input. 
3. Development Requirements.
   
#First Draft 

##3.7 Software System Attributes

###Product Requirements 

**Usability Requirements**

As with any software tool it is important for the Bus Factor programme to implement a high level ease-of-use into the programme. The outputs of 
the programme will depend on the traffic lights and intersections selected by the user. Therefore, to achieve a satisfactory ouput it is important 
that the program can be easily followed and the UI easily manipulated by the user. This will require us to implement a small amount of controls into our user interface (UI) which 
will be paired with sufficient instructions on how to use these controls.
The programme will also be responsible for providing a notification to the user when the "red-light running" event occurs. To increase usability in this 
aspect the user must be able to easily access information about the events after they have been notified. In order to do this, we must implement an easily 
accessible storage space for this information. 

**Efficiency Requirements**

*Performance Requirements*

In order for the Bus Factor programme to meet it's requirements it must deliver high speed performance when completing its tasks. The main functionality of the programme is 
to be able to detect when a bus runs a red light and to notify the user of this event. In order to maintain a high level of efficiency the programme must perform fast enough 
to detect the event. This is important as the time at which the event occured must be accurate for the user. It is also important the the user is notified of the event quickly 
in order for them to take further action as fast as possible. These actions may include emailing the bus company to alert them of the event. 

1. Performance Requirements
      - Programme must be fast enough to detect a bus running a red light and notify the user within a matter of minutes. 
      - Must read video inputs at a fast speed so the detection isn't delayed and inaccurate. 
      - Must notify user quickly (good response time).
      - Accuracy; Must detect the correct lights, must detect the correct colour, must accurately detect when the bus is crossing and not when 
        it's finishing crossing as  the light turns red.
    2. Space Requirements
     - Programme can't use too must memory as there could be a lot of things stored??

 - Must be easy for the user to interact with the programme. 
   - Must be used across Windows for MVP and Linux for end goal. 
   - Understandable UI. 
 
   



