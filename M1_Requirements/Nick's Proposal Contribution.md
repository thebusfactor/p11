## 1. Introduction

### Client

The clients for this project are Hugh and Stephen from ZX Security.
Contact Details:
Hugh: hugh@zxsecurity.co.nz

Stephen: stephen@zxsecurity.co.nz  
Hugh: hugh@zxsecurity.co.nz  

### 1.1 Purpose

The system must take a video input from any standard webcam, and from this input - detect when a bus is seen running a red light & report to the user in real-time.

### 1.2 Scope

The Bus Factor Project will produce a program which can be set up and run on any consumer-available computer, using a commercially available webcam.
The program should be able to run on both Windows and Linux devices, and work when set up at any intersection, from any angle.  
The program will take in a video input. It will then automatically detect the location & status of the red light
in the video, and automatically detect when a bus runs the detected red light. To do this, the state of the light 
must be automatically detected, and the boundary point for the intersection
(I.e. the line not to be crossed by the bus) should be either manually inputted or automatically detected.
When an offence is detected, the program should automatically trigger some sort of event to notify the user - 
either a pre-programmed event or some other user defined code.
Then, a short video clip of the offence should be saved, showing time before and after the offence. 
Extra potential features could include Licence Plate Detection, OBS Integration, Speed Detection of offending vehicles, Reporting events to local Traffic Authorities, 
or prediction/statistics based on factors such as time of offence, weather, or location.  
The software will be used exclusively by the clients to enhance their podcast - "The Bus Factor", by removing the need for them to manually observe and update their livestream
when an offence is detected.
There are no commercial applications for this program. Also, the clients require that the program be developed and released under an OSI-approved license.

---

### 5.3 Risks 

This section will identify the ten most important project risks: their type, likelihood,
impact, and mitigation strategies. These risks are not given in any particular order.

1. **Requirements - Low Risk, High Impact**  
There is a risk that this project may not have requirements and guidelines that are clear enough or demanding enough to facilitate a year-long project management project. 
A lack of clear, manageable requirements from the clients could have a negative impact on the team's ability to practise Project Management. 
As ENGR301 and 302 are at their core, designed to teach the practises of Project Management, this reduced opportunity could result in lower course grades on assessment items,
as the lack of proper requirements and client behaviour would translate to lower quality project management assessments.  
This risk is unlikely, due to the extensive support network offered by the university, senior managers, and lecturers. However, the consequence of such a risk is 
 high. Not only would the grades of the team suffer, but the learning opportunity offered by this real industry project would be essentially wasted, and the team's future
skills or assessments could suffer as a result.  
To mitigate this risk, communication will be established early with both the clients and the senior managers, to ensure that requirements sufficient to the scope of the
project are achieved. The client will be asked for a more substantial set of requirements, and from those requirements the team can scale back to a manageable project, using
the project management techniques of the course. Regular client meetings will be maintained to ensure that these requirements are accurate, and to discuss the progress on the project.

2. **Scope - Low Risk, Medium Impact**  
The clients could provide too many features that they want implemented and extended in the final product, rather than a core deliverable concept that
can be extended with additional features as they arise. Having such a feature bloat could potentially cause a significant time sink for the team, adding and implementing new features
constantly rather than working towards the specified project goals. Based on the initial client communication, this seems highly unlikely. The scope of the project is well-defined, and
there is a clear, core concept that can easily be extended upon. However, there is a risk that this will become a problem later, with more client communication throughout the project.  
This risk can be mitigated by keeping regular communication with the clients, ensuring that they have reasonable expectations from the team, and if necessary, involving the senior manager
to clarify miscommunications. Also, any communication regarding deliverables and extra features of the project should be confirmed in writing, and notes from each meeting should be kept
on the GitLab wiki for the project.

3. **Financial - Low Risk, Low Impact**  
Depending on the method that is used to implement the goals for this project, there could be requirements for processing power beyond that which the team has access to. Machine learning
techniques are a viable approach to the product, as manually writing code to classify and detect busses, intersections and traffic lights would be a monumental task on its own. 
Taking advantage of existing machine learning libraries suited to Image Processing/Computer Vision would make the project much more achievable.
However, this approach could result in unexpected financial requirements for the project, such as hardware capable of performing complex machine learning tasks, or access to a web server 
or physical server on which to perform the machine learning aspects of the project. 
This risk is unlikely, as the university likely has access to hardware setups that would be more than sufficient for this project. However, if these were not accessible by the team, 
other solutions would need to be explored, such as new hardware, or access to a webserver to perform the machine learning on (AWS, for example).  
By doing thorough research into the methods being used in the project, and to reduce the computational power required by the project, this risk could be mitigated. Clients will be
consulted for suggestions during this process, also. Robust testing can be used to ensure these hardware requirements are met.

4. **Licencing - Low Risk, Medium Impact**  
The requirements of this project given to us by the clients may require the use of technologies that are out of the grasp of the team members, such as machine learning, neural networks
or advanced Image Processing/Computer Vision techniques. However, the clients have required that the project be developed
and released under an OSI-approved licence. If the libraries used do not follow these criteria, the project would not be meeting the requirements of the client.  
This can be mitigated by ensuring that all team members understand fully what is required and expected when developing/releasing under an OSI approved licence. This should be researched 
and understood early, to avoid conflicts later. Also, any potentially useful library should be checked out to ensure that it meets these standards before it is approved for use in the 
project. 

5. **Technical Ability - High Risk, Medium Impact**  
Many of the potential solutions to the problems presented by this project require the use of technologies that may be beyond the technical ability of any of the team members. Initial research
into the problems presented by this project suggest that advanced image processing and computer vision libraries may need to be implemented to determine when an incident occurs. If none
of the team members were able to understand the required technology enough to implement it in the project, it would severely impact our ability to deliver on the client's requirements for the 
project. The team would need to scale back the requirements of the project to have some sort of presentable product. 
To handle this, the team should make sure to spend enough time carefully researching the technology required for the project to succeed, and should bring up any concerns/issues with the 
rest of the team as early as possible. Also, the research and development using these technologies should be a collaborative effort, to aid the group understanding of the system.
The team should also manage their expectations when selecting technology to use - use things they know they can handle, rather than deliberately going for the most complicated tech available.

6. **Dynamics of Deployment - Medium Risk, Medium Impact**  
This project is being based around an existing idea - the client's podcast. The clients use only one Point of View, overlooking one intersection, from one specific angle. To test the system
as it is being developed, the clients have offered to provide video files from this perspective. While this would allow for the team to develop and test the product according to the client's minimum
specifications, this one angle of one intersection will not provide the team with enough training data. The full requirements of the project state that the system must be deployable at any intersection, 
set up to work from any (feasible) video angle of the intersection. Without training video data of multiple angles of different intersections, it could be hard to develop the system to meet these robust
requirements, and in the worst-case scenario, the final product would only be deployable on a very particular intersection/angle combination. 
This is a likely risk to encounter, as neither the team nor the clients have immediate access to video footage of busses running different intersections. 
This risk can be mitigated by the team, by ensuring that the need for varied training data is communicated to the clients early, and by procuring our own video footage online, if necessary.

7. **Privacy - Low Risk, Low Impact**  
One of the core aspects of this project involves a continual camera feed overlooking a public space. While legally, there are no laws against filming or taking photos of people in a public space -  
(http://www.police.govt.nz/faq/what-are-the-rules-around-taking-photos-or-filming-in-a-public-place), 
there could be some moral issues among the team about filming people in a public space without their consent. Such moral issues could have a negative effect on a team members contribution to the project,
as they may not be as willing to work on some features of the product, or to implement features that go against their moral compass. This does not appear to be an issue in the early stages of the project,
while the Minimum Viable Product is being developed. However, this could become a risk later, as more features are introduced to the system. To counteract this, the team will ensure that before 
features are included in the product, that all team members and the clients are happy with how the feature will be implemented in an efficient & morally responsible manner. The client’s needs will take
priority, however.

8. **Team Absence or Disputes - High Risk, Medium Impact** 
The team will without a doubt run into issues surrounding team member availability, be it due to injury, illness, bereavement, or other academic or personal commitments. The team has agreed on a collaborative
approach when handling these issues. All team members have contributed to a team calendar, which shows when members are unavailable due to pre-existing commitments. Absent team members will review the notes from
any missed meetings before returning to the project and will try to understand the progress which has happened during their absence. 
When a team member is absent (for whatever reason) the rest of the team will contribute to split the missing team member's workload, to avoid any one member being overburdened.  
Also, there is a risk of disputes arising between team members during the project. If/when this occurs, the productivity of the team could be negatively impacted. Therefore, when a dispute arises, the 
team members not involved in the dispute should do their best to diffuse the situation, and if necessary, involve a senior manager to resolve the conflict. 

9. **Extended Team Absence (Drop out) - Low Risk, Very High Impact**  
Given that this project is over the course of a whole academic year, there is a chance that team members may (due to personal reasons or insufficient academic performance) resolve to leave university to pursue other goals - 
and as a result, leave the team without a member. While this risk seems highly unlikely, given the quality and convictions of the team members, the consequences of such an event would be very severe. The remaining team members
would have greatly increased pressure placed upon them and could be left in the dark about project information that the former team member held. This risk can be managed by the team members 'keeping an eye' on each other, 
and ensuring that they each have enough support to make it through the year. Failing that, the departing team member should ensure that they communicate all important information that they hold on the workings of the project.

10. **Time Management - High Risk, Medium Impact**  
There is a risk that, over the course of the project, the time required to implement new features and aspects is underestimated. This could lead to the team being unable to meet required deadlines, either academic or for deliverables for
the client. This is a likely risk, as the Engr301 course is (for most of the team members) the first proper introduction to project management, and therefore the team may be lacking in the time management skills required for a project
of this scope. The consequences of missing these deadlines/deliverables are severe - missing course deadlines would lead to team members having poor academic results, which could also result in poor morale in the team.
Missing deadlines for client deliverables makes the team and the university look bad and creates more pressure to make up these missed deadlines. 
This risk can be managed by using all the tools that are available to the best of the team's ability. Liberal issue tracking of deadlines (project related and otherwise) will allow the team members to manage their time effectively. Also, 
consistent, honest communication with the clients will ensure that expectations are managed between both parties.


### 3.8 Physical and Environmental Requirements 

The client's requirements dicate that the software must work with any commercially available webcam, and on any commercially available machine. The webcam component of the software could be
either built-in, or a separate peripheral, such as a USB connected webcam. To perform image recognition on the video footage, the webcam must be of a reasonable quality. Blurry or out-of-focus 
footage would be much more difficult to intepret, both visually and via image recognition or computer vision techniques. 
The camera (and by extension, the device running the software) must be positioned in such a way to have an unobstructed view of a given intersection, and in a secure place, so that the device cannot
be disturbed by any outside interference, be it extreme weather, human interference, or otherwise.  
Also, the camera must be set up in a position that allows it to capture all of the Points of Interest in an intersection. These Points of Interest are the Traffic Light being observed, the boundary of
the intersection, and the mid-point of the intersection I.e. where the busses cross through when going through an intersection.



