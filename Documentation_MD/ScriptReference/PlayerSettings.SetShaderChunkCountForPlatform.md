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

#  [PlayerSettings](PlayerSettings.html).SetShaderChunkCountForPlatform

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

## Declaration

public static void
SetShaderChunkCountForPlatform([BuildTarget](BuildTarget.html) buildTarget,
int chunkCount);

### Parameters

buildTarget | The build target to set the shader chunk count for.  
---|---  
chunkCount | The maximum number of chunks to keep in memory for each shader.  
  
### Description

Sets the default limit on the number of shader variant chunks Unity loads and
keeps in memory on the build target.

To limit the amount of memory Unity uses to [load shader
variants](../Manual/shader-loading.html), you can use
`SetShaderChunkCountForPlatform` to set the maximum number of compressed
shader variant chunks you want Unity to load and decompress into CPU memory at
one time.  
  
This parameter overrides
[PlayerSettings.SetDefaultShaderChunkCount](PlayerSettings.SetDefaultShaderChunkCount.html)
on the build target.  
  
The default value is `0`, which means Unity loads and decompresses all the
chunks into memory.  
  
When Unity reaches the limit but needs to load another chunk, Unity removes
the least recently used decompressed chunk from memory to make room.  
  
Use PlayerSettings.SetDefaultShaderChunkSizeInMBForPlatform to limit the size
of compressed chunks on the build target.  
  
Additional resources:
[PlayerSettings.GetShaderChunkCountForPlatform](PlayerSettings.GetShaderChunkCountForPlatform.html),
[PlayerSettings.SetOverrideShaderChunkSettingsForPlatform](PlayerSettings.SetOverrideShaderChunkSettingsForPlatform.html).

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

