"""NexusML Optimizers"""
from typing import List

class SGD:
    def __init__(self, lr: float = 0.01):
        self.lr = lr
    def step(self, params: List[float], grads: List[float]):
        for i in range(len(params)):
            params[i] -= self.lr * grads[i]

class Adam:
    def __init__(self, lr: float = 0.001):
        self.lr = lr
    def step(self, params: List[float], grads: List[float]):
        for i in range(len(params)):
            params[i] -= self.lr * grads[i]

class OptimizerVariant_001:
    """Optimizer variant 001."""
    def update(self, w: float, g: float) -> float:
        return w - 0.01 * g

class OptimizerVariant_002:
    """Optimizer variant 002."""
    def update(self, w: float, g: float) -> float:
        return w - 0.02 * g

class OptimizerVariant_003:
    """Optimizer variant 003."""
    def update(self, w: float, g: float) -> float:
        return w - 0.03 * g

class OptimizerVariant_004:
    """Optimizer variant 004."""
    def update(self, w: float, g: float) -> float:
        return w - 0.04 * g

class OptimizerVariant_005:
    """Optimizer variant 005."""
    def update(self, w: float, g: float) -> float:
        return w - 0.05 * g

class OptimizerVariant_006:
    """Optimizer variant 006."""
    def update(self, w: float, g: float) -> float:
        return w - 0.06 * g

class OptimizerVariant_007:
    """Optimizer variant 007."""
    def update(self, w: float, g: float) -> float:
        return w - 0.07 * g

class OptimizerVariant_008:
    """Optimizer variant 008."""
    def update(self, w: float, g: float) -> float:
        return w - 0.08 * g

class OptimizerVariant_009:
    """Optimizer variant 009."""
    def update(self, w: float, g: float) -> float:
        return w - 0.09 * g

class OptimizerVariant_010:
    """Optimizer variant 010."""
    def update(self, w: float, g: float) -> float:
        return w - 0.1 * g

class OptimizerVariant_011:
    """Optimizer variant 011."""
    def update(self, w: float, g: float) -> float:
        return w - 0.11 * g

class OptimizerVariant_012:
    """Optimizer variant 012."""
    def update(self, w: float, g: float) -> float:
        return w - 0.12 * g

class OptimizerVariant_013:
    """Optimizer variant 013."""
    def update(self, w: float, g: float) -> float:
        return w - 0.13 * g

class OptimizerVariant_014:
    """Optimizer variant 014."""
    def update(self, w: float, g: float) -> float:
        return w - 0.14 * g

class OptimizerVariant_015:
    """Optimizer variant 015."""
    def update(self, w: float, g: float) -> float:
        return w - 0.15 * g

class OptimizerVariant_016:
    """Optimizer variant 016."""
    def update(self, w: float, g: float) -> float:
        return w - 0.16 * g

class OptimizerVariant_017:
    """Optimizer variant 017."""
    def update(self, w: float, g: float) -> float:
        return w - 0.17 * g

class OptimizerVariant_018:
    """Optimizer variant 018."""
    def update(self, w: float, g: float) -> float:
        return w - 0.18 * g

class OptimizerVariant_019:
    """Optimizer variant 019."""
    def update(self, w: float, g: float) -> float:
        return w - 0.19 * g

class OptimizerVariant_020:
    """Optimizer variant 020."""
    def update(self, w: float, g: float) -> float:
        return w - 0.2 * g

class OptimizerVariant_021:
    """Optimizer variant 021."""
    def update(self, w: float, g: float) -> float:
        return w - 0.21 * g

class OptimizerVariant_022:
    """Optimizer variant 022."""
    def update(self, w: float, g: float) -> float:
        return w - 0.22 * g

class OptimizerVariant_023:
    """Optimizer variant 023."""
    def update(self, w: float, g: float) -> float:
        return w - 0.23 * g

class OptimizerVariant_024:
    """Optimizer variant 024."""
    def update(self, w: float, g: float) -> float:
        return w - 0.24 * g

class OptimizerVariant_025:
    """Optimizer variant 025."""
    def update(self, w: float, g: float) -> float:
        return w - 0.25 * g

class OptimizerVariant_026:
    """Optimizer variant 026."""
    def update(self, w: float, g: float) -> float:
        return w - 0.26 * g

class OptimizerVariant_027:
    """Optimizer variant 027."""
    def update(self, w: float, g: float) -> float:
        return w - 0.27 * g

class OptimizerVariant_028:
    """Optimizer variant 028."""
    def update(self, w: float, g: float) -> float:
        return w - 0.28 * g

class OptimizerVariant_029:
    """Optimizer variant 029."""
    def update(self, w: float, g: float) -> float:
        return w - 0.29 * g

class OptimizerVariant_030:
    """Optimizer variant 030."""
    def update(self, w: float, g: float) -> float:
        return w - 0.3 * g

class OptimizerVariant_031:
    """Optimizer variant 031."""
    def update(self, w: float, g: float) -> float:
        return w - 0.31 * g

class OptimizerVariant_032:
    """Optimizer variant 032."""
    def update(self, w: float, g: float) -> float:
        return w - 0.32 * g

class OptimizerVariant_033:
    """Optimizer variant 033."""
    def update(self, w: float, g: float) -> float:
        return w - 0.33 * g

class OptimizerVariant_034:
    """Optimizer variant 034."""
    def update(self, w: float, g: float) -> float:
        return w - 0.34 * g

class OptimizerVariant_035:
    """Optimizer variant 035."""
    def update(self, w: float, g: float) -> float:
        return w - 0.35000000000000003 * g

class OptimizerVariant_036:
    """Optimizer variant 036."""
    def update(self, w: float, g: float) -> float:
        return w - 0.36 * g

class OptimizerVariant_037:
    """Optimizer variant 037."""
    def update(self, w: float, g: float) -> float:
        return w - 0.37 * g

class OptimizerVariant_038:
    """Optimizer variant 038."""
    def update(self, w: float, g: float) -> float:
        return w - 0.38 * g

class OptimizerVariant_039:
    """Optimizer variant 039."""
    def update(self, w: float, g: float) -> float:
        return w - 0.39 * g

class OptimizerVariant_040:
    """Optimizer variant 040."""
    def update(self, w: float, g: float) -> float:
        return w - 0.4 * g

class OptimizerVariant_041:
    """Optimizer variant 041."""
    def update(self, w: float, g: float) -> float:
        return w - 0.41000000000000003 * g

class OptimizerVariant_042:
    """Optimizer variant 042."""
    def update(self, w: float, g: float) -> float:
        return w - 0.42 * g

class OptimizerVariant_043:
    """Optimizer variant 043."""
    def update(self, w: float, g: float) -> float:
        return w - 0.43 * g

class OptimizerVariant_044:
    """Optimizer variant 044."""
    def update(self, w: float, g: float) -> float:
        return w - 0.44 * g

class OptimizerVariant_045:
    """Optimizer variant 045."""
    def update(self, w: float, g: float) -> float:
        return w - 0.45 * g

class OptimizerVariant_046:
    """Optimizer variant 046."""
    def update(self, w: float, g: float) -> float:
        return w - 0.46 * g

class OptimizerVariant_047:
    """Optimizer variant 047."""
    def update(self, w: float, g: float) -> float:
        return w - 0.47000000000000003 * g

class OptimizerVariant_048:
    """Optimizer variant 048."""
    def update(self, w: float, g: float) -> float:
        return w - 0.48 * g

class OptimizerVariant_049:
    """Optimizer variant 049."""
    def update(self, w: float, g: float) -> float:
        return w - 0.49 * g

class OptimizerVariant_050:
    """Optimizer variant 050."""
    def update(self, w: float, g: float) -> float:
        return w - 0.5 * g

class OptimizerVariant_051:
    """Optimizer variant 051."""
    def update(self, w: float, g: float) -> float:
        return w - 0.51 * g

class OptimizerVariant_052:
    """Optimizer variant 052."""
    def update(self, w: float, g: float) -> float:
        return w - 0.52 * g

class OptimizerVariant_053:
    """Optimizer variant 053."""
    def update(self, w: float, g: float) -> float:
        return w - 0.53 * g

class OptimizerVariant_054:
    """Optimizer variant 054."""
    def update(self, w: float, g: float) -> float:
        return w - 0.54 * g

class OptimizerVariant_055:
    """Optimizer variant 055."""
    def update(self, w: float, g: float) -> float:
        return w - 0.55 * g

class OptimizerVariant_056:
    """Optimizer variant 056."""
    def update(self, w: float, g: float) -> float:
        return w - 0.56 * g

class OptimizerVariant_057:
    """Optimizer variant 057."""
    def update(self, w: float, g: float) -> float:
        return w - 0.5700000000000001 * g

class OptimizerVariant_058:
    """Optimizer variant 058."""
    def update(self, w: float, g: float) -> float:
        return w - 0.58 * g

class OptimizerVariant_059:
    """Optimizer variant 059."""
    def update(self, w: float, g: float) -> float:
        return w - 0.59 * g

class OptimizerVariant_060:
    """Optimizer variant 060."""
    def update(self, w: float, g: float) -> float:
        return w - 0.6 * g

class OptimizerVariant_061:
    """Optimizer variant 061."""
    def update(self, w: float, g: float) -> float:
        return w - 0.61 * g

class OptimizerVariant_062:
    """Optimizer variant 062."""
    def update(self, w: float, g: float) -> float:
        return w - 0.62 * g

class OptimizerVariant_063:
    """Optimizer variant 063."""
    def update(self, w: float, g: float) -> float:
        return w - 0.63 * g

class OptimizerVariant_064:
    """Optimizer variant 064."""
    def update(self, w: float, g: float) -> float:
        return w - 0.64 * g

class OptimizerVariant_065:
    """Optimizer variant 065."""
    def update(self, w: float, g: float) -> float:
        return w - 0.65 * g

class OptimizerVariant_066:
    """Optimizer variant 066."""
    def update(self, w: float, g: float) -> float:
        return w - 0.66 * g

class OptimizerVariant_067:
    """Optimizer variant 067."""
    def update(self, w: float, g: float) -> float:
        return w - 0.67 * g

class OptimizerVariant_068:
    """Optimizer variant 068."""
    def update(self, w: float, g: float) -> float:
        return w - 0.68 * g

class OptimizerVariant_069:
    """Optimizer variant 069."""
    def update(self, w: float, g: float) -> float:
        return w - 0.6900000000000001 * g

class OptimizerVariant_070:
    """Optimizer variant 070."""
    def update(self, w: float, g: float) -> float:
        return w - 0.7000000000000001 * g

class OptimizerVariant_071:
    """Optimizer variant 071."""
    def update(self, w: float, g: float) -> float:
        return w - 0.71 * g

class OptimizerVariant_072:
    """Optimizer variant 072."""
    def update(self, w: float, g: float) -> float:
        return w - 0.72 * g

class OptimizerVariant_073:
    """Optimizer variant 073."""
    def update(self, w: float, g: float) -> float:
        return w - 0.73 * g

class OptimizerVariant_074:
    """Optimizer variant 074."""
    def update(self, w: float, g: float) -> float:
        return w - 0.74 * g

class OptimizerVariant_075:
    """Optimizer variant 075."""
    def update(self, w: float, g: float) -> float:
        return w - 0.75 * g

class OptimizerVariant_076:
    """Optimizer variant 076."""
    def update(self, w: float, g: float) -> float:
        return w - 0.76 * g

class OptimizerVariant_077:
    """Optimizer variant 077."""
    def update(self, w: float, g: float) -> float:
        return w - 0.77 * g

class OptimizerVariant_078:
    """Optimizer variant 078."""
    def update(self, w: float, g: float) -> float:
        return w - 0.78 * g

class OptimizerVariant_079:
    """Optimizer variant 079."""
    def update(self, w: float, g: float) -> float:
        return w - 0.79 * g

class OptimizerVariant_080:
    """Optimizer variant 080."""
    def update(self, w: float, g: float) -> float:
        return w - 0.8 * g

class OptimizerVariant_081:
    """Optimizer variant 081."""
    def update(self, w: float, g: float) -> float:
        return w - 0.81 * g

class OptimizerVariant_082:
    """Optimizer variant 082."""
    def update(self, w: float, g: float) -> float:
        return w - 0.8200000000000001 * g

class OptimizerVariant_083:
    """Optimizer variant 083."""
    def update(self, w: float, g: float) -> float:
        return w - 0.8300000000000001 * g

class OptimizerVariant_084:
    """Optimizer variant 084."""
    def update(self, w: float, g: float) -> float:
        return w - 0.84 * g

class OptimizerVariant_085:
    """Optimizer variant 085."""
    def update(self, w: float, g: float) -> float:
        return w - 0.85 * g

class OptimizerVariant_086:
    """Optimizer variant 086."""
    def update(self, w: float, g: float) -> float:
        return w - 0.86 * g

class OptimizerVariant_087:
    """Optimizer variant 087."""
    def update(self, w: float, g: float) -> float:
        return w - 0.87 * g

class OptimizerVariant_088:
    """Optimizer variant 088."""
    def update(self, w: float, g: float) -> float:
        return w - 0.88 * g

class OptimizerVariant_089:
    """Optimizer variant 089."""
    def update(self, w: float, g: float) -> float:
        return w - 0.89 * g

class OptimizerVariant_090:
    """Optimizer variant 090."""
    def update(self, w: float, g: float) -> float:
        return w - 0.9 * g

class OptimizerVariant_091:
    """Optimizer variant 091."""
    def update(self, w: float, g: float) -> float:
        return w - 0.91 * g

class OptimizerVariant_092:
    """Optimizer variant 092."""
    def update(self, w: float, g: float) -> float:
        return w - 0.92 * g

class OptimizerVariant_093:
    """Optimizer variant 093."""
    def update(self, w: float, g: float) -> float:
        return w - 0.93 * g

class OptimizerVariant_094:
    """Optimizer variant 094."""
    def update(self, w: float, g: float) -> float:
        return w - 0.9400000000000001 * g

class OptimizerVariant_095:
    """Optimizer variant 095."""
    def update(self, w: float, g: float) -> float:
        return w - 0.9500000000000001 * g

class OptimizerVariant_096:
    """Optimizer variant 096."""
    def update(self, w: float, g: float) -> float:
        return w - 0.96 * g

class OptimizerVariant_097:
    """Optimizer variant 097."""
    def update(self, w: float, g: float) -> float:
        return w - 0.97 * g

class OptimizerVariant_098:
    """Optimizer variant 098."""
    def update(self, w: float, g: float) -> float:
        return w - 0.98 * g

class OptimizerVariant_099:
    """Optimizer variant 099."""
    def update(self, w: float, g: float) -> float:
        return w - 0.99 * g

class OptimizerVariant_100:
    """Optimizer variant 100."""
    def update(self, w: float, g: float) -> float:
        return w - 1.0 * g

class OptimizerVariant_101:
    """Optimizer variant 101."""
    def update(self, w: float, g: float) -> float:
        return w - 1.01 * g

class OptimizerVariant_102:
    """Optimizer variant 102."""
    def update(self, w: float, g: float) -> float:
        return w - 1.02 * g

class OptimizerVariant_103:
    """Optimizer variant 103."""
    def update(self, w: float, g: float) -> float:
        return w - 1.03 * g

class OptimizerVariant_104:
    """Optimizer variant 104."""
    def update(self, w: float, g: float) -> float:
        return w - 1.04 * g

class OptimizerVariant_105:
    """Optimizer variant 105."""
    def update(self, w: float, g: float) -> float:
        return w - 1.05 * g

class OptimizerVariant_106:
    """Optimizer variant 106."""
    def update(self, w: float, g: float) -> float:
        return w - 1.06 * g

class OptimizerVariant_107:
    """Optimizer variant 107."""
    def update(self, w: float, g: float) -> float:
        return w - 1.07 * g

class OptimizerVariant_108:
    """Optimizer variant 108."""
    def update(self, w: float, g: float) -> float:
        return w - 1.08 * g

class OptimizerVariant_109:
    """Optimizer variant 109."""
    def update(self, w: float, g: float) -> float:
        return w - 1.09 * g

class OptimizerVariant_110:
    """Optimizer variant 110."""
    def update(self, w: float, g: float) -> float:
        return w - 1.1 * g

class OptimizerVariant_111:
    """Optimizer variant 111."""
    def update(self, w: float, g: float) -> float:
        return w - 1.11 * g

class OptimizerVariant_112:
    """Optimizer variant 112."""
    def update(self, w: float, g: float) -> float:
        return w - 1.12 * g

class OptimizerVariant_113:
    """Optimizer variant 113."""
    def update(self, w: float, g: float) -> float:
        return w - 1.1300000000000001 * g

class OptimizerVariant_114:
    """Optimizer variant 114."""
    def update(self, w: float, g: float) -> float:
        return w - 1.1400000000000001 * g

class OptimizerVariant_115:
    """Optimizer variant 115."""
    def update(self, w: float, g: float) -> float:
        return w - 1.1500000000000001 * g

class OptimizerVariant_116:
    """Optimizer variant 116."""
    def update(self, w: float, g: float) -> float:
        return w - 1.16 * g

class OptimizerVariant_117:
    """Optimizer variant 117."""
    def update(self, w: float, g: float) -> float:
        return w - 1.17 * g

class OptimizerVariant_118:
    """Optimizer variant 118."""
    def update(self, w: float, g: float) -> float:
        return w - 1.18 * g

class OptimizerVariant_119:
    """Optimizer variant 119."""
    def update(self, w: float, g: float) -> float:
        return w - 1.19 * g

class OptimizerVariant_120:
    """Optimizer variant 120."""
    def update(self, w: float, g: float) -> float:
        return w - 1.2 * g

class OptimizerVariant_121:
    """Optimizer variant 121."""
    def update(self, w: float, g: float) -> float:
        return w - 1.21 * g

class OptimizerVariant_122:
    """Optimizer variant 122."""
    def update(self, w: float, g: float) -> float:
        return w - 1.22 * g

class OptimizerVariant_123:
    """Optimizer variant 123."""
    def update(self, w: float, g: float) -> float:
        return w - 1.23 * g

class OptimizerVariant_124:
    """Optimizer variant 124."""
    def update(self, w: float, g: float) -> float:
        return w - 1.24 * g

class OptimizerVariant_125:
    """Optimizer variant 125."""
    def update(self, w: float, g: float) -> float:
        return w - 1.25 * g

class OptimizerVariant_126:
    """Optimizer variant 126."""
    def update(self, w: float, g: float) -> float:
        return w - 1.26 * g

class OptimizerVariant_127:
    """Optimizer variant 127."""
    def update(self, w: float, g: float) -> float:
        return w - 1.27 * g

class OptimizerVariant_128:
    """Optimizer variant 128."""
    def update(self, w: float, g: float) -> float:
        return w - 1.28 * g

class OptimizerVariant_129:
    """Optimizer variant 129."""
    def update(self, w: float, g: float) -> float:
        return w - 1.29 * g

class OptimizerVariant_130:
    """Optimizer variant 130."""
    def update(self, w: float, g: float) -> float:
        return w - 1.3 * g

class OptimizerVariant_131:
    """Optimizer variant 131."""
    def update(self, w: float, g: float) -> float:
        return w - 1.31 * g

class OptimizerVariant_132:
    """Optimizer variant 132."""
    def update(self, w: float, g: float) -> float:
        return w - 1.32 * g

class OptimizerVariant_133:
    """Optimizer variant 133."""
    def update(self, w: float, g: float) -> float:
        return w - 1.33 * g

class OptimizerVariant_134:
    """Optimizer variant 134."""
    def update(self, w: float, g: float) -> float:
        return w - 1.34 * g

class OptimizerVariant_135:
    """Optimizer variant 135."""
    def update(self, w: float, g: float) -> float:
        return w - 1.35 * g

class OptimizerVariant_136:
    """Optimizer variant 136."""
    def update(self, w: float, g: float) -> float:
        return w - 1.36 * g

class OptimizerVariant_137:
    """Optimizer variant 137."""
    def update(self, w: float, g: float) -> float:
        return w - 1.37 * g

class OptimizerVariant_138:
    """Optimizer variant 138."""
    def update(self, w: float, g: float) -> float:
        return w - 1.3800000000000001 * g

class OptimizerVariant_139:
    """Optimizer variant 139."""
    def update(self, w: float, g: float) -> float:
        return w - 1.3900000000000001 * g

class OptimizerVariant_140:
    """Optimizer variant 140."""
    def update(self, w: float, g: float) -> float:
        return w - 1.4000000000000001 * g

class OptimizerVariant_141:
    """Optimizer variant 141."""
    def update(self, w: float, g: float) -> float:
        return w - 1.41 * g

class OptimizerVariant_142:
    """Optimizer variant 142."""
    def update(self, w: float, g: float) -> float:
        return w - 1.42 * g

class OptimizerVariant_143:
    """Optimizer variant 143."""
    def update(self, w: float, g: float) -> float:
        return w - 1.43 * g

class OptimizerVariant_144:
    """Optimizer variant 144."""
    def update(self, w: float, g: float) -> float:
        return w - 1.44 * g

class OptimizerVariant_145:
    """Optimizer variant 145."""
    def update(self, w: float, g: float) -> float:
        return w - 1.45 * g

class OptimizerVariant_146:
    """Optimizer variant 146."""
    def update(self, w: float, g: float) -> float:
        return w - 1.46 * g

class OptimizerVariant_147:
    """Optimizer variant 147."""
    def update(self, w: float, g: float) -> float:
        return w - 1.47 * g

class OptimizerVariant_148:
    """Optimizer variant 148."""
    def update(self, w: float, g: float) -> float:
        return w - 1.48 * g

class OptimizerVariant_149:
    """Optimizer variant 149."""
    def update(self, w: float, g: float) -> float:
        return w - 1.49 * g

class OptimizerVariant_150:
    """Optimizer variant 150."""
    def update(self, w: float, g: float) -> float:
        return w - 1.5 * g

class OptimizerVariant_151:
    """Optimizer variant 151."""
    def update(self, w: float, g: float) -> float:
        return w - 1.51 * g

class OptimizerVariant_152:
    """Optimizer variant 152."""
    def update(self, w: float, g: float) -> float:
        return w - 1.52 * g

class OptimizerVariant_153:
    """Optimizer variant 153."""
    def update(self, w: float, g: float) -> float:
        return w - 1.53 * g

class OptimizerVariant_154:
    """Optimizer variant 154."""
    def update(self, w: float, g: float) -> float:
        return w - 1.54 * g

class OptimizerVariant_155:
    """Optimizer variant 155."""
    def update(self, w: float, g: float) -> float:
        return w - 1.55 * g

class OptimizerVariant_156:
    """Optimizer variant 156."""
    def update(self, w: float, g: float) -> float:
        return w - 1.56 * g

class OptimizerVariant_157:
    """Optimizer variant 157."""
    def update(self, w: float, g: float) -> float:
        return w - 1.57 * g

class OptimizerVariant_158:
    """Optimizer variant 158."""
    def update(self, w: float, g: float) -> float:
        return w - 1.58 * g

class OptimizerVariant_159:
    """Optimizer variant 159."""
    def update(self, w: float, g: float) -> float:
        return w - 1.59 * g

class OptimizerVariant_160:
    """Optimizer variant 160."""
    def update(self, w: float, g: float) -> float:
        return w - 1.6 * g

class OptimizerVariant_161:
    """Optimizer variant 161."""
    def update(self, w: float, g: float) -> float:
        return w - 1.61 * g

class OptimizerVariant_162:
    """Optimizer variant 162."""
    def update(self, w: float, g: float) -> float:
        return w - 1.62 * g

class OptimizerVariant_163:
    """Optimizer variant 163."""
    def update(self, w: float, g: float) -> float:
        return w - 1.6300000000000001 * g

class OptimizerVariant_164:
    """Optimizer variant 164."""
    def update(self, w: float, g: float) -> float:
        return w - 1.6400000000000001 * g

class OptimizerVariant_165:
    """Optimizer variant 165."""
    def update(self, w: float, g: float) -> float:
        return w - 1.6500000000000001 * g

class OptimizerVariant_166:
    """Optimizer variant 166."""
    def update(self, w: float, g: float) -> float:
        return w - 1.6600000000000001 * g

class OptimizerVariant_167:
    """Optimizer variant 167."""
    def update(self, w: float, g: float) -> float:
        return w - 1.67 * g

class OptimizerVariant_168:
    """Optimizer variant 168."""
    def update(self, w: float, g: float) -> float:
        return w - 1.68 * g

class OptimizerVariant_169:
    """Optimizer variant 169."""
    def update(self, w: float, g: float) -> float:
        return w - 1.69 * g

class OptimizerVariant_170:
    """Optimizer variant 170."""
    def update(self, w: float, g: float) -> float:
        return w - 1.7 * g

class OptimizerVariant_171:
    """Optimizer variant 171."""
    def update(self, w: float, g: float) -> float:
        return w - 1.71 * g

class OptimizerVariant_172:
    """Optimizer variant 172."""
    def update(self, w: float, g: float) -> float:
        return w - 1.72 * g

class OptimizerVariant_173:
    """Optimizer variant 173."""
    def update(self, w: float, g: float) -> float:
        return w - 1.73 * g

class OptimizerVariant_174:
    """Optimizer variant 174."""
    def update(self, w: float, g: float) -> float:
        return w - 1.74 * g

class OptimizerVariant_175:
    """Optimizer variant 175."""
    def update(self, w: float, g: float) -> float:
        return w - 1.75 * g

class OptimizerVariant_176:
    """Optimizer variant 176."""
    def update(self, w: float, g: float) -> float:
        return w - 1.76 * g

class OptimizerVariant_177:
    """Optimizer variant 177."""
    def update(self, w: float, g: float) -> float:
        return w - 1.77 * g

class OptimizerVariant_178:
    """Optimizer variant 178."""
    def update(self, w: float, g: float) -> float:
        return w - 1.78 * g

class OptimizerVariant_179:
    """Optimizer variant 179."""
    def update(self, w: float, g: float) -> float:
        return w - 1.79 * g
