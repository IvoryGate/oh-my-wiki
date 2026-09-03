---
title: "Unity平台ROAS开启条件和数据差异问题"
source: "https://mp.weixin.qq.com/s/M9tm8PvGtND1yIupZFn_Vw"
author:
  - "[[SimoneLee]]"
published:
created: 2026-09-04
description: "从排查差异问题学习解决问题的思路"
tags:
  - "clippings"
---
SimoneLee 出海流量研究僧 *2024年12月17日 09:00*

Hello，大家好。

我是目前研究出海投放&变现业务的SL。

最近在和Support掰扯一个Appsflyer三方平台和Unity后台的ROAS数据差异的问题。在搞清楚原因后，我整理了遇到的问题和答案，如果大家和我有一样的问题，可以先来看看我的内容能否解决你的问题。

目前仅确保到撰文日期截止是这样的情况，之后平台是否有新的规定或者修改相应的内容，则不确定。

本部分包括以下四个部分：

1Unity平台支持的Advanced Campaign

2Unity平台支持类型Campaign的开启条件

3Unity平台与MMP平台Cost回传的要求

4Unity平台后项数值和MMP平台数值差异的原因

1Unity平台支持的Advanced Campaign

首先，根据Unity平台的官网帮助中心文档来看，Unity平台支持三大类型的Advanced Campaign（高阶广告计划）。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDSvBb3Cr5hGezcTtDoGb4SGg79WDOTW4Ha7tNkHkvGnJr3hbnbAY5AusehD71pyquxiaxWiablXwibg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

第一种是以用户整体LTV中核心ROAS为目标的Campaign。

第二种是以用户留存为目标的Campaign。

第三种是以用户User Journey过程中的事件转化为目标的Campaign。

2Unity平台支持类型Campaign的开启条件

首先在讲述开启条件前，我们先阐述两个概念：

2.1Cohort群组 [（如果对这一概念还不熟悉，可以查看我之前的文章）](https://mp.weixin.qq.com/s?__biz=MzU5MzgzNTQzNQ==&mid=2247483981&idx=1&sn=bef6d5b8e98242ec873eaae209f1d127&scene=21#wechat_redirect)

2.2App与Unity之间的数据回传

要做优化，就需要将对应的install、event、purchase value、ad value等关键事件及价值回传给广告平台。目前Unity支持如下三种方式追踪安装和事件：

| 追踪方式 | 安装 | 安装后事件 |
| --- | --- | --- |
| MMP | ✅ | ✅ |
| SDK | ❎ | ✅(MMP: Appsflyer UA signal for Android & iOS) or (Unity Monetisation SDK for iOS only) |
| S2S(API中的一种) | ✅ | ✅ |

注：

1.Unity支持与Appsflyer、Adjust、Singular、Tenjin、Branch、Kochawa、Appmetrica、Mytracker等多家MMP合作伙伴。

2.Unity官网参考文档：https://docs.unity.com/acquire/en-us/manual/partner-integration

3.事件的回传窗口期，请至少保证15day

2.3Campaign条件

被官方复杂混乱的中文绕昏头脑，又看不太懂英文的朋友们，可以参考下表的总结：

| Campaign类型 | 单国家安装数 | 单国家事件数 | 单国家需要天数 |
| --- | --- | --- | --- |
| ROAS IAA D0 | 200个Unity产生的安装 | 至少1个D0的广告收入 | 如果第一个D0就有了200个安装且Unity后台收到了对应的广告收入，则最快仅需要2day。 |
| ROAS IAA D7 | 200个Unity产生的安装 | 至少1个D7的广告收入 | 如果第一个D7就有了200个安装且Unity后台收到了对应的广告收入，则最快仅需要9day。 |
| ROAS IAP D7 | 10个Unity产生的安装 | 至少10个独立D7的付费事件 | 如果第一个D7就有了10个安装且这10个安装有对应10次Unique付费，则最快仅需要9day。 |
| ROAS Combo D7 | 200个Unity产生的安装 | 至少10个独立D7的付费事件&1个D7的广告收入 | 如果第一个D7就有了200个安装且Unity后台收到了对应的广告收入和10次Unique付费，则最快仅需要9day。 |
| Event D7(需联系AM开启账户权限) | 10个Unity产生的安装 | 至少10个独立D7的映射事件 | 如果第一个D7就有了10个安装且这10个安装有对应10次Unique事件，则最快仅需要9day。 |
| RR D7 | / | 至少一个D7的Session回传 | 如果第一个D7就有留存且Unity后台收到了回传，则最快仅需要9day。 |

注：Unity设置有30天动态窗口期，一旦在30天内无法积累够开启的条件，则会自动跳转下一个30天，这个30天窗口期是动态设置的，所以请保证预算和付费事件选择的合理性。

3Unity平台与MMP平台Cost回传的要求

Unity提供API接口，我们可以使用该API回传到自己的BI或者使用的MMP后台。具体每家平台的对接文档如下：

Appsflyer：

https://support.appsflyer.com/hc/en-us/articles/26078530790289-Bulletin-Unity-Ads-cost-API-integration-update

Adjust：

https://www.help.adjust.com/en/article/measure-ad-spend-with-unity-ads?src=search\_page

Unity：

https://services.docs.unity.com/statistics/v2/index.html

⚠️：部分MMP支持手动上报或者归因链接S2S上传，优先级顺序为SDK>API>链接S2S>手动上报。

4Unity平台后项数值和MMP平台数值差异的可能原因

这里差异是在投放的时候发现：Unity与Appsflyer相比，ROASD0/D3/D7之间的差异很大。

首先两边都用相同的UTC时区看数据，所以可以排除时区问题。分天看cost也是一致的，也合理，因为Cost是由Unity通过API上报给MMP的，理论上就应该没有差异。

那ROAS的不同就是出在Revenue的不一致了。这个Campaign是一个Ad Revenue的Campaign。所以我们需要将Appsflyer的Raw Data数据导出，同时导出一份Cohort视角下的数据，分天及对应的ROASD0-D7数值的表格。

接下来我们将AF的Raw Data通过Python或者Excel打开，筛选某一天的全部数据。然后将这一天Original URL用Excel函数“Text to Column”或者Python的字符串分解，将原始表格中的“value=”拆分出来。这样我们按照相同的Install Timestamp对应的Event Timestamp 同一个自然天去做求和，可以得出一个D0/D3/D7的数值。这个值和Appsflyer100%全部对应，然后把这些值的idfa全部拉出来。

在Unity后台找到Support，把同样这一天的对应的从Appsflyer平台pb回来的安装Raw Data找到。将Unity后台的当天的idfa按照同样的方法拉出来。

我们用列排重的方式，得到差值。

Okay找到这一步，看到差异的数值，我就明白了出现问题的原因，解决了所有的问题。我明白了Appsflyer和Unity平台RR以及ROAS差异的根本原因！

并不是两者之间的时区/数据缺失等问题，根本原因是规则问题：

Appsflyer的ROAS D0中D0的定义是calendar day：

https://support.appsflyer.com/hc/en-us/articles/207040496-Cohort-and-retention-dashboard

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDSvBb3Cr5hGezcTtDoGb4SQ6ctxE6cM27I19vkcsKFaaGdiaMT9nHVMicLVFSrluFiagv2h40bOtxSg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

Unity采用的则是rolling 24 hours去定义D1。

举个例子：

一个UTC时区下，2024年12月15日上午10:00安装的用户，12月16日凌晨04:00产生的ad revenue。

在Appsflyer会将这个ad revenue记为这个用户ROASD1中。（因为从calendar来看属于次日）

在Unity会将这个ad revenue记为这个用户ROASD0中。（因为是从安装开始计算一个rolling的24h，还在这个时间内）

同理这个数值的准确性，还会受到何时接收和回传的影响。

Cost每天UTC0时区会通过Unity回传给Appsflyer。如果选择的是API上报，则每天同步四次。

Ad Revenue什么时候从应用的SDK上报给Appsflyer呢？又是什么时候从Appsflyer回传给Unity呢？这又会造成一些时间差。尽管Unity完全采用标准的时间戳timestamp去做解码时间，但是由于数据回传的不及时，总会导致最近的1-2天，数据是不太准确的。

因此建议去对比过去至少3-5天这样已经排除了时间问题，仅剩下规则问题的ROAS数据。同时，也建议去做平均值的数据对比，这样更加有对比意义。

当然这样的数据差异并不会影响机器的学习，毕竟不是一个数据缺失的问题。如果想要拉齐平台AM和优化师之间的数据差异，最好还是选择一个统一的平台去观测数值。比如，我们将数据权限授权给乙方dsp或者ad network，大家都通过MMP去观测数值，这样减少沟通成本。

同理，你知道另一个平台Adjust是如何计算这一数值的吗？它又遵守哪一种规则呢？

Adjust 采用的是rolling 24 hour去计算！

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAibEj5TnZVruoHepkOxdIicChEZSIoxQ5pibfxg89FIfmIwLp1qzIcelZnKttJwofuM2ltwU9x9Q0pA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

可以参考这里的文档说明！

https://www.help.adjust.com/en/article/how-cohorts-work

知道问题很简单，关键是要学习解决问题的思路并举一反三！

关注我，一起学习～

Bye！

**微信扫一扫赞赏作者**

广告投放 · 目录