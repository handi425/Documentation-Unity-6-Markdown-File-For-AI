[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/DynamicResolution-introduction.html)
  * [中文](/cn/current/Manual/DynamicResolution-introduction.html)
  * [日本語](/ja/current/Manual/DynamicResolution-introduction.html)
  * [한국어](/kr/current/Manual/DynamicResolution-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/DynamicResolution-introduction.html)
  * [中文](/cn/current/Manual/DynamicResolution-introduction.html)
  * [日本語](/ja/current/Manual/DynamicResolution-introduction.html)
  * [한국어](/kr/current/Manual/DynamicResolution-introduction.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Changing resolution scale](resolution-scale.html)
  * [Dynamic Resolution](DynamicResolution-landing.html)
  * Introduction to Dynamic Resolution

[](DynamicResolution-landing.html)

Dynamic Resolution

[](DynamicResolution-control.html)

Control scaling with Dynamic Resolution

# Introduction to Dynamic Resolution

Dynamic resolution is a **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) setting that allows you to dynamically
scale individual render targets, to reduce workload on the GPU. For example,
you can gradually scale down the resolution to maintain a consistent frame
rate. If scaled gradually, **dynamic resolution** A Camera setting that allows
you to dynamically scale individual render targets to reduce workload on the
GPU. [More info](DynamicResolution-landing.html)  
See in [Glossary](Glossary.html#dynamicresolution) can be almost unnoticeable.

## Render pipeline compatibility

Dynamic resolution support depends on which [render pipeline](render-
pipelines.html)A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) your project uses.

**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Built-in Render Pipeline**  
---|---|---|---  
**Dynamic resolution** | Yes (1) | Yes (2) | Yes (1)  
  
**Notes** :

  1. The [Built-in Render Pipeline](built-in-render-pipeline.html), and the [Universal Render Pipeline (URP)](universal-render-pipeline.html) both support dynamic resolution as described in this document.
  2. The [High Definition Render Pipeline (HDRP)](high-definition-render-pipeline.html) supports dynamic resolution, but you enable and use it in a different way. For information on dynamic resolution in HDRP, see [Dynamic resoluton in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Dynamic-Resolution.html).

## Supported platforms

Unity supports dynamic resolution on iOS, macOS and tvOS (Metal only), Android
(Vulkan only), Windows Standalone (DirectX 12 only), and UWP (DirectX 12
only).

## Impact on render targets

With dynamic resolution, Unity does not re-allocate render targets.
Conceptually, Unity scales the render target; however, in reality, Unity uses
aliasing, and the scaled-down render target only uses a small portion of the
original render target. Unity allocates the render targets at their full
resolution, and then the dynamic resolution system scales them down and back
up again, using a portion of the original target instead of re-allocating a
new target.

## Additional resources

  * [FrameTimingManager API reference](../ScriptReference/FrameTimingManager.html)
  * [FrameTimingManager User Manual documentation](frame-timing-manager.html)
  * [ScalableBufferManager API reference](../ScriptReference/ScalableBufferManager.html)
  * [RenderTexture API reference](../ScriptReference/RenderTexture.html)

[](DynamicResolution-landing.html)

Dynamic Resolution

[](DynamicResolution-control.html)

Control scaling with Dynamic Resolution

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

