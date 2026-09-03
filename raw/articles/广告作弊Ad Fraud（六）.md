---
title: "广告作弊Ad Fraud（六）"
source: "https://mp.weixin.qq.com/s/RFUG66FnP6lKkVDDCa0GGQ"
author:
  - "[[SimoneLee]]"
published:
created: 2026-09-04
description: "巧设天罗地网，细究安装真假——论Google、Amazon、Apple之防作弊奇术"
tags:
  - "clippings"
---
SimoneLee 出海流量研究僧 *2025年2月24日 09:00*

Hello，大家好。

我是目前研究出海投放&变现业务的SL。

《三方设防巧遮天，诸家妙法辨忠奸》

《金锁银关护正道，秘法奇谋断妄行》

最近重温了《三侠五义》，说话古风古气的，哈哈。

抽空又来更新了，越来越懒了，而且感觉也没得写了，之后可能有空更新一下！最近看了粉丝们的评论区和私信，发现大家在防护验证的知识体系还是缺少一些基本功。除了我们内部自己的平台验证之外，其实不同的应用商店也都提供了一些基础功能帮助我们验证流量。我们可以用起来。对于营销小伙伴了解一些也是很不错的。

所以这期总结一下目前常见的平台都如何配置这些套件和功能，这个功能可以自己做，也可以交给MMP（如果你没有这个精力和资源的话，算是省心省力，没有打广告哦）。

分三个平台讲：Google Apple Amazon

Google License Verification Library（LVL）

Google License Verification Library (LVL) 的主要作用是验证应用的合法授权，以防止未经授权的安装。为了防作弊，Google LVL通过Google Play License Server进行授权验证，应用启动时会调用LVL，请求GP服务器进行授权验证。在GP的服务器返回验证结果（LICENSED、NOT\_LICENSED或ERROR）后，应用会根据验证的结果决定是否允许此次运行。

参考官网文档：

https://developer.android.com/google/play/licensing/server-side-verification

https://developer.android.google.cn/google/play/licensing/client-side-verification.html#app-publishing

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIALf2ezWr0GcKzmcUjlVYibibTiaTkTyu1diaR4g24prVZ5oUDPafpn69haFpyKygffgRb2d8U6qiaPE4w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

为了防止破解或伪造授权信息，LVL采用了以下安全措施：

(1) 响应数据签名

Google Play的服务器返回的授权响应带有数字签名，使用Google私钥加密。作弊渠道无法伪造服务器响应，因为他们无法伪造Google的签名。在本地应用中，LVL 需要用GP提供的公钥验证签名的真实性。

```perl
String signedData = response.getSignedData(); // Google Play 返回的授权数据String signature = response.getSignature();  // Google Play 返回的签名boolean isValid = verifySignature(signedData, signature, PUBLIC_KEY);if (isValid) {    // 授权通过} else {    // 可能是伪造的授权信息，拒绝访问}
```

(2) 随机化验证请求

Google LVL在每次请求时会加入随机数 (nonce)，防止重放攻击（Replay Attack）。这样，即使作弊渠道试图缓存上一次的授权响应并重复使用，系统仍然能检测到。

```cs
long nonce = new SecureRandom().nextLong(); // 生成随机 noncesendLicenseRequest(nonce);
```

(3) 响应内容混淆

Google LVL采用了Base64编码和一定的混淆技术，防止黑客直接篡改授权数据。攻击者不能直接修改响应，否则签名验证会失败。

(4) 代码混淆与安全性增强

ProGuard/R8：LVL推荐使用ProGuard或R8来混淆代码，防止黑客反编译应用并绕过授权验证。

自定义验证逻辑：Google 建议开发者不要直接使用 LVL 提供的默认实现，而是修改和混淆授权逻辑，使得破解难度提高。

除了LVL自带的机制，我还建议开发者结合Google Play Integrity API进行更严格的安全检查。

当然MMP平台也提供了一些简化版本的服务，我们以Appsflyer为例：

广告主需要将配置好的property同步给Appsflyer的CSM。Appsflyer的CSM将会开启测试模式（只标记不检出），如果数据稳定的话，就可以同步到正式版了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIALf2ezWr0GcKzmcUjlVYibib10rjicpM5nMw12ibGE4SPgVhmgjJx7Qb2ZLibLbicACK3e71cNKbJybd3A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

有两个需要注意的点⚠️：

1.Appsflyer需要购买Protect360服务后才能够开启验证。

2.Appsflyer将这类型Fraud标记的原因算作Bots。

参考官网文档：

https://support.appsflyer.com/hc/en-us/articles/17329535522961-Setting-up-the-Google-License-Verification-Library-LVL

Apple App Store install validation

官方说法如下：Apple App Store Install Validation是一种验证iOS应用的安装来源和合法性的机制，主要用于防止盗版、伪造安装、未经授权的运行等情况。它可以确保应用只在 App Store下载和安装，而不是通过越狱设备、第三方商店或企业签名的方式绕过授权。

苹果没有提供SDK，Apple是利用自己的生态完成验证。

主要包括以下三个环节：

（1）Receipt Validation（收据验证）

每个应用都有一个receipt，用于验证应用来源以及是否合法安装，以及是否有合法的内购。该收据包含设备ID、购买信息、Bundle ID等信息，并由Apple签名。我们可以在应用启动时验证收据，确保应用是从Apple下载的，而不是从第三方来源sideload安装的。一般收据会存储在这里：

```swift
/var/mobile/Applications/{App UUID}/StoreKit/sandboxReceipt
```

那么我们就可以用服务器在线验证：

```cpp
import requestsimport base64
# 读取 receipt 文件with open("receipt", "rb") as f:    receipt_data = base64.b64encode(f.read()).decode()
# 发送到 Apple 服务器验证response = requests.post("https://buy.itunes.apple.com/verifyReceipt", json={    "receipt-data": receipt_data,    "password": "your_shared_secret"})
# 解析返回的 JSON 结果print(response.json())
```

(2) App Store Server API（防止假安装 & 内购欺诈）

用于检测应用安装来源，并防止黑客利用伪造安装数据获取奖励（如广告归因作弊）。Apple提供App Store Server API，我们可以使用getTransactionHistory或getRefundHistoryAPI 来检查用户是否真的从应用下载并购买了应用或订阅。这个API不会被篡改，可以有效检测假装安装或伪造支付信息的情况。

(3) Device Integrity Checks（设备完整性检查）

用于检查设备是否越狱（Jailbroken），并检测是否运行在模拟器或被 Hook。

```cs
func isDeviceJailbroken() -> Bool {    let paths = ["/Applications/Cydia.app", "/Library/MobileSubstrate/MobileSubstrate.dylib",                 "/bin/bash", "/usr/sbin/sshd", "/etc/apt"]    for path in paths {        if FileManager.default.fileExists(atPath: path) {            return true        }    }    return false}
```

Amazon Digital Rights Management API

Amazon没有直接对应Google License Verification Library (LVL)的官方SDK，但Amazon提供了Appstore SDK，其中的DRM (Digital Rights Management) API可以实现类似的功能。它允许广告主检查应用是否是通过Amazon Appstore合法下载的，并防止盗版或未经授权的使用。（可以重点防治某家！！！）

首先，我们需要集成Amazon Appstore SDK，在应用中添加 Amazon 提供的Appstore SDK（可从 Amazon Developer Console 下载）。

友情提供链接🔗：

https://developer.amazon.com/zh/docs/appstore-sdk/integrate-appstore-sdk.html

然后在代码中调用DRM API，就可以实现通过LicenseVerifier进行验证了：

```typescript
import com.amazon.device.drm.LicensingService;import com.amazon.device.drm.model.LicenseResponse;import com.amazon.device.drm.LicensingListener;
public class MyActivity extends Activity {    @Override    protected void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        LicensingService.verifyLicense(new LicensingListener() {            @Override            public void onLicenseValidated(LicenseResponse licenseResponse) {                if (licenseResponse.getLicenseStatus() == LicenseResponse.LicenseStatus.LICENSED) {                    // 授权成功                } else {                    // 未授权（盗版、无效账户等）                }            }        });    }}
```

之后把我们的应用已上传到Amazon Appstore，并启用了DRM保护，就完成了全部操作啦。

为了防止破解或伪造授权信息，DRM采用了以下安全措施：

(1) 服务器签名验证

Amazon DRM服务器的响应包含签名数据，并使用Amazon的私钥加密。应用必须用Amazon提供的公钥验证返回数据的真实性，防止伪造授权信息。

(2) 设备绑定&账户验证

DRM授权信息与用户的Amazon账户绑定，而不是仅仅存储在本地设备上。每次验证时，Amazon服务器会检查当前设备是否属于该账户，防止拷贝授权数据到其他设备使用。

\*独有\*

(3) 授权数据加密&反篡改

Amazon DRM SDK会加密存储授权信息，并采用校验机制，防止作弊渠道手动修改本地授权数据。如果检测到数据被篡改，应用可以拒绝运行。

当然，如果要验证IAP的话，也可以用Amazon IAP (In-App Purchasing) 进行二次授权检查，确保购买验证的安全性。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ofNjybZfTIALf2ezWr0GcKzmcUjlVYibibVMlnY3DXSfS7ibYebrOkIyyt0tnCtSQVvDYLnxNZUnC23Ku2dTE904A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

好了，今天的内容就到这里。

Bye!

关注我，获取更多广告投放变现知识！

**微信扫一扫赞赏作者**

防作弊 · 目录