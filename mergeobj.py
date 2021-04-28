#!/usr/bin/env python

import argparse
import os

import pymesh

parser = argparse.ArgumentParser(description='Merge Obj')
parser.add_argument('input_mesh_a', metavar='input-mesh-a', help='Wavefront OBJ A')
parser.add_argument('input_mesh_b', metavar='input-mesh-b', help='Wavefront OBJ B')
parser.add_argument('output_mesh', metavar='output-mesh', help='Output OBJ')
    
args = parser.parse_args()

if __name__ == '__main__':
    print("Loading Mesh A")
    A = pymesh.load_mesh(args.input_mesh_a)
    print("Loading Mesh B")
    B = pymesh.load_mesh(args.input_mesh_b)
    print("Calclating Union")
    union = pymesh.boolean(A, B, "union", "igl")
    print("Writing result")
    pymesh.save_mesh(args.output_mesh, union)
