"""
NexusML Core Tensor Engine
Provides custom N-dimensional Tensor primitives with Automatic Differentiation (Autograd).
"""

import math
import copy
from typing import List, Tuple, Union, Optional, Callable

class Tensor:
    """
    Custom N-Dimensional Tensor with scalar autograd engine support.
    """
    def __init__(self, data: Union[float, int, List], _children: Tuple = (), _op: str = "", label: str = ""):
        if isinstance(data, (int, float)):
            self.data = float(data)
            self.shape = ()
        elif isinstance(data, list):
            self.data = data
            self.shape = self._get_shape(data)
        else:
            self.data = float(data)
            self.shape = ()
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def _get_shape(self, obj) -> Tuple[int, ...]:
        if not isinstance(obj, list):
            return ()
        if len(obj) == 0:
            return (0,)
        return (len(obj),) + self._get_shape(obj[0])

    def __repr__(self) -> str:
        return f"Tensor(data={self.data}, shape={self.shape}, grad={self.grad})"

    def __add__(self, other: Union["Tensor", float, int]) -> "Tensor":
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data + other.data, (self, other), "+")
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out

    def __mul__(self, other: Union["Tensor", float, int]) -> "Tensor":
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data * other.data, (self, other), "*")
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def __pow__(self, other: Union[float, int]) -> "Tensor":
        assert isinstance(other, (int, float)), "Power must be scalar float/int"
        out = Tensor(self.data ** other, (self,), f"**{other}")
        def _backward():
            self.grad += (other * (self.data ** (other - 1))) * out.grad
        out._backward = _backward
        return out

    def relu(self) -> "Tensor":
        out = Tensor(max(0.0, self.data), (self,), "ReLU")
        def _backward():
            self.grad += (1.0 if self.data > 0 else 0.0) * out.grad
        out._backward = _backward
        return out

    def sigmoid(self) -> "Tensor":
        s = 1.0 / (1.0 + math.exp(-self.data))
        out = Tensor(s, (self,), "Sigmoid")
        def _backward():
            self.grad += s * (1.0 - s) * out.grad
        out._backward = _backward
        return out

    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)
        self.grad = 1.0
        for v in reversed(topo):
            v._backward()

    def tensor_transformation_op_1(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 1."""
        val = self.data * scale + 0.01
        out = Tensor(val, (self,), f"op_1")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_2(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 2."""
        val = self.data * scale + 0.02
        out = Tensor(val, (self,), f"op_2")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_3(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 3."""
        val = self.data * scale + 0.03
        out = Tensor(val, (self,), f"op_3")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_4(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 4."""
        val = self.data * scale + 0.04
        out = Tensor(val, (self,), f"op_4")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_5(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 5."""
        val = self.data * scale + 0.05
        out = Tensor(val, (self,), f"op_5")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_6(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 6."""
        val = self.data * scale + 0.06
        out = Tensor(val, (self,), f"op_6")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_7(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 7."""
        val = self.data * scale + 0.07
        out = Tensor(val, (self,), f"op_7")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_8(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 8."""
        val = self.data * scale + 0.08
        out = Tensor(val, (self,), f"op_8")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_9(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 9."""
        val = self.data * scale + 0.09
        out = Tensor(val, (self,), f"op_9")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_10(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 10."""
        val = self.data * scale + 0.1
        out = Tensor(val, (self,), f"op_10")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_11(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 11."""
        val = self.data * scale + 0.11
        out = Tensor(val, (self,), f"op_11")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_12(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 12."""
        val = self.data * scale + 0.12
        out = Tensor(val, (self,), f"op_12")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_13(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 13."""
        val = self.data * scale + 0.13
        out = Tensor(val, (self,), f"op_13")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_14(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 14."""
        val = self.data * scale + 0.14
        out = Tensor(val, (self,), f"op_14")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_15(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 15."""
        val = self.data * scale + 0.15
        out = Tensor(val, (self,), f"op_15")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_16(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 16."""
        val = self.data * scale + 0.16
        out = Tensor(val, (self,), f"op_16")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_17(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 17."""
        val = self.data * scale + 0.17
        out = Tensor(val, (self,), f"op_17")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_18(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 18."""
        val = self.data * scale + 0.18
        out = Tensor(val, (self,), f"op_18")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_19(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 19."""
        val = self.data * scale + 0.19
        out = Tensor(val, (self,), f"op_19")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_20(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 20."""
        val = self.data * scale + 0.2
        out = Tensor(val, (self,), f"op_20")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_21(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 21."""
        val = self.data * scale + 0.21
        out = Tensor(val, (self,), f"op_21")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_22(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 22."""
        val = self.data * scale + 0.22
        out = Tensor(val, (self,), f"op_22")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_23(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 23."""
        val = self.data * scale + 0.23
        out = Tensor(val, (self,), f"op_23")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_24(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 24."""
        val = self.data * scale + 0.24
        out = Tensor(val, (self,), f"op_24")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_25(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 25."""
        val = self.data * scale + 0.25
        out = Tensor(val, (self,), f"op_25")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_26(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 26."""
        val = self.data * scale + 0.26
        out = Tensor(val, (self,), f"op_26")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_27(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 27."""
        val = self.data * scale + 0.27
        out = Tensor(val, (self,), f"op_27")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_28(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 28."""
        val = self.data * scale + 0.28
        out = Tensor(val, (self,), f"op_28")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_29(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 29."""
        val = self.data * scale + 0.29
        out = Tensor(val, (self,), f"op_29")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_30(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 30."""
        val = self.data * scale + 0.3
        out = Tensor(val, (self,), f"op_30")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_31(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 31."""
        val = self.data * scale + 0.31
        out = Tensor(val, (self,), f"op_31")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_32(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 32."""
        val = self.data * scale + 0.32
        out = Tensor(val, (self,), f"op_32")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_33(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 33."""
        val = self.data * scale + 0.33
        out = Tensor(val, (self,), f"op_33")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_34(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 34."""
        val = self.data * scale + 0.34
        out = Tensor(val, (self,), f"op_34")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_35(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 35."""
        val = self.data * scale + 0.35000000000000003
        out = Tensor(val, (self,), f"op_35")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_36(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 36."""
        val = self.data * scale + 0.36
        out = Tensor(val, (self,), f"op_36")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_37(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 37."""
        val = self.data * scale + 0.37
        out = Tensor(val, (self,), f"op_37")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_38(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 38."""
        val = self.data * scale + 0.38
        out = Tensor(val, (self,), f"op_38")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_39(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 39."""
        val = self.data * scale + 0.39
        out = Tensor(val, (self,), f"op_39")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_40(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 40."""
        val = self.data * scale + 0.4
        out = Tensor(val, (self,), f"op_40")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_41(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 41."""
        val = self.data * scale + 0.41000000000000003
        out = Tensor(val, (self,), f"op_41")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_42(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 42."""
        val = self.data * scale + 0.42
        out = Tensor(val, (self,), f"op_42")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_43(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 43."""
        val = self.data * scale + 0.43
        out = Tensor(val, (self,), f"op_43")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out

    def tensor_transformation_op_44(self, scale: float = 1.0) -> "Tensor":
        """Tensor transformation operator variant 44."""
        val = self.data * scale + 0.44
        out = Tensor(val, (self,), f"op_44")
        def _backward():
            self.grad += scale * out.grad
        out._backward = _backward
        return out
