

# run a small model 
train
```
model_version=0.0.5.0 # base model FlanT5 780m
nohup python -u train_distill_simple.py\
    model_version=${model_version}\
    gpu_id=\'1,2,3,4\'\
    base_model=\'google/flan-t5-base\'\
    batch_size=11b\
    grad_accum_steps=3\
    save_per_step=1000\
    log_interval=2\
    lr=0.0005\
    &> logs/beta_${model_version}.log &
tail -f logs/beta_${model_version}.log
```


test
```
output_path=mnt/data_10t/flan_t5_distill/outputs/
base_model=mnt/data_10t/flan_t5_distill/checkpoints/0.0.2.2_epoch_5_iter_40000
batch_size_fixed=80
dataset=gsm8k_test
gpu_id=\'0,4\'
nohup python test_distill.py\
    base_model=${base_model}\
    output_path=${output_path}\
    batch_size_fixed=${batch_size_fixed}\
    test_data=${dataset}\
    # model_size=11b\
    gpu_id=${gpu_id}\
    &> logs/beta_${base_model##*/}_${dataset}_eval.log & 
tail -f logs/beta_${base_model##*/}_${dataset}_eval.log
```