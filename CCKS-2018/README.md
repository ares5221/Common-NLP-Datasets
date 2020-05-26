## CCKS 2018 微众银行智能客服问句匹配大赛

# **任务描述**

 https://biendata.com/competition/CCKS2018_3/

微众银行智能客服问句匹配大赛是由微众银行提供语料支持，哈尔滨工业大学（深圳）智能计算研究中心负责组织实施的真实场景语句意图匹配任务。

 

语句匹配是自然语言处理的最基本任务之一，是自动问答，聊天机器人，信息检索，机器翻译等各种自然语言处理任务基础。语句匹配问题的复杂性在于，匹配的要求不同，对匹配的定义也不尽相同，比如经典的语句复述判别问题，需要判断两句话是否仅仅是表述方式不同，但意义相同，而在Quora的的的问句匹配语料发布后，大量在该语料库上开展的语句匹配研究工作都沿袭语料发布者的定义，称为语义等价判别，语义等价判定，等价，而不直接判断两个语句是否表达相同的语义，所以其核心是语句的意图匹配。由于来源于真实问答语料库，该任务更加接近于智能客服等自然语言处理任务的实际需求。

 

与基于Quora的的的语义等价判别相同，本次评测任务的主要目标是针对中文的真实客服语料，进行问句意图匹配。集给定两个语句，要求判定两者意图是否相同或者相近。所有语料来自原始的银行领域智能客服日志，并经过了筛选和人工的意图匹配标注。

 

 

**输入：**一个语句对

**输出：**表明该语句对是否表达相同或者相似意图的二值标签（0或1）

 

**示例：**

*样例1*

输入：一般几天能通过审核\ t一般审核通过要多久

输出：1

 

*样例2*

输入：一般会在什么时候来电话\ t一直在等待电话通知

输出：0