from typing import List
from functools import cmp_to_key
import math


class Shape:
    def chu_vi(self):
        pass
    
    def dien_tich(self):
        pass

class Circle(Shape):
    def __init__(self, ban_kinh, x, y):
        self.ban_kinh = ban_kinh
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return 2*math.pi*self.ban_kinh
    
    def dien_tich(self):
        return math.pi*self.ban_kinh*self.ban_kinh

class Rect(Shape):
    def __init__(self, rong, dai, x, y):
        self.rong = rong
        self.dai = dai
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return 2*(self.rong + self.dai)
    
    def dien_tich(self):
        return self.rong*self.dai

class Triangle(Shape):
    def __init__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return self.a + self.b + self.c
    
    def dien_tich(self):
        p = self.chu_vi()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

def read_data(filename: str) -> List[Shape]:
    shapes = []
    with open(filename, 'r') as f:
        while True:
            s = f.readline().strip()
            if not s:
                break
            if s == '#Rect':
                rong, dai = list(map(int, f.readline().strip().split()))
                x, y = list(map(int, f.readline().strip().split()))
                shapes.append(Rect(rong, dai, x, y))
            elif s == '#Circle':
                ban_kinh = int(f.readline().strip())
                x, y = list(map(int, f.readline().strip().split()))
                shapes.append(Circle(ban_kinh, x, y))
            elif s == '#Triangle':
                a, b, c = list(map(int, f.readline().strip().split()))
                x, y = list(map(int, f.readline().strip().split()))
                shapes.append(Triangle(a, b, c, x, y))
    return shapes

def find_max_area(shapes: List[Shape]) -> float:
    max_area = 0.0
    for shape in shapes:
        area = shape.dien_tich()
        if area > max_area:
            max_area = area
    return max_area

def find_max_perimeter(shapes: List[Shape]) -> float:
    max_perimeter = 0.0
    for shape in shapes:
        perimeter = shape.chu_vi()
        if perimeter > max_perimeter:
            max_perimeter = perimeter
    return max_perimeter

def find_max_overlap(shapes: List[Shape]) -> int:
    max_overlap_count = 0
    for i in range(len(shapes)):
        overlap_count = 0
        for j in range(len(shapes)):
            if i != j and is_overlapping(shapes[i], shapes[j]):
                overlap_count += 1
        if overlap_count > max_overlap_count:
            max_overlap_count = overlap_count
    return max_overlap_count

def is_overlapping(shape1: Shape, shape2: Shape) -> bool:
    if isinstance(shape1, Rect) and isinstance(shape2, Rect):
        x1, y1 = shape1.x, shape1.y
        x2, y2 = x1 + shape1.rong, y1 + shape1.dai
        x3, y3 = shape2.x, shape2.y
        x4, y4 = x3 + shape2.rong, y3 + shape2.dai
        if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
            return True
        else:
            return False
    elif isinstance(shape1, Circle) and isinstance(shape2, Circle):
        distance_squared = (shape1.x - shape2.x)**2 + (shape1.y - shape2.y)**2
        radius_sum_squared = (shape1.ban_kinh + shape2.ban_kinh)**2
        if distance_squared < radius_sum_squared:
            return True
        else:
            return False
    else:
        return False

filename = 'G:\\input.txt'

shapes = read_data(filename)

max_area = find_max_area(shapes)
max_perimeter = find_max_perimeter(shapes)
max_overlap_count = find_max_overlap(shapes)

print(max_area)
print(max_perimeter)
print(max_overlap_count)
