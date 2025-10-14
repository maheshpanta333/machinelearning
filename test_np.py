import numpy as np
import pandas as pd

print("=== Simple NumPy integers (no seed) ===")
print("Run 1:", np.random.randint(0, 10, 5))
print("Run 2:", np.random.randint(0, 10, 5))
print("")

print("=== Using np.random.seed(0) (seeded) ===")
np.random.seed(0)
print("After seed(0) run 1:", np.random.randint(0, 10, 5))
np.random.seed(0)
print("After seed(0) run 2 (reset seed):", np.random.randint(0, 10, 5))
print("")

print("=== Different seed gives different but reproducible sequence ===")
np.random.seed(1)
print("seed(1):", np.random.randint(0, 10, 5))
np.random.seed(1)
print("seed(1) again:", np.random.randint(0, 10, 5))
print("")

print("=== New recommended API: np.random.default_rng ===")
rng1 = np.random.default_rng(42)
print("Generator(42) run 1:", rng1.integers(0, 10, 5))
rng2 = np.random.default_rng(42)
print("Generator(42) run 2 (new generator same seed):", rng2.integers(0, 10, 5))
rng3 = np.random.default_rng(7)
print("Generator(7):", rng3.integers(0, 10, 5))
print("")

print("=== pandas.DataFrame.sample with and without random_state ===")
df = pd.DataFrame({"name": list("ABCDEFGHIJ")})
print("DataFrame:\n", df.T.to_string(index=False))
print("\nSample without random_state (run1):\n", df.sample(4).reset_index(drop=True))
print("\nSample without random_state (run2):\n", df.sample(4).reset_index(drop=True))
print("\nSample WITH random_state=0 (run1):\n", df.sample(4, random_state=0).reset_index(drop=True))
print("\nSample WITH random_state=0 (run2):\n", df.sample(4, random_state=0).reset_index(drop=True))
