# test training by tensorflow 2.x framework

traning model on `GPU` by framework tensorflow verison 2.x (currently v2.13, python=3.9) with miniconda environment

- create tensorflow2.x environment `conda create -n tf2 python=3.9`
- activate `tf2` enviroment `conda activate tf2`
- Then install CUDA and cuDNN with conda and pip.

        conda install -c conda-forge cudatoolkit=11.8.0
        pip install nvidia-cudnn-cu11==8.6.0.163

- Configure the system paths. You can do it with the following command every time you start a new terminal after activating your conda environment.

        CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
        export LD_LIBRARY_PATH=$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:$LD_LIBRARY_PATH


- For your convenience it is recommended that you automate it with the following commands. The system paths will be automatically configured when you activate this conda environment.

        mkdir -p $CONDA_PREFIX/etc/conda/activate.d
        echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
        echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

- Install tensorflow `pip install --upgrade pip` and `pip install tensorflow==2.13.*`

- Verify the CPU setup: `python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`

- Verify the GPU setup: `python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

# references

[https://www.tensorflow.org/install/pip](https://www.tensorflow.org/install/pip)