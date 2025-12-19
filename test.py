import sys
import numpy as np
import pandas as pd
import matplotlib

def main():
    print("Python executable:", sys.executable)
    print("Python version:", sys.version.split()[0])

    a = np.array([1, 2, 3])
    df = pd.DataFrame({"x": a, "y": a**2})
    print("\nDataFrame:")
    print(df)

    print("\nmatplotlib version:", matplotlib.__version__)
    print("\n✅ Python + numpy/pandas/matplotlib imports OK")

if __name__ == "__main__":
    main()
