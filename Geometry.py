#  File: Geometry.py

#  Description: Several classes that are fundamental in Solid Geometry - Point, Sphere, Cube, and Cylinder.
#  This will test the various functions whether it is inside, outside, intersecting using OOP method.

#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 2/09/2022

#  Date Last Modified: 2/16/2022

import math
import sys


class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return f'({self.x:.1f}, {self.y:.1f}, {self.z:.1f})'

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean 
    def __eq__(self, other):
        tol = 1.0e-6
        return self.distance(other) < tol


class Sphere(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.center = Point(x, y, z)
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return f'Center: ({self.center.x:.1f}, {self.center.y:.1f}, {self.center.z:.1f}), Radius: {self.radius:.1f}'

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        # surface area formula: 4(pi)r^2
        return float(4 * math.pi * (self.radius ** 2))

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        # volume formula: (4/3)(pi)r^3
        return float((4 / 3) * math.pi * (self.radius ** 3))

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return p.distance(self.center) < self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        distance = self.center.distance(other.center)
        return distance < self.radius - other.radius

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        vertices = a_cube.generate_vertices()
        for vertex in vertices:
            if not self.is_inside_point(vertex):
                return False
        return True

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        # find the radius of the section of the sphere at the upper and lower bounds of the z component of a_cyl
        # if the radius of a_cyl is bigger at this section, return False
        if self.radius ** 2 - (a_cyl.center.z - a_cyl.height / 2 - self.center.z) ** 2 < 0 or \
                self.radius ** 2 - (a_cyl.center.z + a_cyl.height / 2 - self.center.z) ** 2 < 0:
            return False
        new_lower_radius = math.sqrt(self.radius ** 2 - (a_cyl.center.z - a_cyl.height / 2 - self.center.z) ** 2)
        new_upper_radius = math.sqrt(self.radius ** 2 - (a_cyl.center.z + a_cyl.height / 2 - self.center.z) ** 2)
        distance = math.sqrt((self.center.x - a_cyl.center.x) ** 2 + (self.center.y - a_cyl.center.y) ** 2)
        return distance < new_lower_radius - a_cyl.radius and distance < new_upper_radius - a_cyl.radius

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        distance = self.center.distance(other.center)
        if self.is_inside_sphere(other):
            return False

        # distance between centers must be less than or equal to the sum of the radii
        return distance <= self.radius + other.radius

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        vertices = a_cube.generate_vertices()
        if self.is_inside_cube(a_cube):
            return False

        # check each vertex to ensure containment. if at least one but not all are contained, return True
        for vertex in vertices:
            if self.is_inside_point(vertex):
                return True
        return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        circumscribed = Cube(self.center.x, self.center.y, self.center.z, 2 * self.radius / math.sqrt(3))
        return circumscribed


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.center = Point(x, y, z)
        self.side = side

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return f'Center: ({self.center.x:.1f}, {self.center.y:.1f}, {self.center.z:.1f}), Side: {self.side:.1f}'

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        # total surface area formula: 6s^2
        return float(6 * (self.side ** 2))

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        # volume formula: s^3
        return float(self.side ** 3)

    def generate_vertices(self):
        vertices = tuple()     # (x +- s/2, y +- s/2, z +- s/2)
        deltas = [self.side / 2, -self.side / 2]
        for x_change in deltas:
            x_prime = self.center.x + x_change
            for y_change in deltas:
                y_prime = self.center.y + y_change
                for z_change in deltas:
                    z_prime = self.center.z + z_change
                    vertices += (Point(x_prime, y_prime, z_prime),)

        return vertices

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        return abs(self.center.x - p.x) < self.side / 2 and \
               abs(self.center.y - p.y) < self.side / 2 and \
               abs(self.center.z - p.z) < self.side / 2

    def contains_point(self, p):
        return abs(self.center.x - p.x) <= self.side / 2 and \
               abs(self.center.y - p.y) <= self.side / 2 and \
               abs(self.center.z - p.z) <= self.side / 2

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        distance = self.center.distance(a_sphere.center)
        return distance < self.side / 2 - a_sphere.radius

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        vertices = other.generate_vertices()

        # check each vertex to ensure all are within the cube. if any are not, return False
        for vertex in vertices:
            if not self.is_inside_point(vertex):
                return False
        return True

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        xy_distance = math.sqrt((self.center.x - a_cyl.center.x) ** 2 + (self.center.y - a_cyl.center.y) ** 2)

        # check the distance between the centers and compare it to the cube's side and a_cyl's radius
        # check the distance between the z components of the center and compare it to the cube's side and a_cyl's radius
        return xy_distance < self.side / 2 - a_cyl.radius and \
            abs(self.center.z - a_cyl.center.z) < self.side / 2 - a_cyl.height / 2

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        self_vertices = self.generate_vertices()
        other_vertices = other.generate_vertices()
        if self.is_inside_cube(other) or other.is_inside_cube(self):
            return False

        # check every vertex in both cubes for containment in the other
        for vertex in self_vertices:
            if other.contains_point(vertex):
                return True
        for vertex in other_vertices:
            if self.contains_point(vertex):
                return True
        return False

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        if other.center.x - other.side / 2 > self.center.x - self.side / 2:
            x = abs(other.side / 2 - self.center.x + other.center.x)
        else:
            x = abs(self.side / 2 - other.center.x + self.center.x)
        if other.center.y - other.side / 2 > self.center.y - self.side / 2:
            y = abs(other.side / 2 - self.center.y + other.center.y)
        else:
            y = abs(self.side / 2 - other.center.y + self.center.y)
        if other.center.z - other.side / 2 > self.center.z - self.side / 2:
            z = abs(other.side / 2 - self.center.z + other.center.z)
        else:
            z = abs(self.side / 2 - other.center.x + self.center.x)
        return float(x * y * z)

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        inscribed = Sphere(self.center.x, self.center.y, self.center.z, self.side / 2)
        return inscribed


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return (f'Center: ({self.center.x:.1f}, {self.center.y:.1f}, {self.center.z:.1f}), Radius: '
                f'{self.radius:.1f}, Height: {self.height:.1f}')

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        # surface area formula: 2(pi)rh + 2(pi)r^2
        return float(2 * math.pi * self.radius * self.height + 2 * math.pi * (self.radius ** 2))

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        # volume formula: (pi)r^2h
        return float(math.pi * (self.radius ** 2) * self.height)

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        xy_distance = math.sqrt((self.center.x - p.x) ** 2 + (self.center.y - p.y) ** 2)
        return xy_distance < self.radius and abs(self.center.z - p.z) < self.height / 2

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        xy_distance = math.sqrt((self.center.x - a_sphere.center.x) ** 2 + (self.center.y - a_sphere.center.y) ** 2)
        return xy_distance < self.radius - a_sphere.radius and \
            abs(self.center.z - a_sphere.center.z) < self.height / 2 - a_sphere.radius

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        vertices = a_cube.generate_vertices()
        for vertex in vertices:
            if not self.is_inside_point(vertex):
                return False
        return True

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        xy_distance = math.sqrt((self.center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2)
        return xy_distance < self.radius - other.radius and \
            abs(self.center.z - other.center.z) < self.height / 2 - other.height / 2

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        xy_distance = math.sqrt((self.center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2)
        if self.is_inside_cylinder(other) or other.is_inside_cylinder(self):
            return False
        return xy_distance <= self.radius + other.radius and \
            abs(self.center.z - other.center.z) <= self.height / 2 + other.height / 2


def main():
    # read data from standard input
    data = sys.stdin.read()
    lines = data.split("\n")

    # read the coordinates of the first Point p
    px, py, pz = (float(x) for x in lines[0].split()[:3])

    # create a Point object
    p = Point(px, py, pz)

    # read the coordinates of the second Point q
    qx, qy, qz = (float(x) for x in lines[1].split()[:3])

    # create a Point object
    q = Point(qx, qy, qz)

    # read the coordinates of the center and radius of sphereA
    sphere_a_x, sphere_a_y, sphere_a_z, sphere_a_radius = (float(x) for x in lines[2].split()[:4])

    # create a Sphere object
    sphere_a = Sphere(sphere_a_x, sphere_a_y, sphere_a_z, sphere_a_radius)

    # read the coordinates of the center and radius of sphereB
    sphere_b_x, sphere_b_y, sphere_b_z, sphere_b_radius = (float(x) for x in lines[3].split()[:4])

    # create a Sphere object
    sphere_b = Sphere(sphere_b_x, sphere_b_y, sphere_b_z, sphere_b_radius)

    # read the coordinates of the center and side of cubeA
    cube_a_x, cube_a_y, cube_a_z, cube_a_radius = (float(x) for x in lines[4].split()[:4])

    # create a Cube object
    cube_a = Cube(cube_a_x, cube_a_y, cube_a_z, cube_a_radius)

    # read the coordinates of the center and side of cubeB
    cube_b_x, cube_b_y, cube_b_z, cube_b_side = (float(x) for x in lines[5].split()[:4])

    # create a Cube object
    cube_b = Cube(cube_b_x, cube_b_y, cube_b_z, cube_b_side)

    # read the coordinates of the center, radius and height of cylA
    cyl_a_x, cyl_a_y, cyl_a_z, cyl_a_radius, cyl_a_height = (float(x) for x in lines[6].split()[:5])

    # create a Cylinder object
    cyl_a = Cylinder(cyl_a_x, cyl_a_y, cyl_a_z, cyl_a_radius, cyl_a_height)

    # read the coordinates of the center, radius and height of cylB
    cyl_b_x, cyl_b_y, cyl_b_z, cyl_b_radius, cyl_b_height = (float(x) for x in lines[7].split()[:5])

    # create a Cylinder object
    cyl_b = Cylinder(cyl_b_x, cyl_b_y, cyl_b_z, cyl_b_radius, cyl_b_height)

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    origin = Point(0, 0, 0)
    if p.distance(origin) > q.distance(origin):
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

    # print if Point p is inside sphereA
    if sphere_a.is_inside_point(p):
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

    # print if sphereB is inside sphereA
    if sphere_a.is_inside_sphere(sphere_b):
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # print if cubeA is inside sphereA
    if sphere_a.is_inside_cube(cube_a):
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    # print if cylA is inside sphereA
    if sphere_a.is_inside_cyl(cyl_a):
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")

    # print if sphereA intersects with sphereB
    if sphere_b.does_intersect_sphere(sphere_a):
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")

    # print if cubeB intersects with sphereB
    if sphere_b.does_intersect_cube(cube_b):
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    if sphere_a.circumscribe_cube().volume() > cyl_a.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

    # print if Point p is inside cubeA
    if cube_a.is_inside_point(p):
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    # print if sphereA is inside cubeA
    if cube_a.is_inside_sphere(sphere_a):
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")

    # print if cubeB is inside cubeA
    if cube_a.is_inside_cube(cube_b):
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")

    # print if cylA is inside cubeA
    if cube_a.is_inside_cylinder(cyl_a):
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")

    # print if cubeA intersects with cubeB
    if cube_b.does_intersect_cube(cube_a):
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    if cube_a.intersection_volume(cube_b) > sphere_a.volume():
        print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    if cube_a.inscribe_sphere().area() > cyl_a.area():
        print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of "
              "cylA")

    # print if Point p is inside cylA
    if cyl_a.is_inside_point(p):
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")

    # print if sphereA is inside cylA
    if cyl_a.is_inside_sphere(sphere_a):
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")

    # print if cubeA is inside cylA
    if cyl_a.is_inside_cube(cube_a):
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")

    # print if cylB is inside cylA
    if cyl_a.is_inside_cylinder(cyl_b):
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    if cyl_a.does_intersect_cylinder(cyl_b):
        print("cylB does intersect cylA")
    else:
        print("cylB does not intersect cylA")


if __name__ == "__main__":
    main()
