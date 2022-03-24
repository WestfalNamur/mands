# How to design an application.
source and copyright to: https://www.oreilly.com/content/software-architecture-patterns/

## Types os architectures.
#### Layered

The **Layered**, or n-tier, is the most common one and closely matches traditional IT infrastructure. <br>
The architecture is organized into horizontal layers and each layer performs a particular role (i.e. presentation or business logic.). Usually but not always these are 4 layers: presentation, business, persistence, and data base layer which business and persistence layers sometimes combined. Each layer has a specific task, i.e. handle user interaction. They build an abstraction around the work that needs to be done for that specific task. The power of this architecture is the *separation of concerns*, layers only care about their specific task. <br>
Usually layers are *closed*, so each layer can only communicate with the layer below. This is to *isolate* the layers, meaning that changes in a layer only affect, if at all, the layer above. Each layer only needs to know the api of the layer above and not it's internal workings. <br> 
Sometimes it makes sense to have open layers, meaning request from above can bypass this layer.
<br>

#### Event driven

Popular distributed asynchronous architecture pattern. Made up of highly decoupled single-purpose event processing components that asynchronously receive and process events. It consists of two main topologies, the broker and mediator. The mediator orchestrates several events from a central mediator why a broker chains events without the use of a mediator. <br>

#### Microkernel

The microkernel architecture pattern consists of two types of architecture components: a core system and plug-in modules. Application logic is divided between independent plug-in modules and the basic core system, providing extensibility, flexibility, and isolation of application features and custom processing logic. <br>
The core system of the microkernel architecture pattern traditionally contains only the minimal functionality required to make the system operational. Many operating systems implement the microkernel architecture pattern, hence the origin of this pattern’s name. From a business-application perspective, the core system is often defined as the general business logic sans custom code for special cases, special rules, or complex conditional processing. <br>
The plug-in modules are stand-alone, independent components that contain specialized processing, additional features, and custom code that is meant to enhance or extend the core system to produce additional business capabilities. Generally, plug-in modules should be independent of other plug-in modules, but you can certainly design plug-ins that require other plug-ins to be present. Either way, it is important to keep the communication between plug-ins to a minimum to avoid dependency issues.  <br>