# How to design an application.
source and copyright to: https://www.oreilly.com/content/software-architecture-patterns/

## Types os architectures.

The **Layered**, or n-tier, is the most common one and closely matches traditional IT infrastructure. <br>
The architecture is organized into horizontal layers and each layer performs a particular role (i.e. presentation or business logic.). Usually but not always these are 4 layers: presentation, business, persistence, and data base layer which business and persistence layers sometimes combined. Each layer has a specific task, i.e. handle user interaction. They build an abstraction around the work that needs to be done for that specific task. The power of this architecture is the *separation of concerns*, layers only care about their specific task. <br>
Usually layers are *closed*, so each layer can only communicate with the layer below. This is to *isolate* the layers, meaning that changes in a layer only affect, if at all, the layer above. Each layer only needs to know the api of the layer above and not it's internal workings. <br> 
Sometimes it makes sense to have open layers, meaning request from above can bypass this layer.
