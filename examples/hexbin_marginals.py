"""
Hexbin plot with marginal distributions
=======================================

_thumb: .45, .4
"""

import numpy as np
import seaborn as sns

sns.set_theme(style="ticks")

rs = np.random.RandomState(11)
x = rs.gamma(2, size=1000)
y = -0.5 * x + rs.normal(size=1000)

sns.jointplot(x=x, y=y, kind="hex", color="#4CB391")
