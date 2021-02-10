#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# length of one cell (mm).
unit = 1

# Tape colors.
tape_color = Color.BLUE
completion_color = Color.RED

# The 3 angles to check for a path.
angles_to_check = [0, 90, 270]

# Method for driving the robot forward one cell.
def drive_one_unit():
    robot.straight(unit)

# Metod to turn the robot to a given agngle.
def turn_to_angle(angle = 0):
    robot.turn(angle + robot.angle)

# Checks if the the path ahead is available.
def path_open():
    return line_sensor.color == tape_color

# Checks if the maze had been completed
def completed():
    return line_sensor.color == completion_color

# Recursive method to solve the maze.
def solve_maze(angle = 0):
    # Loop through checking for a path on all the sides.
    for a in angles_to_check:
        # Turn to the angle to check.
        turn_to_angle(angle + a)

        # it the path is open, take it.
        if bool(path_open()):
            drive_one_unit()

            # Recursivly call the method again.
            solve_maze(angle + a)

        # Check for completion.
        if completed():
            return

    # Drive back to the previous position.
    turn_to_angle(angle + 180)
    drive_one_unit()

# main function
def main():
    solve_maze()

if __name__ == "__main__":
    main()