import math

def parse_points(input_str):
    # Removing parentheses and splitting by commas
    points = input_str.strip('()').split('),(')
    # Converting each point from string to a tuple of integers
    return [tuple(map(int, point.split(','))) for point in points]

# for calculate angle
def calculate_angle(A, B, C):
    # Create vectors AB and BC
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])

    # Calculate the dot product of AB and BC
    dot_product = AB[0] * BC[0] + AB[1] * BC[1]

    # Calculate the magnitudes of AB and BC
    magnitude_AB = math.sqrt(AB[0] ** 2 + AB[1] ** 2)
    magnitude_BC = math.sqrt(BC[0] ** 2 + BC[1] ** 2)

    # Calculate the cosine of the angle using the dot product formula
    cos_angle = dot_product / (magnitude_AB * magnitude_BC)

    # Calculate the angle in radians and then convert to degrees
    angle = math.acos(cos_angle)  # Angle in radians
    angle_degrees = math.degrees(angle)  # Convert to degrees

    return angle_degrees