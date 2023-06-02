from lstar import learn_dfa

# 定义样本数据
positive_samples = [
    'ab',
    'aab',
    'abb',
    'aaab',
    'abbb',
    'aaaab',
    'abbbb',
    'aaaaab',
    'abbbbb',
]
negative_samples = [
    'a',
    'b',
    'ba',
    'bb',
    'aaa',
    'aabbb',
    'abab',
    'bab',
    'bba',
]

# 创建Learner对象
learner = Learner(positive_samples, negative_samples)

# 学习有限状态自动机
fsm = learner.learn()

# 输出学习结果
print(fsm)