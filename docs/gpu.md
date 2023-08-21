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

`nvcc` stands for NVIDIA CUDA Compiler. It is a compiler provided by NVIDIA as part of the CUDA toolkit, which is a software development platform for creating GPU-accelerated applications. CUDA (Compute Unified Device Architecture) enables developers to write code that can be executed on NVIDIA GPUs (Graphics Processing Units) for parallel computing tasks.

`nvcc` is used to compile CUDA C/C++ source code into GPU machine code. It extends the capabilities of traditional C/C++ compilers by adding GPU-specific keywords, functions, and constructs that allow developers to harness the parallel processing power of NVIDIA GPUs. The resulting compiled code can be executed on compatible NVIDIA GPUs, enabling significant speedups for tasks that can be parallelized.

In summary, `nvcc` is a critical tool for developers who want to write and compile code that takes advantage of NVIDIA GPUs for high-performance parallel computing tasks using the CUDA framework.

# references

[https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi](https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi)

[https://linuxhint.com/install-cuda-ubuntu-2004/](https://linuxhint.com/install-cuda-ubuntu-2004/)

[https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/](https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/)

[cuda-c-programming-guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#)
