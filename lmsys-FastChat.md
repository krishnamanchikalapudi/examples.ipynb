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
   - MAC  
```````
brew install rust cmake
pip3 install --upgrade pip
pip3 install -e .
```````
   - Linux
```````   
pip3 install --upgrade pip
pip3 install -e .
```````

Note: Be patient for the first time execution will be downloads the model.


## Run with model:fastchat-t5-3b-v1.0 with CPU
- Model fastchat-t5-3b is available at [https://huggingface.co/lmsys/fastchat-t5-3b-v1.0](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)
- Note: model size is ~ 9GB
### CLI 
- Follow the below command to download the model and start the service
```````
cd ~/FastChat
python3 -m fastchat.serve.cli —model-path lmsys/fastchat-t5-3b-v1.0 --device cpu
```````
- Service will start in your local CLI environment

### Web app
- Open three terminals for the below command to start the service
- Terminal 1
```````
cd ~/FastChat
python3 -m fastchat.serve.controller
```````
- Terminal 2
```````
cd ~/FastChat
python3 -m fastchat.serve.model_worker --model-path lmsys/fastchat-t5-3b-v1.0  --device cpu 
```````
- Terminal 3
```````
cd ~/FastChat
python3 -m fastchat.serve.test_message --model-name fastchat-t5-3b-v1.0
```````
- Open web browser and go to url: [http://localhost:7860/](http://localhost:7860/)

## Run with model:databricks/dolly-v2-12b with CPU
### CLI 
- Model dolly-v2-12b is available at [https://huggingface.co/databricks/dolly-v2-12b](https://huggingface.co/databricks/dolly-v2-12b)]
- Note: model size is ~24GB
- Follow the below command to download the model and start the service
```````
python3 -m fastchat.serve.cli --model-path databricks/dolly-v2-12b --device cpu
```````
- Your local environment will be used to start the service. 

### Web app
- NOT validated yet!

## Run with model:vicuna-7b-delta-v1.1 with CPU
### CLI 
- Model vicuna-7b is available at [https://huggingface.co/lmsys/vicuna-7b-delta-v1.1](https://huggingface.co/lmsys/vicuna-7b-delta-v1.1)]
- Follow the below command to download the model and start the service
```````
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-delta-v1.1 --device cpu --load-8bit
```````
- Your local environment will be used to start the service. 
### Web app
- NOT validated yet!

