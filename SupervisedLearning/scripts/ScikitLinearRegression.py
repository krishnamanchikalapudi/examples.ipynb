import yfinance as yf
import inspect
import traceback
import time
import datetime
import pandas as pd
from sklearn.linear_model import LinearRegression as skl_LinearRegression
from sklearn.model_selection import train_test_split
import common.MinimumVersion as MinVer
from common.StockData import StockData

class ScikitLinearRegression:
    """ SciKit Linear Regression """
    def __init__(self):
        """Initialize the class"""
        self.check_minimum_version = MinVer.check_minimum_version()
        print(f"check_minimum_version: {self.check_minimum_version}")
 
    def sklearn_regression(self, X, y):
        """Linear Regression using sklearn"""
        startTime = time.perf_counter()
        try:
            model = skl_LinearRegression()
            model.fit(X, y)
            return model
        except Exception:
            print(f" Exception: {traceback.format_exc()}")
            return None
        finally:
            totalTime = (time.perf_counter() - startTime)
            print(f"METHOD: {inspect.stack()[0][3]} completed in {format(totalTime, '6.3f')} seconds")
    

    def sklearn_predict(self, model, X):
        """Predict using the model"""
        print(f"[BEGIN] METHOD: {inspect.stack()[0][3]} at {datetime.datetime.now()}")
        startTime = time.perf_counter()
        try:
            return model.predict(X)

        except Exception:
            print(f" Exception: {traceback.format_exc()}")
            return None
        finally:
            totalTime = (time.perf_counter() - startTime)
            print(f"METHOD: {inspect.stack()[0][3]} completed in {format(totalTime, '6.3f')} seconds")

    def main(self):
        """Main function"""
        if self.check_minimum_version:
            sd = StockData()
            stock_data = sd.stock_data("AAPL", "2021-03-01", "2021-08-31")
            stock_data.reset_index(inplace=True)
            stock_data.drop(columns=["High", "Low", "Volume",
                        "Dividends", "Stock Splits"], inplace=True)
            X = stock_data[['Date']]
            y = stock_data[['Close']]

            print(f"X: {X} \n y: {y}")
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=.2)  # 20% test data
            # Test set
            print(f"\nTest set::")
            print(f"X_test length:{len(X_test)}  y_test length:{len(y_test)} ")
            # Training set
            print(f"\nTraining set::")
            print(f"X_train length:{len(X_train)}  y_train length:{len(y_train)}")
        
            # print(f"X_train: {X_train} \n y_train: {y_train}")
            # Linear Regression - train model
            reg = lr.sklearn_regression(X_train, y_train)

            # Linear Regression - predict
            y_pred = lr.sklearn_predict(reg, X_test)

            # Linear Regression - compare
            y_pred = pd.DataFrame(y_pred, columns=['pred']).reset_index()
            print(f"\nlength:: y_test: {len(y_test)}  y_pred: {len(y_pred)}")
            
            sd.compare(y_test, y_pred)

            print(f"\nRegression Coefficients: {reg.coef_}")
            print(f"\nRegression Intercept: {reg.intercept_}")
            # print(f"\nRegression Score 'r**2': {reg.score(X_test, y_test)}")
            # print(f"\nRegression Mean Squared Error: {reg.score(X_test, y_test)}")

            # plot 
            print(f"*** X_test: \n{X_test} ")
            plot_df = pd.DataFrame({
                "X": X_test.Date.reset_index(drop=True),
                    "y": y_test.Close.reset_index(drop=True),
                    "pred": y_pred.pred.reset_index(drop=True)
                    })
            print(plot_df)
            sd.plot_stock(plot_df)
        else:
            print(f"minimum_version: {self.check_minimum_version}")

if __name__ == "__main__":
    """Main function for LinearRegression"""
    lr = ScikitLinearRegression()
    lr.main()
