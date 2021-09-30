import os, ssl, urllib.request

# BEGIN: fix Python or Notebook SSL CERTIFICATE_VERIFY_FAILED
import ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
# END: fix Python or Notebook SSL CERTIFICATE_VERIFY_FAILED

def retrieve_data(remote_file, local_file):
    if not os.path.exists(local_file) and not os.path.isfile(local_file):
        urllib.request.urlretrieve(remote_file, local_file)
        print(f"File: {local_file} download complete")
    else:
        print(f"File: '{local_file}' already exists!")

remote_filename = 'https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/slump/slump_test.data'
local_filename = './data/concrete_slump.csv'

# main method
if __name__ == '__main__':
    retrieve_data(remote_filename, local_filename)