# test training by pytorch framework

traning model on `GPU` by framework `pytorch` with `miniconda`

- create tensorflow2.x environment `conda create -n torch python=3.8`

- activate `torch` enviroment `conda activate torch`

- Then install pytorch packages by command: `pip3 install numpy --pre torch --force-reinstall --index-url https://download.pytorch.org/whl/nightly/cu117` and `pip3 install torchvision torchaudio`

![result](https://github.com/iteam1/itest/blob/main/assets/Screenshot%202023-08-19%2021:07:20.png?raw=true)

- Open `nvtop` and start training by command `python3 tensorflow/train.py`

![training](https://github.com/iteam1/itest/blob/main/assets/Screenshot%202023-08-20%2012:11:35.png?raw=true)

**Note**

The list you've provided seems to be a collection of package names along with their respective version numbers. These packages are related to NVIDIA's CUDA ecosystem, which is used for GPU-accelerated computing, particularly in the context of deep learning and scientific computing. Each package serves a specific purpose within this ecosystem. Here's a brief explanation of each package:

`nvidia-cublas-cu11`: NVIDIA cuBLAS library for linear algebra operations on GPUs.

`nvidia-cuda-cupti-cu11`: NVIDIA CUDA Profiling Tools Interface (CUPTI) for profiling CUDA applications.

`nvidia-cuda-nvrtc-cu11`: NVIDIA CUDA Runtime Compilation (NVRTC) library for compiling CUDA code at runtime.

`nvidia-cuda-runtime-cu11`: NVIDIA CUDA Runtime library for executing CUDA applications.

`nvidia-cudnn-cu11`: NVIDIA cuDNN (CUDA Deep Neural Network Library) for accelerating deep learning computations.

`nvidia-cufft-cu11`: NVIDIA cuFFT library for Fast Fourier Transform (FFT) computations on GPUs.

`nvidia-curand-cu11`: NVIDIA cuRAND library for random number generation on GPUs.

`nvidia-cusolver-cu11`: NVIDIA cuSOLVER library for dense and sparse linear algebra computations on GPUs.

`nvidia-cusparse-cu11`: NVIDIA cuSPARSE library for sparse matrix operations on GPUs.

`nvidia-nccl-cu11`: NVIDIA NCCL (NVIDIA Collective Communications Library) for multi-GPU and multi-node communication.

`nvidia-nvtx-cu11`: NVIDIA NVTX (NVIDIA Tools Extension) library for annotating and visualizing GPU workloads.

These packages are part of the CUDA toolkit and libraries provided by NVIDIA. They are crucial components for developing and running GPU-accelerated applications, especially in fields such as deep learning, high-performance computing, and scientific simulations. The version numbers indicate the specific release versions of each package. Keep in mind that the versions listed might not be the latest ones, as the software ecosystem can receive updates over time.

# references

[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

[https://docs.activeloop.ai/tutorials/deep-learning/training-models/training-an-image-classification-model-in-pytorch](https://docs.activeloop.ai/tutorials/deep-learning/training-models/training-an-image-classification-model-in-pytorch)
