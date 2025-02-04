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

#  [AssetBundle](AssetBundle.html).RecompressAssetBundleAsync

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

## Declaration

public static
[AssetBundleRecompressOperation](AssetBundleRecompressOperation.html)
RecompressAssetBundleAsync(string inputPath, string outputPath,
[BuildCompression](BuildCompression.html) method, uint expectedCRC,
[ThreadPriority](ThreadPriority.html) priority);

### Parameters

inputPath | Path to the [AssetBundle](AssetBundle.html) to recompress.  
---|---  
outputPath | Path to the recompressed [AssetBundle](AssetBundle.html) to be generated. Can be the same as inputPath.  
method | The compression method, level and blocksize to use during recompression. Only some [BuildCompression](BuildCompression.html) types are supported (see note).  
expectedCRC | CRC of the [AssetBundle](AssetBundle.html) to test against. Testing this requires additional file reading and computation. Pass in 0 to skip this check. Unity does not compute a CRC when the source and destination [BuildCompression](BuildCompression.html) are the same, so no CRC verification takes place (see note).  
priority | The priority at which the recompression operation should run. This sets thread priority during the operation and does not effect the order in which operations are performed. Recompression operations run on a background worker thread.  
  
### Description

Asynchronously recompress a downloaded/stored AssetBundle from one
[BuildCompression](BuildCompression.html) to another.

Method must be a [BuildCompression](BuildCompression.html) whose name ends
with Runtime, for example LZ4Runtime, otherwise an ArgumentException is
thrown. When the destination [BuildCompression](BuildCompression.html) is the
same as the source, this becomes a copy operation internally, and Unity does
not compute a CRC of the uncompressed data. Passing in a non-zero expectedCRC
in this case raises a warning, and no CRC validation takes place.

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

