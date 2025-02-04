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
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html).CreateSkyboxRendererList

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

public [Rendering.RendererList](Rendering.RendererList.html)
CreateSkyboxRendererList([Camera](Camera.html) camera);

## Declaration

public [Rendering.RendererList](Rendering.RendererList.html)
CreateSkyboxRendererList([Camera](Camera.html) camera,
[Matrix4x4](Matrix4x4.html) projectionMatrix, [Matrix4x4](Matrix4x4.html)
viewMatrix);

## Declaration

public [Rendering.RendererList](Rendering.RendererList.html)
CreateSkyboxRendererList([Camera](Camera.html) camera,
[Matrix4x4](Matrix4x4.html) projectionMatrixL, [Matrix4x4](Matrix4x4.html)
viewMatrixL, [Matrix4x4](Matrix4x4.html) projectionMatrixR,
[Matrix4x4](Matrix4x4.html) viewMatrixR);

### Parameters

camera | The camera that is used for rendering the skybox.  
---|---  
projectionMatrix | The projection matrix used during XR rendering of the skybox.  
viewMatrix | The view matrix used during XR rendering of the skybox.  
projectionMatrixL | The left eye projection matrix used during Legacy single pass XR rendering of the skybox.  
viewMatrixL | The left eye view matrix used during Legacy single pass XR rendering of the skybox.  
projectionMatrixR | The right eye projection matrix used during Legacy single pass XR rendering of the skybox.  
viewMatrixR | The right eye view matrix used during Legacy single pass XR rendering of the skybox.  
  
### Returns

**RendererList** Returns a new RendererList based on the settings you pass in.

### Description

Creates a new skybox [RendererList](Rendering.RendererList.html).

A [RendererList](Rendering.RendererList.html) represents a set of draw
commands. To draw the skybox in a RendererList, add the
[CommandBuffer.DrawRendererList](Rendering.CommandBuffer.DrawRendererList.html)
command to a [CommandBuffer](Rendering.CommandBuffer.html).

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

