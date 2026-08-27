"""Test Suite 7: NexusML Advanced Solvers & Deep Learning Blocks"""

import unittest
from nexusml.core.numerical_solvers import NewtonRaphsonSolver
from nexusml.core.signal_processing import FourierTransform
from nexusml.models.deep_learning_blocks import AttentionLayer
from nexusml.models.boosting_engine import GradientBoostingEngine
from nexusml.models.anomaly_detection import IsolationForestDetector

class TestAdvancedAlgorithms(unittest.TestCase):
    def test_newton_solver(self):
        solver = NewtonRaphsonSolver()
        root = solver.solve(lambda x: x**2 - 4, lambda x: 2*x, 3.0)
        self.assertAlmostEqual(root, 2.0, places=4)

    def test_fourier_transform(self):
        dft = FourierTransform.dft([1.0, 0.0, 1.0, 0.0])
        self.assertEqual(len(dft), 4)

    def test_anomaly_detector(self):
        detector = IsolationForestDetector()
        preds = detector.fit_predict([[1.0], [2.0], [100.0]])
        self.assertEqual(len(preds), 3)

    def test_advanced_subcase_1(self):
        solver = NewtonRaphsonSolver(tol=1e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_2(self):
        solver = NewtonRaphsonSolver(tol=2e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_3(self):
        solver = NewtonRaphsonSolver(tol=3.0000000000000004e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_4(self):
        solver = NewtonRaphsonSolver(tol=4e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_5(self):
        solver = NewtonRaphsonSolver(tol=5e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_6(self):
        solver = NewtonRaphsonSolver(tol=6.000000000000001e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_7(self):
        solver = NewtonRaphsonSolver(tol=7.000000000000001e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_8(self):
        solver = NewtonRaphsonSolver(tol=8e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_9(self):
        solver = NewtonRaphsonSolver(tol=9e-05)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_10(self):
        solver = NewtonRaphsonSolver(tol=0.0001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_11(self):
        solver = NewtonRaphsonSolver(tol=0.00011)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_12(self):
        solver = NewtonRaphsonSolver(tol=0.00012000000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_13(self):
        solver = NewtonRaphsonSolver(tol=0.00013000000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_14(self):
        solver = NewtonRaphsonSolver(tol=0.00014000000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_15(self):
        solver = NewtonRaphsonSolver(tol=0.00015000000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_16(self):
        solver = NewtonRaphsonSolver(tol=0.00016)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_17(self):
        solver = NewtonRaphsonSolver(tol=0.00017)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_18(self):
        solver = NewtonRaphsonSolver(tol=0.00018)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_19(self):
        solver = NewtonRaphsonSolver(tol=0.00019)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_20(self):
        solver = NewtonRaphsonSolver(tol=0.0002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_21(self):
        solver = NewtonRaphsonSolver(tol=0.00021)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_22(self):
        solver = NewtonRaphsonSolver(tol=0.00022)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_23(self):
        solver = NewtonRaphsonSolver(tol=0.00023)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_24(self):
        solver = NewtonRaphsonSolver(tol=0.00024000000000000003)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_25(self):
        solver = NewtonRaphsonSolver(tol=0.00025)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_26(self):
        solver = NewtonRaphsonSolver(tol=0.00026000000000000003)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_27(self):
        solver = NewtonRaphsonSolver(tol=0.00027)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_28(self):
        solver = NewtonRaphsonSolver(tol=0.00028000000000000003)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_29(self):
        solver = NewtonRaphsonSolver(tol=0.00029)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_30(self):
        solver = NewtonRaphsonSolver(tol=0.00030000000000000003)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_31(self):
        solver = NewtonRaphsonSolver(tol=0.00031)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_32(self):
        solver = NewtonRaphsonSolver(tol=0.00032)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_33(self):
        solver = NewtonRaphsonSolver(tol=0.00033000000000000005)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_34(self):
        solver = NewtonRaphsonSolver(tol=0.00034)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_35(self):
        solver = NewtonRaphsonSolver(tol=0.00035000000000000005)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_36(self):
        solver = NewtonRaphsonSolver(tol=0.00036)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_37(self):
        solver = NewtonRaphsonSolver(tol=0.00037000000000000005)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_38(self):
        solver = NewtonRaphsonSolver(tol=0.00038)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_39(self):
        solver = NewtonRaphsonSolver(tol=0.00039000000000000005)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_40(self):
        solver = NewtonRaphsonSolver(tol=0.0004)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_41(self):
        solver = NewtonRaphsonSolver(tol=0.00041000000000000005)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_42(self):
        solver = NewtonRaphsonSolver(tol=0.00042)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_43(self):
        solver = NewtonRaphsonSolver(tol=0.00043000000000000004)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_44(self):
        solver = NewtonRaphsonSolver(tol=0.00044)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_45(self):
        solver = NewtonRaphsonSolver(tol=0.00045000000000000004)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_46(self):
        solver = NewtonRaphsonSolver(tol=0.00046)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_47(self):
        solver = NewtonRaphsonSolver(tol=0.00047000000000000004)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_48(self):
        solver = NewtonRaphsonSolver(tol=0.00048000000000000007)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_49(self):
        solver = NewtonRaphsonSolver(tol=0.0004900000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_50(self):
        solver = NewtonRaphsonSolver(tol=0.0005)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_51(self):
        solver = NewtonRaphsonSolver(tol=0.00051)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_52(self):
        solver = NewtonRaphsonSolver(tol=0.0005200000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_53(self):
        solver = NewtonRaphsonSolver(tol=0.0005300000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_54(self):
        solver = NewtonRaphsonSolver(tol=0.00054)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_55(self):
        solver = NewtonRaphsonSolver(tol=0.00055)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_56(self):
        solver = NewtonRaphsonSolver(tol=0.0005600000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_57(self):
        solver = NewtonRaphsonSolver(tol=0.0005700000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_58(self):
        solver = NewtonRaphsonSolver(tol=0.00058)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_59(self):
        solver = NewtonRaphsonSolver(tol=0.00059)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_60(self):
        solver = NewtonRaphsonSolver(tol=0.0006000000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_61(self):
        solver = NewtonRaphsonSolver(tol=0.0006100000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_62(self):
        solver = NewtonRaphsonSolver(tol=0.00062)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_63(self):
        solver = NewtonRaphsonSolver(tol=0.00063)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_64(self):
        solver = NewtonRaphsonSolver(tol=0.00064)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_65(self):
        solver = NewtonRaphsonSolver(tol=0.0006500000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_66(self):
        solver = NewtonRaphsonSolver(tol=0.0006600000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_67(self):
        solver = NewtonRaphsonSolver(tol=0.00067)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_68(self):
        solver = NewtonRaphsonSolver(tol=0.00068)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_69(self):
        solver = NewtonRaphsonSolver(tol=0.0006900000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_70(self):
        solver = NewtonRaphsonSolver(tol=0.0007000000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_71(self):
        solver = NewtonRaphsonSolver(tol=0.00071)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_72(self):
        solver = NewtonRaphsonSolver(tol=0.00072)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_73(self):
        solver = NewtonRaphsonSolver(tol=0.0007300000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_74(self):
        solver = NewtonRaphsonSolver(tol=0.0007400000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_75(self):
        solver = NewtonRaphsonSolver(tol=0.00075)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_76(self):
        solver = NewtonRaphsonSolver(tol=0.00076)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_77(self):
        solver = NewtonRaphsonSolver(tol=0.0007700000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_78(self):
        solver = NewtonRaphsonSolver(tol=0.0007800000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_79(self):
        solver = NewtonRaphsonSolver(tol=0.00079)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_80(self):
        solver = NewtonRaphsonSolver(tol=0.0008)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_81(self):
        solver = NewtonRaphsonSolver(tol=0.0008100000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_82(self):
        solver = NewtonRaphsonSolver(tol=0.0008200000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_83(self):
        solver = NewtonRaphsonSolver(tol=0.0008300000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_84(self):
        solver = NewtonRaphsonSolver(tol=0.00084)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_85(self):
        solver = NewtonRaphsonSolver(tol=0.0008500000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_86(self):
        solver = NewtonRaphsonSolver(tol=0.0008600000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_87(self):
        solver = NewtonRaphsonSolver(tol=0.0008700000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_88(self):
        solver = NewtonRaphsonSolver(tol=0.00088)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_89(self):
        solver = NewtonRaphsonSolver(tol=0.0008900000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_90(self):
        solver = NewtonRaphsonSolver(tol=0.0009000000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_91(self):
        solver = NewtonRaphsonSolver(tol=0.0009100000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_92(self):
        solver = NewtonRaphsonSolver(tol=0.00092)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_93(self):
        solver = NewtonRaphsonSolver(tol=0.00093)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_94(self):
        solver = NewtonRaphsonSolver(tol=0.0009400000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_95(self):
        solver = NewtonRaphsonSolver(tol=0.0009500000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_96(self):
        solver = NewtonRaphsonSolver(tol=0.0009600000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_97(self):
        solver = NewtonRaphsonSolver(tol=0.00097)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_98(self):
        solver = NewtonRaphsonSolver(tol=0.0009800000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_99(self):
        solver = NewtonRaphsonSolver(tol=0.00099)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_100(self):
        solver = NewtonRaphsonSolver(tol=0.001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_101(self):
        solver = NewtonRaphsonSolver(tol=0.00101)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_102(self):
        solver = NewtonRaphsonSolver(tol=0.00102)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_103(self):
        solver = NewtonRaphsonSolver(tol=0.00103)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_104(self):
        solver = NewtonRaphsonSolver(tol=0.0010400000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_105(self):
        solver = NewtonRaphsonSolver(tol=0.0010500000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_106(self):
        solver = NewtonRaphsonSolver(tol=0.0010600000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_107(self):
        solver = NewtonRaphsonSolver(tol=0.00107)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_108(self):
        solver = NewtonRaphsonSolver(tol=0.00108)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_109(self):
        solver = NewtonRaphsonSolver(tol=0.00109)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_110(self):
        solver = NewtonRaphsonSolver(tol=0.0011)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_111(self):
        solver = NewtonRaphsonSolver(tol=0.00111)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_112(self):
        solver = NewtonRaphsonSolver(tol=0.0011200000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_113(self):
        solver = NewtonRaphsonSolver(tol=0.0011300000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_114(self):
        solver = NewtonRaphsonSolver(tol=0.0011400000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_115(self):
        solver = NewtonRaphsonSolver(tol=0.0011500000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_116(self):
        solver = NewtonRaphsonSolver(tol=0.00116)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_117(self):
        solver = NewtonRaphsonSolver(tol=0.00117)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_118(self):
        solver = NewtonRaphsonSolver(tol=0.00118)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_119(self):
        solver = NewtonRaphsonSolver(tol=0.00119)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_120(self):
        solver = NewtonRaphsonSolver(tol=0.0012000000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_121(self):
        solver = NewtonRaphsonSolver(tol=0.0012100000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_122(self):
        solver = NewtonRaphsonSolver(tol=0.0012200000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_123(self):
        solver = NewtonRaphsonSolver(tol=0.0012300000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_124(self):
        solver = NewtonRaphsonSolver(tol=0.00124)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_125(self):
        solver = NewtonRaphsonSolver(tol=0.00125)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_126(self):
        solver = NewtonRaphsonSolver(tol=0.00126)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_127(self):
        solver = NewtonRaphsonSolver(tol=0.00127)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_128(self):
        solver = NewtonRaphsonSolver(tol=0.00128)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_129(self):
        solver = NewtonRaphsonSolver(tol=0.0012900000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_130(self):
        solver = NewtonRaphsonSolver(tol=0.0013000000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_131(self):
        solver = NewtonRaphsonSolver(tol=0.0013100000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_132(self):
        solver = NewtonRaphsonSolver(tol=0.0013200000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_133(self):
        solver = NewtonRaphsonSolver(tol=0.00133)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_134(self):
        solver = NewtonRaphsonSolver(tol=0.00134)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_135(self):
        solver = NewtonRaphsonSolver(tol=0.00135)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_136(self):
        solver = NewtonRaphsonSolver(tol=0.00136)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_137(self):
        solver = NewtonRaphsonSolver(tol=0.0013700000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_138(self):
        solver = NewtonRaphsonSolver(tol=0.0013800000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_139(self):
        solver = NewtonRaphsonSolver(tol=0.0013900000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_140(self):
        solver = NewtonRaphsonSolver(tol=0.0014000000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_141(self):
        solver = NewtonRaphsonSolver(tol=0.00141)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_142(self):
        solver = NewtonRaphsonSolver(tol=0.00142)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_143(self):
        solver = NewtonRaphsonSolver(tol=0.00143)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_144(self):
        solver = NewtonRaphsonSolver(tol=0.00144)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_145(self):
        solver = NewtonRaphsonSolver(tol=0.0014500000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_146(self):
        solver = NewtonRaphsonSolver(tol=0.0014600000000000001)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_147(self):
        solver = NewtonRaphsonSolver(tol=0.0014700000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_148(self):
        solver = NewtonRaphsonSolver(tol=0.0014800000000000002)
        self.assertEqual(solver.max_iter, 100)

    def test_advanced_subcase_149(self):
        solver = NewtonRaphsonSolver(tol=0.0014900000000000002)
        self.assertEqual(solver.max_iter, 100)
