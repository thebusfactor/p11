# Project Proposal and Requirements Document

The aim of the project proposal and requirements document is to
capture the requirements for the software your group is to build. It
should communicate clearly to the supervisor, client and course
coordinator exactly what the software you build is going to do, and
what constraints it must meet while doing so.

The document should also demonstrate your understanding of the main
analysis principles and quality guidelines, using tools and associated
notations as necessary to communicate the requirements precisely,
unambiguously and clearly in a written technical document. Page specifications below are *limits not targets* and refer to the pages in the PDF generated from the markdown. Because the size of your document is necessarily limited, you should ensure
that you focus your efforts on those requirements that are most
important to completing a successful system: if sections are at their
page limit, indicate how many would items be expected in a complete
specification. 

The ENGR 301 project proposal and requirements document should be based
on the standard ISO/IEC/IEEE 29148:2011(E), primarily sections 8.4 and
9.5, plus section 9.4 for projects involving hardware and ISO 25010
SQuaRE for systemic requirements. The proposal and requirements
document should contain the sections listed below, and conform to the
formatting rules listed at the end of this brief. 

All team members are expected to contribute equally to the document and list
their contributions in section 6 of the document. You should work on
your document in your team's GitLab repository in a directory called
"M1_Requirements". If more than one team member has contributed to a particular 
commit, all those team member IDs should be included in the first line
of the git commit message. ``git blame``, ``git diff``, file histories, etc. will be tools used to assess individual contributions, so everyone is encouraged to contribute individually, commit early and commit often. Any team wishing to separate individually contributed sections into a single file before collation into the single proposal document for submission is welcome to do so.

## 3. Specific requirements  

20 pages outlining the requirements of the system.
You should apportion these these pages across the following 
subsections to focus on the most important parts of your product.

### 3.1 External interfaces

See 9.5.10. for most systems this will be around one page.

### 3.2 Functions

This is typically the longest subsection in the document - see 9.5.11.
List up to fifty use cases (in order of priority for development), and
for at least top ten focal use cases, write a short goal statement and
use case body (up to seven pages).  Identify the use cases that
comprise a minimum viable product.

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
