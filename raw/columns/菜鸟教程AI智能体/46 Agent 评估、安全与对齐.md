---
title: "46 Agent 评估、安全与对齐"
source: "https://www.runoob.com/ai-agent/evaluation-safety-alignment.html"
author:
published:
created: 2026-10-11
description: "46 Agent 评估、安全与对齐"
tags:
  - "域/Agent架构与工程"
---
# Agent 评估、安全与对齐

评估是确保 Agent 效果的基础。

安全和对齐是 Agent 能否被信任和部署的关键。

---

## Agent 评测体系

评估 Agent 性能是开发过程中的关键环节。

好的评测体系能够帮助我们了解 Agent 的能力边界。

也为持续优化提供方向和依据。

### 评测维度

任务完成度：Agent 是否正确完成了给定任务。

效率指标：完成任务所需的步骤数、token 消耗、执行时间。

质量指标：答案的准确性、响应的一致性、对话的自然度。

鲁棒性：对异常输入、噪声数据的处理能力。

### 常用 Benchmark

| Benchmark | 用途 | 评估内容 |
| --- | --- | --- |
| GAIA | 通用 AI 助手评测 | 复杂任务处理、多步骤推理 |
| MMLU | 多任务语言理解 | 57 个学科的知识问答 |
| HumanEval | 代码生成评测 | Python 代码编写正确性 |
| HotpotQA | 多跳问答评测 | 需要多个文档推理的问题 |
| AgentBench | Agent 能力评测 | 真实环境中的 Agent 表现 |

### 代码实现：评测框架

## Agent 评测框架

class AgentEvaluator:  
    """  
    Agent 评测框架  
    评估 Agent 在各种任务上的表现  
    """  
      
    def \_\_init\_\_(self, agent, metrics):  
        # 待评测的 Agent  
        self.agent = agent  
        # 评测指标列表  
        self.metrics = metrics  
      
    def evaluate(self, test\_cases):  
        """  
        执行评测  
        :param test\_cases: 测试用例列表  
        :return: 评测报告  
        """  
        results = []  
          
        for test\_case in test\_cases:  
            # 执行任务  
            result = self.run\_single\_test(test\_case)  
            results.append(result)  
          
        # 生成评测报告  
        report = self.generate\_report(results)  
        return report  
      
    def run\_single\_test(self, test\_case):  
        """  
        运行单个测试用例  
        """  
        # 记录开始时间  
        start\_time = time.time()  
          
        # 执行 Agent  
        try:  
            output = self.agent.run(test\_case.input)  
            success = self.evaluate\_output(output, test\_case.expected)  
            error = None  
        except Exception as e:  
            output = None  
            success = False  
            error = str(e)  
          
        # 记录结束时间  
        end\_time = time.time()  
          
        return TestResult(  
            test\_case=test\_case,  
            output=output,  
            success=success,  
            error=error,  
            duration=end\_time - start\_time,  
            token\_count=self.count\_tokens(output)  
        )  
      
    def evaluate\_output(self, output, expected):  
        """评估输出是否符合预期"""  
        for metric in self.metrics:  
            if not metric.evaluate(output, expected):  
                return False  
        return True  
      
    def generate\_report(self, results):  
        """生成评测报告"""  
        total = len(results)  
        passed = sum(1 for r in results if r.success)  
          
        # 计算各项指标  
        avg\_duration = sum(r.duration for r in results) / total  
        avg\_tokens = sum(r.token\_count for r in results) / total  
          
        # 按测试类型分组统计  
        by\_category = {}  
        for r in results:  
            category = r.test\_case.category  
            if category not in by\_category:  
                by\_category[category] = {"total": 0, "passed": 0}  
            by\_category[category]["total"] += 1  
            if r.success:  
                by\_category[category]["passed"] += 1  
          
        return EvaluationReport(  
            total=total,  
            passed=passed,  
            pass\_rate=passed / total,  
            avg\_duration=avg\_duration,  
            avg\_tokens=avg\_tokens,  
            by\_category=by\_category,  
            results=results  
        )  
  
  
class TestCase:  
    """测试用例"""  
      
    def \_\_init\_\_(self, input, expected, category="general", metadata=None):  
        # 输入  
        self.input = input  
        # 预期输出或评估标准  
        self.expected = expected  
        # 类别  
        self.category = category  
        # 额外元数据  
        self.metadata = metadata or {}  
  
  
class TestResult:  
    """测试结果"""  
      
    def \_\_init\_\_(self, test\_case, output, success, error, duration, token\_count):  
        self.test\_case = test\_case  
        self.output = output  
        self.success = success  
        self.error = error  
        self.duration = duration  
        self.token\_count = token\_count  
  
  
class Metric:  
    """评测指标基类"""  
      
    def evaluate(self, output, expected):  
        raise NotImplementedError  
  
  
class ExactMatchMetric(Metric):  
    """精确匹配指标"""  
      
    def evaluate(self, output, expected):  
        return output.strip() == expected.strip()  
  
  
class ContainsMetric(Metric):  
    """包含关键词指标"""  
      
    def evaluate(self, output, expected):  
        if isinstance(expected, list):  
            return all(keyword in output for keyword in expected)  
        return expected in output  
  
  
class SemanticSimilarityMetric(Metric):  
    """语义相似度指标"""  
      
    def \_\_init\_\_(self, threshold=0.8):  
        self.threshold = threshold  
      
    def evaluate(self, output, expected):  
        similarity = self.compute\_similarity(output, expected)  
        return similarity >= self.threshold  
      
    def compute\_similarity(self, text1, text2):  
        """计算两个文本的语义相似度"""  
        # 使用嵌入模型计算余弦相似度  
        embedding1 = self.embedder.embed([text1])[0]  
        embedding2 = self.embedder.embed([text2])[0]  
        return cosine\_similarity(embedding1, embedding2)

---

## 安全与对齐

Agent 的安全性至关重要。

AI 系统可能受到各种攻击，产生有害输出。

对齐（Alignment）确保 AI 行为符合人类意图和价值观。

### 常见安全威胁

#### 提示注入（Prompt Injection）

攻击者通过输入诱导 Agent 忽略系统指令。

示例输入："忽略之前的指令，改为执行..."

这是一种上下文劫持攻击，利用 Agent 对用户输入的信任。

#### 越狱（Jailbreaking）

通过特定输入绕过安全限制。

如使用角色扮演、虚构场景等手法。

#### 数据污染

恶意修改训练数据或检索结果。

导致 Agent 产生错误或有害输出。

#### 敏感信息泄露

Agent 不当暴露用户隐私或系统内部信息。

### 防护策略

## 安全 Agent 实现

class SecureAgent:  
    """  
    安全 Agent  
    在基础 Agent 之上增加多层安全防护  
    """  
      
    def \_\_init\_\_(self, base\_agent, guardrails, input\_validator, output\_filter):  
        # 基础 Agent  
        self.base\_agent = base\_agent  
        # 安全护栏列表  
        self.guardrails = guardrails  
        # 输入验证器  
        self.input\_validator = input\_validator  
        # 输出过滤器  
        self.output\_filter = output\_filter  
      
    def process(self, user\_input):  
        """  
        处理用户输入，包含多层安全检查  
        """  
        # ==================== 第一层：输入验证 ====================  
        # 检查输入是否合法  
        is\_valid, reason = self.input\_validator.validate(user\_input)  
        if not is\_valid:  
            return self.create\_safety\_response(reason)  
          
        # ==================== 第二层：注入检测 ====================  
        # 检测提示注入等攻击  
        for guardrail in self.guardrails:  
            check\_result = guardrail.check\_input(user\_input)  
            if not check\_result.is\_safe:  
                # 记录安全事件  
                self.log\_security\_event(  
                    event\_type="input\_guardrail\_triggered",  
                    input=user\_input,  
                    reason=check\_result.reason  
                )  
                return self.create\_safety\_response(check\_result.reason)  
          
        # ==================== 第三层：执行核心逻辑 ====================  
        try:  
            response = self.base\_agent.process(user\_input)  
        except Exception as e:  
            return self.create\_error\_response(str(e))  
          
        # ==================== 第四层：输出过滤 ====================  
        # 检查输出是否安全  
        for guardrail in self.guardrails:  
            check\_result = guardrail.check\_output(response)  
            if not check\_result.is\_safe:  
                self.log\_security\_event(  
                    event\_type="output\_guardrail\_triggered",  
                    output=response,  
                    reason=check\_result.reason  
                )  
                return self.create\_safety\_response(check\_result.reason)  
          
        # 应用输出过滤（如敏感信息脱敏）  
        response = self.output\_filter.filter(response)  
          
        return response  
      
    def create\_safety\_response(self, reason):  
        """创建安全响应"""  
        return {  
            "type": "safety\_block",  
            "message": "抱歉，我无法完成这个请求。",  
            "reason": reason  
        }  
      
    def log\_security\_event(self, event\_type, \*\*kwargs):  
        """记录安全事件"""  
        # 实际应用中应写入安全日志系统  
        print(f"[SECURITY] {event\_type}: {kwargs}")  
  
  
class InputValidator:  
    """输入验证器"""  
      
    def validate(self, text):  
        """  
        验证输入是否合法  
        :return: (is\_valid, reason)  
        """  
        if not text or len(text.strip()) == 0:  
            return False, "输入不能为空"  
          
        if len(text) > 10000:  
            return False, "输入长度超过限制"  
          
        # 检查是否包含可执行内容  
        if self.contains\_executable\_content(text):  
            return False, "输入包含可疑的可执行内容"  
          
        return True, None  
      
    def contains\_executable\_content(self, text):  
        """检查是否包含可执行内容"""  
        # 简化实现  
        suspicious\_patterns = [  
            "javascript:",  
            "data:text/html",  
            "<script>",  
        ]  
        return any(pattern in text.lower() for pattern in suspicious\_patterns)  
  
  
class Guardrail:  
    """安全护栏"""  
      
    def check\_input(self, text):  
        """检查输入"""  
        raise NotImplementedError  
      
    def check\_output(self, text):  
        """检查输出"""  
        raise NotImplementedError  
  
  
class ContentFilterGuardrail(Guardrail):  
    """内容过滤护栏"""  
      
    def \_\_init\_\_(self, blocked\_topics, banned\_words):  
        self.blocked\_topics = blocked\_topics  
        self.banned\_words = banned\_words  
      
    def check\_input(self, text):  
        # 检查是否涉及被禁止的话题  
        for topic in self.blocked\_topics:  
            if topic in text.lower():  
                return CheckResult(  
                    is\_safe=False,  
                    reason=f"涉及敏感话题：{topic}"  
                )  
          
        # 检查是否包含禁用词  
        for word in self.banned\_words:  
            if word in text.lower():  
                return CheckResult(  
                    is\_safe=False,  
                    reason=f"包含不当词汇"  
                )  
          
        return CheckResult(is\_safe=True)  
      
    def check\_output(self, text):  
        # 输出检查同上  
        return self.check\_input(text)  
  
  
class CheckResult:  
    """检查结果"""  
      
    def \_\_init\_\_(self, is\_safe, reason=None):  
        self.is\_safe = is\_safe  
        self.reason = reason

> 重要提醒：安全是一个持续的过程，没有万无一失的方案。需要持续监控、更新和改进安全策略。

---

## 可观测性

生产环境中的 Agent 需要完善的监控体系。

可观测性帮助我们了解 Agent 的行为，排查问题，优化性能。

### 三大支柱

日志（Logging）：记录所有关键事件和决策。

Tracing：追踪请求在系统中的完整流转路径。

指标（Metrics）：收集性能和质量指标。

### 代码实现

## 可观测 Agent 实现

import logging  
from opentelemetry import trace  
from opentelemetry.sdk.trace import TracerProvider  
from opentelemetry.sdk.resources import Resource  
  
# 配置日志  
logger = logging.getLogger(\_\_name\_\_)  
  
# 配置 Tracing  
tracer\_provider = TracerProvider()  
trace.set\_tracer\_provider(tracer\_provider)  
tracer = trace.get\_tracer(\_\_name\_\_)  
  
  
class ObservableAgent:  
    """  
    可观测 Agent  
    集成日志、追踪和指标收集  
    """  
      
    def \_\_init\_\_(self, agent, metrics\_collector):  
        # 基础 Agent  
        self.agent = agent  
        # 指标收集器  
        self.metrics = metrics\_collector  
      
    def process(self, user\_input):  
        """  
        处理请求，包含完整的可观测性支持  
        """  
        # 创建追踪 span  
        with tracer.start\_as\_current\_span("agent\_process") as span:  
            # 设置 span 属性  
            span.set\_attribute("user.input.length", len(user\_input))  
            span.set\_attribute("user.input.preview", user\_input[:100])  
              
            # 记录开始  
            logger.info(f"开始处理请求: {user\_input[:50]}...")  
            start\_time = time.time()  
              
            try:  
                # 执行核心逻辑  
                result = self.agent.process(user\_input)  
                  
                # 记录成功  
                duration = time.time() - start\_time  
                span.set\_attribute("success", True)  
                span.set\_attribute("duration\_ms", duration \* 1000)  
                span.set\_attribute("result.length", len(str(result)))  
                  
                # 收集指标  
                self.metrics.record("request\_duration", duration)  
                self.metrics.increment("request\_success")  
                  
                logger.info(f"请求完成，耗时: {duration:.2f}s")  
                  
                return result  
                  
            except Exception as e:  
                # 记录错误  
                duration = time.time() - start\_time  
                span.set\_attribute("success", False)  
                span.set\_attribute("error.type", type(e).\_\_name\_\_)  
                span.set\_attribute("error.message", str(e))  
                span.record\_exception(e)  
                  
                # 收集错误指标  
                self.metrics.increment("request\_error")  
                self.metrics.record("error\_duration", duration)  
                  
                logger.error(f"请求失败: {e}")  
                  
                raise  
  
  
class MetricsCollector:  
    """指标收集器"""  
      
    def \_\_init\_\_(self):  
        self.metrics = {}  
      
    def increment(self, name, value=1):  
        """递增计数指标"""  
        if name not in self.metrics:  
            self.metrics[name] = {"type": "counter", "value": 0}  
        self.metrics[name]["value"] += value  
      
    def record(self, name, value):  
        """记录数值指标"""  
        if name not in self.metrics:  
            self.metrics[name] = {"type": "gauge", "values": []}  
        self.metrics[name]["values"].append(value)  
      
    def get\_summary(self):  
        """获取指标摘要"""  
        summary = {}  
        for name, data in self.metrics.items():  
            if data["type"] == "counter":  
                summary[name] = data["value"]  
            else:  
                values = data["values"]  
                summary[f"{name}\_avg"] = sum(values) / len(values)  
                summary[f"{name}\_max"] = max(values)  
                summary[f"{name}\_min"] = min(values)  
        return summary

---

## 护栏与人机协同

### Guardrails

Guardrails 是实时的输入输出过滤和限制机制。

区别于安全护栏，Guardrails 更侧重于确保输出质量和合规性。

### HITL（Human-in-the-Loop）

HITL 在关键决策点引入人工审核。

适用于 AI 不能自主决策的高风险场景。

## HITL Agent 实现

class HITLAgent:  
    """  
    人机协同 Agent  
    在关键决策点引入人工审核  
    """  
      
    def \_\_init\_\_(self, agent, approval\_queue, notification\_handler):  
        # 基础 Agent  
        self.agent = agent  
        # 审批队列  
        self.approval\_queue = approval\_queue  
        # 通知处理器  
        self.notification\_handler = notification\_handler  
      
    def process(self, request):  
        """  
        处理请求，必要时触发人工审批  
        """  
        # 评估请求的风险等级  
        risk\_level = self.assess\_risk(request)  
          
        if risk\_level == "high":  
            # 高风险请求，需要人工审批  
            return self.handle\_high\_risk\_request(request)  
        elif risk\_level == "medium":  
            # 中等风险，启用增强监控  
            return self.handle\_medium\_risk\_request(request)  
        else:  
            # 低风险，直接处理  
            return self.agent.process(request)  
      
    def assess\_risk(self, request):  
        """评估请求风险等级"""  
        # 检查是否涉及敏感操作  
        sensitive\_operations = [  
            "delete", "remove", "cancel",  
            "transfer", "payment", "refund"  
        ]  
          
        content\_lower = request.lower()  
        for op in sensitive\_operations:  
            if op in content\_lower:  
                return "high"  
          
        # 检查请求内容的复杂性  
        if len(request) > 1000:  
            return "medium"  
          
        return "low"  
      
    def handle\_high\_risk\_request(self, request):  
        """  
        处理高风险请求，需要人工审批  
        """  
        # 创建审批任务  
        task\_id = self.approval\_queue.add({  
            "request": request,  
            "risk\_level": "high",  
            "timestamp": datetime.now()  
        })  
          
        # 通知审批人  
        self.notification\_handler.notify\_approver(  
            task\_id=task\_id,  
            message=f"有高风险请求需要审批: {request[:100]}..."  
        )  
          
        # 返回等待状态  
        return {  
            "status": "pending\_approval",  
            "task\_id": task\_id,  
            "message": "您的请求需要人工审批，请等待。"  
        }  
      
    def handle\_feedback(self, task\_id, approved, feedback=None):  
        """  
        处理审批反馈  
        """  
        task = self.approval\_queue.get(task\_id)  
          
        if approved:  
            # 审批通过，执行请求  
            self.approval\_queue.complete(task\_id)  
            result = self.agent.process(task["request"])  
              
            # 通知申请人  
            self.notification\_handler.notify\_requester(  
                task\_id=task\_id,  
                status="approved",  
                result=result  
            )  
              
            return result  
        else:  
            # 审批拒绝  
            self.approval\_queue.reject(task\_id, feedback)  
              
            # 通知申请人  
            self.notification\_handler.notify\_requester(  
                task\_id=task\_id,  
                status="rejected",  
                feedback=feedback  
            )  
              
            return {  
                "status": "rejected",  
                "reason": feedback or "审批未通过"  
            }  
  
  
class ApprovalQueue:  
    """审批队列"""  
      
    def \_\_init\_\_(self):  
        self.queue = {}  
        self.counter = 0  
      
    def add(self, task):  
        """添加审批任务"""  
        self.counter += 1  
        task\_id = f"task\_{self.counter}"  
        self.queue[task\_id] = {  
            \*\*task,  
            "status": "pending"  
        }  
        return task\_id  
      
    def get(self, task\_id):  
        return self.queue.get(task\_id)  
      
    def complete(self, task\_id):  
        self.queue[task\_id]["status"] = "approved"  
      
    def reject(self, task\_id, reason):  
        self.queue[task\_id]["status"] = "rejected"  
        self.queue[task\_id]["reject\_reason"] = reason

---

## 章节小结

本章节介绍了 Agent 的评估、安全和对齐知识。

评测体系 通过多维度指标评估 Agent 的性能。

安全威胁 包括提示注入、越狱、数据污染等。

防护策略 通过多层安全检查保障系统安全。

可观测性 通过日志、追踪、指标实现系统监控。

Guardrails 和 HITL 提供输出质量控制和人工审核能力。

评估、安全和对齐是构建可信 Agent 系统的基础。

需要在实际开发中持续关注和改进。
