# This Python file uses the following encoding: utf-8


from math import pi

def circle_area(r):
    if type(r) not in [int, float]: 
        raise TypeError
    if r < 0:
        raise ValueError("negatives must not be used!")
    return pi*(r**2)

if __name__ == "main":
    # Test function
    radii = [2, 0, -3, 2 + 5j, True, "radius"]
    message = "Area of circles with r = {radius} is {area}"

    for r in radii:
        Area = circle_area(r)
        print(message.format(radius=r, area=Area))
