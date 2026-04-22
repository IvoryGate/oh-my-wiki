---
title: "出海投放基础知识之归因（四）SKAN归因"
source: "https://mp.weixin.qq.com/s/F8P70m7tyxvEw_9eRVkmng"
author:
  - "[[SimoneLee]]"
published: 2024-12-03
description: "系统性讲解 SKAN 归因"
tags:
  - "clippings"
---
原创 SimoneLee 出海流量研究僧

 _2024年12月3日 09:01_ _北京_ 听全文

Hello，大家好。

我是目前研究出海投放&变现业务的Simonsen Lee。

  

今天我们继续讲解归因的内容。上周有一位友人想要我系统性讲解一下SKAN。这可是个大工程！最近周六日都在构思这篇文章，我不想解释的像其它文章一样太过笼统，也不想解释过于复杂。为了方便大多数零基础的朋友也能够读懂，我也补充了很多市面上不会讲的背后内容，最后洋洋洒洒就构成了这篇1W字左右的文章。所以这是一篇付费文章，大概付费金额是14元，差不多一杯奶茶钱。

那么话不多说，今天就来讲解一下苹果的SKAdNetwork(StoreKit Ad Network)，简称SKAN，到底是什么？**SKAN是苹果公司为广告归因设计的一部分，集成在其StoreKit框架中，用于帮助广告主衡量广告效果，同时保护用户隐私。**

  

今天文章的内容包括如下部分：

1.StoreKit框架都包含什么？苹果为什么要开发这StoreKit框架？

2.LAT和ATT是什么？

3.SKAN归因原理是什么？（从SKAN3.0讲起）

4.SKAN3.0的局限性和SKAN4.0有什么更新？

5.SKAN4.0的局限性

  

1.StoreKit框架都包含什么？苹果为什么要开发StoreKit框架？

苹果的StoreKit框架是一个用于在应用内实现与App Store和相关服务交互的开发工具包。它支持各种与数字商品和服务相关的功能，包括应用内购买、订阅管理、促销活动等。Storekit框架最主要包括以下两个A和B部分：

A订阅&付费：

- 一次性商品：如虚拟货币、永久解锁功能。
    
- 消耗型商品：可多次购买的商品，如游戏中的体力或虚拟道具。
    
- 非消耗型商品：一次购买即可永久使用的内容，如额外关卡。
    
- 自动续订订阅：如流媒体服务或新闻订阅。
    
- 非续订订阅：如有固定期限的课程或杂志订阅。
    

  

B隐私：SKAdNetwork，用于隐私安全的广告归因，帮助广告主衡量广告效果而不追踪用户行为。  

具体包括哪些内容，大家可以参考Apple的官方文档：

_https://developer.apple.com/documentation/storekit_  

那么苹果为什么开发Storekit框架？

虚假的回答：简化开发者的API适配工作，建立支付系统提供统一的用户支付体验，保障用户隐私安全。

真实的回答：保证苹果的生态政策（确保分成收益），推动苹果生态系统的价值（提升平台营销收入）。  

  

2.LAT和ATT是什么？

要说SKAN归因，就绕不开LAT（Limited Ad Tracking）和ATT（App Tracking Transparency），也就是在<应用追踪透明度>框架下的<限制广告追踪>。

ATT是苹果在 iOS14下推出的框架，旨在帮助用户自主选择是否允许应用追踪他们在其他应用和网站上的活动。ATT 框架下，用户需要主动授权（而不是主动拒绝），广告平台才可获取标识符对用户发送定向广告。只有在用户选择同意追踪时，广告主才能够访问其广告标识符（IDFA）。是否追踪&用户设备上何时显示ATT弹窗则完全取决于应用开发者。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ofNjybZfTIBJwQIxWYCu5Je9T6b80a4I0MEUWJ8JohicibEtgF4OcGnu4iaUNn21ewZLMoLYmhm67Rd7DewOrKXsg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0)

一般建议应用开发者在注册后立即询问用户或者首个应用内广告出现之前ATT弹窗。打开ATT弹窗，对于应用开发者有如下好处：  

1用户授权之后，可以帮助开发者实现确定性归因，评估自己的营销效果。

_⚠️要想实施确定性归因的条件：用户需要同时给UA活动的广告平台下游应用和推广应用同时通过ATT，授权IDFA。__确定性归因和概率性归因都是在现有框架下，由移动营销合作伙伴MMP所提供的服务，即作为一个裁判，衡量归因效果。__如果对目前归因框架和细节不清楚的，可以查看我之前写过的文章：_

[_https://mp.weixin.qq.com/s/N-VFc8S6GiUIF6WMByxkNA?token=1999225179&lang=zh_CN_](https://mp.weixin.qq.com/s?__biz=MzU5MzgzNTQzNQ==&mid=2247483864&idx=1&sn=a4996ff2951357588cb9c1be44044f0b&scene=21#wechat_redirect)

2用户授权之后，帮助开发者衡量用户的后续行为，如果有应用内广告的话，授权IDFA的设备，可以有效提升ARPDAU。

  

理想状况中：用户授不授权ATT都是用户自己的行为。为了保护用户的隐私，我们如何在不使用用户的IDFA（准确性归因）或者IP/User-Agent（概率性归因）的情况下，去做归因呢？同时，为了保证用户隐私，如何让数据的流通环节尽可能的减少呢？  

所以Apple推出了SKAN归因框架。

  

3.SKAN归因原理是什么？（从SKAN3.0讲起）

我们首先来看SKAN框架中归因的参与方都有哪三个：

1.发布方应用A：展示广告的具体应用，如Facebook/Township等具体的app。

2.目标应用B：在广告中被推广的应用，即广告主的应用。

3.广告平台C：连接应用广告主与发布方的平台，如Facebook/Unity等大媒体平台或Ad Network。

  

**很多伙伴会好奇，SKAN框架中，移动营销合作伙伴MMP去哪里了？**

**没错，在SKAN框架中，不需要MMP再去当裁判，Apple自己做了这个工作。****（当裁判过瘾啊）**

那么MMP就没有用处了吗？

实则不然，我们接下来会说明在SKAN框架下，之前的归因平台MMP的“新作用”。

首先看一下SKAN的原理：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIBJwQIxWYCu5Je9T6b80a4IrSz5TbN8yoSicv7rafNLfVjaq5gCDgfOf7mngm7vgrWCINuxvV8xUrA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

我们以一个简单的归因流程为例，带入之前说的三方A、B、C来看新框架下的内容：

1.广告平台C在其下游A应用中展示B应用的广告，展示广告时会附带一个 由苹果发布的SKAN签名，其中包含一条广告标识符（Ad Signature）。如果广告显示3秒以上，发布广告的应用A将通知SKAdNetwork框架，将其标记为一次成功展示。如果用户与广告发生了交互，发布方显示目标应用的StoreKit。StoreKit显示后，SKAdNetwork将其记录为成功渲染。随后用户便可以在App Store中下载该应用。  

2.用户下载并安装应用。首次打开应用时，苹果会通过SKAN签名来验证他们是来自哪一广告系列。

3.首次启动时，应用调用registerAppForAdNetworkAttribution，开始 SKAN的注册流程，并启动24小时的安装计时器。

4.如果计时结束且没有中断，系统向广告平台发送回传信息。如果在此期间发生转化事件，应用调用updateConversionValue，更新转化值并将计时器重置为 24 小时。

5.如果 24小时内没有进一步更新，计时结束。为了隐藏安装时间，SKAN 最多等待 24小时，之后向广告平台和配置好的端点(仅支持iOS15及以上版本)发送回传。该回传包含安装信息但不包括安装时间，同时附带转化值。

6.如果用户在SKAdNetwork的归因窗口平台(通常为 24 小时)内安装并启动应用，安装将被归因于广告，设备将回传信息发送给广告平台，并向广告主发送一份副本。

  

这里面有一些新的概念，也是Apple自己当裁判之后，SKAN制定的新规定：

首先是广告交互类型：

之前的归因模型中，有浏览和点击两种，还包括平台之间争抢利益，所新创建的各种新Engagement Click或者View。

SKAdNetwork重新定义了两种交互类型:

1.浏览。浏览这一行为的定义为广告显示3秒以上，且需要包含广告标识符才是有效浏览行为。

_Apple的标准绝了！之前各种network瞎上报曝光，确实给整个广告生态造成了极大的破坏。但是这也引出了另一个问题：__你知道为什么现在大多平台都要求客户打开View Attribution吗？_

2.StoreKit渲染：指通过StoreKit框架加载和显示App Store产品页面。具体有两个应用场景，如下图所示：

应用内广告点击：用户点击StoreKit广告时，会看到另一个应用的App Store页面，用户可以在不离开当前应用的情况下查看并下载该应用。

App Store链接：在应用设置StoreKit链接打开App Store页面。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ofNjybZfTIBJwQIxWYCu5Je9T6b80a4IqlgLvMKk1lFjJLmoUMqWRYianUG3AyswneFEmJ94GFTK3djVGygXSGA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ofNjybZfTIBJwQIxWYCu5Je9T6b80a4IibXBhY9KZqyyWUSj18TpoS8nKdxn0dwEibwtbic5l4V6jYXHZ8Zgia9Hng/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

  

其次是事件：

在之前的归因场景中：只要你想统计一个用户使用app过程中的所有事件（包括安装激活事件），那么你就可以在MMP的SDK内，埋点所有想要统计的事件，然后我们一个事件对应一个事件ID，那么我们可以统计整个用户的终身LT的所有事件。这个时候，可以理解用户是没有隐私的。

在Apple的新框架下，提出了Conversion value (也就是CV)。

Apple允许开发者最多设置64个想要埋点纪录的事件。为什么是64个事件呢？因为对应计算机中二进制的6Bit的数字。

先来说明一下二进制和十进制的转化：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ofNjybZfTIBJwQIxWYCu5Je9T6b80a4IVMw9w0ESnFPo9HPSENicWicIeTgLfo8m5xNUZRVrJDRlA6YpAELduYHA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

  

其实本质上理解很简单，之前我们一个事件也对应一个事件唯一的标识符，这个用户完成了这个事件，产生一个唯一的事件ID。

现在，我们一个事件依然对应一个事件的唯一标识符（CV），只不过我们限制了可以定义事件的总数为63（因为激活安装为第一个事件），且只告诉广告主这位用户完成了这个事件，不告诉广告主具体的ID去定位到这位用户。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIBJwQIxWYCu5Je9T6b80a4Io8ic1jusI0AdFZ472IKNeGbvYnRkBcvj8OAOupUic9fsAZ4YXDe5Iy8Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

  

之后是计时器：  

Apple在SKAN中新设计了一个计时器功能：

App首次安装时候首先调用registerAppforAdNetworkattribution()，记录一个安装激活；

在第一个调用产生后，应用开发者可以在24小时的循环周期内反复调用第二个updateConversionValue()： 去更新转化数值CV。

如果没有24h内没有新的事件来改变转化值，则纪录这个CV为000000，即为十进制的0，代表安装。如果有，则持续更新CV，直到一个事件在24h之后，再无可以更改CV映射的事件产生。

此方法有两个目的：

1.第一个调用产生一个安装通知,是一个加密签名的数据包,用于验证是否来自广告。

2.第二个调用为设备在检测时间内去尽可能的纪录用户的行为，更新转化数值。每次CV值成功，计时器都会继续延迟下一个24个小时。

确定了最终这个用户的CV之后，Apple又会在最多24小时内把CV值回传给广告平台。也就是说如果这个用户只有安装激活的话，转化值在第一个24h结束第一个计时器，在第二个计时器内，随机时间回传给广告平台。也就是说广告主在24-48小时内收到pb。

在之前的IDFA归因下，我们基本可以接近实时拿到安装和事件。

举个极端例子，如果CV值对应的转换事件设置不恰当，用户每24小时固定产生一个你映射的事件，那么CV一直会从0更新到63，那么你在知道用户安装之后，要在60多天后才拿到这个用户最终的CV值。

我们再举一个例子，帮助大家理解问题：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ofNjybZfTIBJwQIxWYCu5Je9T6b80a4Ig6TVPCc7FW971zMZibSvqxt8R9RuN3KpyKqIiaryM9TGJgb1J988H7YQ/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

  

最后是隐私阈值：

更为糟糕的事，CV值最终是否能够传递给广告主还要看用户的行为是否满足Apple的隐私阈值。

这是阈值具体是什么呢？抱歉，Apple没说，一切都是黑盒。根据我之前的测试数据来看，每天安装数据在200个以上才比较符合。不知道Apple是否又会频繁调整隐私阈值。

如果不符合阈值呢，那Apple会回传的CV值为null。对于新开的广告系列或者效果一般的广告来说，不符合隐私阈值拿到CV值为null的占比高达90%！

  

**说到这里全程没有MMP的关系，那么MMP究竟有什么用呢？**

打个巴掌给个甜枣！

上文我们提到了转化值，这些转化值怎样传给广告平台呢？如何收集所有被归因的广告平台发来的数据回传？广告主可以做到分别与几十家规模各异的广告平台进行对接么？为了要优化广告，就需要将每个转化值代表的意义发给每个广告平台。广告主需要一个对接工作机制已经准备就绪的平台。

MMP之前就与很多广告平台的SDK有了很久的合作与对接。这一点，比Apple要成熟许多。MMP的新作用是负责数据汇总，通过归因和优化应用数据及广告活动表现指标，帮助营销人员实现数据衡量、可视化和优化投放效果。

同时MMP还能够提供一些新功能，比如：

1将CV和事件以及对应的收入映射，方便我们计算ROAS/RR等指标。

2对于回传为null的值做预估，评估渠道的表现。

3延迟回传的用户做收益预估

......

我们以Appsflyer为例，介绍一下MMP加入下，整体的流程是什么样子：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1d15uvuU9HF4ibIjznNQ37IJ0otISjvYrOFoLU4WtqOWYnae5PAZbFwiag/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

在查看了新的思路之后，我们来解释一下MMP有哪些新的优势：

1重构CV值

首先，一个事件按照之前归因模式下，我们需要确认事件的名称、次数、附带的value以及对应的归因窗口期。

现在一个二进制的CV就想要一次性说明清楚这一个事件，实在有些复杂。那么MMP是如何帮助广告主的呢？是**CV映射表！**在Appsflyer的后台，我们有SKAN操作值转化台：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1dE4ocxVP4ZrF5pwBcBNqWRa7knTEu2TLjZbfiaWsNPIxDbsiaqmrk6SLg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

我们以最复杂的IAP收入（因为涉及value）来说：

我们选择“000000”中的红色两位来定义用户的付费金额，按照可能的付费金额，用00代表付费金额<$10,用01代表$10<付费金额<$50，用10代表$50<付费金额<$100，11代表$100<付费金额。

同理，蓝色代表用户行为，用00代表仅安装，用01代表注册，用10代表订阅，用11代表付费。（事件漏斗由浅入深）

那么就会有：000000；000001；000010；000011；000111；001011；001111；这七种CV值，分别对应相应的事件和付费金额（如果有的话）。

同理，我们可以与之前一样，也可以设置该事件的归因窗口期。正如AF的设置一样，这两个计时器同时计时，iOS的优先级更高。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1d2f1fNQjVPicKULiaVd9oGEJGIrceIPzyRFp70llaaaFbLDkyGjcl5NEQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9)

比如，我如上图一样设置事件的计时窗口为12小时，那么：以之前说的001011这个事件为例：

001011转化成十进制就是11，也就是MMP平台设置11这个转化值对应的事件是：用户在安装激活的12h内，产生了漏斗中标记的付费事件，且付费金额为$50-$100之间。

MMP为了方便计算预估的后项ROAS指标，则会使用这个区间的中间值上报，也就是说MMP在后台会将这个事件映射成：一个用户付费了，付费金额为平均值$75，但是没有对应的事件ID。

我们只能根据这条campaign下汇总数据的统计结果，去衡量这条campaign的大概效果。

这里需要注意两点：

1使用MMP，一定要保证给每个平台回传的CV都是统一的。

2.CV映射值调整的时候，在部分平台（比如FB）同步生效需要36-48小时不等，更改CV映射表期间应该暂停广告投放。

2预估CV为null的数值

根据Appsflyer的官方文档来说：

某些情况下，Apple会为了保护用户隐私而不上报确切的转化值（CV），这时CV值即为null。AppsFlyer会将一个null值记为一次激活。

null值和零值的含义不同：零值：用户激活了应用，但未在用户行为窗口期内完成任何可衡量的操作。因此该指标的准确值就是0，这不是由模型推算出来的值。null值：无法获知用户完成了什么操作，因为Apple未上报CV。

null值会使您的效果指标失真。为了克服这类问题，更准确地呈现应用使用情况，我们会将通过推算模型将null值转化为0-63的转化值。

SKAN模型预估：我们会根据带有转化值的SKAN激活分布来推算null值激活的确切转化值。这里使用的算法是动态的，会综合考量多种变量。

假设共有100个激活，其中60个为null值、10个为CV=1、5个为CV=3，还有25个为CV=5。

也就是说，共有40个带有转化值的激活，其中25%的转化值为1，12.5%的转化值为3，还有62.5%的转化值为5。

根据上述分布比例来推算60个转化值为null的激活，可得出以下数据：15个激活的转化值为1，7个激活的转化值为3，38个激活的转化值为5。

该数据会在SKAN面板和API指标中呈现。未经调整的原始数据（即不包含模型推算数据）会与模型推算数据并列呈现，并标记为unmodeled。

可用的数据维度包括：应用、媒体渠道、广告系列和广告组。如果某个维度的推算数据不可用，则相应的值会显示为N/A。

可根据转化值推算的指标包括：revenue/event number/eCPA/ARPU/ROI/ROAS。

3最终SKAN面板样貌

最终的SKAN面板样貌和之前Overview的面板基本一致，区别仅在于大多数数据是预估且没有时效性不如之前。

这里也给一些新的使用SKAN的广告主一些建议：

1用户的行为到底怎么选，映射的CV到底如何设置？  

用户的行为要按照漏斗的机制去排列，保证连续和合理性！这一方面方便营销同学查看数据，另一方面，也方便我们之后去根据我们用户整体的事件和转化率去调整我们CV映射数值。

如果想要尽快评估效果，可以选择用户在24小时内普遍能够完成的行为，使用高位标记收益，低位标记行为，尽快评估广告平台效果。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ofNjybZfTIBJwQIxWYCu5Je9T6b80a4IOrBLvLqG4kuVVG5Rq0wSibRORjTkqJmle2QhqnLB0hXY2Ric0y9hOtGg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10)

2如果用户在第一个24小时内频繁转化，更新CV值，那么我们如何快速衡量广告平台当天的投放效果呢？

除了合理设置CV之外，我们还可以使用MMP的功能来强制回传和预估效果。

强制回传指的就是我将用户事件的窗口期就设置为24h，那么即便有新事件更新CV，那么我也能够在24h内得到一个最深层次漏斗事件。

预估效果，就是合理调整事件的收入value。比如我的用户付费集中在$30-$60之间，那么根据统计学的概率检验原理，在一定的数据量基础和置信区间内，分层越多，这样估算值与实际值之间的偏差越小，最终效果衡量就会好很多。

这里也给大家留了一个问题：SKAN归因从整体角度来说：是一种确定性归因还是概率性归因呢？

  

4.SKAN3.0的局限性和SKAN4.0有什么更新？

前面说了这么多，我们总结一下SKAN3.0的一些局限：

  

1衡量窗口限制为24-48小时:SKAN 在安装后24-48小时内提供归因数据，但缺少时间戳。这使得广告主难以确定用户操作的确切时间，无法及时分析广告表现、调整营销策略。

2广告活动颗粒度有限:SKAN 允许每个应用最多同时投放100组不同的广告系列，这使得广告主难以了解不同广告系列的具体表现和差异，进而进行更细致的区分与分析。

3高比例的null转化值:高比例的null转化值大大降低了广告效果的可见度。营销人员只能获得不完整的数据，难以准确衡量广告支出回报率(ROAS)，深入分析用户的激活后行为。

  

在 2022年的WWDC大会上，苹果发布了SKAN4.0版本。SKAN4.0引入了更长的LTV信号、更细颗粒度的数据，以及网页到应用流量的衡量功能。不过各广告平台目前正处于向SKAN4.0过渡的不同阶段，有些平台尚未完全支持所有新功能。

  

以下是 SKAN 4.0 的关键更新:

  

1 更长的 LTV 衡量窗口（目的：帮助客户获取更多广告系列的转化效果数据）

最长为激活后 35 天:在此前的 SKAN 版本中，广告主只能收到1次回传。而在 SKAN 4.0中，广告主最多可以基于不同的活动窗口收到3次回传(0-2天、3-7天和8-35天)通过这些窗口，广告主可以了解用户在不同阶段进行了哪些交互。需要注意的是，虽然广告主无法将这3次回传对应到特定用户，但可以统计某些事件的发生次数。从最初仅限于第0或第1天的限制性窗口，到长达35 天的衡量窗口，这一变化极大地提升了数据可用性。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1dxmkvZyiaicjLXibP3IzVEiameic2k11BTHWKeldCNywjolWu0bXSuY1llvA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11)

  

我们可以看到：

追踪用户整体的生命流程中使用app的每一步：

前2天内产生第一个事件安装激活，纪录第一个CV；

这个CV在第3天到第四天之间，计时器设定随机时间回传给广告平台。

  

在第3-7天再纪录一个用户漏斗事件，记录为第二个CV；

这个CV在第8天到第13天之间，计时器设定随机时间回传给广告平台。

  

在第8-35天再纪录一个用户漏斗事件，纪录为第三个CV；

这个CV在第36天到第41天之间，计时器设定随机时间回传给广告平台。

  

*我们可以看到计时器在这里的作用是：混淆真实事件发生的时间。

  

所以理想状况下，一个广告系列，会有三次CV的回传。

  

那么如果我的应用，比如是一个超休闲游戏，我用户的整体LT也就5天内，那第三次回调对我来说没有任何用处？  

  

别急，苹果给了另一个新功能：

2 Lock Window（目的：帮助广告主提前锁定用户效果并pb给广告平台）

Apple推出了lockWindow功能，可以在每个窗口的具体时间节点进行锁定。锁定后，窗口时长被缩短至指定节点，框架会确定截至该节点的最新转化值，然后开启回调-返回/归因计时器。例如，如果要监测的所有事件都发生在安装后5天内，就可以在第五天应用锁定并开始随机24-144小时计时器，没有必要等待7天，这样您就节约了两天的时间。不过，在使用 lockWindow功能时，请务必注意"监测空档期"。例如，即便将回调1发送节点锁定在10小时，您也必须等待余下的62小时结束，回调2窗口才会开始。在这62小时中，您无法收到任何SKAN信息。

  

下图直观地展示了回调窗口和回调设置，以及回调2在第5天处的lockWindow锁定。请注意：每个窗口中只能有1个锁定，但每个窗口的锁定节点可以不同。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1d1XLG7ZoxnIwdflAEbgmAV7QBHrqKdS1p9qicWWkGyDtKl5FYMJfiaOwA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12)

  

即然增加了回传CV的次数，那我想多设置一些事件的回传，可以吗？原有的64位CV不太够用了啊！

Okay，苹果同样重新建了一个新功能：

3 重构CV值（目的：避免大量返回null值）

之前SKAN3.0的CV值只有一种，就是0-63位的数值。

现在我们将转化值分为两种：细颗粒度和粗颗粒度转换值。每次我们接收到的转化值是细颗粒度和粗颗粒度的其中一种！

  

**细颗粒度（Fine-Grained Conversion Values）**

细颗粒度仍然是 0 到 63 的数字范围（共 64 个值），可以捕捉用户行为的具体细节，例如用户完成的特定事件、消费金额等。适用于在用户数据足够多、隐私门槛（Privacy Threshold）达标时，为广告主提供精确的归因信息。

**粗颗粒度（Coarse-Grained Conversion Values）**

粗颗粒度值被分为以下三种类型：

高（High）：对应高价值（深度漏斗）的用户行为，例如高价值购买、长时间使用等。

中（Medium）：对应中等价值的用户行为，例如普通的应用内活动或小额消费。

低（Low）：对应低价值行为，例如安装后仅打开应用，或停留在初始界面。

广告主可以预定义不同用户活动对应的粗颗粒度值。  

当系统检测到隐私门槛未达到时，不返回细颗粒度值，而是返回粗颗粒度信息。这样即使不满足SKAN3.0的隐私阈值，也能够获取广告系列的大概效果，比较适合在小规模或新用户群中使用。

  

我们来举一个例子，方便大家理解，假设我们CV映射表包含粗细两种：

细颗粒度转化值映射如下：

CV = 0：仅安装。

CV = 10：完成注册。

CV = 25：首次购买 $10。

CV = 50：消费金额 $50+。

粗颗粒度转化值映射如下：

高（High）：用户完成多次购买或高级行为。

中（Medium）：用户完成教程或一次购买。

低（Low）：用户仅打开应用。

回传示例：

当隐私门槛达标：返回 CV = 25，表示用户消费了 $10。

当隐私门槛未达标：返回 Medium，表示用户进行了中等行为（例如完成教程或小额购买）。

  

我们记得SKAN3.0中的隐私门槛是一个黑盒，那么SKAN4.0中依然是这样吗？有什么更新？苹果在SKAN4.0中做了一次重大调整：

  

4 群组匿名度（目的：更新隐私门槛的指标，帮助客户获得更多信息）

根据一个应用的安装数，Apple 将其划分为 4 种群组匿名性阈值/等级，即Tier 0，Tier 1，Tier 2 和Tier 3，安装次数越少等级越低。而应用所属的级别，决定了Apple回传的数据类型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1dAnc7J157nd5h4s6oFAXbKPTTbYgqmzUYfxba0wSEOaVic2JGBz8L3xg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13)

  

_*一般来说，根据我的经验来看，至少当广告系列中的安装数达到1000左右才能够解锁Tier4等级。_

  

现在我们来看看结合了群组匿名度+粗细颗粒度的数据在三次回传中是如何回传的，请看下图1和图2：

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1dJhojJs4PNbqTWPbcl1xUbE7xwianWzQ7m2xKyUUibf4kbqN3FNa1mmdw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=14)

  

图1 WWDC英文PDF原文解释：

coarse-conversion-vale为粗颗粒度

conversion-value(fine grained)为细颗粒度

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1dBBWh2eRgaiaGqXgnYBMnvmGHbqQwfBxZZoTR4TbxxZUiaybkJHd33kQg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=15)

图二 Google&Appsflyer报告中文翻译

  

本质说的都是同一件事：对于Tier0的广告系列，回传将不包含转化值(即 null 值)。而对于Tier1的广告系列，第1次回传仅包含粗略转化值和2位来源标识符(source identifier)。但是，对于Tier2或Tier3的广告，第1次回传包含细颗粒度转化值和2-4位来源标识符。只有在群组匿名度不为0时，SKAN才会发送第2次和第3次回传，且回传仅包含粗颗粒度转化值和2位来源标识符。

  

很多人可能理解了粗细颗粒度转化值，那source identifier又是什么呢？

5 Source Identifier

SKAN3.0的推广活动ID在SKAN4.0中被重命名为来源ID(source identifier)，且分为不同层级。之前的推广活动ID仅包含两位数字，最多只有100 种组合；但来源ID最多可包含4位数，ID值也提高至最多10000个。广告主可以利用这些数字添加更多推广活动参数 (如地理位置等)，获取更多信息。如下图中英文双语言介绍：

我们以四位的source identifier为例，这个来源ID可以从0000到9999，因此对应10000种可能的数字。我们使用最后两位（个位和十位）数字来作为campaign的编码区；使用百位数字来作为位置的编码区；使用千位数字来作为广告位的编码区。

那么，我们就用1529代表，一个投放在Unity广告平台中激励视频广告位美国区域campaign name为Merge-ROAS-D7的Source Identifier。

怎么样，是不是解释一下，就很好理解了？

与转化值一样，来源ID也受群组匿名度影响。也就是说，群组匿名度等级越高，推广活动能收到的来源ID数位就越多。高匿名度等级能收到所有4位数，中等匿名度能收到3位，而低匿名度只能收到2位来源ID。如下图中英文所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1d8hRX96ttQS96jT9y6ZOWEJMHpICEf9ABVHfpSiaGXnyTTlnibntiboibibw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=16)

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1d4ibK5lgjib6onDdQnicQL7VmxMcV3Q5dgt0zTdJHrLS3URdhqvm6PK7cw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=17)

所以，看到这里，请回头看一下按照匿名度来说，每一次回传，客户都会收到哪种维度的source idnetifier：当应用处于第 0 层和第 1 层时，只能接收到源标识符的最后两位数字。但当进入第 2 层和第 3 层，即安装数量增加时，应用就可以接收源标识符的后 2 位数字或全部数字，具体取决于广告平台。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAicRTAMFsPCUlLSpDBtsD1dZ5c7yFMYvMEORUe71jdjQyLT1z1ldJgYvCLMgUpXmiao4sYia67Ly5jA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=18)

  

5.SKAN4.0的局限性

SKAN4.0的局限性：

尽管SKAN4.0与此前的版本相比有了显著改善，但它依然具有一些其局限性，例如:

1.回传延迟:SKAN4.0回传中的明显延迟导致广告主难以确定用户的具体安装日期。回传延迟最长可达6天，为精准衡量广告效果带来了更大难度。

2.广告主获得的数据颗粒度有限:虽然第1次回传可以包含多达64个转化值，但第2和第3次回传仅包含3个粗略转化值。此外，与第1次回传的4位标识符相比，第2和第3次回传的来源标识符只有2位，大大降低了数据的颗粒度和准确性。

3.难以衡量完整的用户旅程:SKAN 4.0的几次回传是相互独立的，广告主难以将不同的回传关联起来以构成用户旅程的完整链路，当用户旅程涉及在多次交互和转化时，这一问题尤为突出。

MMP能提供什么新功能呢？

说实话，目前我还没有机会尝试过SKAN4.0框架下和MMP合作的流程。所以这一部分暂时不再赘述。大家可以参考MMP各家平台的Help Center查看它们提供的新功能。

谢谢，今天就到这里，希望能够帮助到大家！

  

_部分参考资料来源：_

_Appsflyer SKAN指南：_

_https://support.appsflyer.com/hc/zh-cn/sections/6552135379985_  

_Adjust ATT和SKAN解决方案：_

_https://help.adjust.com/zh/article/ios-att-and-skadnetwork  
_

_Tenjin 帮助中心：_

_https://docs.tenjin.com/docs/introduction-to-skadnetwork_  

稀罕作者

 感谢投喂，一起学习！ 

43 人付费

![头像](https://wx.qlogo.cn/mmopen/ajNVdqHZLLBYcNwC4PLmacDtcQq5XwQmxrMkhln7qDwdWWud5N6FBn7fnmTljAicgia1DGWTKkpZC0pL1cQ9BibKQolku64V4O9pW7aDg3UjsBMnibEQhqKZwr6Wefm8MpaibZtFiagomBGibk/96)![头像](https://wx.qlogo.cn/mmopen/ZO13GCB8FM777kzBh77hp9d00cHy4WibonoMGlJ19EibiaZy6ibHqahZsRrgKZdticQx9xsjPITMQrPK8BLbPCogx82OLoVua9LBIxo5EsPspeDnWu2vJvGXZ7c4SAhlMME7m/132)![头像](https://wx.qlogo.cn/mmopen/PiajxSqBRaELiaVjFVotZeqhlgkbtS73RM4BsibES0tNNGJGU1g5qIvmz3cGduDCdZp90Kbd0Z2SGWseY83DCDFVYn1dUL5SuDMNxkmxb4A2S6a7LKZMxrx2LSkGW5mI3tD/132)![头像](https://wx.qlogo.cn/mmopen/PiajxSqBRaEJQgsd6f8aVjSCtTbAx2mnVIcN7icfeA2w5ibcFHZduhwRmA6hRJJd9EmMLxNBfibLRz0MZFzMBOZsplHwkuTSYYOQyAkaLicPpLaC6Fic6vnfxsr4MAsDPbdibtP/132)![头像](https://wx.qlogo.cn/mmopen/ZO13GCB8FM6WH1PsXQ0PK9ianic3H2njMIAHAMunP5DdeskEuRx2Le7fDLRrDPia4iaYVap31snxeUJL4nG3qAVibicLh0g0l6icyI6gic4XJMEngFf9Y4m6yTUXRN2dj7dEjKWI/132)![头像](https://wx.qlogo.cn/mmopen/N4HWkmwbSVTr6Que7MMTvbBnzkxyibbf3vWiaDicWLvia3EEfNUQPYn5qpJInhKEJJMNP65MEHO5dfuA5nqcYV7hqgF8oIEpXGQt/132)![头像](https://wx.qlogo.cn/mmopen/ajNVdqHZLLDIkkg5KGlepG1ZOBVCsQDBJ2UBCpDuOWziaEiazynlSJeRhQTBT6a2kfmBvIalx5YGM1QHE88iaS7Ag/132)![头像](https://wx.qlogo.cn/mmopen/N4HWkmwbSVTaSeua1JA1lRy2hotMjGRn5zMEdUiczny9P3hc8e3sVDaZjUJQf5lvnfJEe6o5HAIRhszt89MM7h2GK9JicQFha4d7ZiaVZsVqKo2b5sibAM35X6Avictv9YIEI/132)![头像](https://wx.qlogo.cn/mmopen/ZO13GCB8FM44YchUNHQ58u8KZtfpDebwwOTLXa4rGPPK1QVkPKpcg7sXauvJR2KkgNXLo6VdIrNIQsichIoUjhnuicicNnNriblfbVOeqsEIQO1HXeObGibA28Ma0jzq7XK81/132)![头像](https://wx.qlogo.cn/mmopen/PiajxSqBRaEK7BgtKb5qetucgquwknGYvDLicXicJHZ4rfRpIUZOgy50TTVOAuR7FcaTUX77VNGOibpaSkka6ibCHD751ibciaVvR0ozy3tXVBTJAsJzX4oKoIhfbAtUibfXFHb6/132)![头像](https://wx.qlogo.cn/mmopen/pRflFKCOOibPiaAgnjtKVicRKR5n2c15D3ichl1OmmUVIUaiaa4Yl8w5tuMBoDuJtk3e7L8gdbj475uOE7soicqms4rmALAVJLdaPH/132)![头像](https://wx.qlogo.cn/mmopen/PiajxSqBRaELS7NWNOUAGyWzibn2z1QTt5GdibVRzse8tcMwWw7N5NibiadfrVfXUwfK70eKpAak7pOzguFvyDaAia9UUBYlJvk02rahLXF82FjY8NqtD5ia2odmd2DtKOr71J7/132)![头像](https://wx.qlogo.cn/mmopen/PiajxSqBRaELKOLbPeT5wnbicUVzKyqM3ibSfciczBsw2W8kwXzqnUAcPNLpwEY5KicM9hf9DBOSaFqWPicwfRczv5dmjRGjfeKVibYgibTOmIbqiaUl8apE8NNAwWJk5sdfoxyuu/132)![头像](https://wx.qlogo.cn/mmopen/N4HWkmwbSVRyJ6MzpKbIfHLia6XSKMklCHlbONc9AlI2YG6VqDYYTWjlUwKFYKPKBK0prW8Q5XsQAiayrVGpfx0hHm6BOgSMd0dJib6s1GZDIhaZDiaPO3G1BncSToySIopM/132)![头像](https://wx.qlogo.cn/mmopen/N4HWkmwbSVRnlVUbqovmCbFicrQzymTSC6tWxXmIyzU0OSic5CzmprvGyP14Icult3T5KWiauP54SMvalLGMLiahYL08vKthN6LDeTHDzTKPFLtJADCFKldzvwh0dq5XD9C7/132)![头像](https://wx.qlogo.cn/mmopen/FIX1G5ic7B9micbxylU5vQ7oIf3od1Qq1u9A9HxiaDuKslNEs4MNIRwkDkKndbSaibQJU0QWUxXHQuASocURSvttibgzxmAKBYHYek1rGP8BQXCR099I9D1bjvBnMu6vWp8Kia/132)![头像](https://wx.qlogo.cn/mmopen/bAzCbm8W4uGNt2jFoicLic5L8zJCJ5HMQbo6aTe847ibDib0icnWuFrnABJ8vQvJicEMlX6A1U1SQUgku9RfeoUNiaLzJofKnKXYoJA0m8vbIPzubdvABoFIarNiazdRUXMV9cfb/132)![头像](https://wx.qlogo.cn/mmopen/PiajxSqBRaEIemK7dLD6q5tIOibPd9Ug21Xgb3x4jjQia3pIhIvjZppiaySj0ib7ajpNCwuDiaiaHRvC8G8EAkD5v4L1ic5ezntWse6DYiath0OuCp1LNXPiaKqticWLeuFhiaeD1OpZ/132)![头像](https://wx.qlogo.cn/mmopen/N4HWkmwbSVTjicCTGCnXvmkEKo0bFic0ia7aPwDeYIvsWcDVScksHCMq3rJ4WNKuZwLnwgu4QWb9luY8PC6PjhX1594kS044Ply8kjJqCoHmkmLNBBSWRGP2781k5ntiaSAM/132)![头像](https://wx.qlogo.cn/mmopen/PiajxSqBRaEJrPopg2mwOGT2YoY8NsMheTITDCMuDfhIOgyZ9PTibPqFXHa8ibICEAIhnxTCWkGsU5JzN4ASmHwJFZlbnicoAZg4KKWmDcfqfo1b1Cd9YEXre5eiaiaZ2UPREI/132)![头像](https://wx.qlogo.cn/mmopen/ajNVdqHZLLDh1rzxDh2zd5KShyZF6WB3gHX7AMRM3I19tRiaXvhX2JydVicyaTY6AzhH3tPOBhIUVAG6q3Vg8TCw/132)![头像](https://wx.qlogo.cn/mmopen/pRflFKCOOibOH1UbEP0ib3KzXkBvLoEWnDNYfh8pWfqt9wygDBYJHFraE7TR4IGmATIiawiaiauH0B1uxibSYEuRdv6YmEVUCKb1X5olVj6xkcsiczl1pS0OciclILjXXo69dBuV/132)![头像](https://wx.qlogo.cn/mmopen/ZO13GCB8FM5dxNUnGoHjwjOM90G0eFEGoBrJSZ9SgYrsLjajBXD34wQ4PxgX2g53PA1h6f0eiaHRuCt4E1kvxGRIVXD9lDqT2Wd0ztjsOOakvgFAkpA7smYUHZsAuUxS2/132)![头像](https://wx.qlogo.cn/mmopen/ajNVdqHZLLC7b51AWtrofPdF7DR3BQm8ATW0hXZ16lciaIFE0Dy8QE11drAp5yfVOSg6dYlTicU7Kv7jITmktTGYkD6Rm74GYdIcGjFGnLQ8tZw9hesJUza2uXx1DJo5Oy/132)![头像](https://wx.qlogo.cn/mmopen/ZO13GCB8FM4z0UXtWPTkJzEBTt2j82oORG7N10JQFWIx04f0GXDJpJ1YMpvDYHwuSRfamJRSoL4ibtaPcoPpJicHgyP1E69yfIUnbvZwk1rT6DowNFPz9OulVfsXYfZlTj/132)![头像](https://wx.qlogo.cn/mmopen/bAzCbm8W4uElqVLfd1r8OK3ht38QqzlcTsqrmbict31p705B1EUIy6icLOpgYuJqxCibKPMClFibD0ZXicIszqUibPLe9Ztj1K3Q8KnfxMbPmQjj6BZlNOHWpYhYTaxHqyegVz/132)![头像](https://wx.qlogo.cn/mmopen/ZO13GCB8FM5TPzWyyichK02TcmCchKicNRYJvibodn2YDWPx3ErxvwHDicb3OjQRVW1qLz33004Jf16eEDQ8GSKQjBrEfXeIuAwEGzT8vQCkgJ3eDicoCyDBcbvroZba2sic7C/132)![头像](https://wx.qlogo.cn/mmopen/N4HWkmwbSVThlQmvUWOCMNXraN0wWFQIFXb3W5tY4CAzPtULJm49l6oH4QwELGBQwwSx2DDchaNuHOdbhLTZgiaM6mgTL9ZmPD36xgJoFAibQlLEAvsSmc2ncC10KQwBHE/132)![头像](https://wx.qlogo.cn/mmopen/PiajxSqBRaEJv4OKkdJ0LC71Foqeib2cofpTkrX6MwoOfCmVxdiawnXayFZYzmYoGwPFEey8ZmyQIfVryzTLEoHJnYNxunlwppeM9pBv7e772uRMbZmfuWpEtB1I3bUj84l/132)![头像](https://wx.qlogo.cn/mmopen/bAzCbm8W4uEdibzibdPCIicwWBRnspo8Pv43e27WiaD0gia824XOTJg8MVdqxA22joNicOtqwBvbCLZ6MNvOCqaEpDuJI7SOAiboAC9juaiaghicUDEf6Ge54w0GTjg7PVdyS3b06/132)![头像](https://wx.qlogo.cn/mmopen/pRflFKCOOibNp2378XwMicKhsWKV2hueyQLUS32C5ibkkeZhGic9dEEceibwMveArB1rSBicpEXr1CQ7OfWgthL1REnvDavQjudD4g/132)![头像](https://wx.qlogo.cn/mmopen/ZO13GCB8FM5auKcISfnGrlbIbx8dCpnicXmB796xpgV83rKjCL7BL4Vibician74Xcjs9asNU4d4qPZANWb7aTyV7k6vjr2mlzJtaHTSfyjZZvut1ATQGKUiajLHVs0CtAvlO/132)

归因基础知识 · 目录

上一篇出海投放基础知识之归因（三）下一篇再营销Retargeting(一)

​