### 3.7 Software system attributes

## 3.7.1 Product Requirements

In order to meet the expectations of the ZX Security clients, the product created throughout the Bus Factor project must meet a range of requirements. Such requirements
include the the usability, efficiency, usability and security of the product. By considering these factors when creating the product, the team will be able to produce 
a programme which completes the specified goals to a high quality standard.

### 3.7.1.1 Usability Requirements

As with any software tool it is important for the Bus Factor programme to implement a high level ease-of-use into the programme. The outputs of the programme will depend
on the traffic lights and intersections selected by the user. Therefore, to achieve a satisfactory output it is important that the program can be easily manipulated by the
user. This means that a user should be able to easily select an intersection or light using their mouse and the programme will only select the wanted area. 

In order to increase ease of use, the team will implement a small amount of controls into our user interface (UI) which will be paired with sufficient instructions
on how to use these controls. The programme will also be responsible for providing a notification to the user when the "red-light running" incident occurs. To increase usability 
in this aspect the user must be able to easily access information about the incidents after they have been notified. In order to do this, the team must implement an easily accessible
storage space for this information or send such information to a space specified by the user. 

### 3.7.1.2 Efficiency Requirements

#### 3.7.1.2.1 Performance 

In order for the Bus Factor programme to meet its requirements it must complete its tasks at a high speed. The main functionality of the programme is to be able 
to detect when a bus runs a red light and to notify the user of this event. In order to maintain a high level of efficiency the programme must detect and report
on the incident with a fast response time. This is important as the time at which the event occured must be accurate for the user. It is also important the the user
is notified of the event quickly in order for them to take further action as fastas possible. These actions may include emailing the bus company to alert them of 
the event. 

The Bus Factor project must also perform with a high level of accuracy. Therefore, it must accurately detect when an incident occurs and identify the entity 
which has caused it. It must also accurately report back to the user in order to give them the correct information about the incident. If the program does not fulfill these
requirements it has the potential to accuse the wrong entity of causing the incident. This may have detrimental consequences when making this information known to the 
listeners of the podcast or bus company. 

#### 3.7.1.2.2 Space Requirements

The Bus Factor programme is planned to initially be set up by the user then run in the background of their device. As the amount of memory taken up by the programme will affect the speed
at which a device is run, it is important for the programme to use as little memory as possible. In order to do so, the team must consider the amount of memory the features of the programme 
take up and how this can be decreased where possible. Part of the features of the planned programme includes the ability to store static images and video clips of an incident when it happens. 
Therefore, it is important for the programme to efficiently store these files in order to decrease the amount of memory used. 

### 3.7.1.3 Maintainabilty

It is important for any software project to implement a high level of maintainability within its code. This allows future reviewers or users of the code to easily change, add 
or extract parts of it to use themselves. As this project contains open-source code it is likely that it's uses will extend from the context of the Bus Factor. Therefore, 
it is important that this project has a high level of maintainability. This will also be beneficial to the team as we develop and improve on our code. After completing
the minimal viable product, the team plans to extend the programme to contain more features. Keeping a maintainable code will allow for us to do this easily without 
having to change the code which has already been written. 

To keep a maintainable code, the programme must display low coupling between it’s elements. This means the team must create classes which include little to no dependencies on
other classes. The code must also be easily readable, therefore, using appropriate variable and method names and Javadocs where necessary. Methods must also contain a small 
amount of code and only perform minimal functionalities. The maintainabilty of the programme will also promote reusabilty. If the client wishes to use parts of the programme 
in future projects the future programmer should have the abilty to easily extract parts of the code due to low coupling between its elements.

### 3.7.1.4 Flexibility

As part of the product, the programme itself must be able to function across a range of contexts. The final Bus Factor programme must have the ability to monitor different 
intersections, whilst only selecting one set of lights and stop line at a time. Therefore, the programme must have the flexibilty to take a range of different 
inputs. The final product must also have the flexibilty to use live input files from a webcam as well as a video file. 

### 3.7.1.5 Security 

The security of the project and the information gathered from it is a functional requirement which the team must hold in high regard. The code of the programme we are developing 
will be open-source, therefore, the team will not have to worry about who can access our code when it is complete. As previously mentioned in section 3.7.1.2.2, the programme will 
store video files and static images of the events that occur. These video files will be filmed on public property, therefore, can legally be accesible by anyone who is not using such images for commercial use [2]. 
However, the team intends to take an ethical approach when dealing with such footage and information, see section 3.7.2.1. 

Prior to completion the team must protect the privacy of the project information. This includes the information about or gathered from clients, discussions amongst team members
and any documents which are not included in the programmes source code. In order to protect this data, the team will only use protected discussion platforms which are monitored by ECS department members. 

### 3.7.1.6 Availability 

The Bus Factor project will produce a programme which uses video files or live camera inputs to monitor intersections. Consequently, the programme should be available to users who can provide this requirement. 
As part of the features of the minimum viable product for our project, the team aims to have the programme run on a Windows system. As a feature of the final product, the programme will run on Linux based system as
well. Therefore, the Bus Factor programme will be available to all users who are using these operating system. 

## 3.7.2 External Requirements

In conjunction with the product requirements, it is important that the team considers external requirements relating to the project. Such requirements which 
must be considered may include ethical practices behind the project and the rules and regulations which must be considered thorughout development. 

### 3.7.2.1 Ethical Requirements

In order to meet the ethical requirements for software development, the team must act according to the best interests of the clients, the public and the team members [1]. This will create a project which 
complies with the clients needs and creates a team environment which will promote productivity and communication. In order to meet the clients wishes the team will remain in constant communication with the client and 
will not make any choices which will largely affect the final product without first consulting the clients. The main method of communication between the team members and the clients will be through email. If further 
discussion is needed we will meet up with the clients when we believe necessary.

As previously mentioned in section (*Space Requirements & Security Requirements*) our programme will involve storing footage and images of people around the intersection. This cannot be avoided as the
busses and intersections will be located in a highly public area. According to the NZ Privacy Act the collection and use of images of individuals in a public space is considered legal, as long as such images
are not used for commercial use without the individuals consent. Although filming other individuals in a public space is legal, the team will take precausions to avoid offending the public when 
this footage is reviewed or used. In order to do this the programme will not display the individuals in a mocking or insulting way.  

Throughout our group project the team aims to use strong teamwork skills in order to produce a high quality product for our clients. To do this, the members will communicate their ideas to eachother 
when making decisions and will be respectful towards eachothers opinions. The team will also delegate work fairly and produce their work in a timely manner, therefore, not having an effect on the overall 
team's performance. 

### 3.7.2.2 Regulatory Requirements

Similarly with any software related product, the Bus Factor project must comply with a range of regulations and standards set by the clients, the team and other 
external rules. As previously stated in section (*Ethical Requirements*), the project will require us to consider the New Zealand Privacy Act [2] when using footage or images collected. As 
our clients do not intend to use such files commercially, the users will not need to be concerned about gathering permission from the individuals. 

Part of our project will involve integrating open CV and other external libraries into our code. Therefore, our program must comply with the licenses supplied by 
these libraries. Such licenses include the Open CV license agreement [3].

#Bibliography for Section 3.7 (if needed)

[1] https://www.computer.org/web/education/code-of-ethics
[2] https://www.privacy.org.nz/the-privacy-act-and-codes/privacy-act-and-codes-introduction/
[3] https://opencv.org/license.html

# 5.1 Schedule

## Project Deadlines

The assigned project deadlines are as follows:

| Item                  | Description                                          | Date     |
| :--------------------:|:----------------------------------------------------:|:--------:|
| Architecture Prototype| Document and demonstration of make up of programme.  |14/05/18  |
| Essay                 | Essay describing MVP and current project status.     |10/06/18  |
| Minimum Viable Product| Presentation for the minimum product developed.      |15/06/18  |

## Organised Timetable

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





