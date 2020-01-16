import numpy as np
from plyfile import PlyData, PlyElement
from Edge import Edge

def read_ply(path='test_plys/test1.ply'):
    plydata = PlyData.read(path)


def main():
    print("Main")


if __name__ == "__main__":
    main()