# Large Model Systems Organization FastChat
- [https://lmsys.org](https://lmsys.org)
## Prequsite
- RAM: 16GB
- CPU: 4

## Install
- Clone git repo
```````
git clone https://github.com/lm-sys/FastChat.git
cd FastChat
```````
- Follow README.md [Method 1: With pip](https://github.com/lm-sys/FastChat/blob/main/README.md#method-1-with-pip) instructions
```````
pip3 install fschat
```````
- Follow README.md [Method 2: From source](https://github.com/lm-sys/FastChat/blob/main/README.md#method-2-from-source) instructions
```````
brew install rust cmake
pip3 install --upgrade pip
pip3 install -e .
```````

Note: Be patient for the first time execution will be download the model and make sure you have at least 10GB of storage space available on your deive. 


## Run with model:fastchat-t5-3b-v1.0 with CPU
- Model fastchat-t5-3b is available at [https://huggingface.co/lmsys/fastchat-t5-3b-v1.0](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)
- Follow the below command to download the model and start the service
```````
python3 -m fastchat.serve.cli —model-path lmsys/fastchat-t5-3b-v1.0 --device cpu
```````
- Service will start in your local environment


## Run with model:databricks/dolly-v2-12b with CPU
- Model fastchat-t5-3b is available at [https://huggingface.co/databricks/dolly-v2-12b](https://huggingface.co/databricks/dolly-v2-12b)]
- Follow the below command to download the model and start the service
```````
python3 -m fastchat.serve.cli --model-path databricks/dolly-v2-12b --device cpu
```````
- Your local environment will be used to start the service. 

## Run with model:vicuna-7b-delta-v1.1 with CPU
- Model vicuna-7b is available at [https://huggingface.co/lmsys/vicuna-7b-delta-v1.1](https://huggingface.co/lmsys/vicuna-7b-delta-v1.1)]
- Follow the below command to download the model and start the service
```````
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-delta-v1.1 --device cpu
```````
- Your local environment will be used to start the service. 


