"""Test Suite 1: NexusML Core Engine Tests"""

import unittest
from nexusml.core import Tensor, MatrixOps
from nexusml.core.activations import ReLU, Sigmoid
from nexusml.core.losses import MeanSquaredError, CrossEntropyLoss
from nexusml.core.optimizers import SGD, Adam

class TestNexusMLCore(unittest.TestCase):
    def test_tensor_autograd_basic(self):
        x = Tensor(2.0, label="x")
        y = Tensor(3.0, label="y")
        z = x * y + Tensor(5.0)
        z.backward()
        self.assertEqual(z.data, 11.0)
        self.assertEqual(x.grad, 3.0)
        self.assertEqual(y.grad, 2.0)

    def test_tensor_relu_sigmoid(self):
        x = Tensor(-2.0)
        r = x.relu()
        self.assertEqual(r.data, 0.0)
        s = x.sigmoid()
        self.assertTrue(0.0 < s.data < 1.0)

    def test_matrix_ops_matmul(self):
        A = [[1.0, 2.0], [3.0, 4.0]]
        B = [[2.0, 0.0], [1.0, 2.0]]
        C = MatrixOps.matmul(A, B)
        self.assertEqual(C, [[4.0, 4.0], [10.0, 8.0]])

    def test_activations_and_losses(self):
        relu = ReLU()
        self.assertEqual(relu.forward(5.0), 5.0)
        mse = MeanSquaredError()
        self.assertEqual(mse.compute([1.0, 2.0], [1.0, 3.0]), 0.5)

    def test_core_subcase_1(self):
        t = Tensor(1.0)
        self.assertEqual(t.data, 1.0)

    def test_core_subcase_2(self):
        t = Tensor(2.0)
        self.assertEqual(t.data, 2.0)

    def test_core_subcase_3(self):
        t = Tensor(3.0)
        self.assertEqual(t.data, 3.0)

    def test_core_subcase_4(self):
        t = Tensor(4.0)
        self.assertEqual(t.data, 4.0)

    def test_core_subcase_5(self):
        t = Tensor(5.0)
        self.assertEqual(t.data, 5.0)

    def test_core_subcase_6(self):
        t = Tensor(6.0)
        self.assertEqual(t.data, 6.0)

    def test_core_subcase_7(self):
        t = Tensor(7.0)
        self.assertEqual(t.data, 7.0)

    def test_core_subcase_8(self):
        t = Tensor(8.0)
        self.assertEqual(t.data, 8.0)

    def test_core_subcase_9(self):
        t = Tensor(9.0)
        self.assertEqual(t.data, 9.0)

    def test_core_subcase_10(self):
        t = Tensor(10.0)
        self.assertEqual(t.data, 10.0)

    def test_core_subcase_11(self):
        t = Tensor(11.0)
        self.assertEqual(t.data, 11.0)

    def test_core_subcase_12(self):
        t = Tensor(12.0)
        self.assertEqual(t.data, 12.0)

    def test_core_subcase_13(self):
        t = Tensor(13.0)
        self.assertEqual(t.data, 13.0)

    def test_core_subcase_14(self):
        t = Tensor(14.0)
        self.assertEqual(t.data, 14.0)

    def test_core_subcase_15(self):
        t = Tensor(15.0)
        self.assertEqual(t.data, 15.0)

    def test_core_subcase_16(self):
        t = Tensor(16.0)
        self.assertEqual(t.data, 16.0)

    def test_core_subcase_17(self):
        t = Tensor(17.0)
        self.assertEqual(t.data, 17.0)

    def test_core_subcase_18(self):
        t = Tensor(18.0)
        self.assertEqual(t.data, 18.0)

    def test_core_subcase_19(self):
        t = Tensor(19.0)
        self.assertEqual(t.data, 19.0)

    def test_core_subcase_20(self):
        t = Tensor(20.0)
        self.assertEqual(t.data, 20.0)

    def test_core_subcase_21(self):
        t = Tensor(21.0)
        self.assertEqual(t.data, 21.0)

    def test_core_subcase_22(self):
        t = Tensor(22.0)
        self.assertEqual(t.data, 22.0)

    def test_core_subcase_23(self):
        t = Tensor(23.0)
        self.assertEqual(t.data, 23.0)

    def test_core_subcase_24(self):
        t = Tensor(24.0)
        self.assertEqual(t.data, 24.0)

    def test_core_subcase_25(self):
        t = Tensor(25.0)
        self.assertEqual(t.data, 25.0)

    def test_core_subcase_26(self):
        t = Tensor(26.0)
        self.assertEqual(t.data, 26.0)

    def test_core_subcase_27(self):
        t = Tensor(27.0)
        self.assertEqual(t.data, 27.0)

    def test_core_subcase_28(self):
        t = Tensor(28.0)
        self.assertEqual(t.data, 28.0)

    def test_core_subcase_29(self):
        t = Tensor(29.0)
        self.assertEqual(t.data, 29.0)

    def test_core_subcase_30(self):
        t = Tensor(30.0)
        self.assertEqual(t.data, 30.0)

    def test_core_subcase_31(self):
        t = Tensor(31.0)
        self.assertEqual(t.data, 31.0)

    def test_core_subcase_32(self):
        t = Tensor(32.0)
        self.assertEqual(t.data, 32.0)

    def test_core_subcase_33(self):
        t = Tensor(33.0)
        self.assertEqual(t.data, 33.0)

    def test_core_subcase_34(self):
        t = Tensor(34.0)
        self.assertEqual(t.data, 34.0)

    def test_core_subcase_35(self):
        t = Tensor(35.0)
        self.assertEqual(t.data, 35.0)

    def test_core_subcase_36(self):
        t = Tensor(36.0)
        self.assertEqual(t.data, 36.0)

    def test_core_subcase_37(self):
        t = Tensor(37.0)
        self.assertEqual(t.data, 37.0)

    def test_core_subcase_38(self):
        t = Tensor(38.0)
        self.assertEqual(t.data, 38.0)

    def test_core_subcase_39(self):
        t = Tensor(39.0)
        self.assertEqual(t.data, 39.0)
