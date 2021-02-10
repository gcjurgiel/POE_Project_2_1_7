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
unit = 100

# Tape colors.
tape_color = Color.BLUE
completion_color = Color.RED

# Method for driving the robot forward one cell.
def drive_one_unit():
    robot.straight(unit)

# Metod to turn the robot right 90 degrees.
def turn_right():
    robot.turn(90)

# Metod to turn the robot left 90 degrees.
def turn_left():
    robot.turn(-90)

# Checks if the the path ahead is available.
def path_open():
    return line_sensor.color == tape_color

# Checks if the maze had been completed.
def completed():
    return line_sensor.color == completion_color

# Method to solve the maze by following the right wall.
def solve_maze():
    # Loop through checking for a path on all the sides.
    while not completed():
        # Turn to the right to check for the right wall.
        turn_right()

        # If there is a wall, turn left untill there is an opening .
        while not path_open():
            turn_left()

        # Drive into the open path.
        drive_one_unit()

# main function
def main():
    solve_maze()

if __name__ == "__main__":
    main()