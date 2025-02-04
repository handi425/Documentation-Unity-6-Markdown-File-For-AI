[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/render-graph-compute-shader-run.html)
  * [中文](/cn/current/Manual/urp/render-graph-compute-shader-run.html)
  * [日本語](/ja/current/Manual/urp/render-graph-compute-shader-run.html)
  * [한국어](/kr/current/Manual/urp/render-graph-compute-shader-run.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/render-graph-compute-shader-run.html)
  * [中文](/cn/current/Manual/urp/render-graph-compute-shader-run.html)
  * [日本語](/ja/current/Manual/urp/render-graph-compute-shader-run.html)
  * [한국어](/kr/current/Manual/urp/render-graph-compute-shader-run.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../urp/customizing-urp.html)
  * [Render graph system in URP](../urp/render-graph.html)
  * [Compute shaders in the render graph system in URP](../urp/render-graph-compute-shader.html)
  * Run a compute shader in a render pass in URP

[](../urp/render-graph-compute-shader.html)

Compute shaders in the render graph system in URP

[](../urp/render-graph-compute-shader-input.html)

Create input data for a compute shader in URP

# Run a compute shader in a render pass in URP

To create a render pass that runs a compute **shader** A program that runs on
the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), do the following:

  1. Set up the render pass to use a compute shader.
  2. Add an output buffer.
  3. Pass in and execute the compute shader.
  4. Get the output data from the output buffer.

To check if a platform supports compute shaders, use the
[`SystemInfo.supportsComputeShaders`](https://docs.unity3d.com/ScriptReference/SystemInfo-
supportsComputeShaders.html) API

## Set up the render pass to use a compute shader

When you [create a `ScriptableRenderPass`](render-graph-write-render-
pass.html), do the following:

  1. Use `AddComputePass` instead of `AddRasterRenderPass`.
  2. Use `ComputeGraphContext` instead of `RasterGraphContext`.

For example:

    
    
    class ComputePass : ScriptableRenderPass
    {
        ...
    
        public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer contextData)
        {
            ...
            // Use AddComputePass instead of AddRasterRenderPass.
            using (var builder = renderGraph.AddComputePass("MyComputePass", out PassData data))
            {
                ...
    
                // Use ComputeGraphContext instead of RasterGraphContext.
                builder.SetRenderFunc((PassData data, ComputeGraphContext context) => ExecutePass(data, context));
    
                ...
            }
        }
    }
    
    

## Add an output buffer

To create a buffer the compute shader outputs to, follow these steps:

  1. Create a graphics buffer, then add a handle to it in your pass data.
    
        // Declare an output buffer
    public GraphicsBuffer outputBuffer;
    
    // Add a handle to the output buffer in your pass data
    class PassData
    {
        public BufferHandle output;
    }
    
    // Create the buffer in the render pass constructor
    public ComputePass(ComputeShader computeShader)
    {
        // Create the output buffer as a structured buffer
        // Create the buffer with a length of 5 integers, so the compute shader can output 5 values.
        outputBuffer = new GraphicsBuffer(GraphicsBuffer.Target.Structured, 5, sizeof(int));
    }
    

  2. Use the `ImportBuffer` render graph API to convert the buffer to a handle the render graph system can use, then set the `BufferHandle` field in the pass data. For example:
    
        BufferHandle outputHandleRG = renderGraph.ImportBuffer(outputBuffer);
    passData.output = outputHandleRG;
    

  3. Use the `UseBuffer` method to set the buffer as a writeable buffer in the render graph system.
    
        builder.UseBuffer(passData.output, AccessFlags.Write);
    

## Pass in and execute the compute shader

Follow these steps:

  1. Pass the compute shader to the render pass. For example, in a `ScriptableRendererFeature` class, expose a `ComputeShader` property, then pass the compute shader into the render pass class.

  2. Add a `ComputeShader` field to your pass data, and set it to the compute shader. For example:
    
        // Add a `ComputeShader` field to your pass data
    class PassData
    {
        ...
        public ComputeShader computeShader;
    }
    
    // Set the `ComputeShader` field to the compute shader
    passData.computeShader = yourComputeShader;
    

  3. In your `SetRenderFunc` method, use the [`SetComputeBufferParam`](https://docs.unity3d.com/ScriptReference/Rendering.CommandBuffer.SetComputeBufferParam.html) API to attach the buffer to the compute shader. For example:
    
        // The first parameter is the compute shader
    // The second parameter is the function that uses the buffer
    // The third parameter is the StructuredBuffer output variable to attach the buffer to
    // The fourth parameter is the handle to the output buffer
    context.cmd.SetComputeBufferParam(passData.computeShader, passData.computeShader.FindKernel("Main"), "outputData", passData.output);
    

  4. Use the [`DispatchCompute`](https://docs.unity3d.com/ScriptReference/Rendering.CommandBuffer.DispatchCompute.html) API to execute the compute shader.
    
        context.cmd.DispatchCompute(passData.computeShader, passData.computeShader.FindKernel("CSMain"), 1, 1, 1);
    

## Get the output data from the output buffer

To fetch the data from the output buffer, use the
[`GraphicsBuffer.GetData`](https://docs.unity3d.com/ScriptReference/GraphicsBuffer.GetData.html)
API.

You can only fetch the data after the render pass executes and the compute
shader finishes running.

For example:

    
    
    // Create an array to store the output data
    outputData = new int[5];
    
    // Copy the output data from the output buffer to the array
    outputBuffer.GetData(outputData);
    

## Example

For a full example, refer to the example called **Compute** in the [render
graph system URP package samples](package-samples.html).

## Additional resources

  * [Compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
  * [Writing shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)

[](../urp/render-graph-compute-shader.html)

Compute shaders in the render graph system in URP

[](../urp/render-graph-compute-shader-input.html)

Create input data for a compute shader in URP

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

