[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/accessing-frame-data.html)
  * [中文](/cn/current/Manual/urp/accessing-frame-data.html)
  * [日本語](/ja/current/Manual/urp/accessing-frame-data.html)
  * [한국어](/kr/current/Manual/urp/accessing-frame-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/accessing-frame-data.html)
  * [中文](/cn/current/Manual/urp/accessing-frame-data.html)
  * [日本語](/ja/current/Manual/urp/accessing-frame-data.html)
  * [한국어](/kr/current/Manual/urp/accessing-frame-data.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../urp/customizing-urp.html)
  * [Render graph system in URP](../urp/render-graph.html)
  * [Frame data in the render graph system in URP](../urp/render-graph-frame-data.html)
  * Get data from the current frame in URP

[](../urp/render-graph-frame-data.html)

Frame data in the render graph system in URP

[](../urp/render-graph-get-previous-frames.html)

Get data from previous frames in URP

# Get data from the current frame in URP

You can fetch the textures that the Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) creates for the
current frame, for example the active color buffer or a G-buffer texture, and
use them in your render passes.

These textures are called frame data, resource data, or frame resources. This
documentation refers to these textures as frame data.

Some textures might not exist in the frame data, depending on which injection
point you use to insert your custom render pass into the URP frame rendering
loop. For more information about which textures exist when, refer to
[Injection points reference](customize/custom-pass-injection-points.html).

## Get frame data

The frame data is in the `ContextContainer` object that URP provides when you
override the `RecordRenderGraph` method.

Follow these steps to get a handle to a texture in the frame data:

  1. Get all the frame data as a `UniversalResourceData` object, using the `Get` method of the `ContextContainer` object.

For example:

    
        public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameContext)
    {
        using (var builder = renderGraph.AddRasterRenderPass<PassData>("Get frame data", out var passData))
        {
            UniversalResourceData frameData = frameContext.Get<UniversalResourceData>();
        }
    }
    

  2. Get the handle to a texture in the frame data.

For example, the following gets a handle to the active color texture:

    
        TextureHandle activeColorTexture = frameData.activeColorTexture;
    

You can then read from and write to the texture. Refer to [Use a texture in a
render pass](render-graph-read-write-texture.html).

The texture handle is valid only for the current render graph in the current
frame.

You can use the
[ConfigureInput](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ScriptableRenderPass.html#UnityEngine_Rendering_Universal_ScriptableRenderPass_ConfigureInput_UnityEngine_Rendering_Universal_ScriptableRenderPassInput_)
API to make sure URP generates the texture you need in the frame data.

## Example

For a full example, refer to the example called **TextureReference w.
FrameData** in the [Universal Render Pipeline (URP) package samples](package-
samples.html).

## Additional resources

  * [Frame data textures reference for URP](render-graph-frame-data-reference.html)
  * [Rendering](rendering-in-universalrp.html)
  * [Render pipeline concepts](urp-concepts.html)
  * [Deferred rendering path in URP](rendering/deferred-rendering-path-landing.html)

[](../urp/render-graph-frame-data.html)

Frame data in the render graph system in URP

[](../urp/render-graph-get-previous-frames.html)

Get data from previous frames in URP

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

