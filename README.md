In order to run experiemnts just run main.py file.

The 4 number displayed after each experiment run are Score, Dirt collected, Dirt collected (%), Existence of priority area (%) respectively.

All classes mentioned bellow are within eponymous files.

Supervised system uses StatefulBot class as its agent, the supervisor is described in supervisor.py file. 
Only 2, 4, 8, 10 number of bots parameters can be handled by supervisor, due to hardcoded cell division function.
Didn't have time to implement general solution.

Distributed system uses DistributedBot class as its agent.

Baseline method uses BasicBot class as its agent.

Bot class is a base class that handles movement and appearence.

All other classes are supporting ones, they dont carry any behavioral weight.

Appologies for no comments, Didn't have time to add them at the end.