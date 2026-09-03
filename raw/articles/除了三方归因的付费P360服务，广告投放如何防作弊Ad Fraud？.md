---
title: "除了三方归因的付费P360服务，广告投放如何防作弊Ad Fraud？"
source: "https://mp.weixin.qq.com/s/x_IetJU2EOxLm_wvKY8trQ"
author:
  - "[[SimoneLee]]"
published:
created: 2026-09-04
description: "广告主要不要自建归因？"
tags:
  - "clippings"
---
SimoneLee 出海流量研究僧 *2025年1月7日 10:00*

Hello，大家好。

我是目前研究出海投放&变现业务的SL。

抱歉，有点标题党了，哈哈。这个文章本身是为了回答一位粉丝朋友的问题：广告主要不要自建归因系统？

在回答这个问题的时候，我提到了一些广告主平替MMP防作弊的功能。所以就把这两部分放在一起讲解了。如果大家只想看：除了付费购买P360服务外，还有什么便宜的方法，可以直接拉到文章最后面。

\---

正文开始：

1为什么要自建归因？

2自建归因的好处？

3自建归因的难点？

很多朋友会觉得：目前市面上的三方MMP平台已经有很多了，为什么还要自己搞一套归因平台呢？

目前市面上的归因平台五花八门：从功能较多的Appsflyer、服务完善的Adjust、到价格相对便宜的后起之秀Tenjin、Singular。还有一些擅长防作弊的Kochava、对技术人员友好的Appmetrica以及可以免费使用少量归因、支持按月付费的MyTracker。

1为什么要自建归因？

有这个问题的朋友，其实无外乎有以下几种考量：

1数据隐私，MMP虽说是一个三方公正客观评判的平台，但是不管是Engagement、还是收购参赛选手等行为，MMP平台都收集了大量行业的一手数据。对于广告主，尤其品类头部大客来说，数据泄漏给竞争对手都是最担心的考量。这时候物理隔离，可以实现百分百杜绝后患。

2iOS平台，SKAN3.0框架给MMP打了一个巴掌，SKAN4.0又给了MMP一个甜枣。但是本身归因这个事情已经是苹果自己的活儿了，所以即便规则再复杂，跳出MMP这个事，也就变得更加可行了。很难不去想象安卓端Sandbox隐私沙盒上线后，又会擦出什么样的火花。

3想实现一些更为复杂的功能：包括APK、W2A、PWA等各种花活儿，又苦于MMP的更新频率太慢，所以干脆自己直接上手。

4为了摆脱归因平台制定的霸王规则。目前大家都在Last click的圈子里面玩，但是我们想跳出来，做一套自己的规则，比如有效触点等新的归因方法。其实这个不能算一个合理的理由。一方面，大媒体都是自归因，你搞不搞这一套和他们没什么关系，顶多整整ad network/dsp或者网盟。另一方面，除非自己的预算超级多，不然很多dsp并不会和你玩这个游戏。

5收费过高，其实这一点不应该算一个问题，因为现在市场环境下行，有很多足够便宜的三方平台。即使选择自建归因平台，你也需要考虑自己的技术能不能够承接住这些多进程高并发的技术问题。

2自建归因的好处？

1数据掌控

自建平台能够更好地掌控数据隐私和使用，尤其是在数据合规性要求（如GDPR、CCPA）日益严格的情况下。同时，自建归因有一个额外的好处，就是实时干预投放的效果，通过上报不同的数据，影响ECPM，从而影响量级，并且还能通过挑选流量，影响流量质量，提升投放产出比。

2可扩展性

这就是刚才说的，可以根据自身需求，支持新的媒体渠道或定制化归因模型。

3缩减成本

自建平台的初期投入较高，但之后的长期维护成本可能会低于外部平台服务费用。

3自建归因的难点？

1技术难题

如果我们拥有强大的技术团队和预算支持，搭建归因平台是可行的。现成的开源工具（如PostHog、Snowplow）可以用作基础，但需要定制化开发。一般如果咱们家能够做到RTA竞价且产品又足够多的话，其实可以考虑自建归因平台。

同理还需要考量以下几个问题：

a如何和各家媒体平台对接，达成归因和数据回传延迟较少且数据正确？

b即便自建归因，但是和大媒体的对接依然还要遵守对方的规则。如何在不影响规则的情况下，实现自建模型的归因结果准确呢？

其实一般建议走渠道包，这是最朴素暴力避免归因规则影响的方法。但是不一定会有这么多支持的版本让你做投放。

c如今广告fraud遍布，如何避免fraud？

fraud问题需要特殊关注，毕竟MMP积累了足够多的数据。他们对fraud的防治会有自己专属的方法。看IP、device id、ctit这些小方法可能是最基础的手段，我们如何积累自己的规则呢？

这里插播一下，有一些防作弊的小工具和套件，大家可以撺掇领导在业余时间付费用一用，有的还挺好的，能捕捉到某家dsp花里胡哨的广告形式，也能锤倒一些头部网盟，哈哈。

这里列出了几个名气比较大的：

Fraud Blocker 属于头部产品了

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIB22ibghicCwvIubJ97DAzZRLS4y3rDR2OJrd72Ihy4pzcV6aia1icdLhkn3EDlIiaiaBy4S7A1xTF2YhOg/640?wx_fmt=png&from=appmsg#imgIndex=0)

https://fraudblocker.com/?utm\_source=bofapps

Spider AF 这个在日本比较出名，专攻Affiliate

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIB22ibghicCwvIubJ97DAzZRLImcfhzdc0oeKfTO6HbPl4BjVibia2bSicwVaia4Wr0vy9n2ybhy6w6x6Yw/640?wx_fmt=png&from=appmsg#imgIndex=1)

https://spideraf.com/

mFilterIt 记忆中双印客户特别喜欢用这个，貌似也是一家印度公司。之前有客户靠这个锤倒了一家国内的公司。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIB22ibghicCwvIubJ97DAzZRLNhJWBHmnWsrmBlFbiaXEPByq2sK4tF9ddEjqBHMoAFamSczdMEzYL9g/640?wx_fmt=png&from=appmsg#imgIndex=2)

https://www.mfilterit.com/ad-fraud-detection/

d稳定且强大的数据库

要不直接上云，要不就有足够大的数据库，这个问题无解。

总结：

如果你的公司足够大（不一定是体量，只要是一个垂类的Top级别）且产品足够多，且对大媒体都有一定的话语权，那有必要自建归因平台。否则，没有必要。还是把重心放在产品研发和用户运营上。

我目前想到的几个问题如上，希望能够有所帮助！

Bye！

**微信扫一扫赞赏作者**

广告平台 · 目录