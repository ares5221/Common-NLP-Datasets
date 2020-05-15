# LCQMC: A Large-scale Chinese Question Matching CorpusChinese Psychological QA DataSet



**Introduction:**

Question matching is a fundamental task of QA, which is usually recognized as a semantic matching task, sometimes a paraphrase identification task. The goal of the task is to search questions that have similar intent as the input question from an existing database. We introduce a large-scale Chinese question matching corpus (named LCQMC). LCQMC is more general than paraphrase corpus as it focuses on intent matching rather than paraphrase. The corpus contains 260,068 question pairs with manual annotation and we split it into three parts, i.e., a training set containing 238,766 question pairs, a development set with 8,802 question pairs, and a test set with 12,500 question pairs. We test several well-known sentence matching methods on it. The experimental results not only demonstrate the good quality of LCQMC, but also provide solid baseline performance for further researches on this corpus.

该论文是哈工大发表的一个中文问答匹配数据集的论文，对于整个中文问答匹配的知识背景、方法、数据集构建方式等都有一些描述，该数据集被广泛应用在一些中文语义匹配的评测中，比如百度的simNet。

LCQMC更多的关注在intent matching（意图匹配）而不是paraphrase（短语）方面。构建的方式是先针对不同的领域从百度问答中抽取高频的相关问题，然后通过Wasserstein distance进行初步筛选，最后人工进行标注。



示例数据

```  json
喜欢打篮球的男生喜欢什么样的女生	爱打篮球的男生喜欢什么样的女生	1
我手机丢了，我想换个手机	我想买个新手机，求推荐	1
大家觉得她好看吗	大家觉得跑男好看吗？	0
求秋色之空漫画全集	求秋色之空全集漫画	1
```
### 数据解释

每行代表一条数据，分三部分，前两个为中文语句，第三部分为1，0表示的数据

1表示两个句子语义相似，0表示语义不相似


### 数据统计
数据集一共有260068对标注结果，分为三部分，238766训练集、8802验证集和12500测试集。
