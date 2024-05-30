import pickle

# 加载.pkl数据
with open('/home/group2024-rqn/FlanT5-CoT-Specialization/processed_data/processed_data/processed_data/in_context_chain_of_thought.pkl', 'rb') as f:
    data = pickle.load(f)

# 将数据写入文本文件
with open('/home/group2024-rqn/FlanT5-CoT-Specialization/processed_data/processed_data/processed_data/in_context_chain_of_thought.txt', 'w') as f:
    for item in data:
        f.write(str(item) + '\n')