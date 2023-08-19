# install miniconda
- download miniconda [Miniconda3 Linux 64-bit](https://docs.conda.io/en/latest/miniconda.html) file
- install miniconda `bash Miniconda3-latest-Linux-x86_64.sh`
- if you'd prefer that conda's base environment not be activated on startup, set the auto_activate_base parameter to false:  `conda config --set auto_activate_base false`
- check `miniconda3` version `miniconda3/bin/conda --version`
- create new environment `miniconda3/bin/conda create -n env38 python=3.8`
- activate your environment `source miniconda3/bin/activate miniconda3/envs/env38`
- deactivate your environment `conda deactivate`

# install git
- install git command `sudo apt install git`
- check git version `git --version`
- config user email `git config --global user.email you@example.com`
- config user name `git config --global user.name Your Name`

# install vscode
- install command vscode `sudo snap install --classic code`

# install docker