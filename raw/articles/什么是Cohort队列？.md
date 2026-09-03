---
title: "什么是Cohort队列？"
source: "https://mp.weixin.qq.com/s/lxWyDbiLOmcmELq0W4iQsA"
author:
  - "[[SimoneLee]]"
published:
created: 2026-09-04
description: "广告投放中的同周期分析指的到底是什么？"
tags:
  - "clippings"
---
SimoneLee 出海流量研究僧 *2024年12月16日 09:00*

Hello，大家好。

我是目前研究出海投放&变现业务的SL。

不管是甲方还是乙方，只要是效果类广告都不得不面对的一个需求就是去分析渠道获取用户的后项表现，也就是用户质量。我们经常听到同事说：看一下这个渠道的同期群分析/cohort效果等说法，那么他们说的这个概念到底是什么意思呢？

今天帮助大家解释一个分析效果时，必须掌握的概念：Cohort(队列)。知道了Cohort的概念之后，我们就能够方便地去进行Cohort Analysis。

Cohort的定义：

Cohort是指根据某种共有的特征或事件，将一群用户或实体分组。每个cohort中的成员有着某些相同的属性，比如同一安装时间、同一购买行为、同一注册来源等。常见的有如下两种：

时间维度Cohort：基于某个时间点或时间段。例如：按照用户注册时间分组。比如根据注册时间来看，将用户分为“2024年10月注册用户”、“2024年11月注册用户”、“2024年12月注册用户”等。

行为维度Cohort：基于用户完成的某个事件。例如：按照第一次购买的时间，或安装应用后首次使用功能的时间。比如根据完成首次付费事件的用户的付费金额来看，分为“低于10¥付费”、“处于10¥-20¥付费”等。

Cohort的用途：

Cohort分析帮助我们更细致地观察特定用户群体的行为轨迹，比如分析不同群体的用户在生命周期内的行为差异，或者比较不同广告活动引流的用户群体，评估不同组用户的价值和生命周期表现。

在广告行业里面，经常使用cohort数据分析的关键指标包括：

RR留存率：同一cohort中的用户在不同时间点是否仍在使用。

LR流失率：同一cohort中用户离开或停止使用的比例。

ARPU(每用户平均收入)：针对不同cohort计算其贡献的收入。

ROAS(投放回收比例)：针对不同cohort计算其回报率，即收入/成本。

CR转化率：从某一行为(如注册)到目标行为(如购买)的转化比例。

说到这里，可能大家对这一概念还是比较模糊，这里贴心帮大家举一个非常详细的例子：

假设，今天是2024年12月18日。 我们在Unity平台上从2024年12月10日开始，在美国地区投放了一个广告系列。投放时间从2024年12月10日开始，我们今天从后台开始观测数据，无论哪张报表都是通过UTC时区记录。优化师点进后台，先大概看一眼数据走向：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDSvBb3Cr5hGezcTtDoGb4StujVn0gOB3eQ9TyqgVZJIPkVibicTIsT7dy3iaxiaIlu44bs4eIFjFibbuw/640?wx_fmt=png&from=appmsg#imgIndex=0)

假设只看ROAS的话，优化师会说：诶，这个ROAS表现真的很不错，给这个渠道多加预算！但是真的是这样的吗？表现更好了吗？我们以每一个用户获取的LTV视角来看，每天的广告消耗和用户付费金额如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDSvBb3Cr5hGezcTtDoGb4Sw5wniaRGfyeZusuNRn1MOWbNxewmpNwIPB4MibGDNNnmdFpkWA23Faww/640?wx_fmt=png&from=appmsg#imgIndex=1)

我们将同一天安装的用户视为同一个cohort，然后将每个cohort用户按照同周期的行为去做对比。 比如我们都去对比每批用户进来之后的当天的ROAS，第一天的ROAS等数值。 这样可以排除大R的影响，也更有对比意义。这就是Cohort Analysis。 比如上面在cohort的视角下，我们去对比ROASD0的数据，我们虽然能够看到有好转的趋势，但是还是不如之前的表现。 如果对比更深一些的ROASD3数据的话，这个趋势是下降的，我们甚至会觉得表现是不好的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDSvBb3Cr5hGezcTtDoGb4SmjiaibGTX7AEf83maT1iaQcaH2myZIW7rQRJXeIEhl9T9ZOjUUKwCS7ew/640?wx_fmt=png&from=appmsg#imgIndex=2)

(上图中灰色区域分别对应上三角和下三角，这些区域的数据因为时间还未到达或已经超过，所以无法计算)

上面的图表有点模糊，这里我给大家把原文档的位置链接放在这里：

https://docs.google.com/spreadsheets/d/1vBRbpIur3A0e5Lvqw7OIMR5MWkkF0J5asEFFjC-xRVo/edit?gid=0#gid=0

如果大家有需要的话，可以进入到Google Doc里面去查看。

最后说一点，Cohort与Overview的区别:

在数据分析中，Overview（概览）侧重于整体指标的宏观展示，而Cohort则专注于不同用户群体（队列）的时间趋势。

例如：Overview会告诉你每天新增了多少用户。Cohort会告诉你，2024年1月注册的用户在2月的活跃率是多少，与2023年12月注册的用户相比表现如何。

关注我，带你继续学习～

Bye！

**微信扫一扫赞赏作者**

广告投放 · 目录