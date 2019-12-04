# Homomorphic Encryption in Facebook Users' Data
### Introduction to CS Research (Northeastern University, Prof. Rose Yu)
### Natalie Hsu, Nicole Danuwidjaja

*Problem: Companies collect and find patterns to power algorithms that provide personalized experiences and share data with third parties. Data anonymity is not guaranteed and private information can still be exploited.*

Homomorphic Encryption is an encryption scheme that allows computations to be performed on encrypted data without compromising on features or security, protecting users from exploitation. The encryption is an important advance in privacy research and data sharing as it maintains data security while still allowing for the analysis of user data to improve technological functionality. In our research paper, we will examine the possible use cases of homomorphic encryption within social networking platforms in order to ensure that users can secure the privacy of their personal data while third parties can still gather research on user data.

*Purpose: To use sample Facebook datasets to conduct an experiment on the validity of homomorphic encryption.*

# Usage
Our research project utilizes the [Lab41's PySEAL GitHub Repository](https://github.com/Lab41/PySEAL/).

Docker Documentation: https://docs.docker.com/

Install [Docker Desktop](https://docs.docker.com/toolbox/toolbox_install_windows/) or [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/) (for legacy computers)

Start Docker Toolbox for Windows with *Docker Quickstart Terminal* within a command prompt:
```
> cd "%ProgramFiles%\Docker Toolbox"
> "%ProgramFiles%\Git\bin\bash.exe"
$ ./start.sh
```

Check that all pre-requisites have been met: `docker-machine create --driver virtualbox default`

`docker version` should confirm that Docker is installed and running!

Clone the PySEAL repo:
```
> cd ~
> git clone https://github.com/Lab41/PySEAL.git
```

Build Python wrapper for PySEAL by running executable `build-docker.sh`

Build Docker image to create a `seal` image that can be imported as a Python package: `docker build -t seal-save`

Add package to local host: `docker run -t -v "path:/root/FacebookProjectHe" seal-save`

