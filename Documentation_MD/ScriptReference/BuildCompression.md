[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# BuildCompression

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Contains information about compression methods, compression levels and block
sizes that are supported by Asset Bundle compression at build time and
recompression at runtime.

The formats that are currently supported are exposed with static properties.
There are three supported BuildCompression types for compressing AssetBundles
during builds (LZ4, LZMA and Uncompressed) and two supported recompression
methods for runtime (LZ4Runtime and UncompressedRuntime).  
  
Additional resources:
[AssetBundle.RecompressAssetBundleAsync](AssetBundle.RecompressAssetBundleAsync.html),
[AssetBundles compression](../Manual/AssetBundles-Cache.html),
[BuildAssetBundleOptions.ChunkBasedCompression](BuildAssetBundleOptions.ChunkBasedCompression.html),
[BuildAssetBundleOptions.UncompressedAssetBundle](BuildAssetBundleOptions.UncompressedAssetBundle.html),
[BuildOptions.CompressWithLz4](BuildOptions.CompressWithLz4.html),
[CompressionType](CompressionType.html), [Caching](Caching.html).

### Static Properties

[LZ4](BuildCompression.LZ4.html)| LZ4HC "Chunk Based" Compression.  
---|---  
[LZ4Runtime](BuildCompression.LZ4Runtime.html)| LZ4 Compression for runtime
recompression.  
[LZMA](BuildCompression.LZMA.html)| LZMA Compression.  
[Uncompressed](BuildCompression.Uncompressed.html)| Uncompressed Asset Bundle.  
[UncompressedRuntime](BuildCompression.UncompressedRuntime.html)| Uncompressed
Asset Bundle.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

