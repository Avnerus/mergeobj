#!/bin/bash
docker run -it --rm -v `pwd`:/models pymesh/pymesh /models/mergeobj.py /models/cube.obj /models/cone.obj /models/cuebcone.obj
