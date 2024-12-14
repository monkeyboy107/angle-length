import argparse
import numpy
import csv

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--radius',     '-r', required=True, type=float,  help='Radius of the circle')
  parser.add_argument('--min_length', '-m', default=1.0,   type=float,  help='Minumum length segment')
  parser.add_argument('--max_length', '-l', required=True, type=float,  help='Maximum length required')
  parser.add_argument('--precision',  '-p', default=1.0,   type=float,  help='How how precise do you want to be')
  parser.add_argument('--display',    '-D', action='store_true',        help='If set will output on terminal')
  parser.add_argument('--output',     '-o',                 type=str,   help='Outputs a CSV to specified path')

  args = parser.parse_args()
  
  angles = []
  for length in numpy.arange(args.min_length, args.max_length + args.precision, args.precision):
    angle = find_angle(length, args.radius)
    if args.display:
      print(f'For the length of {length}, the angle is {angle}')
    angles.append({'length': length, 'angle': angle})
  
  if args.output:
     with open(args.output, 'w', newline='') as stream:
       fields = ['length', 'angle']
       writer = csv.DictWriter(stream, fieldnames=fields)
       
       writer.writeheader()
       for line in angles:
         writer.writerow(line)
  return angles

def find_angle(length, radius):
  angle = length/radius
  return angle

if '__main__' == __name__:
  angles = main()
