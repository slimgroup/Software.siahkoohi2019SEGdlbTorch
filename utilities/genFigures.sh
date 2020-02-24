 #!/bin/bash -l

frequency=14.33
sampling_rate=0.1
scheme=random

experiment_name=wavefield-reconstruction_freq${frequency}_A_train_${sampling_rate}SamplingRate_${scheme}_evolving_training_set
repo_name=wavefield-reconstruction-torch

path_script=$HOME/$repo_name/src/
path_data=$HOME/data
path_model=$HOME/model/$experiment_name
savePath=$path_model/test

python run_plot_data.py --input_data $path_data --save_path $savePath --result_path $path_model/sample \
	--freq $frequency --sampling_scheme $scheme