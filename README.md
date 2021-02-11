# POE_Project_2_1_7
This project contins code of Principles of Engineering Project 2.1.7. The project asked us to build and program a robot to preform some task. We decided to have out robot solve a maze. The course is typically taught with Vex robotics robots, but since class is virtual are using a Lego Mindstorm Ev3. The project contains two menthods of solving the maze: one that follows the right wall, and another recusive depth first search.
 
## Follow the Right Wall
The method has the robot follow the right wall of the maze around untill it finds the exit. It does this by having the robot coninually cheack it's right side to see it the wall it there. If there is no wall it will drive to the right, but if there is a wall to the right it will continue moving forward. Howerver if the robo'ts forward path is blocked, it will go left.

## Recursive Depth First Search
The [depth first search](https://en.wikipedia.org/wiki/Depth-first_search?scrlybrkr=84853519) method is a bit more complicated, but it tends to solve the maze faster (though they both have the same worst case time complexity of O(n)). The method has the robot recusivly cheack for and takign the first open path it finds. This continues to build a recursive tree untill it is blocked, and it must go back down the tree. The robot backtrackes it path, checking any unchecked paths as it goes. It continues untill the maze is solved.

## VEXCode VR
The `VEXCodeVR` folder contains a proof of concept programs to be run on the [VEXCode VR website](https://vr.vex.com/). They wee used for testing the methodology remotly beofre attempting it on a physical robot.
