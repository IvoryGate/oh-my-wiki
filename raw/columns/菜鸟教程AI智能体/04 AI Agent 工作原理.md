---
title: "04 AI Agent 工作原理"
source: "https://www.runoob.com/ai-agent/ai-agent-working-principle.html"
author:
published:
created: 2026-10-11
description: "04 AI Agent 工作原理"
tags:
  - "域/Agent架构与工程"
---
# AI Agent 工作原理

前面我们已经介绍了 AI Agent 的基本概念和核心组件。接下来看看这些组件是如何协同工作的，以及如何使用 Python 实现一个简单的 Agent。

传统的大语言模型（LLM）主要根据输入的上下文生成回答。如果没有连接外部工具，它通常无法直接读取本地文件、查询实时数据或操作其他软件。

AI Agent 则在模型基础上结合工具调用、任务状态管理和执行控制，使程序能够根据目标执行多个操作步骤，并利用执行结果决定下一步做什么。

例如，用户提出"读取 Excel 文件，统计销售额并生成图表"。Agent 可以读取文件、调用 Python 处理数据、生成图表，最后将结果保存到指定目录。

**AI Agent 的关键在于：模型负责决策，工具负责执行，程序根据执行反馈持续推进任务。**

## AI Agent 的基本组成

一个典型的 LLM Agent 通常包含模型、工具和任务状态管理等部分。

| 组成部分 | 主要作用 |
| --- | --- |
| 模型（LLM） | 理解任务、分析上下文，决定下一步操作。 |
| 工具（Tools） | 执行文件操作、搜索、计算和 API 调用。 |
| 状态与记忆（State / Memory） | 记录任务进度、对话历史和工具执行结果。 |
| 执行控制（Agent Runtime） | 调度工具、处理错误、控制循环和终止任务。 |

其中，模型通常负责生成决策，工具负责与外部环境交互，执行程序则负责组织整个任务流程。

对于简单任务，Agent 可能不需要复杂的规划系统或长期记忆；对于多步骤任务，则需要保存任务状态，以便根据执行结果继续工作。

![AI Agent 基本组成](https://www.runoob.com/wp-content/uploads/2025/12/ai-agent-core-runoob-3-scaled.png)

---

## AI Agent 的类型

Agent 并不都是通过大语言模型实现的。在人工智能研究中，智能体可以根据决策机制和系统架构分为不同类型。

| Agent 类型 | 主要特点 | 应用场景 |
| --- | --- | --- |
| 反应式 Agent（Reactive Agent） | 根据当前输入或环境状态作出响应 | 规则控制、简单游戏 AI |
| 目标导向 Agent（Goal-based Agent） | 根据目标选择能够推进任务的操作 | 任务规划、自动化工作流 |
| 效用型 Agent（Utility-based Agent） | 通过效用函数比较不同操作的预期效果 | 路径规划、资源优化 |
| 学习型 Agent（Learning Agent） | 通过学习机制改进决策策略 | 强化学习、智能控制 |
| 多智能体系统（Multi-Agent） | 由多个 Agent 协作完成任务 | 软件开发、复杂任务协作 |

上述类型并不完全互斥。例如，一个目标导向 Agent 也可以具有学习能力，多智能体系统中的每个 Agent 也可以采用不同的决策机制。

目前常见的 LLM Agent，通常围绕用户目标，利用大语言模型选择工具、处理反馈并执行任务。

## AI Agent 的执行流程

理解 Agent 工作原理，最重要的是理解它的执行循环（Agent Loop）。

一种常见的实现方式是 ReAct（Reasoning and Acting），即将推理和行动结合起来。

Agent 不一定一次完成所有决策，而是可以根据工具执行结果，持续判断下一步应该做什么。

基本过程如下：

```
用户输入任务
    ↓
模型分析当前任务
    ↓
选择工具并生成参数
    ↓
执行程序调用工具
    ↓
获取工具返回结果
    ↓
模型判断任务是否完成
    ├── 未完成：继续调用工具
    └── 已完成：输出最终结果
```

例如，用户要求"查找某个 Python 库的最新版本，并生成安装命令"。

1. Agent 判断需要查询软件包版本。
2. 调用软件包信息查询工具。
3. 获取版本号和相关信息。
4. 根据查询结果生成安装命令。
5. 检查结果是否满足要求，然后向用户返回。

如果查询失败，Agent 可以根据错误信息重试，也可以选择停止任务并报告失败原因。

需要注意，ReAct 只是 Agent 的一种执行模式。实际系统也可以使用预定义工作流、任务规划器或其他编排机制。

### 一次完整的工具调用过程

假设用户提出以下任务：

**帮我计算商品总价，单价 89 元，购买 6 件，再减去 30 元优惠券。**

Agent 可以按照下面的方式处理：

**第一步：理解任务**

模型识别出单价、数量和优惠金额，判断需要执行数值计算。

**第二步：选择工具**

假设系统提供了名为 `calculate_total` 的计算工具，模型可以生成以下参数：

```
{
    "price": 89,
    "quantity": 6,
    "discount": 30
}
```

**第三步：执行工具**

Agent 的执行程序接收参数，调用实际的 Python 函数：

```
def calculate_total(price, quantity, discount):
    return price * quantity - discount
```

**第四步：获取结果**

工具返回：

```
504
```

**第五步：生成回答**

模型根据工具返回的结果，向用户说明：

商品总价为 89 × 6 = 534 元，减去 30 元优惠券后，实际需要支付 504 元。

这个过程展示了 Agent 中模型与工具的分工：模型负责理解任务和选择操作，执行程序调用函数，工具计算结果，最后再由模型整理回答。

---

## Python 中实现 AI Agent

下面使用 Python 实现一个简单的 Agent 工作流程。

为了方便初学者理解，我们先使用普通 Python 函数分别模拟感知、决策、行动和记忆模块，再将它们组合成一个可以运行的程序。

**注意：**下面的基础示例使用关键词匹配进行决策，没有连接真正的大语言模型，因此属于 Agent 工作流程的教学模拟，而不是完整的 LLM Agent。

![Python Agent 程序架构](https://www.runoob.com/wp-content/uploads/2026/02/68040279-910a-4bf9-8f0b-8b7bd88138c2.webp)

### 1、感知模块

感知模块负责获取外部输入。

在命令行程序中，最简单的感知方式就是使用 Python 的 `input()` 函数读取用户输入。

## 实例

# 感知模块：读取用户输入  
  
def perceive():  
    user\_input = input("请输入指令：")  
    return user\_input.strip()  
  
  
# 获取用户输入  
message = perceive()  
  
print("收到指令：", message)

执行程序后，假设输入：

```
请输入指令：计算 10 + 5
收到指令： 计算 10 + 5
```

这里的感知模块只处理文本输入。对于其他 Agent，还可以通过 API 获取数据、读取文件或者使用多模态模型处理图片和音频。

### 2、决策模块

决策模块负责分析输入，决定执行什么操作。

真实的 LLM Agent 通常利用模型进行任务理解和工具选择。这里先通过关键词判断模拟这一过程。

## 实例

# 决策模块：根据关键词选择操作  
  
def make\_decision(message):  
    message = message.strip()  
  
    if message.lower() in ("退出", "exit", "quit"):  
        return "exit"  
  
    if "天气" in message:  
        return "weather"  
  
    if "计算" in message:  
        return "calculator"  
  
    return "chat"  
  
  
# 测试决策模块  
message = "帮我计算 10 + 5"  
  
decision = make\_decision(message)  
  
print("决策结果：", decision)

执行结果：

```
决策结果： calculator
```

该示例只负责识别任务类型，并没有理解完整的数学表达式。

在实际 Agent 系统中，模型可以根据工具说明和用户指令，生成更具体的操作参数。

### 3、工具与行动模块

行动模块负责执行决策模块选择的操作。

工具可以是普通 Python 函数，也可以是外部 API、数据库接口或代码执行环境。

下面定义一个简单的计算器工具，支持加、减、乘、除运算。

## 实例

# 计算器工具  
  
def calculator(a, b, operator):  
    if operator == "+":  
        return a + b  
  
    if operator == "-":  
        return a - b  
  
    if operator == "\*":  
        return a \* b  
  
    if operator == "/":  
        if b == 0:  
            raise ValueError("除数不能为 0")  
        return a / b  
  
    raise ValueError("不支持的运算符")  
  
  
# 调用工具  
result = calculator(3, 5, "\*")  
  
print("计算结果：", result)

执行结果：

```
计算结果： 15
```

在这个例子中，`calculator()` 就是一个工具。Agent 可以根据任务需要调用它，并使用其返回结果。

相比直接使用 `eval()`，这种明确指定运算符的方式更容易限制允许执行的操作。

对于更复杂的计算器，可以使用 Python 的 `ast` 模块解析受限制的数学表达式，但不应该直接使用 `eval()` 执行不可信的用户输入。

### 4、记忆模块

记忆模块用于保存对话历史、任务状态以及工具调用结果。

对于简单的命令行 Agent，可以使用 Python 列表保存当前会话内容。

## 实例

# 使用列表保存对话历史  
  
history = []  
  
def save\_message(role, content):  
    history.append({  
        "role": role,  
        "content": content  
    })  
  
  
# 模拟用户与 Agent 的对话  
save\_message("user", "计算 3 + 5")  
save\_message("assistant", "计算结果：8")  
  
save\_message("user", "再乘以 2")  
save\_message("assistant", "计算结果：16")  
  
# 查看历史记录  
for item in history:  
    print(item["role"], ":", item["content"])

执行结果：

```
user : 计算 3 + 5
assistant : 计算结果：8
user : 再乘以 2
assistant : 计算结果：16
```

这里的历史记录是预先写入的示例数据，仅用于演示保存方式，并不表示程序已经能够理解"再乘以 2"这样的上下文指令。

如果需要让 Agent 真正利用对话历史作出决策，可以将相关历史信息传递给模型，或者在执行程序中维护明确的任务状态。

对于需要跨会话保存的数据，可以进一步使用 SQLite、Redis 或其他数据库。

---

## 实践练习：创建一个简单的命令行 Agent

前面分别实现了输入读取、任务判断、工具执行和历史记录。接下来将这些功能组合成一个可以持续运行的命令行程序。

这个程序包含以下功能：

- 支持连续输入指令。
- 根据关键词选择天气或计算工具。
- 支持加、减、乘、除运算。
- 记录本次会话历史。
- 输入"退出"后结束程序。

为了方便测试，天气查询使用固定的模拟数据，不会调用真实的天气 API。

计算器使用正则表达式解析简单算式，不执行任意 Python 代码。

## 实例

import re  
  
# 模拟天气数据  
WEATHER\_DATA = {  
    "北京": "晴，25℃",  
    "上海": "多云，23℃",  
    "广州": "小雨，28℃",  
    "深圳": "晴，29℃"  
}  
  
# 短期记忆：保存对话历史  
history = []  
  
  
# 感知模块：读取输入  
def perceive():  
    return input("您：").strip()  
  
  
# 决策模块：识别任务类型  
def make\_decision(message):  
    if message.lower() in ("退出", "exit", "quit"):  
        return "exit"  
  
    if "天气" in message:  
        return "weather"  
  
    if "计算" in message or re.search(  
        r"\d\s\*[\+\-\\*/]\s\*\d", message  
    ):  
        return "calculator"  
  
    return "chat"  
  
  
# 天气工具：返回模拟数据  
def get\_weather(message):  
    for city, weather in WEATHER\_DATA.items():  
        if city in message:  
            return f"{city}天气：{weather}（模拟数据）"  
  
    return "请输入北京、上海、广州或深圳进行查询。"  
  
  
# 计算器工具  
def calculator(message):  
    # 只识别两个数字组成的简单算式  
    pattern = (  
        r"(-?\d+(?:\.\d+)?)"  
        r"\s\*([\+\-\\*/])\s\*"  
        r"(-?\d+(?:\.\d+)?)"  
    )  
  
    match = re.search(pattern, message)  
  
    if not match:  
        return "请输入算式，例如：计算 10 + 5"  
  
    a = float(match.group(1))  
    op = match.group(2)  
    b = float(match.group(3))  
  
    if op == "+":  
        result = a + b  
    elif op == "-":  
        result = a - b  
    elif op == "\*":  
        result = a \* b  
    elif op == "/":  
        if b == 0:  
            return "计算错误：除数不能为 0"  
        result = a / b  
    else:  
        return "不支持的运算符"  
  
    return f"计算结果：{result:g}"  
  
  
# 行动模块：调用对应工具  
def execute\_action(decision, message):  
    if decision == "weather":  
        return get\_weather(message)  
  
    if decision == "calculator":  
        return calculator(message)  
  
    return "暂时无法处理该指令，请尝试天气查询或计算。"  
  
  
# 保存对话历史  
def save\_history(role, content):  
    history.append({  
        "role": role,  
        "content": content  
    })  
  
  
# Agent 主循环  
def run\_agent():  
    print("简单 Agent 已启动")  
    print("支持天气查询、算术计算")  
    print("输入"退出"结束程序\n")  
  
    while True:  
        try:  
            message = perceive()  
        except (EOFError, KeyboardInterrupt):  
            print("\n程序已结束")  
            break  
  
        if not message:  
            continue  
  
        # 识别任务  
        decision = make\_decision(message)  
  
        if decision == "exit":  
            print("Agent：再见！")  
            break  
  
        # 保存用户输入  
        save\_history("user", message)  
  
        # 执行操作  
        response = execute\_action(decision, message)  
  
        # 输出结果  
        print("Agent：", response)  
  
        # 保存 Agent 回复  
        save\_history("assistant", response)  
  
    # 显示本次对话历史  
    print("\n本次对话历史：")  
  
    for item in history:  
        print(f"{item['role']}：{item['content']}")  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
    run\_agent()

将以上代码保存为 `simple_agent.py`，然后在终端执行：

```
python simple_agent.py
```

也可以使用：

```
python3 simple_agent.py
```

程序运行示例：

```
简单 Agent 已启动
支持天气查询、算术计算
输入“退出”结束程序

您：北京天气
Agent： 北京天气：晴，25℃（模拟数据）

您：计算 10 + 5
Agent： 计算结果：15

您：计算 20 / 4
Agent： 计算结果：5

您：退出
Agent：再见！

本次对话历史：
user：北京天气
assistant：北京天气：晴，25℃（模拟数据）
user：计算 10 + 5
assistant：计算结果：15
user：计算 20 / 4
assistant：计算结果：5
```

**程序说明：**

- `perceive()`：读取用户输入。
- `make_decision()`：根据输入识别任务类型。
- `get_weather()`：返回预先定义的模拟天气数据。
- `calculator()`：解析并执行简单算术运算。
- `execute_action()`：根据决策调用对应工具。
- `save_history()`：保存用户消息和程序回复。
- `run_agent()`：负责组织整个执行循环。

这个程序不依赖第三方 Python 库，使用 Python 3 即可运行。

需要注意，程序的决策逻辑仍然是固定的关键词匹配，因此无法像真正的大语言模型一样理解复杂语义，也不会根据历史对话自动进行多步骤推理。

它的主要目的是展示 Agent 中输入、决策、工具调用、状态保存和执行循环之间的关系。

## 如何将它升级为真正的 LLM Agent？

上面的程序已经具备基本的执行框架，但最重要的决策模块仍由固定规则实现。

如果要让程序具备大语言模型驱动的任务理解与工具选择能力，可以将关键词匹配替换为 LLM 的工具调用机制。

基本步骤如下：

1. 选择一个支持工具调用的大语言模型。
2. 定义可以调用的工具及参数。
3. 将用户任务和工具定义发送给模型。
4. 读取模型返回的工具调用请求。
5. 验证参数并执行对应的 Python 函数。
6. 将工具结果返回给模型，继续下一轮处理。
7. 任务完成后，输出最终结果。

例如，在基础示例中，工具选择是通过以下代码完成的：

```
if "天气" in message:
    return "weather"
```

如果接入支持 Function Calling 的大语言模型，就可以让模型根据用户指令及工具说明，判断是否需要调用 `get_weather`，并生成相关参数。

这样就不再需要为每一种自然语言表达单独编写关键词判断规则。

不过，实际开发仍需要限制工具权限、验证参数、处理调用错误，并设置执行次数和运行时间限制。

### 常见开发方式

开发 LLM Agent 时，可以选择直接调用模型 API，也可以使用 Agent 开发框架。

| 开发方式 | 特点 | 适用场景 |
| --- | --- | --- |
| 原生 Python + LLM API | 自己实现工具调用和执行循环 | 学习原理、简单 Agent |
| LangChain / LangGraph | 提供工具集成、状态管理和工作流编排能力 | 多步骤 Agent、复杂业务流程 |
| LlamaIndex | 提供数据连接、检索和 Agent 相关组件 | 知识库、文档处理、数据检索 |
| Microsoft Agent Framework | 提供 Agent 与多 Agent 工作流开发能力 | 企业应用、Agent 协作 |

对于初学者，建议先理解 Python 函数调用、JSON 数据、API 请求和任务循环，再逐步学习框架。

这样更容易理解 Agent 的实际执行过程，也方便排查工具调用失败、状态管理错误等问题。

---

## 总结

AI Agent 的工作原理可以概括为：接收任务、分析任务、选择工具、执行操作、读取反馈，并根据结果决定是否继续执行。

一个典型的 LLM Agent 通常包含以下几个关键部分：

- **大语言模型：**理解任务并生成决策。
- **工具：**执行具体操作并返回结果。
- **状态与记忆：**保存任务上下文和执行进度。
- **执行循环：**组织模型调用、工具执行和结果检查。

本文通过 Python 实现了一个简单的命令行 Agent 流程模拟，展示了这些模块如何协同工作。

下一步可以尝试连接真正的大语言模型 API，让模型自主选择工具，再逐步加入文件处理、数据库查询和多步骤任务规划等能力。

开发 Agent 时，不仅要关注模型能否正确理解任务，还需要考虑工具执行是否可靠、权限是否合理，以及如何判断任务已经完成。

> 更多资料可以参考：
>
> - [ReAct：结合推理与行动的语言模型研究](https://arxiv.org/abs/2210.03629)
> - [LangChain 官方文档](https://docs.langchain.com/)
> - [Microsoft Agent Framework 文档](https://learn.microsoft.com/en-us/agent-framework/)
