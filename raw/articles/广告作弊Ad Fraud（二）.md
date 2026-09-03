---
title: "广告作弊Ad Fraud（二）"
source: "https://mp.weixin.qq.com/s/0C93g782qaTRs7kvAZ_isg"
author:
  - "[[SimoneLee]]"
published:
created: 2026-09-04
description: "虚假安装是怎么回事？"
tags:
  - "clippings"
---
SimoneLee 出海流量研究僧 *2025年1月20日 09:00*

Hello，大家好。

我是目前研究出海投放&变现业务的SL。

接下来，我们会逐步分析前文所述的各种ad fraud的特征并说明我们可以采取的应对策略。当然纯靠开发者自身依然无法保证百分百避免作弊流量，所以我会再介绍一下不同MMP平台提供了哪些工具以及如何利用这些平台提供的功能做出我们自己独特的解决方案。

今天我们讲述的内容包括以下这几部分：

虚假安装之设备农场&机器人

- 定义及原理
- 基本的避免方法

定义及原理

设备农场：作弊平台通过模拟器重置设备ID的方式，反复刷新并虚拟点击广告主广告，批量大规模下载安装广告主应用。

机器人：作弊平台通过恶意代码，实现反编译归因等平台的SDK，实现模拟安装的行为。（常见于开源SDK）

本质上这两种方法产生的用户都不是真实的用户，所以对广告平台的风险极大。

我们先探讨设备农场的进化史：虚拟机->刷机/改机->设备农场->云端设备->积分墙->混量->more......

虚拟机指的是利用电脑模拟手机等移动设备，实现伪装。

刷机/改机分别指的是：

刷机：通过修改设备上的Device ID如GAID、IMEI和OS Version等移动设备信息实现伪装。目前简单的刷机基本逃不过风控和MMP的检测。

改机：简单来说，就是通过逆向排查应用设备的环境参数去获取设备参数位置，然后伪造信息、协议后就可以实现定制化伪装真实设备。

设备农场：用单个的真实实体移动设备去实现伪装。常见的场景如下：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ofNjybZfTIBiamm3iaD4Rnbf85NkkUnntGz5fWTgiaC4diap1icFpEicKEoEvYVL4hq1mT0WbicIIpxl6vdNrT234PQjQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

设备农场的成本其实已经非常高昂了，利润极低。

当然聪明的作弊者为了规避被检出率会去洗白设备。作弊者为了绕过MMP的检测机制，会通过走代理的方式，直接刷头部Ad Network+大App的量来洗白自己的设备。这个方法去年被海外的MMP设置了渠道和代理双向握手验证。不过路是死的，人是活的，所以......

云端设备：简单来说，设备农场上云服务器后的产物。

积分墙：这个内容不好说。目前国内对这个的定义很模糊。比如网赚产品尚且可以定义为违规，但是地推流量、常见的Digital Turbine、Tapjoy这些大型积分墙业务公司又是合规的正向产品（如果流量下游审核严谨，不来自网赚/刷机的话）。

混量：目前很多作弊渠道在流量采买上是多种形式混合而成的。它不一定全部是虚假安装的流量，往往是一部分真实流量再加一些归因劫持/大点击/虚假设备的量。这样混装起来，能够实现甲方的KPI要求，同时自己也有利润空间。

接着，我们梳理一下机器人：作弊平台通过恶意代码，由隐藏在用户设备中另一个应用程序上的恶意软件执行，实现反编译归因平台或者其他广告平台的SDK，实现模拟安装的行为。

具体来看，作弊者劫持SDK（假设为应用程序内数据分析的SDK）及其后端服务器的SSL加密通信，进行MITM攻击。一旦攻破SDK通信后，就可以利用该应用的SDK把标准的安装URL发送给MMP服务器平台。这个URL并不是一开始就能够准确确定的，所以需要不断试错并调整URL中的动态/静态参数（ [详见归因基础知识了解更多](https://mp.weixin.qq.com/s?__biz=MzU5MzgzNTQzNQ==&mid=2247483869&idx=1&sn=662fc83628f888be5e8fa0bef946f317&scene=21#wechat_redirect) ，比如写死上报数据的siteid，测试广告ID等动态变化的部分），通过类似“撞库”的过程，最终捕获实时请求的结果。如果成功地追踪到了MMP的安装事件，则可以证明已经成功破解了SDK的安装事件的上报逻辑。

基本的避免方法

对于投放&运营来说：在足够了解自己的产品基础上，我们可以利用一些基本的行业经验和简单的规则去判断是否有虚假安装的流量：

基础维度：

货不对板：比如最为基础的一个逻辑验证，投放米国的产品出现大量霓虹设备语言的安装。

OS Version：假设我们上架的应用只能在Android9+以上版本的设备上才能正常使用。但是分析渠道的时候，发现某些渠道的流量来源于一些非常低OS版本/特别集中的设备供应商，那可以初步判断渠道是有问题的。

New Device Rate：对于一个广告来说，是有概率投放到新设备比例上的，这当然很正常，但是过高的新设备比例则明显不正常。毕竟海外Appsflyer平台是拿到了市场上98%的设备信息。即使是国内，神策和数美等平台也拿到了足够多的数据。所以你的应用99%的情况下，新旧设备分布是遵守大盘的，不会全部都是新设备，高于20%就已经是一个危险的数据指标了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIBiamm3iaD4Rnbf85NkkUnntGNJW019Oycj6gib0h8icKgZ0q1Oicr7tibpWFbkta23tGcJshR8LbcysLGw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

IP和VPN检验：VPN的工作原理是通过选定的VPN的专用服务器而不是互联网服务提供商（ISP）路由设备互联网连接。作弊者使用VPN来掩盖他们的操作并隐藏他们的IP地址，以避免被列入MMP和Ad Network平台的黑名单。MMP平台本身提供了IP验证的套件（如Adjust中的MaxMind）。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIBiamm3iaD4Rnbf85NkkUnntG4v9v0iayWictPsBVD6nzfnzQ9OdUFAjhViabTgTibcfShwFW7TfGZbhibPw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

素材维度：了解所有素材类型和尺寸，拒绝一切非正常规格验证的素材上报点击和曝光。具体来看，比如在明确我们在所有广告平台都没有图片类型素材的话，如果后续中有上报来自image的点击，则可以判定渠道有问题。

规则验证：Appsflyer提供了广告主自行设置Rule防作弊的功能，投放同学可以和运营同学一起根据用户的数据表现，设置规则。比如IP/OS Version的黑白名单。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIBiamm3iaD4Rnbf85NkkUnntG770M6JBSUbc8S2fuTuKWYXtrpTfGur9nKsZC8ykmDkrUyKKD7aYThg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

对于产品同学来说，更需要从技术层面给予一些支持，避免更为复杂的作弊方式：

建立风控系统：这可能是XJD产品最为熟悉的环节，不过现在作弊的情况，其他的品类也可以考虑加入基础风控模型。一般风控系统和MMP的Protect高级服务都会包括识别用户行为，将程序化、非人类行为模式的安装排除归因。说到建立风控模型，就一定逃不过通过时序等各种算法定义用户，将不同的用户分到不同的验证池子，这个后续有时间再写。

设备传感器验证：一般产品（常见于安卓）可以收集用户设备上安装的app、屏幕尺寸分辨率、系统亮度、是否打开了usb调试、所有音量、陀螺仪、是否有设备指纹、是否root、是否充电、电量、手机网络(wif/4G)等字段验证用设备是否有问题。

闭源SDK：与开源不同，闭源技术开发的SDK源代码对作弊者来说，相对难以模拟和反编译。一般来说，反编译后上报URL的行为通常会从应用程序使用的SDK版本以外的SDK版本发送点击和安装，我们需要定期更新并及时留意某些特定SDK版本的安装是否不合理。

CUID埋点：这里是以Appsflyer为例，从应用开始准备发包前，就埋好CUID这个收集字段。官方推荐当用户完成注册后就生成一个CUID给这个用户。确实我们可以利用字段有无去识别一些渠道。但是部分渠道可能依然不承认用户为虚假用户，没关系，还有2.0版本，直接通过CUID和用户安装事件深度绑定，将Application SDK引入。这时候大量没有任何CUID的用户的渠道一定是虚假流量。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIBiamm3iaD4Rnbf85NkkUnntGYoOjFBL9S0vlfkU8butrTUNv1xwuPBRqFbB8R7W49NYqu2RoeK9kibw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

SDK和S2S事件上报以及验证：

我们知道事件的上传可以包括SDK和S2S两种。之前有部分渠道可以做到机刷SDK事件，但是现在有的作弊者可以刷S2S事件了，对此只能说真心佩服。我也遇到过，给一个纯IAA的游戏刷出IAP付费事件的情况，甲方自己都懵了，我也只能建议作弊者多长点心，刷之前看看产品类型再说。

SDK作弊，常见于安装（安装是一个事件）、伪造广告收入。安装上述已有探讨。这里多提一句，如果你接入了外置network或者mediation的SDK平台，可以设置一步S2S激励回调的验证，识别一些作弊流量。

另外，Appsflyer应该是目前归因后验证数据做的最全面的MMP了，你可以识别归因后的用户行为是否合规。如果产品规模也比较大的客户，可以考虑购买附加的服务。不过需要注意的是，如果发现渠道流量质量有问题需要核减的情况，建议在次月8号之后再去统一核减上个月的流量。这是因为虽然Appsflyer是实时去检查归因后数据的，但是Appsflyer次月8号后，即便检测出之前的流量仍然有问题，也不会体现在PAF报告中了。

此外就是，尽量从S2S走事件，SDK相对不太安全。对于S2S的放作弊，暂时没有什么特别好的方法，只能从风控下手。不过不排除暴力打端口的可能性？

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIBiamm3iaD4Rnbf85NkkUnntG27YK3BEQJqEib9APoIABAiaNOJnGVq2sacg7SAOCw8BavSbLzn8wNuYQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

一个简单的风控+事件上报组合系统逻辑

Bye!

关注我，获取更多广告投放变现知识！

**微信扫一扫赞赏作者**

防作弊 · 目录