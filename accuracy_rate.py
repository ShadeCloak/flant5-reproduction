import re

def calculate_consistency_rate(filename, output_filename):
    with open(filename, 'r') as file:
        data = file.read()
    groups = data.split('Q:')

    consistent_count = 0
    total_count = 0
    with open(output_filename, 'w') as output_file:
        for group in groups:
            match = re.search(r'The answer is (\d+)', group)
            a_model_answer = match.group(1) if match else None
            match = re.search(r'#### (\d+)', group)
            a_answer = match.group(1) if match else None
            if a_model_answer == a_answer:
                consistent_count += 1
                output_file.write(f'Q:{group}\n')
            total_count += 1
    consistency_rate = (consistent_count / total_count) * 100

    return f'{consistency_rate:.2f}%'

filename = '/home/group2024-rqn/FlanT5-CoT-Specialization/mnt/data_10t/flan_t5_distill/outputs/gsm8k_test_0.0.2.2_epoch_5_iter_40000.txt'
#filename = '/home/group2024-rqn/FlanT5-CoT-Specialization/mnt/data_10t/flan_t5_distill/outputs/gsm8k_test_0.0.5.1_epoch_0_iter_1000.txt'
output_filename = 'output.txt'
print(calculate_consistency_rate(filename, output_filename))
