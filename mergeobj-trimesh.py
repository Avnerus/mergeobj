#!/usr/bin/env python

import argparse
import os

import trimesh

parser = argparse.ArgumentParser(description='Merge Obj')
parser.add_argument('input_mesh_a', metavar='input-mesh-a', help='Wavefront OBJ A')
parser.add_argument('input_mesh_b', metavar='input-mesh-b', help='Wavefront OBJ B')
parser.add_argument('output_mesh', metavar='output-mesh', help='Output OBJ')
    
args = parser.parse_args()

if __name__ == '__main__':
    trimesh.util.attach_to_log()

    print("Loading Mesh A")
    A = trimesh.load(args.input_mesh_a, force='mesh', resolver=None)
    print("Loading Mesh B")
    B = trimesh.load(args.input_mesh_b, force='mesh', resolver=None)
    print("Concatenating")
    combined = trimesh.util.concatenate( [ A, B ] )
    print("Writing result")
    trimesh.exchange.export.export_mesh(combined, args.output_mesh, file_type="obj")
