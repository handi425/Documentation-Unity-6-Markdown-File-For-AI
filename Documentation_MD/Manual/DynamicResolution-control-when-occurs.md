[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/DynamicResolution-control-when-occurs.html)
  * [中文](/cn/current/Manual/DynamicResolution-control-when-occurs.html)
  * [日本語](/ja/current/Manual/DynamicResolution-control-when-occurs.html)
  * [한국어](/kr/current/Manual/DynamicResolution-control-when-occurs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/DynamicResolution-control-when-occurs.html)
  * [中文](/cn/current/Manual/DynamicResolution-control-when-occurs.html)
  * [日本語](/ja/current/Manual/DynamicResolution-control-when-occurs.html)
  * [한국어](/kr/current/Manual/DynamicResolution-control-when-occurs.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Changing resolution scale](resolution-scale.html)
  * [Dynamic Resolution](DynamicResolution-landing.html)
  * Control when Dynamic Scaling happens

[](DynamicResolution-control.html)

Control scaling with Dynamic Resolution

[](DynamicResolution-enable-disable.html)

Enable or disable Dynamic Resolution for render targets

# Control when Dynamic Scaling happens

The `ScalableBufferManager.ResizeBuffers` function immediately scales **render
textures** A special type of Texture that is created and updated at runtime.
To use them, first create a new Render Texture and designate one of your
Cameras to render into it. Then you can use the Render Texture in a Material
just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) when called. However, you can
modify this behavior by using the `DynamicallyScalableExplicit` flag. Render
textures marked with `DynamicallyScalableExplicit` will scale when you call
`RenderTexture.ApplyDynamicScale`, instead of being automatically scaled when
`ScalableBufferManager.ResizeBuffers` is called. Scaling causes render texture
contents to be invalidated, so you must use `DynamicallyScalableExplicit` and
`RenderTexture.ApplyDynamicScale` to ensure render texture data persists
through scale factor changes.

For instance, temporal anti-aliasing improves the visual quality of the
current frame by reusing data from previous frames. If the **dynamic
resolution** A Camera setting that allows you to dynamically scale individual
render targets to reduce workload on the GPU. [More info](DynamicResolution-
landing.html)  
See in [Glossary](Glossary.html#dynamicresolution) scale factor changes
between frames, you need to preserve the previous frame’s data. You can
achieve this by marking the render textures containing this data with
`DynamicallyScalableExplicit`, allowing them to remain valid even after
calling `ScalableBufferManager.ResizeBuffers`. You only need to resize the
current frame’s render texture using `RenderTexture.ApplyDynamicScale`,
ensuring the previous frame’s render texture remains valid for sampling.

[](DynamicResolution-control.html)

Control scaling with Dynamic Resolution

[](DynamicResolution-enable-disable.html)

Enable or disable Dynamic Resolution for render targets

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

