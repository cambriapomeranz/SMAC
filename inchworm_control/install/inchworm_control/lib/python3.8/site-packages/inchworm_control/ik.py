import math
import random

def inverseKinematicsMQP(Px, Py, Pz):
    L_base = 3.125  # base to joint 1
    L1 = 1          # Joint 1 to Joint 2
    L2 = 6.432      # Joint 2 to Joint 3
    L3 = 6.432      # Joint 3 to Joint 4
    L4 = 1          # Joint 4 to Joint 5
    L_endEffector = 3.125  # Joint 5 to EE

    # adjust Z axis of the end-effector 
    Pz_adjusted = -Pz

    # Joint 1 only for rotation 
    theta1 = math.atan2(Py, Px)

    # Calculate the pose in the XZ-plane
    Wx = math.sqrt(Px**2 + Py**2)
    Wz = Pz_adjusted

    # Joint 2 to the center of the wrist 
    D = math.sqrt(Wx**2 + Wz**2)

    # Check if the position is reachable
    if D > (L2 + L3):
        raise ValueError('Position is not reachable')

    # Solve joints 2 and 3
    cosTheta2 = (L2**2 + D**2 - L3**2) / (2 * L2 * D)
    theta2 = math.atan2(Wz, Wx) - math.acos(cosTheta2)

    cosTheta3 = (L2**2 + L3**2 - D**2) / (2 * L2 * L3)
    theta3 = math.acos(cosTheta3) - math.pi

    # joint 4
    theta4 = -theta2 + theta3

    # Joint 5 doesn't affect the pose 
    theta5 = 0

    # Convert radians to degrees
    theta1 = math.degrees(theta1)
    theta2 = math.degrees(-theta2)
    theta3 = math.degrees(theta3)
    theta4 = math.degrees(-theta4)
    theta5 = math.degrees(theta5)

    return theta1, theta2, theta3, theta4, theta5

# Generate random values for Px, Py, Pz
Px = 3
Py = 0
Pz = 1

# Call the function with random values
try:
    theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(Px, Py, Pz)
    result = (theta1, theta2, theta3, theta4, theta5)
    print(result)
except ValueError as e:
    result = str(e)

result

