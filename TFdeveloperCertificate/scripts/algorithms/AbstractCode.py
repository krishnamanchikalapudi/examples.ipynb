import inspect
import time
import datetime
import logging
import tensorflow as tf
import scripts.utils.FileExten as FileExten
'''
This class is the base class for all algorithms.
'''
class AbstractCode:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    data_dir = "../../data"
    class_name = "DownloadDataSet.py"  # f"{__class__.__name__}"
    # Constructor

    def __init__(self):
        method_name = f"{inspect.stack()[0][3]}"
        logging.debug(f"[BEGIN] CLASS: {self.class_name} "
                      f"METHOD: {method_name} at {datetime.datetime.now()}")
        startTime = time.perf_counter()
        try:
            print(f"Data Dir: {self.data_dir}")
        finally:
            totalTime = (time.perf_counter() - startTime)
            logging.debug(
                f"[END] CLASS: {self.class_name} METHOD: {method_name} completed in {format(totalTime, '6.3f')} seconds or {format(totalTime / 60, '6.3f')} minutes ")

    def retrieve_data(self, dataset_name, exten=FileExten.ZIP, download_url=None):
        '''
        This method downloads the data set from the internet.
            :param dataset_name:
            :param exten: File extension
            :param download_url: URL to download the data set from internet
        '''
        method_name = f"{inspect.stack()[0][3]}"
        logging.debug(f"[BEGIN] CLASS: {self.class_name} "
                      f"METHOD: {method_name} at {datetime.datetime.now()}")
        startTime = time.perf_counter()
        try:
            if download_url is not None:
                tf.keras.utils.get_file(f"{dataset_name+exten}",
                                        download_url,
                                        extract=True,
                                        cache_dir=self.data_dir,
                                        cache_subdir=dataset_name)
                print(
                    f"Download dataset:{dataset_name+exten} to {self.data_dir+'/'+dataset_name}")
            else:
                print(f"Download URL is NONE")
        finally:
            totalTime = (time.perf_counter() - startTime)
            logging.debug(
                f"[END] CLASS: {self.class_name} METHOD: {method_name} completed in {format(totalTime, '6.3f')} seconds or {format(totalTime / 60, '6.3f')} minutes ")
