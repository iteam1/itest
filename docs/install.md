# install miniconda
- download miniconda [Miniconda3 Linux 64-bit](https://docs.conda.io/en/latest/miniconda.html) file
- install miniconda `bash Miniconda3-latest-Linux-x86_64.sh`
- if you'd prefer that conda's base environment not be activated on startup, set the auto_activate_base parameter to false:  `conda config --set auto_activate_base false`
- check `miniconda3` version `miniconda3/bin/conda --version`
- create new environment `miniconda3/bin/conda create -n env38 python=3.8`
- activate your environment `source miniconda3/bin/activate miniconda3/envs/env38`
- deactivate your environment `conda deactivate`
- remove your environment `conda remove --name ENV_NAME --all`

# install git
- install git command `sudo apt install git`
- check git version `git --version`
- config user email `git config --global user.email you@example.com`
- config user name `git config --global user.name Your Name`

# install vscode
- install command vscode `sudo snap install --classic code`

# install docker
- Update the apt package index and install packages to allow apt to use a repository over HTTPS:

        sudo apt-get update
        sudo apt-get install ca-certificates curl gnupg

- Add Docker’s official GPG key:

        sudo install -m 0755 -d /etc/apt/keyrings
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
        sudo chmod a+r /etc/apt/keyrings/docker.gpg

- Use the following command to set up the repository:

        echo \
        "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
        "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

- Update the apt package index: `sudo apt-get update`

- Install Docker Engine, containerd, and Docker Compose `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

- Check docker version `docker --version`

- Verify that the Docker Engine installation is successful by running the hello-world image `sudo docker run hello-world`

# references

[https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

[https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)