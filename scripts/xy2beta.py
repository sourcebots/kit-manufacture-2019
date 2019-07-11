#!/usr/bin/env python3

"""
Converts the XY (pick-and-place coordinates) file produced by the pcb software to the format
expected by Beta Layout.
"""

# Input format:
#   refdes,footprint,part-id,x,y,angle,layer
# e.g.
#   J17,"header_127_10w_sr.fp","sr-cn-header2x5-1.27mm",47.50,86.27,270,top
# Detailed at http://pcb.geda-project.org/pcb-cvs/pcb.html#Centroid-File-Format

# Output format:
#   refdes  x       y       angle   value   package layer
# e.g.
#   C101    47.94   248.92  180.00  100p    0603    top
# Detailed at https://uk.beta-layout.com/pcb/technology/assembly_guide.html (section 3).

import csv
import re
import sys

csv.register_dialect("beta_xy",
  delimiter="\t",
  quoting=csv.QUOTE_NONE,
)

def remove_comment_lines(lines):
  return (line for line in lines if not line.startswith("#"))

def part_id_to_value(s):
  try:
    return s.split("-", 2)[2]
  except IndexError:
    return s

def footprint_to_package(s):
  suffix = "_sr.fp"
  assert s.endswith(suffix)
  return s[:-len(suffix)]

def convert_row(input_row):
  refdes, footprint, part_id, x, y, angle, layer = input_row
  value = part_id_to_value(part_id)
  package = footprint_to_package(footprint)
  return (refdes, x, y, angle, value, package, layer)

def print_header():
  print("Filename: ...")
  print()
  print("Position of PCB:")
  print("left under edge: X=0 / Y=0")
  print()
  print("\t".join(("name", "X-axis", "Y-axis", "angle", "value", "package", "side")))

def print_output_rows(rows):
  csv.writer(sys.stdout, dialect="beta_xy").writerows(rows)

input_lines = iter(sys.stdin)
input_lines = remove_comment_lines(input_lines)
input_rows = csv.reader(input_lines)
output_rows = map(convert_row, input_rows)
print_header()
print_output_rows(output_rows)
