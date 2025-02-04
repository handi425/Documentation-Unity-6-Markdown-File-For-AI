[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetBundles-Integrity.html)
  * [中文](/cn/current/Manual/AssetBundles-Integrity.html)
  * [日本語](/ja/current/Manual/AssetBundles-Integrity.html)
  * [한국어](/kr/current/Manual/AssetBundles-Integrity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetBundles-Integrity.html)
  * [中文](/cn/current/Manual/AssetBundles-Integrity.html)
  * [日本語](/ja/current/Manual/AssetBundles-Integrity.html)
  * [한국어](/kr/current/Manual/AssetBundles-Integrity.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [AssetBundles](AssetBundlesIntro.html)
  * AssetBundle Download Integrity and Security

[](AssetBundles-Troubleshooting.html)

Troubleshooting

[](Build-MultiProcess.html)

Multi-Process AssetBundle Building (Experimental)

# AssetBundle Download Integrity and Security

You can choose to either distribute your AssetBundles with your game or app,
or they can be downloaded from remote servers by your game or app. In the
latter case, when you download AssetBundles, it’s important to take
precautions to prevent AssetBundle data corruption as well as attacks by
malicious actors. A common cause of mysterious crashes on user devices comes
from data corruption in downloaded AssetBundles. Such situations can cost a
large amount of effort and time to diagnose and resolve. And, even though
AssetBundles cannot contain executable code, changing serialized data could
allow an attacker to exploit a vulnerability in the game code or the Unity
runtime.

## Download With a Secure Protocol

[UnityWebRequestAssetBundle](../ScriptReference/Networking.UnityWebRequestAssetBundle.html)
can be used to download and cache AssetBundles from the internet. When using
this API you should use the HTTPS protocol in your URL, unless your URL refers
to a local web server that runs on the same machine. The HTTP protocol is not
secure and is vulnerable to a malicious man in the middle attack.

## CRC Checksums

Unity provides the tools for you to use a checksum to determine that an
AssetBundle is not corrupted or modified when downloading it. A 32-bit
checksum is generated during the AssetBundle build process and recorded in the
.manifest file and exposed by
[BuildPipeline.GetCRCForAssetBundle](../ScriptReference/BuildPipeline.GetCRCForAssetBundle.html).
When you use a CRC check, it ensures the AssetBundle data was not corrupted or
tampered with after it was built. You must provide this CRC when downloading
AssetBundles through `UnityWebRequestAssetBundle.GetAssetBundle` so that
invalid AssetBundles content cannot make it into the cache. See [AssetBundle
compression and caching](AssetBundles-Cache.html) for additional details.

If you download or distribute AssetBundles yourself, and do not use the built-
in AssetBundle Cache, then you should be sure to perform integrity checks
prior to using any content that you have retrieved. One way to do that is to
use the optional parameters on the AssetBundle Load APIs to pass in the
expected CRC value. When provided, the loading system calculates the checksum
of the uncompressed content of the AssetBundle before loading it. If the CRC
of the AssetBundle does not match the provided CRC, the AssetBundle will not
load. For AssetBundles compressed with LZ4 this can be costly because it
forces the file to be fully decompressed into RAM. For LZMA compressed
AssetBundles the load already forces a full content decompression, so
performing the CRC check is not a significant additional cost. Overall it can
be practical to avoid the cost of CRC calculations by performing the integrity
check once, as the file is retrieved and stored on the device, rather than
repeating it at each load.

Note: If you are using AssetBundle **compression** A method of storing data
that reduces the amount of storage space it requires. See [Texture
Compression](class-TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) then you shouldn’t use other
common hash algorithms (such as md5) to validate your AssetBundle files. This
is because Unity sometimes recompresses your AssetBundles even if their
contents didn’t change, which means the file content hash may change in cases
when the contents of the file are actually still valid. In contrast, the CRC
value for an AssetBundle is calculated from its uncompressed content, which
remains constant even when the bundle is recompressed.

Note: the AssetBundle hash that a Unity build calculates and stores inside the
.manifest is not a hash of the AssetBundle’s full file content. It can be used
as a version value for the AssetBundle but is not suitable to use for file
corruption detection.

## User Generated Content

If you allow users to upload content that is distributed to other players
(User Generated Content), it is your responsibility to filter this data for
inappropriate or malicious content. We do not recommend that you let users
build and upload binary AssetBundle files. It is preferable to have your users
upload their source assets and let you, the developer, build the AssetBundle
binary file for them. This will make it easier for you to filter out malicious
or inappropriate content through manual and automated processes. It also
enables you to rebuild the AssetBundles as needed if you upgrade to a later
Unity version.

[](AssetBundles-Troubleshooting.html)

Troubleshooting

[](Build-MultiProcess.html)

Multi-Process AssetBundle Building (Experimental)

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

