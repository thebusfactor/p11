## 1. Introduction
One page overall introduction including sections 1.1 and 1.2.

### Client

The clients for this project are Hugh and Stephen from ZX Security.
Contact Details:
Hugh: hugh@zxsecurity.co.nz

Stephen: stephen@zxsecurity.co.nz  
Hugh: hugh@zxsecurity.co.nz  

### 1.1 Purpose

The system must take a video input from any standard webcam, and from this input - detect when a bus is seen running a red light & report to the user in realtime.

### 1.2 Scope

The Bus Factor Project will produce a program which can be set up and run on any consumer-available computer, using a commercially available webcam.
The program should be able to run on both Windows and Linux devices, and work when set up at any intersection, from any angle.  
The program will take in a video input. It will then automatically detect the location & status of the red light
in the video, and automatically detect when a bus runs the detected red light. To do this, the state of the light 
must be automatically detected, and the boundary point for the intersection
(I.e. the line not to be crossed by the bus) should be either manually inputted or automatically detected.
When an offence is detected, the program should automatically trigger some sort of event to notify the user - 
either a preprogrammed event or some other user defined code.
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

1. **Requirements**  
There is a risk that this project may not have requirements and guidelines that are clear enough, or demanding enough to facilitate a year-long project management project. 
A lack of clear, manageable requirements from the clients could have a negative impact on the team's ability to practise Project Management. 
As ENGR301 and 302 are at their core, designed to teach the practises of Project Management, this reduced opportunity could result in lower course grades on assessment items,
as the lack of proper requirements and client behaviour could translate to lower quality project management assessments.  
This risk is somewhat unlikely, due to the extensive support network offered by the university, senior managers, and lecturers. However, the consequence of such a risk is 
quite high. Not only would the grades of the team suffer, but the learning opportunity offered by this real industry project would be essentially wasted, and the team's future
skills or assessments could suffer as a result.  
In order to mitigate this risk, communication will be established early with both the clients and the senior managers, to ensure that requirements sufficient to the scope of the
project are achieved. The client will be asked for a more substantial set of requirements, and from those requirements the team can scale back to a manageable project, using
the project management techniques of the course. Regular client meetings will be maintained to ensure that these requirements are accurate, and to discuss the progress on the project.

2. **Scope**  
The clients could go to the opposite extreme, providing far too many features that they want implemented and extended in the final product, rather than a core deliverable concept that
can be extended with additional features as they arise. Having such a feature bloat could potentially cause a significant time sink for the team, adding and implementing new features
constantly rather than working towards the specified project goals. Based on the initial client communication, this seems highly unlikely. The scope of the project is well-defined, and
there is a clear, core concept that can easily be extended upon. However, there is a risk that this will become a problem later on, with more client communication throughout the project.  
This risk can be mitigated by keeping regular communication with the clients, ensuring that they have reasonable expectations from the team, and if necessary, involving the senior manager
to clarify miscommunications. Also, any communication regarding deliverables and extra features of the project should be confirmed in writing, and notes from each meeting should be kept
on the GitLab wiki for the project.

3. **Financial**  
Depending on the method that is used to implement the goals for this project, there could be a requirement for processing power beyond that which the team has access to. Machine learning
techniques seem to be a viable approach to the product, as manually writing code to classify and detect busses, intersections and traffic lights could be a monumental task on its own. 
Taking advantage of existing machine learning libraries suited to Image Processing/Computer Vision would make the project much more achieveable.
However, this approach could result in unexpected financial requirements for the project, such as hardware capable of performing machine learning algorithms, or access to a web server 
or physical server on which to perform the machine learning aspects of the project. 
This risk is unlikely, as the university likely has access to hardware setups that would be more than sufficient for this project. However, if these were not accessible by the team, 
other solutions would need to be explored, such as new hardware, or access to a webserver to perform the machine learning on (AWS, for example).  
By doing thorough research into the methods being used in the project, and to reduce the computational power required by the project, this risk could be mitigated. Clients will be
consulted for suggestions during this process, also. Robust testing can be used to ensure these hardware requirements are met.

4. **Licencing**  
The requirements of this project given to us by the clients may require the use of technologies that are out of the grasp of the team members, such as machine learning, neural networks
or advanced Image Processing/Computer Vision techniques. This could result in the use of pre-existing libraries to help. However, the clients have required that the project be developed
and released under an OSI-approved licence. If the libaries used do not follow this criteria, the project would not be meeting the requirements of the client.  
This can be mitigated by ensuring that all team members understand fully what is required and expected when developing/releasing under an OSI approved licence. This should be researched 
and understood early, to avoid conflicts later. Also, any potentially useful library should be checked out to ensure that it meets these standards before it is approved for use in the 
project. 

5. **Technical Ability**  
Words

6. **Dynamics of Deployment**  
And

7. **Privacy**  
Things