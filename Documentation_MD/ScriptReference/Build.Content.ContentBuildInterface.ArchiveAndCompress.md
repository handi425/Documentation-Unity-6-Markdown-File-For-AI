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

#
[ContentBuildInterface](Build.Content.ContentBuildInterface.html).ArchiveAndCompress

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

public static uint ArchiveAndCompress(ResourceFile[] resourceFiles, string
outputBundlePath, [BuildCompression](BuildCompression.html) compression);

## Declaration

public static uint ArchiveAndCompress(ResourceFile[] resourceFiles, string
outputBundlePath, [BuildCompression](BuildCompression.html) compression, bool
stripUnityVersion);

### Parameters

resourceFiles |  Array of [ResourceFile](Build.Content.ResourceFile.html) structs pointing to the files that should be copied into the Archive.   
---|---  
outputBundlePath |  File path of the output Archive file.   
compression |  Type of compression to apply to the content of the Archive.   
stripUnityVersion |  By default the Archive file will record the version of the Unity Editor that created the Archive. When true is passed for this parameter the version will not be recorded in the Archive header. This can be useful when rebuilding AssetBundles after a minor upgrade of the Unity Editor, to make sure otherwise identical AssetBundles generate the exact same full-file content. Note: The CRC and hash values calculated by Unity for AssetBundles ignore the Archive Header. So it is not necessary to strip the Unity Version in the Archive Header when using those for integrity and version tracking.   
  
### Description

Create a Unity archive file, containing the content of one or more resource
files.

Generate a Unity Archive file. This low level API is exposed primarily for use
by the **Scriptable Build Pipeline** package. For example, when building
AssetBundles using
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html) it is
not necessary to call this API because the AssetBundle Archive files are
created automatically.  
  
Additional resources:
[ArchiveFileInterface](Unity.IO.Archive.ArchiveFileInterface.html).

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

