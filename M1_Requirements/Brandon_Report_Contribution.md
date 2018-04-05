## 3.3 Usability Requirements
The usability of the final product should meet both the requirements & objectives expected of the client including the usability needs of stakeholders. These usability requirements & objectives split up into three different criteria measurable effectiveness, efficiency and satisfaction criteria based in the context of use of bus factor software program.

### Measurable Effectiveness
The quality of the software program while being used from the stakeholder perspective defined as how effective the software program is at performing it’s intended task.  Hence for the bus factor project to meet usability requirements & objectives the product will need to perform it’s intended task effectively. 
*	Required at least a 90% accuracy detection rate on buses passing red lights. If the product didn’t have a good level of accuracy, the product would appear broken or unusable from a stakeholder perspective. Accuracy requirements will also apply to the end goal of detection of buses occurring with undefined hardware, intersections, and angles. 
*	Number plate letter digitalization will be required to have a 95% confidence that digitalization is correct else the software program should refuse to produce a letter sequence of the plate. The confidence requirement stops false reports of number plates that didn’t skip red lights. If false reports of number plates would to frequently occur, stakeholder’s confidence in the accuracy of the software would reduce significantly.
*	Video moments generation of when buses are crossing red lights are required to have 90% accuracy when generating video clips of the bus that crossed the red light. If the video clips didn’t include the correct bus, the software product would appear buggy to stakeholders. 

### Efficiency
How efficient the software program is at performing the task of detecting buses running red lights will affect the stakeholder’s opinion on the usability of the software product. The efficiency of the software program defined on how well the software uses its hardware resources and how quickly software calculations take.
*	All user input is required to have a response time 0.1 seconds ensuring the software program appears to be reacting instantaneously; this includes all background calculations necessary to generate some form of response. If the response takes longer than 0.1 seconds with user input, the software program will feel clunky to stakeholders.
*	The bus factor software program objectively should not be using more than 20 percent CPU and will be required to feel more of a passive user of the CPU and not the main user. If the software program felt like the main user of the CPU, it would make the software product feel badly designed and not fit for use.
*	Flagging of buses passing red lights are required to take no longer than 0.5 seconds. If the flagging process takes too long the software product will feel inaccurate and performing its task ineffectively to stakeholders. 

### Satisfaction
Satisfaction of the user using the software product will be defined based on their experience with the software product which directly affects the usability of the software product to the stakeholder. For the user to be satisfied with the product, it must perform detection of buses running red lights as expected by the user and be pleased with the experience of getting the product doing the detection task. 
*	Required at most five mouse button presses for installing the software product. While most users will have some technical background, the experience of using the product should be easy. If the process of installation was too long, it could result in stakeholders not bothering to use the software product at all. 
*	Required that any form of necessary input with the software product while running is self-intuitive. Input also includes configuration input such defining areas of where the traffics lights will be. If the input system is found unintuitive by stakeholders, the satisfaction of stakeholders will be affected reducing the usability of the software product.
*	The user-defined code system will be required to take no longer than ten mins to understand for the average programmer; ensuring that the user-defined code system will be usable to an average programmer. If the user-defined code system took too long to understand due to the complexity the experience for the programmer would be negatively affecting their satisfaction with the software product hence reducing the usability. 

## 3.4 Performance Requirements
The performance of the final software product should meet the standards of stakeholders, so that experience of using the software product is a usable experience.  Performance requirements of a software project split into two different parts static numerical requirements & dynamic numerical requirements. 

### Static Numerical Requirements
Static performance requirements is a form of capacity of a defined number things that software system should be able to handle.
*	Only one human user at a time using the software product as there is no form of networking as the system is a background automated process. 
*	Required to handle 30 images a sec of video at least at 640 by 480 resolution. If the software product couldn’t handle 30 images a sec, it would lead to accuracy issues; With flagging buses passing red lights as the bus would drive away before the system has a chance to detect the bus. 
*	Handle all form of user input in 0.1 seconds including background process required to respond to the user. The user input requirement of 0.1 seconds is to ensure the system feels responsive to the stakeholders.
*	Event flagging for user-defined code is required to allow up to 10 other software systems running on the local machine. External code users of up ten requirement are to allow external code system to be useful but not affect the accuracy of the software product. 

### Dynamic Numerical Requirements
Dynamic performance requirement is a requirement based on how the software system should perform at both normal workload and peak workload such as increased users.
*	Required to handle up detection on 1-16 buses at any point in time. The requirement of up 16 buses to ensure that software system can perform its core task at an intersection such as a 4-lane cross section.
*	Maintain a 90% percent accuracy on buses pass reds light that the camera can see at a high level of traffic. High level of traffic would suggest the visible roads by the camera view filled by vehicles. Volume requirement on the amount of traffic is ensuring that software system is flexible with any intersection in the world no matter the traffic.
*	Flagging of buses passing red lights are required to take no longer than 0.5 seconds when handling between 1 to 16 buses at an intersection.
*	User configuration for more than one intersection should not affect the process time of the software product by more than 0.1 seconds. The complexity of the intersection should not a have a significant effect on the performance of the software product.


## 3.5 Logical Database Requirements