# #!/bin/bash -l

frequency=14.33
sampling_rate=0.1
scheme=random

experiment_name=wavefield-reconstruction_freq${frequency}_A_train_${sampling_rate}SamplingRate_${scheme}_evolving_training_set
repo_name=Software.siahkoohi2019SEGdlbTorch

path_script=$HOME/$repo_name/src/
path_data=$HOME/data
path_model=$HOME/model/$experiment_name

python $path_script/main.py --experiment $experiment_name --phase test \
	--freq $frequency --data_path $path_data --cuda 1 \
	--checkpoint_dir $path_model/checkpoint --sample_dir $path_model/sample --log_dir $path_model/log
