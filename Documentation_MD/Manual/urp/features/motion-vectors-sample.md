[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/motion-vectors-sample.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-sample.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-sample.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-sample.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/motion-vectors-sample.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-sample.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-sample.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-sample.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Motion vectors in URP](../../urp/features/motion-vectors-landing.html)
  * Sample motion vectors in a shader in URP

[](../../urp/features/motion-vectors-custom-shader.html)

Output a motion vector texture in a custom shader in URP

[](../../urp/features/motion-vectors-troubleshooting.html)

Troubleshooting motion vectors in URP

# Sample motion vectors in a shader in URP

Any `ScriptableRenderPass` implementation can request the motion vector
texture as input. To do that, add the `ScriptableRenderPassInput.Motion` flag
in the
[ScriptableRenderPass.ConfigureInput](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@16.0/api/UnityEngine.Rendering.Universal.ScriptableRenderPass.html#UnityEngine_Rendering_Universal_ScriptableRenderPass_ConfigureInput_UnityEngine_Rendering_Universal_ScriptableRenderPassInput_)
method in the
[AddRenderPasses](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@16.0/api/UnityEngine.Rendering.Universal.ScriptableRendererFeature.html#UnityEngine_Rendering_Universal_ScriptableRendererFeature_AddRenderPasses_UnityEngine_Rendering_Universal_ScriptableRenderer_UnityEngine_Rendering_Universal_RenderingData__)
callback of your custom Renderer Feature. If no other effect in the frame is
using motion vectors, setting this input flag forces the URP renderer to
inject the motion vector render pass into the frame.

To sample the motion vector texture in your **shader** A program that runs on
the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) pass, declare the shader
resource for it in the `HLSLPROGRAM` section:

    
    
        TEXTURE2D_X(_MotionVectorTexture);
        SAMPLER(sampler_MotionVectorTexture);
    

To perform the sampling, use the following macro:

    
    
        SAMPLE_TEXTURE2D_X(_MotionVectorTexture, sampler_MotionVectorTexture, uv);
    

The `_X` postfix ensures that the texture is correctly declared and sampled
when targeting **XR** An umbrella term encompassing Virtual Reality (VR),
Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting
these forms of interactive applications can be referred to as XR devices.
[More info](../../XR.html)  
See in [Glossary](../../Glossary.html#XR) platforms.

[](../../urp/features/motion-vectors-custom-shader.html)

Output a motion vector texture in a custom shader in URP

[](../../urp/features/motion-vectors-troubleshooting.html)

Troubleshooting motion vectors in URP

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

