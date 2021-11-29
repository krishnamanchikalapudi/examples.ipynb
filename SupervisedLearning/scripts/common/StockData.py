from re import T
import yfinance as yf
import inspect
import traceback
import time
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

class StockData:
    """StockData"""
    def __init__(self):
        pass

    def stock_data(self, ticker, start_date, end_date):
        """
            Get stock data from Yahoo Finance
        """
        startTime = time.perf_counter()
        try:
            stock = yf.Ticker(ticker)
            stock_data = stock.history(start=start_date, end=end_date)
            return stock_data
        except Exception:
            print(traceback.format_exc())
            return None
        finally:
            totalTime = (time.perf_counter() - startTime)
            print(f"METHOD: {inspect.stack()[0][3]} completed in {format(totalTime, '6.3f')} seconds ")
       
    def compare(self, y_test, y_pred):
        """
            Compare two Data Frames: y_test and y_pred
            """
        startTime = time.perf_counter()
        try:
            compare_df = pd.DataFrame(
                {"y_test": y_test['Close'], "y_pred": y_pred['pred']})
            compare_df.reset_index(inplace=True)
            return compare_df
        finally:
            totalTime = (time.perf_counter() - startTime)
            print(f"METHOD: {inspect.stack()[0][3]} completed in {format(totalTime, '6.3f')} seconds")

    def plot_stock(self, sdata, ptitle="Plot Supervised Learning"):
        """
            Plot stock data
        """
        startTime = time.perf_counter()
        try:
            # Generate the plot
            # fig = px.scatter_3d(sdata, x='sepal_width',
            #                     y='sepal_length', z='petal_width', title=ptitle)
            # fig.update_traces(marker=dict(size=5))
            # fig.add_traces(go.Surface(
            #     x=sdata.x, y=sdata.y, z=sdata.pred, name='pred_surface'))
            # fig.show()
            # %matplotlib inline
            mpl.rcParams['axes.grid'] = True
            plt.figure(figsize=(25, 15))
            plt.subplot(1, 2, 1);
            plt.plot(sdata.X, sdata.y,
                     color='blue', label='Market Close $', marker='o')
            plt.title(ptitle)
            plt.xlabel("Date", fontsize=18)
            plt.ylabel('Close Price $', fontsize=18)
            plt.legend(loc='best')
            plt.show()
        finally:
            totalTime = (time.perf_counter() - startTime)
            print(f"METHOD: {inspect.stack()[0][3]} completed in {format(totalTime, '6.3f')} seconds")



if __name__ == "__main__":
    sd = StockData()
    stock_data = sd.stock_data("AAPL", "2021-03-01", "2021-08-31")
    print(stock_data)
