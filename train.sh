
# run a small model 
model_version=0.0.5.1 # base model FlanT5 780m
nohup python -u train_distill_simple.py\
    model_version=${model_version}\
    gpu_id=\'0\'\
    base_model=\'google/flan-t5-base\'\
    batch_size=11b\
    grad_accum_steps=15\
    save_per_step=10000\
    log_interval=2\
    lr=0.0005\
    &> logs/beta_${model_version}.log &
tail -f logs/beta_${model_version}.log
