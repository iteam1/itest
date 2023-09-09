# check CUDA-capable GPU

CUDA support is available across a wide range of NVIDIA GPU series. As of my last knowledge update in September 2021, here are some of the notable GPU series that support CUDA:

`GeForce GTX Series`: This series includes GPUs like GTX 1000 and GTX 900 series. They offer CUDA support for general-purpose computing tasks.

`GeForce RTX Series`: This series includes GPUs like RTX 3000, RTX 2000, and RTX 1000 series. These GPUs not only support CUDA but also introduce hardware support for ray tracing and AI-related tasks through features like RT Cores and Tensor Cores.

`NVIDIA Titan Series`: The Titan series GPUs are high-performance GPUs designed for both gaming and professional workloads. They provide robust CUDA support and are often used for machine learning, scientific simulations, and other compute-intensive tasks.

`NVIDIA Quadro Series`: The Quadro series is tailored for professional workstations and applications. They offer extensive CUDA capabilities and are used in fields like 3D rendering, CAD, and scientific simulations.

`NVIDIA Tesla Series`: The Tesla series GPUs are specifically designed for high-performance computing and data center applications. They have a strong emphasis on CUDA performance and are widely used in scientific research and data analysis.

`NVIDIA A100`: A part of the NVIDIA Ampere architecture, the A100 is a data center GPU designed for AI and high-performance computing workloads. It features dedicated Tensor Cores for AI tasks and offers extensive CUDA capabilities.

It's important to note that CUDA support can vary across different models within a series. Also, newer GPU models may have been released after my last update, so I recommend checking the official NVIDIA website or other reliable sources for the latest information on CUDA support for specific GPU models.

# Verify the system has a CUDA-capable
- check *NVIDIA-GPU* PCI connection by command `lspci | grep -i nvidia`
- list current gpu info `sudo lshw -C display`
- check gpu-cuda-capable at [gpus-cuda-capable](https://developer.nvidia.com/cuda-gpus)

# Verify the system is running a supported version of Linux
- check linux version `uname -m && cat /etc/*release`

# Verify the system has gcc installed
The gcc compiler is required for development using the CUDA Toolkit. It is not required for running CUDA applications. It is generally installed as part of the Linux installation
- check gcc version `gcc --version`

# Verify the system has the correct kernel headers and development packages installed
Ensure the correct version of the kernel headers and development packages are installed prior to installing the CUDA Drivers,The CUDA Driver requires that the kernel headers and development packages for the running version of the kernel be installed at the time of the driver installation, as well whenever the driver is rebuilt
- check kernel version `uname -r`

# Install Nvidia Driver
- Update Ubuntu `sudo apt update && sudo apt upgrade -y`
- Check GPU version and Drivers `ubuntu-drivers devices`
- Install driver `sudo apt install nvidia-driver-515`
- After installed, I will reboot my server computer system using `sudo reboot`
- Check driver `nvidia-smi` or `watch -n 0.1 nvidia-smi`

# Install CUDA
- Update Ubuntu `sudo apt update && sudo apt upgrade -y`
- Install CUDA toolkit `sudo apt-get -y install nvidia-cuda-toolkit`
- Check installation `nvcc --version` or `which nvcc`
- Install CUDA Deep Neural Network library (DNN), cuDNN library `sudo apt-get -y install nvidia-cudnn`
- Find where your cuda installed `find / -type d -name cuda 2>/dev/null`

# Install Nvidia-container-toolkit

    $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
    $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    
    $ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
    $ sudo systemctl restart docker

**Note**

`nvcc` stands for NVIDIA CUDA Compiler. It is a compiler provided by NVIDIA as part of the CUDA toolkit, which is a software development platform for creating GPU-accelerated applications. CUDA (Compute Unified Device Architecture) enables developers to write code that can be executed on NVIDIA GPUs (Graphics Processing Units) for parallel computing tasks.

`nvcc` is used to compile CUDA C/C++ source code into GPU machine code. It extends the capabilities of traditional C/C++ compilers by adding GPU-specific keywords, functions, and constructs that allow developers to harness the parallel processing power of NVIDIA GPUs. The resulting compiled code can be executed on compatible NVIDIA GPUs, enabling significant speedups for tasks that can be parallelized.

In summary, `nvcc` is a critical tool for developers who want to write and compile code that takes advantage of NVIDIA GPUs for high-performance parallel computing tasks using the CUDA framework.

NVIDIA cuDNN (CUDA Deep Neural Network Library) is a software library developed by NVIDIA to accelerate deep learning computations on NVIDIA GPUs. It provides optimized implementations of various operations and functions commonly used in deep neural networks, such as convolution, pooling, normalization, activation functions, and more.

cuDNN is specifically designed to improve the performance of deep learning frameworks like TensorFlow, PyTorch, Caffe, and others that utilize GPUs for training and inference of deep neural networks. It takes advantage of the parallel processing capabilities of GPUs to significantly speed up the computation-heavy tasks involved in training and using neural networks.

Some key features of cuDNN include:

Performance Optimization: cuDNN provides highly optimized GPU-accelerated implementations of common operations in deep neural networks, making training and inference much faster compared to using only general-purpose libraries.

Compatibility: cuDNN is designed to seamlessly integrate with popular deep learning frameworks, making it relatively easy for developers to leverage its performance benefits without major code modifications.

Flexible Configuration: It offers various configuration options to fine-tune the performance based on the specific hardware and network architecture being used.

Support for Different Precisions: cuDNN supports different data precisions, such as single-precision (float32) and half-precision (float16), allowing developers to choose the level of precision based on their application's requirements.

In summary, NVIDIA cuDNN is a crucial library for deep learning practitioners as it enhances the speed and efficiency of training and deploying neural networks on NVIDIA GPUs, ultimately leading to faster model development and improved performance.

**Note**
The CUDA Toolkit provided by NVIDIA and the CUDA Toolkit available through Miniconda are both tools for developing GPU-accelerated applications using CUDA. However, there are some differences between the two, primarily related to how they are distributed and managed:

Source of Distribution:

`NVIDIA CUDA Toolkit`: The CUDA Toolkit provided by NVIDIA is the official distribution of CUDA directly from NVIDIA. It includes all the components necessary for CUDA development, such as the 
CUDA runtime, cuDNN, NVCC (NVIDIA CUDA Compiler), and other GPU libraries.

`CUDA Toolkit via Miniconda`: The CUDA Toolkit available through Miniconda is distributed as part of the Conda package management system. It provides an alternative method for managing CUDA installations within Conda environments. This version is typically maintained by the Conda community and might not always be as up-to-date as the official NVIDIA distribution.
Version and Update Frequency:

`NVIDIA CUDA Toolkit`: The official NVIDIA distribution is likely to be the most up-to-date and stable version of CUDA. NVIDIA regularly releases new versions with performance improvements, bug fixes, and support for the latest GPUs.

`CUDA Toolkit via Miniconda`: The version of CUDA available through Miniconda might not be updated as frequently as the official NVIDIA distribution. It might take some time before new releases are made available in the Conda repositories.
Ease of Installation and Environment Management:

`NVIDIA CUDA Toolkit`: Installing the official CUDA Toolkit directly from NVIDIA involves downloading the installer and following the installation instructions. It doesn't require the use of Conda.

`CUDA Toolkit via Miniconda`: Installing CUDA through Miniconda involves using Conda's package management system. This provides the benefits of environment isolation and simplified package management, but might not provide the latest CUDA version immediately.
Customization and Control:

`NVIDIA CUDA Toolkit`: Installing CUDA directly from NVIDIA allows you to customize the installation options and configurations to suit your needs.

`CUDA Toolkit via Miniconda`: While Conda provides some level of customization, the options might be more limited compared to a direct installation from NVIDIA.
In summary, the main difference between the CUDA Toolkit from NVIDIA and the one available via Miniconda lies in their distribution channels, update frequency, and ease of installation. If you need the latest features and performance improvements, the official NVIDIA distribution might be the better choice. However, if you prefer managing your CUDA installations using Conda environments or if you value the convenience of Conda's package management system, the Miniconda distribution might be suitable for your use case.

# references

[https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi](https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi)

[https://linuxhint.com/install-cuda-ubuntu-2004/](https://linuxhint.com/install-cuda-ubuntu-2004/)

[https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/](https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/)

[cuda-c-programming-guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#)
