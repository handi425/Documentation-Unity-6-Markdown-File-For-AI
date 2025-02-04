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

# ArchiveFileInterface

class in Unity.IO.Archive

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

Provides methods for managing Unity archive files.

This class offers a low level interface for managing Unity Archive Files.  
  
Once an Archive is mounted its contents can be accessed with
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) or
[ContentLoadInterface.LoadContentFileAsync](Unity.Loading.ContentLoadInterface.LoadContentFileAsync.html).  
  
AssetBundles are an example of an Archive file and can be loaded with this
API. However, typically AssetBundles are loading using the
[AssetBundle](AssetBundle.html) class, or via the Addressables package.  
  
Another example of an Archive file is the `data.unity3d` file generated when
[BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html) is called with
[BuildOptions.CompressWithLz4](BuildOptions.CompressWithLz4.html) or
[BuildOptions.CompressWithLz4HC](BuildOptions.CompressWithLz4HC.html). In that
case this API is not normally needed, because the contents of the Archive are
automatically available in the player.  
  
Additional resources:
[ContentBuildInterface.ArchiveAndCompress](Build.Content.ContentBuildInterface.ArchiveAndCompress.html).

### Static Methods

[GetMountedArchives](Unity.IO.Archive.ArchiveFileInterface.GetMountedArchives.html)|
Retrieves all mounted archives.  
---|---  
[MountAsync](Unity.IO.Archive.ArchiveFileInterface.MountAsync.html)| Loads all
files in an archive to a mount point.  
  
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

