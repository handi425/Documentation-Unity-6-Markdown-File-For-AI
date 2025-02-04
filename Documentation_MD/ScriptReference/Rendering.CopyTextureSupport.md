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

# CopyTextureSupport

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

Support for various [Graphics.CopyTexture](Graphics.CopyTexture.html) cases.

Most modern platforms and graphics APIs support quite flexible texture copy
(e.g. copy from a [RenderTexture](RenderTexture.html) into a
[Cubemap](Cubemap.html) face). However some older systems might not support
certain parts of texture copy functionality. This enum indicates support for
this. Use [SystemInfo.copyTextureSupport](SystemInfo-copyTextureSupport.html)
to check for support before calling
[Graphics.CopyTexture](Graphics.CopyTexture.html).  
  
Direct3D 11, Direct3D 12, and Metal platforms generally support flexible
texture copy (all CopyTextureSupport flags are set).  
  
OpenGL supports flexible texture copy since OpenGL 4.3; OpenGL ES supports
flexible texture copy since OpenGL ES 3.1 with Android Extension Pack; on
earlier versions there's no copy support right now
([CopyTextureSupport.None](Rendering.CopyTextureSupport.None.html)).  
  
Direct3D9 systems have somewhat limited texture copy support (can't copy 3D
textures, and can't copy between textures and render textures).  
  
WebGL currently do not have texture copy support
([CopyTextureSupport.None](Rendering.CopyTextureSupport.None.html)).  
  
Additional resources: [Graphics.CopyTexture](Graphics.CopyTexture.html),
[SystemInfo.copyTextureSupport](SystemInfo-copyTextureSupport.html).

### Properties

[None](Rendering.CopyTextureSupport.None.html)| No support for
Graphics.CopyTexture.  
---|---  
[Basic](Rendering.CopyTextureSupport.Basic.html)| Basic Graphics.CopyTexture
support.  
[Copy3D](Rendering.CopyTextureSupport.Copy3D.html)| Support for Texture3D in
Graphics.CopyTexture.  
[DifferentTypes](Rendering.CopyTextureSupport.DifferentTypes.html)| Support
for Graphics.CopyTexture between different texture types.  
[TextureToRT](Rendering.CopyTextureSupport.TextureToRT.html)| Support for
Texture to RenderTexture copies in Graphics.CopyTexture.  
[RTToTexture](Rendering.CopyTextureSupport.RTToTexture.html)| Support for
RenderTexture to Texture copies in Graphics.CopyTexture.  
  
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

