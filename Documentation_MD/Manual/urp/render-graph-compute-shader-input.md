[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/render-graph-compute-shader-input.html)
  * [中文](/cn/current/Manual/urp/render-graph-compute-shader-input.html)
  * [日本語](/ja/current/Manual/urp/render-graph-compute-shader-input.html)
  * [한국어](/kr/current/Manual/urp/render-graph-compute-shader-input.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/render-graph-compute-shader-input.html)
  * [中文](/cn/current/Manual/urp/render-graph-compute-shader-input.html)
  * [日本語](/ja/current/Manual/urp/render-graph-compute-shader-input.html)
  * [한국어](/kr/current/Manual/urp/render-graph-compute-shader-input.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../urp/customizing-urp.html)
  * [Render graph system in URP](../urp/render-graph.html)
  * [Compute shaders in the render graph system in URP](../urp/render-graph-compute-shader.html)
  * Create input data for a compute shader in URP

[](../urp/render-graph-compute-shader-run.html)

Run a compute shader in a render pass in URP

[](../urp/render-graph-view.html)

Analyze a render graph in URP

# Create input data for a compute shader in URP

When you [run a compute shader in a render pass](render-graph-compute-shader-
run.html), you can allocate a buffer to provide input data for the compute
**shader** A program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader).

Follow these steps:

  1. Create a graphics buffer, then add a handle to it in your pass data. For example:
    
        // Declare an input buffer
    public GraphicsBuffer inputBuffer;
    
    // Add a handle to the input buffer in your pass data
    class PassData
    {
        ...
        public BufferHandle input;
    }
    
    // Create the buffer in the render pass constructor
    public ComputePass(ComputeShader computeShader)
    {
        // Create the input buffer as a structured buffer
        // Create the buffer with a length of 5 integers, so you can input 5 values.
        inputBuffer = new GraphicsBuffer(GraphicsBuffer.Target.Structured, 5, sizeof(int));
    }
    

  2. Set the data in the buffer. For example:
    
        var inputValues = new List<int> { 1, 2, 3, 4, 5 };
    inputBuffer.SetData(inputValues);
    

  3. Use the `ImportBuffer` render graph API to convert the buffer to a handle the render graph system can use, then set the `BufferHandle` field in the pass data. For example:
    
        BufferHandle inputHandleRG = renderGraph.ImportBuffer(inputBuffer);
    passData.input = inputHandleRG;
    

  4. Use the `UseBuffer` method to set the buffer as a readable buffer in the render graph system. For example:
    
        builder.UseBuffer(passData.input, AccessFlags.Read);
    

  5. In your `SetRenderFunc` method, use the [`SetComputeBufferParam`](https://docs.unity3d.com/ScriptReference/Rendering.CommandBuffer.SetComputeBufferParam.html) API to attach the buffer to the compute shader. For example:
    
        // The first parameter is the compute shader
    // The second parameter is the function that uses the buffer
    // The third parameter is the RWStructuredBuffer input variable to attach the buffer to
    // The fourth parameter is the handle to the input buffer
    context.cmd.SetComputeBufferParam(passData.computeShader, passData.computeShader.FindKernel("Main"), "inputData", passData.input);
    

## Example

For a full example, refer to the example called **Compute** in the [Universal
Render Pipeline (URP) package samples](package-samples.html).

## Additional resources

  * [Compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
  * [Writing shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)

[](../urp/render-graph-compute-shader-run.html)

Run a compute shader in a render pass in URP

[](../urp/render-graph-view.html)

Analyze a render graph in URP

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

