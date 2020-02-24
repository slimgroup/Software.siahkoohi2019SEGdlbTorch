# Deep-learning based ocean bottom seismic wavefield recovery (PyTorch)

Codes for generating results in Siahkoohi, A., Kumar, R. and Herrmann, F.J., 2019. Deep-learning based ocean bottom seismic wavefield recovery. In SEG Technical Program Expanded Abstracts 2019 (pp. 2232-2237).  doi: [10.1190/segam2019-3216632.1](https://doi.org/10.1190/segam2019-3216632.1).

## Prerequisites

This code has been tested using Deep Learning AMI (Amazon Linux) Version 24.2 on Amazon Web Services (AWS). We performed the test on `g3s.xlarge` and `g4dn.xlarge` instances. Follow the steps below to install the necessary libraries:

```bash
cd $HOME
git clone git@github.com/alisiahkoohi/wavefield-reconstruction-torch.git
cd $HOME/wavefield-reconstruction-torch
conda create -n torch pip python=3.6
source activate torch
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
pip install --user -r  requirements.txt

```


## Dataset

Links have been provided in `RunTraining.sh` script to automatically download the 14.33 Hz monochromatic seismic data into the necessary directory. Total size of the dataset for each fequency is 6.52GB + 6.52GB + 6.52GB + 118KB.

## Script descriptions

`RunTraining.sh`\: script for running training. It will make `model/` and `data/` directory in `/home/ec2-user/` for storing training/testing data and saved neural net checkpoints and final results, respectively. Next, it will train a neural net for the experiment for 14.33 Hz monochromatic seismic data.

`RunTesting.sh`\: script for testing the trained neural net. It will reconstruct the entire subsampled 14.33 Hz monochromatic seismic data and place the result in `sample/` directory to be used for plotting purposes.

`src/main.py`\: constructs `wavefield_reconstrcution` class using given arguments in `RunTraining.sh`\, defined in `model.py` and calls `train` function in the defined  `wavefield_reconstrcution` class.

`src/model.py`: includes `wavefield_reconstrcution` class definition, which involves `train` and `test` functions.


### Running the code

To perform training, run:

```bash
# Running on GPU

bash RunTraining.sh

```

To evaluated the trained network on test data set run the following. It will automatically load the latest checkpoint saved.

```bash
# Running on GPU

bash RunTesting.sh

```

To generate and save figures shown in paper for 14.33 Hz monochromatic seismic data run the following:

```bash

bash utilities/genFigures.sh

```

The saving directory can be changed by modifying `savePath` variable in `utilities/genFigures.sh`\.


## Citation

If you find this software useful in your research, please cite:

```bibtex
@conference {siahkoohi2019SEGdlb,
	title = {Deep-learning based ocean bottom seismic wavefield recovery},
	booktitle = {SEG Technical Program Expanded Abstracts},
	year = {2019},
	note = {(SEG, San Antonio)},
	month = {09},
	pages = {2232-2237},
	keywords = {machine learning, obn, reciprocity, reconstruction, SEG},
	doi = {10.1190/segam2019-3216632.1}
	author = {Ali Siahkoohi and Rajiv Kumar and Felix J. Herrmann}
}
```

## Questions

Please contact alisk@gatech.edu for further questions.


## Author

Ali Siahkoohi
