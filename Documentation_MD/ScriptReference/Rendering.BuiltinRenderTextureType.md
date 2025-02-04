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

# BuiltinRenderTextureType

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

Built-in temporary render textures produced during camera's rendering.

When camera is rendering the Scene, in some cases it can produce temporary
render textures in the process (e.g. depth textures, deferred G-buffer etc.).
This enum indicates these temporary render textures.  
  
BuiltinRenderTextureType can be used as a
[RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html) in some
functions of [CommandBuffer](Rendering.CommandBuffer.html).  
  
Additional resources: [CommandBuffer](Rendering.CommandBuffer.html),
[RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html).

### Properties

[PropertyName](Rendering.BuiltinRenderTextureType.PropertyName.html)| A
globally set property name.  
---|---  
[BufferPtr](Rendering.BuiltinRenderTextureType.BufferPtr.html)| The raw
RenderBuffer pointer to be used.  
[RenderTexture](Rendering.BuiltinRenderTextureType.RenderTexture.html)| The
given RenderTexture.  
[CurrentActive](Rendering.BuiltinRenderTextureType.CurrentActive.html)|
Currently active render target.  
[CameraTarget](Rendering.BuiltinRenderTextureType.CameraTarget.html)| Target
texture of currently rendering camera.  
[Depth](Rendering.BuiltinRenderTextureType.Depth.html)| Camera's depth
texture.  
[DepthNormals](Rendering.BuiltinRenderTextureType.DepthNormals.html)| Camera's
depth+normals texture.  
[ResolvedDepth](Rendering.BuiltinRenderTextureType.ResolvedDepth.html)|
Resolved depth buffer from deferred.  
[GBuffer0](Rendering.BuiltinRenderTextureType.GBuffer0.html)| Deferred shading
G-buffer #0 (typically diffuse color).  
[GBuffer1](Rendering.BuiltinRenderTextureType.GBuffer1.html)| Deferred shading
G-buffer #1 (typically specular + roughness).  
[GBuffer2](Rendering.BuiltinRenderTextureType.GBuffer2.html)| Deferred shading
G-buffer #2 (typically normals).  
[GBuffer3](Rendering.BuiltinRenderTextureType.GBuffer3.html)| Deferred shading
G-buffer #3 (typically emission/lighting).  
[Reflections](Rendering.BuiltinRenderTextureType.Reflections.html)|
Reflections gathered from default reflection and reflections probes.  
[MotionVectors](Rendering.BuiltinRenderTextureType.MotionVectors.html)| Motion
Vectors generated when the camera has motion vectors enabled.  
[GBuffer4](Rendering.BuiltinRenderTextureType.GBuffer4.html)| Deferred shading
G-buffer #4 (typically occlusion mask for static lights if any).  
[GBuffer5](Rendering.BuiltinRenderTextureType.GBuffer5.html)| G-buffer #5
Available.  
[GBuffer6](Rendering.BuiltinRenderTextureType.GBuffer6.html)| G-buffer #6
Available.  
[GBuffer7](Rendering.BuiltinRenderTextureType.GBuffer7.html)| G-buffer #7
Available.  
  
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

