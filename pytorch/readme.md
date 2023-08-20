# test training by paddle framework

traning model on `GPU` by framework `pytorch` with `miniconda`

- create tensorflow2.x environment `conda create -n torch python=3.8`

- activate `torch` enviroment `conda activate torch`

- Then install pytorch packages by command: `pip3 install numpy --pre torch --force-reinstall --index-url https://download.pytorch.org/whl/nightly/cu117` and `pip3 install torchvision torchaudio`

![result](https://github.com/iteam1/itest/blob/main/assets/Screenshot%202023-08-19%2021:07:20.png?raw=true)

- Open `nvtop` and start training by command `python3 tensorflow/train.py`

![training](https://github.com/iteam1/itest/blob/main/assets/Screenshot%202023-08-20%2009:00:07.png?raw=true)

# references

[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

[https://docs.activeloop.ai/tutorials/deep-learning/training-models/training-an-image-classification-model-in-pytorch](https://docs.activeloop.ai/tutorials/deep-learning/training-models/training-an-image-classification-model-in-pytorch)