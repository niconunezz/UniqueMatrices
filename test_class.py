import pytest
from methods import *
class TestClass:
    def test_m1(self):
        A = np.array([[1,1,1,3],[1,2,3,0],[1,3,4,-2]])
        answer = np.array([[1,0,0,5],[0,1,0,-1],[0,0,1,-1]])
        assert np.array_equal(reduced_echelon(A), answer)
    def test_m2(self):
        A = np.array([[0,3,-6,6,4,-5],[3,-7,8,-5,8,9],[3,-9,12.0,-9,6,15]])
        answer = np.array([[1,0,-2,3,0,-24],[0,1,-2,2,0,-7],[0,0,0,0,1,4]])
        assert np.array_equal(reduced_echelon(A), answer)
    def test_m3(self):
        A =np.array([[1, 2, 0, 1, 0, 0],[0, 0, 0, 3, 0, 0],[0, 0, 1, 3, 1, 0]])
        answer = np.array([[1, 2, 0, 0, 0, 0],[0, 0, 1, 0, 1, 0],[0, 0, 0, 1, 0, 0]])
        assert np.array_equal(reduced_echelon(A), answer)
    def test_m4(self):
        A = np.array([
        [1, 0, 0, 0, 1],
        [0, 2, 0, 2, 0],
        [0, 0, 3, 0, 0],
        [0, 4, 0, 4, 0],
        [5, 0, 0, 0, 5]
        ])
        answer = np.array([
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
        ])
        assert np.array_equal(reduced_echelon(A), answer)
    
    def test_m5(self):
        A = np.array([
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ])
        answer = np.array([
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ])
        assert np.array_equal(reduced_echelon(A), answer)