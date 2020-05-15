# The BQ Corpus: A Large-scale Domain-specific Chinese Corpus For Sentence Semantic Equivalence Identification



**Introduction:**

As the semantic matching task, sentence semantic equivalence identification (SSEI) is a fundamental task of natural language processing (NLP) in question answering (QA), automatic customer service and chat-bots. In customer service systems, two questions are defined as semantically equivalent if they convey the same intent or they could be answered by the same answer. We introduce the Bank Question (BQ) corpus, a large-scale domain-specific Chinese corpus for SSEI. The BQ corpus contains 120,000 question pairs from online bank custom service logs. It is split into three parts: 100,000 pairs for training, 10,000 pairs for validation, and 10,000 pairs for test. We present five SSEI benchmark performance on our corpus, including state-of-the-art algorithms. As the largest manually annotated public Chinese SSEI corpus in the bank domain, the BQ corpus is not only useful for Chinese question semantic matching research, but also a significant resource for cross-lingual and cross-domain SSEI research.

该论文是哈工大发表的一个中文问答匹配数据集的论文，对于整个中文问答匹配的知识背景、方法、数据集构建方式等都有一些描述，该数据集被广泛应用在一些中文语义匹配的评测中，比如百度的simNet。

示例数据

```  json
{"gold_label": "0",
 "ID": 0,
 "sentence2": "4。  号码来微粒贷", 
 "sentence1": "用微信都6年，微信没有微粒贷功能"},
{"gold_label": "0", 
 "ID": 1,
 "sentence2": "还有多少钱没还", 
 "sentence1": "微信消费算吗"},
{"gold_label": "0", 
 "ID": 2, 
 "sentence2": "怎么最近安全老是要改密码呢好麻烦", 
 "sentence1": "交易密码忘记了找回密码绑定的手机卡也掉了"}
```
### 数据解释

字典格式数据，分四部分，

| key        | val                                              |
| ---------- | ------------------------------------------------ |
| gold_label | 数据标签，1表示两个句子语义相似，0表示语义不相似 |
| ID         | 语句对id                                         |
| sentence2  | 句子2                                            |
| sentence1  | 句子1                                            |




### 数据统计
数据集一共有120,000 对标注结果，分为三部分，10,000 训练集、100,000验证集和10,000 测试集。
