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

# CameraEvent

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

Defines a place in camera's rendering to attach
[CommandBuffer](Rendering.CommandBuffer.html) objects to.

Unity's rendering loop can be extended by adding so called "command buffers"
at various points in camera rendering. For example, you could add some custom
geometry to be drawn right after the skybox is drawn.  
  
Additional resources: [CommandBuffer](Rendering.CommandBuffer.html),
[LightEvent](Rendering.LightEvent.html), [command buffers
overview](../Manual/GraphicsCommandBuffers.html).

### Properties

[BeforeDepthTexture](Rendering.CameraEvent.BeforeDepthTexture.html)| Before
camera's depth texture is generated.  
---|---  
[AfterDepthTexture](Rendering.CameraEvent.AfterDepthTexture.html)| After
camera's depth texture is generated.  
[BeforeDepthNormalsTexture](Rendering.CameraEvent.BeforeDepthNormalsTexture.html)|
Before camera's depth+normals texture is generated.  
[AfterDepthNormalsTexture](Rendering.CameraEvent.AfterDepthNormalsTexture.html)|
After camera's depth+normals texture is generated.  
[BeforeGBuffer](Rendering.CameraEvent.BeforeGBuffer.html)| Before deferred
rendering G-buffer is rendered.  
[AfterGBuffer](Rendering.CameraEvent.AfterGBuffer.html)| After deferred
rendering G-buffer is rendered.  
[BeforeLighting](Rendering.CameraEvent.BeforeLighting.html)| Before lighting
pass in deferred rendering.  
[AfterLighting](Rendering.CameraEvent.AfterLighting.html)| After lighting pass
in deferred rendering.  
[BeforeFinalPass](Rendering.CameraEvent.BeforeFinalPass.html)| Before final
geometry pass in deferred lighting.  
[AfterFinalPass](Rendering.CameraEvent.AfterFinalPass.html)| After final
geometry pass in deferred lighting.  
[BeforeForwardOpaque](Rendering.CameraEvent.BeforeForwardOpaque.html)| Before
opaque objects in forward rendering.  
[AfterForwardOpaque](Rendering.CameraEvent.AfterForwardOpaque.html)| After
opaque objects in forward rendering.  
[BeforeImageEffectsOpaque](Rendering.CameraEvent.BeforeImageEffectsOpaque.html)|
Before image effects that happen between opaque & transparent objects.  
[AfterImageEffectsOpaque](Rendering.CameraEvent.AfterImageEffectsOpaque.html)|
After image effects that happen between opaque & transparent objects.  
[BeforeSkybox](Rendering.CameraEvent.BeforeSkybox.html)| Before skybox is
drawn.  
[AfterSkybox](Rendering.CameraEvent.AfterSkybox.html)| After skybox is drawn.  
[BeforeForwardAlpha](Rendering.CameraEvent.BeforeForwardAlpha.html)| Before
transparent objects in forward rendering.  
[AfterForwardAlpha](Rendering.CameraEvent.AfterForwardAlpha.html)| After
transparent objects in forward rendering.  
[BeforeImageEffects](Rendering.CameraEvent.BeforeImageEffects.html)| Before
image effects.  
[AfterImageEffects](Rendering.CameraEvent.AfterImageEffects.html)| After image
effects.  
[AfterEverything](Rendering.CameraEvent.AfterEverything.html)| After camera
has done rendering everything.  
[BeforeReflections](Rendering.CameraEvent.BeforeReflections.html)| Before
reflections pass in deferred rendering.  
[AfterReflections](Rendering.CameraEvent.AfterReflections.html)| After
reflections pass in deferred rendering.  
[BeforeHaloAndLensFlares](Rendering.CameraEvent.BeforeHaloAndLensFlares.html)|
Before halo and lens flares.  
[AfterHaloAndLensFlares](Rendering.CameraEvent.AfterHaloAndLensFlares.html)|
After halo and lens flares.  
  
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

