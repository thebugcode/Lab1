Lab1odaodaoda
====

So you've chosen your projects. It's time to file down the requirements for the solution you are developing.

Part 1. Creating the system vision
---

At first, one needs to create a representation of the problem description. It can be provided as a table or a list and should include the following sections:

**1. Business Context**

*Who will use the solution, how will it stand with other solutions. 2 sentences of the backround about where the system will reside*

**2. Business Opportunities**

*4-6 sentences that will describe the problem and the need for the solution. What will happen when you deliver the solution?*

**3. Problem Description**

*This section should be split into several parts:*

- Problem

	*One sentence about the problem. Explain it at the best of your ability. Brevity matters.*
- Concerns

	*Who are the ones encountering the problem now*
- Consequences

	*What are the consequences of the problem. How does it impede work?*
- Successful solution

	*What key points will your solution deliver? Long/short run? 2 sentences*
- Task of the system

	*Therefore, what are you aiming to solve. Keep it as short as possible. 1 sentence.*

Part 2. Identifying the stakeholders
---

The second step is to create a table of *stakeholders* and their responsibilities. The table should contain the following columns:

- Stakeholder


- Role

	*a rough description of the role of this stake holder within the organisation. What do they represent?*

- Description

	*a description of the interaction of the stakeholder with the software system*

The most important part, however, is identifying the stakeholders. They include the immediate users of the system as well as all the secondary affected users, oferators, support, maintenance, etc. While identifying the stakeholders, one should ask himself the following questions:
Who uses the system?

- Who is affected by the introduction of the system?
- Who benefits from the system?
- Who operates the system?
- Who maintains the system?
- Who accepts the system?
- What expectations do the stakeholders have?
- What tasks, competencies, and responsibilities do the stakeholders have?

Part 3. Documenting the functional requirements of the system
---

The functional requirements of the selected system define the functionality the system is to provide. From these you will later derive the use-case scenarios for your application. In the event that your application interacts withsome third-party services, investigate the feasability of the used services.

The functional requirements should be provided in the following format:

- Requirement

	*An expression describing an action performed or provided by the system, such as* `Log In`, `Import Customer Data`, `Create Instant Win Game`

- Description

	*A sentence or two delving into the specific requirement. If the functionality represents a different behavior for different stakeholders, please provide an outline of the difference*

Part 4. Non-functional requirements
---

The non-functional requirement of the system is a constraint imposed on it, which has an architectural value. For instance, one of the systems might need to be developed in 1 month and provide audio assistance for the visually impaired. Since both of these requirements will highly affect the development and the architectural organization of the system, they need to be included and taken into consideration.

The format for the non-functional requirements is as follows:

- Requirement

	*A definition of the requirement as a noun.* `Extensibility`, `Usability` *and* `Delivery Time` *are possible examples*

- Description

	*A brief (1 sentence) description of the requirement. Something like* `Must be running on the JVM`

Part 5. Architectural sketch
---

Using the data from the previous steps, design a sketch of the system's main components. Each of the components should be characterized by their responsibility. The sketch should also highlight the system's key abstractions. Please include the actors that interact with the system.

The sketch can be provided in the form of a Component Diagram (UML) or a simple blocks-and-arrows notation. In case there is a role relationship between the blocks or a multiplicity, specify that too.

Part 6. Functional blocks
---

Some of the blocks have related responsibilities. They should be grouped in *functional building blocks*, which will define the modularity of the system. Therefore, the sketch will now change - it will also include the grouping of similar blocks. Where possible, justify the grouping.

Part 7. Select an architecture
---

You have to select one or more styles for the application. Why do you think this is a good choice? What needs to be changed in your sketch to reflect the architecture and make use of its advantages?

Styles:

- Layered architecture
- Dataflow
- Client/server
- Rich Client vs. Thin Client
- Publish/subscribe
- SOA
- n-tier architecture

Part 8. Architectural principles
---

Please describe how does your sketch comply with the following architectural principles:

- Loose coupling
- High cohesion
- Design for change
- Separation of concerns
- Information hiding
- Liskov substitution
- Interface segregation
- Modularity
- Convention over configuration

Part 9. An architectural sketch
---

Redesign your sketch from scratch, ro that it would respect as many of the principles and comply with the selected architectural style. It should contain both the functional building blocks and the smaller modules of the system.

No conclusions necessary.


Part 10. Have fun!
---






Reading Material
----------------

1. *Oliver Vogel et al.*, **Software Architecture - a Comprehensive Framework and Guide for Practitioners**
2. *Ian Gorton*, **Essential Software Architecture**, 2nd ed.
3. *Danny Greefhorst, Erik Proper*, **Architecture Principles - The Cornerstones of Enterprise Architecture**

Extra book:
*James Coplien, Gertrud Bjørnvig*, **Lean Architecture for Agile Software Development**






