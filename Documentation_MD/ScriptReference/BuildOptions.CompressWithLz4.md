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

#  [BuildOptions](BuildOptions.html).CompressWithLz4

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

Use chunk-based LZ4 compression when building the Player.

This value allows content to be stored in a compressed form when the Player is
deployed to a device. Decompression is performed in real time when the Player
reads the data. Scene or Asset loading might be faster or slower depending on
disk read speed when compared to using uncompressed data.  
  
When this flag is passed the player content is stored inside a Unity Archive
file named **data.unity3d**. The build process splits the data into 128KB
chunks and applies LZ4 compression to each chunk. For higher compression the
[BuildOptions.CompressWithLz4HC](BuildOptions.CompressWithLz4HC.html) flag can
be used instead.  
  
This archive file contains the following content:

  1. Player settings - _globalgamemanagers_ and _globalgamemanagers.assets*_ files.
  2. Scenes and referenced Assets - _level*_ and _sharedassets*.asset_ files.
  3. Assets from Resources folders - _resources.assets_ files.
  4. Global Illumination data - GI/level* files.
  5. Built-in resources - _Resources/unity_builtin_extra_ file.

This archive file does not contain the _Resources/unity default resources_
file.  
  
This feature is supported for **Standalone** , **Android** and **iOS** build
targets and is default for **WebGL** target.  
Enabling _CompressWithLz4_ in **Android** might be a significant performance
boost when loading data, as LZ4 decompression is faster than the default Zip
decompression.  
  
**Note:**  
Using chunk-based compression for player data will reduce the size of the
player on the device, while still allowing efficient loading. However chunk-
based compression is typically not as small as full-file compression, and it
will not compress much further if another layer of compression is applied at
packaging time. Hence the game installer might end up a bit larger when using
this flag.  
  
LZ4 compression can also be applied to AssetBundles, see
[BuildAssetBundleOptions.ChunkBasedCompression](BuildAssetBundleOptions.ChunkBasedCompression.html)
and [AssetBundles-Cache](../Manual/AssetBundles-Cache.html).  
  
Additional resources: [ReducingFilesize](../Manual/ReducingFilesize.html),
[ArchiveHandle.Compression](Unity.IO.Archive.ArchiveHandle.Compression.html).

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

