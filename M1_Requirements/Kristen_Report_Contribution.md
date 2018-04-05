#Project Proposal

# 5.1 Schedule

Identify dates for key project deliverables: 
-Client meetings (rouhgly once every 3 weeks)
-Own pr
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


###External Requirements

1. Ethical Requirements 
   - Security of data. 
   - Protect peoples privacy; includes the bus drivers and the pedestrians on the bus or on the streets surrounding intersections.
   - Can't release data like license plates to the wrong people.
   - Create product according to clients wants and needs.
   - Product ethics: be aware of entities that are filmed. 
2. Legislative Requirements???
3. Regulatory Requirements
   - (Write everything that the client expects us to do??)


###Product Requirements

 
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

##Product Requirements

In order to meet the expectations of the ZX Security clients, the product created 
throughout the Bus Factor project must meet a range of requirements. Such requirements
include the the usability, efficiency, usability and security of the product. 
By considering these factors when creating the product, we will be able to produce 
a programme which completes the specified goals at a high quality standard.

**Usability Requirements**

As with any software tool it is important for the Bus Factor programme to implement
a high level ease-of-use into the programme. The outputs of the programme will depend
on the traffic lights and intersections selected by the user. Therefore, to achieve
a satisfactory output it is important that the program can be easily followed and the
UI easily manipulated by the user. This will require us to implement a small amount
of controls into our user interface (UI) which will be paired with sufficient instructions
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

**Dependency Requirements**

It is important for any software project to implement a high level of maintainability 
within its code. This allows future reviewers or users of the code to easily change 
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
Javadocs where necessary. Methods must also contain a small amount of cod and only perform minimal
functionalities. In addition to maintainable code, the programme itself must be able to function
across a range of contexts. For example, the user must be able to use the programme with any video 
input which provides an appropriate intersection. 

**Security Requirements**


The security of the project and the information gathered from it is a functional requirement which the 
team must hold in high regard. The code of the programme we are developing will be open-source, therefore, 
the team will not have to worry about who can access our code when it is complete. 
As previously mentioned in section (Space Requirements), the programme will store video files and
static images of the events that occur. These video files will be filmed on public property, therefore
can legally be accesible by anyone (*add reference?*). However, as an additional feature the output files may 
be password protected if the user wishes to do so. (*Check with group*).
Prior to completion the team must protect the privacy of the project information. This includes the information 
about or gathered from clients, discussions amongst the group and any documents which are not included in the
programmes source code. In order to protect this data, the team will only use protected discussion 
platforms which are monitored by ECS department members. 

###External Requirements


**Ethical Requirements**


1. Releasing private vehicle's license plates. 
2. Releasing bus license plates. 
3. Releasing footage of people around the interface.  

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
   - 
3. Dependency Requirements
     - Must be maintainable, code can be easily changed in future for other users as this is an open source project??
     - Classes can't depend too much on each other so they can be easily separated and possibly independantly tested. 
     - Programme and information regarding red light running must be readily available to users. 
     - Must be reliable. This will give us accurate data about running red lights and make sure that the event isn't missed. 
     - Must be easy to change video input, programmw can be used across multiple intersections. 
 
   



