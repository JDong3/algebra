from vector import *
import copy


def parallel(v1: Vector, v2: Vector) -> bool:
    return v1.parallel(v2)


def dot(v1: Vector, v2: Vector) -> int:
    return Vector(copy.deepcopy(v1.data)).dot(Vector(copy.deepcopy(v2.data)))




