# test training by tensorflow 2.x framework

traning model on `GPU` by framework `tensorflow` with `miniconda`

- create tensorflow2.x environment `conda create -n tf2 python=3.8`

- activate `tf2` enviroment `conda activate tf2`

- Then install tensorflow packages by command: `pip install tensorflow`

- Then install CUDA and cuDNN with conda and pip.

        conda install -c conda-forge cudatoolkit=11.8.0
        pip install nvidia-cudnn-cu11==8.6.0.163

- check your `tensorflow` can work with gpu by command `python3 tensorflow/check.py`

![result](https://github.com/iteam1/itest/blob/main/assets/Screenshot%202023-08-19%2021:18:35.png?raw=true)

**Note**:
If you get these message:

        File "/home/gom/miniconda3/envs/tf2/lib/python3.8/site-packages/keras/src/optimizers/optimizer.py", line 1347, in apply_grad_to_update_var
            return self._update_step_xla(grad, var, id(self._var_key(var)))
        Node: 'Adam/StatefulPartitionedCall_8'
        libdevice not found at /home/gom/miniconda3/envs/tf2/lib/nvvm/libdevice/libdevice.10.bc
                [[{{node Adam/StatefulPartitionedCall_8}}]] [Op:__inference_train_function_1382]

Firstly, searching for nvvm directory and then verified that libdevice directory existed: `find / -type d -name nvvm 2>/dev/null`, Then export the environment variable `export XLA_FLAGS=--xla_gpu_cuda_data_dir=/usr/lib/cuda` (check where is your cuda, it can be in `/usr/local/cuda` or `/usr/bin/cuda`)

# references

[Tensorflow, CUDA and Nvidia Driver Install](https://docs.google.com/document/u/0/d/1MQ35ZeMZupJQCz4pUmI2Z0j6yD5VaVRWYBtosGNK0p8/mobilebasic)

[https://www.tensorflow.org/install/pip](https://www.tensorflow.org/install/pip)

[https://www.tensorflow.org/guide/gpu](https://www.tensorflow.org/guide/gpu)

[https://www.tensorflow.org/tutorials/images/classification](https://www.tensorflow.org/tutorials/images/classification)

[TensorFlow libdevice not found. Why is it not found in the searched path](https://stackoverflow.com/questions/68614547/tensorflow-libdevice-not-found-why-is-it-not-found-in-the-searched-path)