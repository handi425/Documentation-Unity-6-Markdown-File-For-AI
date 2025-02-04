[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/customize/blit-overview.html)
  * [中文](/cn/current/Manual/urp/customize/blit-overview.html)
  * [日本語](/ja/current/Manual/urp/customize/blit-overview.html)
  * [한국어](/kr/current/Manual/urp/customize/blit-overview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/customize/blit-overview.html)
  * [中文](/cn/current/Manual/urp/customize/blit-overview.html)
  * [日本語](/ja/current/Manual/urp/customize/blit-overview.html)
  * [한국어](/kr/current/Manual/urp/customize/blit-overview.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../urp/customizing-urp.html)
  * Blit in URP

[](../../urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)

Custom render pass workflow in URP

[](../../urp/render-graph.html)

Render graph system in URP

# Blit in URP

To **blit** A shorthand term for “bit block transfer”. A blit operation is the
process of transferring blocks of data from one place in memory to another.  
See in [Glossary](../../Glossary.html#blit) from one texture to another in a
custom render pass in the Universal **Render Pipeline** A series of operations
that take the contents of a Scene, and displays them on a screen. Unity lets
you choose from pre-built render pipelines, or write your own. [More
info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (URP), use the [Blitter
API](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@latest?subfolder=/api/UnityEngine.Rendering.Blitter.html) from
the Core Scriptable Render Pipeline (SRP).

The **shader** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) you use with the `Blitter` API
must be a hand-coded shader. [Shader Graph](../../shader-graph.html) shaders
aren’t compatible with the `Blitter` API.

**Note:** Don’t use the `CommandBuffer.Blit` or `Graphics.Blit` APIs, or APIs
that use them internally such as `RenderingUtils.Blit`. These APIs might break
**XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality
(AR) and Mixed Reality (MR) applications. Devices supporting these forms of
interactive applications can be referred to as XR devices. [More
info](../../XR.html)  
See in [Glossary](../../Glossary.html#XR) rendering, and aren’t compatible
with native render passes.

For example in the `Execute` function in a render pass, add the following:

    
    
    {
        Blitter.BlitCameraTexture(commandBuffer, sourceTexture, destinationTexture, materialToUse, passNumber);
    }
    

For a full example, refer to [Example of a Scriptable Renderer Feature in
Compatibility Mode](../renderer-features/create-custom-renderer-feature.html).

## Additional resources

  * The blit examples in the [URP RenderGraph Samples](../package-sample-urp-package-samples.html)
  * [Custom render pass workflow](../renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [Textures in the Render Graph system](../working-with-textures.html)

[](../../urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)

Custom render pass workflow in URP

[](../../urp/render-graph.html)

Render graph system in URP

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

