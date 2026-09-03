---
title: "广告作弊Ad Fraud（三）"
source: "https://mp.weixin.qq.com/s/sJHTGT6xZ-OYD9Ql6cSjBw"
author:
  - "[[SimoneLee]]"
published:
created: 2026-09-04
description: "归因劫持，是怎么一回事？"
tags:
  - "clippings"
---
SimoneLee 出海流量研究僧 *2025年1月27日 14:40*

Hello，大家好。

我是目前研究出海投放&变现业务的SL。

上一篇 [文章](https://mp.weixin.qq.com/s?__biz=MzU5MzgzNTQzNQ==&mid=2247484044&idx=1&sn=e16e62ca6d2735db7d7d948e7e1145eb&scene=21#wechat_redirect) ，我们集中讨论了广告作弊的第一大类：虚假安装。今天我们来继续讨论另一种作弊形式：

归因劫持

区别&损失

归因劫持与虚假安装最大的区别就是归因劫持的安装都是真实用户。归因劫持换句话说，就是各家渠道（包括大媒体，也包括小网盟）在MMP设定的规则之间相互博弈的过程中对自己利益最大化的一种手段。

归因劫持对比虚假安装来说，对广告主造成的损失相对较小，毕竟用户都是真实用户。但是，你可能会有两个损失：

（1）本该给A渠道的付款实际上走到了B渠道；如果A/B两个渠道之间的收费CPI相差不多的话，从付费的角度考虑，损失不大；此外，如果劫持的是自然用户，那么本不该付费的自然用户你付款了......冤大头。

（2）不过，这里面还有一个深度的损失：如果A渠道强烈依靠回传去做算法定向用户的话，那劫持量级很大的情况下，A渠道会很难跑起来，甚至会疯狂被MMP拒绝。

分类与识别方法

我们在 [归因基础逻辑](https://mp.weixin.qq.com/s?__biz=MzU5MzgzNTQzNQ==&mid=2247483864&idx=1&sn=a4996ff2951357588cb9c1be44044f0b&scene=21#wechat_redirect) 中，讲过：目前用户与广告的交互类型，依然是“点击”和“浏览”两大类，且MMP遵守的依然是“last click”模型，SRN和non-SRN各自凭借自己的“话语权”有自定义的归因窗口期。

所有的归因劫持都绕不开交互类型、归因模型和归因窗口期这三个点。

我们按照第一篇文章中讲述的逻辑依次讲解“点击”和“浏览”两大类型。

大点击撞库

这类型渠道（渠道下游有很多应用）在接收到我们的单子后，会疯狂地向MMP发送虚假/恶心的点击数据。根据渠道的“能力”大小，可以做如下区分：

弱：我悄悄放一个小的广告位，用户容易误触，那我上报点击也合理嘛！

中：我在一个广告位放置多个广告，前后叠加多条广告，用户点击后，即可上报多个广告的点击，聪明！

强：既然用户也不想看到广告，那我干脆放置一个广告位，我直接广告位透明度设置为100%或者缩小到肉眼看不出来，这样用户根本看不到，只要有正常应用内的点击，我就可以上报点击，嘿嘿！

666盐都不盐了：什么广告位，浪费我的时间，直接默认应用后台运行期间，随机上报点击吧，总有能碰上的，省事！

......

这种类型的渠道，他们劫持的既有可能是其他渠道正常投放的客户，也有可能是本身自然流量带来的用户。这些渠道本身不能够带来任何帮助，所以一定要避免这类型渠道！如果你的产品是榜单产品，放心吧，会被这类渠道盯上的。

监听安装（安卓独有）

这种作弊方式安卓独有，原理是安卓应用的所有APP，都需要配置并依赖系统广播来收听系统广播的信息。那么只要渠道在自己的监听App内创建一个BroadcastReceiver类接收并处理系统广播，并在AndroidManifest.xml中添加额外的权限后，就可以实现收听系统广播（包括接收装置上其他新安装的信息）。

比如你手机中安装了很多奇奇怪怪的产品（常见于VPN/工具/APK包）监听到你正在安装一个新的应用，那么他们就可以在你跳转商店页或者完成下载之前抢时间去给MMP上报一个点击，那根据“Last Click”的归因规则来看，就归因给最近一次的劫持渠道了。

渠道劫持

这里的渠道指的不是广告平台，而是不同的第三方应用商店。在安卓设备上，除三星、华为、小米等各种设备自带的应用商店外，还有数不胜数的第三方应用商店。如果一个应用在每个商店都有上架的话，不排除会有部分应用商店劫持其他渠道安装的可能。

广告主（在A和B两个应用商店平台上都有上架）有一个应用程序想要推广，他在某一个渠道上线了广告计划并设置了跳转到A商店的路径。

此时，有一个用户手机上同时有A和B应用商店，在观看并点击了这个渠道的素材后，点击跳转到的不是A应用商店而是一个落地页，该落地页提示：“应用不安全，建议从应用商店B下载。” 如果此时用户退出落地页，转而去应用商店B里搜索应用并完成下载，则此时B劫持了A。

花样百出：

这里是我目前遇到的部分视频渠道针对目前归因平台逻辑的一些漏洞而开发的“花活”。

1视频广告点击退出按钮，放在犄角旮旯的地方，真的能一次就点准退出吗？

2一个视频广告播放完毕，点击退出还有5秒倒计时才能退出，自己设置规则，视频播放结束就上报点击/视频播放3s上报曝光......为了“抢”到更多归因，让Google也开始整“高互动广告”、MMP开始重新调整归因优先级策略，另一种妥协？

3在一个Banner广告位放置多个广告，美其名曰“推荐应用”，\[还是缺少GDPR铁拳，你有什么权限就能做个性化推荐了，难怪会有周期性的波动？\]，只要用户有一个点击行为在这个广告位的位置（交互框产生），批量上报多个应用的虚假点击。至于跳转商店页的话，点了哪个跳转一下，其余的点击不都是白赚的嘛。

4跑AMZ的流量，有自己的小伎俩。整个中间页就想做业务了吗？Appsflyer的跳转域名加白，你以为是针对谁？

5曝光归因全部开启，首先曝光确实能够带来安装，但是50%以上都来自曝光归因就有点离谱了吧。

6Onelink，有事没事千万别开启Onelink，除非你要跑CTV，不然Onelink概率归因你就受着当冤大头吧。

7......

识别方法：

CVR（Conversion Rate install/click）

大点击渠道特有的指标，CVR极低。一万次点击能有一个安装就不错了。遇到这样的渠道或者子渠道，可以直接关闭或者屏蔽。

ATP（Attribution Type Proportion）

归因交互类型占比，正常CTA：VTA = 8:2。VTA占比过高的请直接关闭对方的VTA归因或者下调归因窗口期为12小时以内。

Two CTIT（Click Time to Install Begin & Install Time）

首先，先上图：这是来自于Appsflyer的raw data数据。你可以自己去后台下载自己应用的数据。这里只是方便我来解释一下概念：

Attribution Touch Type：交互发生的类型，可以利用这个去统计ATP的占比。

Attribution Touch Time：点击/曝光上报的时间

Install Time：安装的时间

Event Time：埋点事件发生的时间，这里事件是安装，所以事件和install time一致

Event Name：埋点事件的名称，安装。（安装也是一种事件）

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykfwmoL5BJY7ic5OYT3c4X387nQYicWahNO7vb04tNZ37SlqGoYQVpf0HtA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

除此以外，如果你的应用是安卓设备，你还可以获取到另外两个重要的时间戳，分别是Google Play Click Time和Google Play Install Begin Time，我喜欢将他们简称为GPCT和GPBT。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykfxKCLzB7H6MOBPJBoUcpSJKsqVJOtatsxQic2YNWOskvGxsCqBRNcNQA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

GP的Click时间和渠道的Click时间之间差值特别小，呈现极端的下降趋势且不能为负数，基本都在1-3s内完成。对于安卓设备来说，很多走referral归因的，这两个时间上报就是一样的，所以我们还需要看CTIT。

Two CTIT：将install begin time和install time分别减去attribution time，得到的就是点击/曝光和安装/安装开始之间的时间差。注意需要修改为number的数字格式并乘以24得到的才是小时数。如果我们要查看相隔的秒数，则需要再乘以两次60转化为秒。正常的点击到安装一定是一条遵守正态分布的曲线。

比如，正常的CTIT曲线是这样子的：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykfyhQqPD6SWCx6Tv4e2ekVWa1ibNQfibMqibS0aibh6zVcROKVtUvy53EOjg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

过短的CTIT曲线，往往意味着安装监听劫持：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykf0OoqWf67pYG7uadE1P9eUYFNBey0Oj7mib99Vbn2xGFwia8xrxtO9nDA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

过长的CTIT曲线，往往意味着大点击撞库或者是一些视频渠道的频繁曝光去撞自然用户：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykfYYfLEibmtFU7GPPyVa7ibdw0mvvPDkYPh0Lm9O3P6QBbPgWicics675adA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

当然，一个渠道既有劫持，又有大点击，也不是不可能：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykfIb2u6Zib3Nu0dbPyDvEKT289EscTVuEicCsKa07ubVFwRHdqzEhQPa0A/640?wx_fmt=png&from=appmsg#imgIndex=5)

另外就是两个CTIT曲线的重合：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykfMyTplShTNonHaHovnfgO8IerEs9HQCntQbQVq6Y6nQWkFynpwUv6ibA/640?wx_fmt=png&from=appmsg#imgIndex=6)

如果两个曲线的分布比例不一致，或者install begin time\<install time，那么一定有问题。

助攻率：这个在之前的文章 [出海投放基础知识之归因（三）](https://mp.weixin.qq.com/s?__biz=MzU5MzgzNTQzNQ==&mid=2247483916&idx=1&sn=48e14de356f9eb135e3c8835dc32fc44&scene=21#wechat_redirect) 有讲述。略过不表，如果你发现渠道有问题，可以关注一下他的助攻率。

关注归因模型占比：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIAd7RVgmZa5dic0SKDibjQFTK6bm9bdrung3cKeMMq5EEz2lCeKopefmndst46TrmbAmwVBc286pDIQ/640?wx_fmt=png&from=appmsg#imgIndex=7)

第一篇文章中，我们讲述了现在Appsflyer的新归因模型，这个功能早就上线了，不知道大家注意到没：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykfeLP0mWkXhiaw9H3SlSo280oyCicw3HaW2vnBJyMsFmruxVJepN1DoKzQ/640?wx_fmt=png&from=appmsg#imgIndex=8)

AF已经在配置页面，更新了归因窗口期的设置，默认都是48h，如果你要更新的话，可以赶快更新。不知道AF是否通知到所有广告主了。

这是有资格上报engaged\_click和engaged\_view的ad network列表（果然没有某家...），如果你觉得有一些渠道VTA比较猖獗，建议直接关闭该渠道的VTA或者将engagement的归因窗口期也缩减。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIDJVYyVSJUsaAH56tfMaykfgZxSV4SamxcyZ2FJq9pSaqYSYicGlQ89ZNPY6L4d2Bl6etC7Q1MCdHw/640?wx_fmt=png&from=appmsg#imgIndex=9)

这是待考核的partner（需要主动联系）：

Jampp

Fluent

AWIN

Rakuten

OPPOPAI Pre-Install

VK Ads (ex. myTarget)

Vivo Preload

OPPO Global

Mistplay

Amazon DSP

Adikteev

Criteo

OPPO

Glance

OPPO Store Traffic(Global)

XiaomiPAI Pre-Install

YouAppi

Yandex Direct

vivo Global

Remerge

adjoe GmbH

Treasure Data

Xiaomi Global

Smadex

Bigo

Motorola Pre-Install

Amazon

Bidease

Yahoo Japan

Kakao

Line

Reddit

Trade Desk

Samsung

Adaction

Adaction3

Stackadapt

Cauly

Naver

Hotstar

Truecaller

Josh

PayTM

Transsion

Huawei

Mintegral

Apple Search Ads

Meta ads

Google Ads (Adwords)

X Ads (formerly Twitter Ads)

Snapchat

ByteDance Ads China

TikTok For Business - Advanced SRN

TikTok for Business - Legacy

Google Marketing Platform (DV360/CM360)

AdColony

Digital Turbine On Device

Digital Turbine

Appreciate

Liftoff

Appnext

AppLovin

ironSource

Moloco

Unity Ads

Tapjoy

Vungle

Kuaishou

Aura from Unity

Tencent AMS

Chartboost

Appier

kwaiforbusiness

Mobupps

Kayzen

InMobi DSP

另外，我们在raw data中也可以筛选engagement\_type的字段，另外在原original\_URL中长这个样子：

https://app.appsflyer.com/XXXXXXX?af\_ua=X&af\_ad\_type=Video&redirect=false&af\_lang=de&advertising\_id=X&is\_lat=false&af\_ref=X&af\_ad=X&af\_siteid=X&af\_adset=X&af\_click\_lookback=7d&clickid=X&af\_engagement\_type=click\_to\_app&af\_ip=X&pid=X&af\_channel=X&c=X&idfa=&af\_c\_id=X&af\_ad\_id=X

综上，就是归因劫持的全部内容。

Bye!

关注我，获取更多广告投放变现知识！

**微信扫一扫赞赏作者**

防作弊 · 目录