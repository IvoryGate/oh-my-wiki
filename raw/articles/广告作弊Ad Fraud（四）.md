---
title: "广告作弊Ad Fraud（四）"
source: "https://mp.weixin.qq.com/s/seJBg60X2f75QOpJMA2mvw"
author:
  - "[[SimoneLee]]"
published:
created: 2026-09-04
description: "新的一年，继续探索与总结！"
tags:
  - "clippings"
---
SimoneLee 出海流量研究僧 *2025年2月10日 09:00*

Hello，大家好。

我是目前研究出海投放&变现业务的SL。

新年假期没有更新，过年回来周日加急更新一篇文章。

前面的三篇文章我们讲述了基本的fraud概念和检测方法。这些基础概念可以帮助我们日常中培养看数据的敏感程度（比如识别short\_ctit等），理解大多数的作弊方法。但是，在我们的日常工作中其实已经购买了不同的MMP平台SaaS服务。这些MMP平台也提供了不少的防作弊解决工具和套件。我们应该如何合理使用这些平台已有的工具，实现我们自身的防作弊方案呢？

从这篇文章开始，会依次深度讲解每一个归因平台提供的防作弊解决方案。首先从Appsflyer开始，之后会依次介绍Adjust、Singular等比较常见的平台。如果你对其他归因平台也感兴趣，可以留言，我会根据人数多少决定写对应的文章。

本文整体会首先介绍Appsflyer的识别作弊框架，将AF识别的作弊类型依次说明。之后会依次简单介绍Appsflyer提供的最基础且免费的ProtectLITE到付费的Protect360和高阶功能Validation rule、Event rule以及FPS。

Appsflyer的防作弊功能体系

Protect LITE 与 Protect360

Validation & Event rule

Fraud Protection Studio FPS

一、Appsflyer的防作弊功能体系

首先介绍Appsflyer的整体防作弊框架：

Appsflyer有实时检测拦截(real-time)和归因后再检测(post-attribution)两套防作弊组合方案。

实时检测发生在归因判定的环节中，在判定某一次安装是否是虚假安装、渠道是否是正常流量的时候就能够作出判断。对于凭空捏造的安装可以直接认定安装无效且对流量来源的渠道做出“惩罚”，比如24小时内所有上报点击全部判定无效等。对于安装劫持的渠道，也会正确按照归因模型重新判定并记录到正确的渠道上，并将劫持渠道标记助攻。实时检测的数据实时更新。

归因后再检测发生在归因判定环节之后。这时候，归因的结果已经不能修改了。虽然Appsflyer此刻已经完成判定安装的来源任务，但是人无完人，这个结果是真的可信的吗？随着作弊手段的升级，应用内事件作弊的发生，也促使Appsflyer不得不去做后项验证，建立新的模型去判定自己的初次判断是否正确，结合新的后项数据再做流量的甄别。

所以一般被判定为归因后作弊的情况，无外乎两种：逃过了安装捕捉，但是Appsflyer检测到应用内事件作弊 & Appsflyer学习到了新的作弊方式并部署了新模型。归因后再检测的数据每天UTC时区上午10时更新。

我们知道：Appsflyer按照归因激活收费，但是归因后识别的假量不会收费。

一旦该渠道pid或子渠道site\_id(统称为source)被识别到归因后作弊，后续该source的：点击会被拦截过滤、当月的安装会被标记为作弊激活、所有的应用内事件被标记为假量。

Appsflyer的官网提供了常见作弊的检测方法和他们的应对措施，如下图所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwH0YEW4ia2dibWOtyo0BF0Bz5ic7kNcMxu15vZ6KYcNwqB7gCrbmTosLoKQ/640?wx_fmt=png&from=appmsg#imgIndex=0)

这些内容，基本在之前的文章中有讲述，我们今天重点教会大家知道Appsflyer的看板上的字段都是什么意思，如何导出对应的数据和平台掰扯。

我们先不讲看板，因为看板的数据是从底表aggregate制作的，我们直接从Appsflyer提供的raw data底表数据讲起。在Raw Data Report中，如下字段与AF判定的fraud有关(红色的可以不关注)：

| 字段名称 | 解释说明 |
| --- | --- |
| blocked\_reason | 激活(安装)被拦截原因 |
| blocked\_reason\_rule | 已弃用 |
| blocked\_reason\_value | 激活(安装)被拦截的补充说明 |
| blocked\_sub\_reason | 激活(安装)被拦截的子原因 |
| detection\_date | 归因后再检测到作弊时间 |
| fraud\_reason | 同blocked\_reason |
| fraud\_sub\_reason | 同blocked\_sub\_reason |
| is\_organic | 判定为fraud的激活产生的应用内事件是否和自然流量有关 |
| rejected\_reason | 同blocked\_reason/待弃用 |
| rejected\_reason\_value | 归因后识别出的被劫持的激活/应用内事件，显示其真实的有效助攻渠道。可能出现的值为contributor\[1-3\]或者organic。 |

我们详细看一下Blocked Reason和Blocked Sub Reason都包含哪些类型：

Appsflyer提供了四层基础防作弊漏斗，分别是点击、安装、聚类、事件。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwHbUrIxCcO3HzTyjdElrdU8LValPy9I6gvufWjOMZKHo6tboENZziclQg/640?wx_fmt=png&from=appmsg#imgIndex=1)

每一种类型的原因和解释在Appsflyer的帮助中心都有说明，这里放几张截图和我的一些补充说明。

点击：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwH93KicSJVOibxwpnRNr3HCp0Pl8TBQ1EQAxXZbT1BGaaYbrRlWu67V8Mw/640?wx_fmt=png&from=appmsg#imgIndex=2)

（1）ip\_blacklist：Appsflyer的IP第三方服务商是Digital Element，用于动态检测全球IP。（Adjust为Max Mind）

（2）invalid\_fingerprint：概率归因时使用该字段，SDK上报不受影响。

（3）click\_capping：该渠道的一段时间内的作弊率极高，导致Appsflyer全渠道判定24小时内该渠道发送的点击/曝光全部无效。

（4）click\_signing：类似于SKAN的点击签名，取决于ad\_network是否适配，目的是防止冒用渠道。

（5）input\_validation：渠道名称无效，我只见过一次刷apk量换MMP平台报错出现这个错误。

安装（根据之前说的作弊两大类可以分类）：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwHK5gHVZmnMIjycGCCN3OLLgoDMUIicszC2Xic01HsjHVMEFSxncDBLhug/640?wx_fmt=png&from=appmsg#imgIndex=3)

聚类（根据之前说的作弊两大类可以分类）：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwHIWIe262pPQ1uwuQO4aiaFKsgEQ69y6DHcecaiaMxEgIVnwiclTicvcUD7Q/640?wx_fmt=png&from=appmsg#imgIndex=5)

事件：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwHWO80yWsUybowQpCkyiaQRicr4crlQ3vCZbla9jAqQx20y83DRDj5OmXQ/640?wx_fmt=png&from=appmsg#imgIndex=7)

每一类blocked reason都比较细和复杂，长篇大论不适合展开。如果你有问题可以咨询Appsflyer的客户支持，当然也可以咨询我，有时间我会解释你的疑问。

这里补充一个我当时看这个分类时候的困惑，不知道你有没有想过：为什么Appsflyer分四层漏斗？安装和事件我理解可以分为两类，聚类又是个什么鬼东西？它为什么放在安装和事件之间？

Appsflyer提供了四层基础防作弊漏斗，分别是点击、安装、聚类、事件。

不知道大家高中是不是都是学理工的，这个概念其实很像我们在高中物理和数学的傅立叶级数和大学学的信号与系统中讲述的傅立叶变换，信号在时域和频域之间来回转变，给我们切换了另一种视角去看信号。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwHNTia8zOHzLts6At49c1v4K0FBadNtMa5VIm67dnznicBiaricSyaRvUUeQ/640?wx_fmt=png&from=appmsg#imgIndex=8)

安装也是一样，用户从点击->安装->事件其实是一种时间有序的行为，我们当然可以根据这样的逻辑或者在每一个步骤中去穿插规则验证是否是fraud。但是我们换一种视角。将所有的用户行为（你可以理解成将信号分解成无数正弦or余弦函数的叠加）按照时间、行为特征去聚类（这是一个机器学习术语，你可以简单理解为通过制定规则把不同的用户放在一堆）后，他会在另一个维度上分成一堆不同的用户集合。那么与自然流量或者大多数正常安装相比，如果无法在规则内聚类成功（比如两类人完全不一样），则同样可以判定为fraud。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwHqAwUzFfUy0YUIwCp2hUibibicZysJpj5gRV0jjEb964TqbcDWCvYRS3EA/640?wx_fmt=png&from=appmsg#imgIndex=9)

二、Protect LITE 与 Protect360

是什么？

Appsflyer根据客户付费与否，推出了免费的Protect LITE和付费的Protect 360。Protect LITE是一个免费的版本，它提供了基础的实时拒绝激活，没有应用内事件、规则、归因后拒绝。当然付费的Protect 360就能够全部解锁这些功能。

怎么用？

最常见的使用场景就是和平台掰扯核减了。目前很少有平台不认可Appsflyer的核减报告。所以如果你本身应用的体量很大且有充足的预算购买这项服务的话，可以使用这项功能导出PAF的原始报告，与渠道结算的时候核减。（注意要月初8号之后再核减哦！）

其次就是日常运营环节中了：观察不同network之间每天的助攻率波动（之前文章有写）帮助我们查验是否有渠道之间的劫持，同时也建议将自然流量放在同一张chart里面观察趋势。这样的话，对于劫持的自然量的渠道来说会呈现相反且非常直观的趋势。观察同一个network的子渠道分布，有一些明显fraud的子渠道也要block掉。

三、Validation & Event rule

为了满足多需求的广告主，Appsflyer提供了新的功能帮助广告主制定除基础识别方法外的新规则。之所以把他们两放在一起，是因为他们都是广告主自己制定的。

Validation Rule：比如常见的忠实用户定义、自定义的CTIT Gap、特定版本的特殊规则等。

Event Rule：比如用户在整体User journey中绕不开的事件（比如游戏埋一个tutorial的点）、事件顺序（为了防止渠道破解SDK去反刷事件）等。

这两个新功能不与赘述，但是有一个需要注意的点：我个人推荐不要给某些渠道因为特殊原因单独绕过一些规则。

四、Fraud Protection Studio FPS

这个就更和普通的用户没有关系了。这实际上是Appsflyer的一个自定义的防作弊套件。

正常情况下，Appsflyer将流量分成两类：正常和作弊，如红框所示。

切换成这个FPS后，Appsflyer将流量分成两类：正常和作弊，但是判定为作弊的流量可以选择为仅标记or上报。当然，上报的阈值也是由你自定义的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDNjHbyIm2DZdDk9aae1AwHBicqrzcNUUZfbFFD4N05ic5Jmm0ibKic7KjwiaxYr7XI8tSIwiamW4ib0xOHQ/640?wx_fmt=png&from=appmsg#imgIndex=10)

这个功能的推出，我个人猜测🤨觉得可能有两方面原因：

第一是：确实有一部分W2A或者其他可以正常归因流程中经常被识别为作弊的流量需要有新的解决方案推出，因为传统的模型一定会将这部分归因标记就无法给渠道结算了，对于Appsflyer来说，没收到费用也是一笔损失。

第二是：这个有点阴谋论了，有一部分甲乙方确实可以借这个钻空子。纯属猜测哈，无真实证据哈，开个玩笑。

好了，今天的内容就到这里。

Bye!

关注我，获取更多广告投放变现知识！

**微信扫一扫赞赏作者**

防作弊 · 目录