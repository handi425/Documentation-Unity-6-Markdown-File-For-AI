[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
  * [中文](/cn/current/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
  * [中文](/cn/current/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../urp/customizing-urp.html)
  * [Compatibility Mode in URP](../../urp/compatibility-mode.html)
  * Write a Scriptable Render Pass in Compatibility Mode in URP

[](../../urp/compatibility-mode.html)

Compatibility Mode in URP

[](../../urp/renderer-features/how-to-fullscreen-blit.html)

Example of a Scriptable Renderer Feature in Compatibility mode in URP

# Write a Scriptable Render Pass in Compatibility Mode in URP

**Note:** Unity no longer develops or improves the rendering path that doesn’t
use the [render graph API](../render-graph.html). Use the render graph API
instead when developing new graphics features. To use the instructions on this
page, enable **Compatibility Mode (Render Graph Disabled)** in URP graphics
settings (**Project Settings** > **Graphics**).

To create a Scriptable Render Pass in the Universal **Render Pipeline** A
series of operations that take the contents of a Scene, and displays them on a
screen. Unity lets you choose from pre-built render pipelines, or write your
own. [More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (URP), follow these
steps:

  1. Create a C# script that inherits the `ScriptableRenderPass` class. For example:
    
        using UnityEngine.Rendering;
    using UnityEngine.Rendering.Universal;
    
    public class ExampleRenderPass : ScriptableRenderPass
    {
    }
    

  2. In the class, add variables for the materials and textures you use in the render pass.

For example, the following code sets up a handle to a texture, and a
descriptor to configure the texture.

    
        private RTHandle textureHandle;
    private RenderTextureDescriptor textureDescriptor;
    

  3. Override the `Configure` method to set up the render pass. Unity calls this method before executing the render pass.

For example:

    
        public override void Configure(CommandBuffer cmd, RenderTextureDescriptor cameraTextureDescriptor)
    {
        //Set the texture size to be the same as the camera target size.
        textureDescriptor.width = cameraTextureDescriptor.width;
        textureDescriptor.height = cameraTextureDescriptor.height;
    
        //Check if the descriptor has changed, and reallocate the texture handle if necessary.
        RenderingUtils.ReAllocateIfNeeded(ref textureHandle, textureDescriptor);
    }
    

  4. Override the `Execute` method with your rendering commands. Unity calls this method every frame, once for each **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera).

For example:

    
        public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)
    {
        // Get a CommandBuffer from pool
        CommandBuffer cmd = CommandBufferPool.Get();
    
        // Add rendering commands to the CommandBuffer
        ...
    
        // Execute the command buffer and release it back to the pool
        context.ExecuteCommandBuffer(cmd);
        CommandBufferPool.Release(cmd);
    }
    

## Inject a render pass into the render loop

To inject a render pass into the render loop in Compatibility Mode, refer to
the following:

  * [Use the `RenderPipelineManager` API](../customize/inject-render-pass-via-script.html)
  * [Use a Scriptable Renderer Feature](scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)

For a complete example, refer to [Example of a Scriptable Renderer Feature in
Compatibility mode](../renderer-features/how-to-fullscreen-blit.html).

## Additional resources

  * [Custom render pass workflow](../renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [Writing custom shaders in URP](../writing-custom-shaders-urp.html)

[](../../urp/compatibility-mode.html)

Compatibility Mode in URP

[](../../urp/renderer-features/how-to-fullscreen-blit.html)

Example of a Scriptable Renderer Feature in Compatibility mode in URP

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

