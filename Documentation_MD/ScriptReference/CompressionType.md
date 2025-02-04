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

# CompressionType

enumeration

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

Compression Method for Asset Bundles.

When building or recompressing Asset Bundles, these are the available
compression methods. Some of these are only available for building and cannot
be used for recompression.  
  
Additional resources: [AssetBundles compression](../Manual/AssetBundles-
Cache.html),
[AssetBundle.RecompressAssetBundleAsync](AssetBundle.RecompressAssetBundleAsync.html),
[ArchiveHandle.Compression](Unity.IO.Archive.ArchiveHandle.Compression.html).

### Properties

[None](CompressionType.None.html)| Uncompressed Asset Bundles are larger than
compressed Asset Bundles, but they are the fastest to access once downloaded.  
---|---  
[Lzma](CompressionType.Lzma.html)| LZMA compression results in smaller
compressed Asset Bundles but they must be entirely decompressed before use.  
[Lz4](CompressionType.Lz4.html)| LZ4 compression results in larger compressed
files than LZMA, but does not require the entire bundle to be decompressed
before use.  
[Lz4HC](CompressionType.Lz4HC.html)| LZ4HC is a high compression variant of
LZ4. LZ4HC compression results in larger compressed files than LZMA, but does
not require the entire bundle to be decompressed before use.  
  
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

