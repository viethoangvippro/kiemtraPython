from ast import Constant
import traceback
import pandas as pd

import random

import random

def generate_input_file(file_path, n):
    with open(file_path, 'w') as f:
        for i in range(10):
            shape_type = random.choice(['Rect', 'Circle', 'Triangle'])
            f.write(f'#{shape_type}\n')
            if shape_type == 'Rect':
                width = random.randint(1, 10)
                height = random.randint(1, 10)
                x = random.randint(0, 20)
                y = random.randint(0, 20)
                f.write(f'{width} {height}\n')
                f.write(f'{x} {y}\n')
            elif shape_type == 'Circle':
                radius = random.randint(1, 10)
                x = random.randint(0, 20)
                y = random.randint(0, 20)
                f.write(f'{radius}\n')
                f.write(f'{x} {y}\n')
            else:
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                x = random.randint(0, 20)
                y = random.randint(0, 20)
                f.write(f'{a} {b} {c}\n')
                f.write(f'{x} {y}\n')
generate_input_file('G:\\input2.txt', 9)