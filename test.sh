output_path=mnt/data_10t/flan_t5_distill/outputs/
base_model=mnt/data_10t/flan_t5_distill/checkpoints/0.0.5.1_epoch_1_iter_60000
batch_size_fixed=80
dataset=gsm8k_test
gpu_id=\'0,1\'
nohup python test_distill.py\
    base_model=${base_model}\
    output_path=${output_path}\
    batch_size_fixed=${batch_size_fixed}\
    test_data=${dataset}\
    # model_size=11b\
    gpu_id=${gpu_id}\
    &> logs/beta_${base_model##*/}_${dataset}_eval.log & 
tail -f logs/beta_${base_model##*/}_${dataset}_eval.log