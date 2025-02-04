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

#  [RenderTexture](RenderTexture.html).dimension

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

[Switch to Manual](../Manual/class-RenderTexture.html "Go to RenderTexture
Component in the Manual")

public [Rendering.TextureDimension](Rendering.TextureDimension.html)
dimension;

### Description

Dimensionality (type) of the render texture.

By default render textures are "2D" type, but it is also possible to have
Cubemap or 3D render textures by changing dimension before they are created.  
  
[Cubemap](Cubemap.html) render textures are most often used for dynamic
cubemap reflections, see
[Camera.RenderToCubemap](Camera.RenderToCubemap.html). A cubemap render
texture must have the same [width](RenderTexture-width.html) and
[height](RenderTexture-height.html), and must be power of two size.  
  
3D (volumetric) render textures currently only work on compute shader capable
platforms (like [UsingDX11GL3Features](../Manual/UsingDX11GL3Features.html)).
You can render into them using "random access writes" from a pixel shader or a
compute shader. Use [volumeDepth](RenderTexture-volumeDepth.html) to set 3D
depth, and [enableRandomWrite](RenderTexture-enableRandomWrite.html) to enable
arbitrary writes into it.  
  
Additional resources: [TextureDimension](Rendering.TextureDimension.html).

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

