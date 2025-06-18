import yfinance as yf
import inspect
import traceback
import time
import datetime
import pandas as pd
import numpy as np
import sklearn as skl


def check_minimum_version():
    """
    Check the minimum version of scikit-learn on the given path.

    Parameters
    ----------
    path : str
        Path to the scikit-learn package.

    Returns
    -------
    bool
        True if the minimum version is satisfied.
    """
    startTime=time.perf_counter()
    try:
        assert np.__version__ >= "1.19"
        print(f"Numpy Version: {np.__version__}")
        assert pd.__version__ >= "1.2"
        print(f"Pandas Version: {pd.__version__}")
        assert skl.__version__ >= "0.20"
        print(f"sklearn Version: {skl.__version__}")
        assert yf.__version__ >= "0.1.63"
        print(f"yfinance Version: {yf.__version__}")
        return True
    except Exception as err:
        print(f"AssertionError: {err}")
        print(traceback.format_exc())
        return False
    finally:
        totalTime=(time.perf_counter() - startTime)
        print(f"METHOD: {inspect.stack()[0][3]} completed in {format(totalTime, '6.3f')} seconds or {format(totalTime / 60, '6.3f')} minutes ")
