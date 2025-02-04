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

**Method group is Obsolete**  

#
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html).DrawRenderers

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

**Obsolete** DrawRenderers is obsolete and replaced with the RendererList API:
construct a RendererList using ScriptableRenderContext.CreateRendererList and
execture it using CommandBuffer.DrawRendererList.

## Declaration

public void
DrawRenderers([Rendering.CullingResults](Rendering.CullingResults.html)
cullingResults, ref
[Rendering.DrawingSettings](Rendering.DrawingSettings.html) drawingSettings,
ref [Rendering.FilteringSettings](Rendering.FilteringSettings.html)
filteringSettings);

**Obsolete** DrawRenderers is obsolete and replaced with the RendererList API:
construct a RendererList using ScriptableRenderContext.CreateRendererList and
execture it using CommandBuffer.DrawRendererList.

## Declaration

public void
DrawRenderers([Rendering.CullingResults](Rendering.CullingResults.html)
cullingResults, ref
[Rendering.DrawingSettings](Rendering.DrawingSettings.html) drawingSettings,
ref [Rendering.FilteringSettings](Rendering.FilteringSettings.html)
filteringSettings, ref
[Rendering.RenderStateBlock](Rendering.RenderStateBlock.html) stateBlock);

**Obsolete** DrawRenderers is obsolete and replaced with the RendererList API:
construct a RendererList using ScriptableRenderContext.CreateRendererList and
execture it using CommandBuffer.DrawRendererList.

## Declaration

public void
DrawRenderers([Rendering.CullingResults](Rendering.CullingResults.html)
cullingResults, ref
[Rendering.DrawingSettings](Rendering.DrawingSettings.html) drawingSettings,
ref [Rendering.FilteringSettings](Rendering.FilteringSettings.html)
filteringSettings, NativeArray<ShaderTagId> renderTypes,
NativeArray<RenderStateBlock> stateBlocks);

**Obsolete** DrawRenderers is obsolete and replaced with the RendererList API:
construct a RendererList using ScriptableRenderContext.CreateRendererList and
execture it using CommandBuffer.DrawRendererList.

## Declaration

public void
DrawRenderers([Rendering.CullingResults](Rendering.CullingResults.html)
cullingResults, ref
[Rendering.DrawingSettings](Rendering.DrawingSettings.html) drawingSettings,
ref [Rendering.FilteringSettings](Rendering.FilteringSettings.html)
filteringSettings, [Rendering.ShaderTagId](Rendering.ShaderTagId.html)
tagName, bool isPassTagName, NativeArray<ShaderTagId> tagValues,
NativeArray<RenderStateBlock> stateBlocks);

### Parameters

cullingResults | The set of visible objects to draw. You typically obtain this from [ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html).  
---|---  
drawingSettings | A struct that describes how to draw the objects.  
filteringSettings | A struct that describes how to filter the set of visible objects, so that Unity only draws a subset.  
stateBlock | A set of values that Unity uses to override the GPU's render state.  
tagName | The name of a [SubShader Tag](../Manual/SL-SubShaderTags.html) or [Pass Tag](../Manual/SL-PassTags.html).  
isPassTagName | If set to true, `tagName` specifies a [Pass Tag](../Manual/SL-PassTags.html). Otherwise, `tagName` specifies a [SubShader Tag](../Manual/SL-SubShaderTags.html).  
tagValues | An array of [ShaderTagId](Rendering.ShaderTagId.html) structs, where the [name](Rendering.ShaderTagId-name.html) is the value of a given [SubShader Tag](../Manual/SL-SubShaderTags.html) or [Pass Tag](../Manual/SL-PassTags.html).  
renderTypes | An array of [ShaderTagId](Rendering.ShaderTagId.html) structs, where the [name](Rendering.ShaderTagId-name.html) is the value of a [SubShader Tag](../Manual/SL-SubShaderTags.html) that has the name "RenderType".  
stateBlocks | An array of structs that describe which parts of the GPU's render state to override.  
  
### Description

Schedules the drawing of a set of visible objects, and optionally overrides
the GPU's render state.

This function creates commands to draw the specified geometry, and adds the
commands to the internal command list of the `ScriptableRenderContext`. The
`ScriptableRenderContext` executes all the commands in its internal list when
[ScriptableRenderContext.Submit](Rendering.ScriptableRenderContext.Submit.html)
is called.  
  
This example demonstrates using a
[CommandBuffer](Rendering.CommandBuffer.html) to set clear the render target,
and then calling this function to draw geometry:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleRenderPipeline : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public ExampleRenderPipeline()
        {
        }  
      
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html)[] cameras)
        {
            // Create and schedule a command to clear the current render target
            var cmd = new [CommandBuffer](Rendering.CommandBuffer.html)();
            cmd.ClearRenderTarget(true, true, [Color.black](Color-black.html));
            context.ExecuteCommandBuffer(cmd);
            cmd.Release();  
      
            // Iterate over all Cameras
            foreach ([Camera](Camera.html) camera in cameras)
            {
                // Get the culling parameters from the current [Camera](Camera.html)
                camera.TryGetCullingParameters(out var cullingParameters);  
      
                // Use the culling parameters to perform a cull operation, and store the results
                var cullingResults = context.Cull(ref cullingParameters);  
      
                // [Update](PlayerLoop.Update.html) the value of built-in shader variables, based on the current [Camera](Camera.html)
                context.SetupCameraProperties(camera);  
      
                // Tell Unity which geometry to draw, based on its [LightMode](Experimental.GlobalIllumination.LightMode.html) [Pass](ShaderData.Pass.html) tag value
                [ShaderTagId](Rendering.ShaderTagId.html) shaderTagId = new [ShaderTagId](Rendering.ShaderTagId.html)("ExampleLightModeTag");  
      
                // Tell Unity how to sort the geometry, based on the current [Camera](Camera.html)
                var sortingSettings = new [SortingSettings](Rendering.SortingSettings.html)(camera);  
      
                // Create a [DrawingSettings](Rendering.DrawingSettings.html) struct that describes which geometry to draw and how to draw it
                [DrawingSettings](Rendering.DrawingSettings.html) drawingSettings = new [DrawingSettings](Rendering.DrawingSettings.html)(shaderTagId, sortingSettings);  
      
                // Tell Unity how to filter the culling results, to further specify which geometry to draw
                // Use [FilteringSettings.defaultValue](Rendering.FilteringSettings-defaultValue.html) to specify no filtering
                [FilteringSettings](Rendering.FilteringSettings.html) filteringSettings = [FilteringSettings.defaultValue](Rendering.FilteringSettings-defaultValue.html);  
      
                // Schedule a command to draw the geometry, based on the settings you have defined
                context.DrawRenderers(cullingResults, ref drawingSettings, ref filteringSettings);  
      
                // Schedule a command to draw the [Skybox](Skybox.html) if required
                if (camera.clearFlags == [CameraClearFlags.Skybox](CameraClearFlags.Skybox.html) && [RenderSettings.skybox](RenderSettings-skybox.html) != null)
                {
                    context.DrawSkybox(camera);
                }  
      
                // Instruct the graphics API to perform all scheduled commands
                context.Submit();
            }
        }
    }
    

**Overriding the render state**  
  
When you draw geometry using this function, you can use one or more
[RenderStateBlock](Rendering.RenderStateBlock.html) structs to override the
GPU's render state in the following ways:

  * You can use the `stateBlock` parameter to provide a single [RenderStateBlock](Rendering.RenderStateBlock.html) struct. Unity uses the render state defined in `stateBlock` for all the geometry that this function draws.
  * You can use the `stateBlocks` parameter to provide an array of [RenderStateBlock](Rendering.RenderStateBlock.html) structs, and the `renderTypes` parameter to provide an array of values for the [SubShader Tag](../Manual/SL-SubShaderTags.html) with a name of `RenderType`. For each element in the `renderTypes` array, if Unity finds geometry with a SubShader Tag name of `RenderType` and a matching value, it uses the render state defined in the corresponding element of the `stateBlocks` array. If there are multiple matches, Unity uses the first one. If an element in the `renderTypes` array has the default value for [ShaderTagId](Rendering.ShaderTagId.html), Unity treats this as a catch-all and uses the corresponding render state for all geometry.
  * You can use the `stateBlocks` parameter to provide an array of [RenderStateBlock](Rendering.RenderStateBlock.html) structs, and use the `tagName`, `tagValues`, and `isPassTagName` parameters to specify the name and values of any [SubShader Tag](../Manual/SL-SubShaderTags.html) or [Pass Tag](../Manual/SL-SubShaderTags.html). For each element in the `tagNames` and `tagValues` arrays, Unity identifies geometry with a matching SubShader Tag or Pass Tag name and value, and applies the render state defined in the corresponding element of the `stateBlocks` array. If there are multiple matches, Unity uses the first one. If an element in the `tagValues` has the default value for [ShaderTagId](Rendering.ShaderTagId.html), Unity treats this as a catch-all and uses the corresponding render state for all geometry.

This example demonstrates how to override the render state:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using Unity.Collections;  
      
    public class OverrideRenderStateExample
    {
        [ScriptableRenderContext](Rendering.ScriptableRenderContext.html) scriptableRenderContext;  
      
        // Override the render state for all geometry that this function draws
        public void OverrideRenderStateForAll([CullingResults](Rendering.CullingResults.html) exampleCullingResults, [DrawingSettings](Rendering.DrawingSettings.html) exampleDrawingSettings, [FilteringSettings](Rendering.FilteringSettings.html) exampleFilteringSettings)
        {
            // Tell Unity how to override the render state
            var stateBlock = new [RenderStateBlock](Rendering.RenderStateBlock.html)([RenderStateMask.Depth](Rendering.RenderStateMask.Depth.html));
            stateBlock.depthState = new [DepthState](Rendering.DepthState.html)(true, [CompareFunction.LessEqual](Rendering.CompareFunction.LessEqual.html));  
      
            // Schedule a command to draw the geometry using the desired render state
            // Unity will execute all scheduled commands during the next call to [ScriptableRenderContext.Submit](Rendering.ScriptableRenderContext.Submit.html)
            scriptableRenderContext.DrawRenderers(exampleCullingResults, ref exampleDrawingSettings, ref exampleFilteringSettings, ref stateBlock);
        }  
      
        // Override the render state for all geometry that has a SubShader Tag
        // with a name of "RenderType" and a value of "ExampleRenderTypeTagValue"
        public void OverrideRenderStateUsingRenderTypeTag([CullingResults](Rendering.CullingResults.html) exampleCullingResults, [DrawingSettings](Rendering.DrawingSettings.html) exampleDrawingSettings, [FilteringSettings](Rendering.FilteringSettings.html) exampleFilteringSettings)
        {
            // Create the parameters that tell Unity how to override the render state
            var stateBlock = new [RenderStateBlock](Rendering.RenderStateBlock.html)([RenderStateMask.Depth](Rendering.RenderStateMask.Depth.html));
            stateBlock.depthState = new [DepthState](Rendering.DepthState.html)(true, [CompareFunction.Greater](Rendering.CompareFunction.Greater.html));
            var stateBlocks = new NativeArray<[RenderStateBlock](Rendering.RenderStateBlock.html)>(1, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            stateBlocks[0] = stateBlock;  
      
            // Create the parameters that tell Unity when to override the render state
            [ShaderTagId](Rendering.ShaderTagId.html) renderType = new [ShaderTagId](Rendering.ShaderTagId.html)("ExampleRenderTypeTagValue");
            var renderTypes = new NativeArray<[ShaderTagId](Rendering.ShaderTagId.html)>(1, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            renderTypes[0] = renderType;  
      
            // Schedule a command to draw the geometry using the desired render state
            // Unity will execute all scheduled commands during the next call to [ScriptableRenderContext.Submit](Rendering.ScriptableRenderContext.Submit.html)
            scriptableRenderContext.DrawRenderers(exampleCullingResults, ref exampleDrawingSettings, ref exampleFilteringSettings, renderTypes, stateBlocks);  
      
            // DrawRenderers copies the array contents, so it is safe to dispose of the native arrays
            stateBlocks.Dispose();
            renderTypes.Dispose();
        }  
      
        // Override the render state in two different ways.
        // Use one state for all geometry that has a [Pass](ShaderData.Pass.html) Tag
        // with a name of "ExamplePassTagName" and a value of "ExamplePassTagValue".
        // For all other geometry, use a second state.
        public void OverrideRenderStateUsingPassTag([CullingResults](Rendering.CullingResults.html) exampleCullingResults, [DrawingSettings](Rendering.DrawingSettings.html) exampleDrawingSettings, [FilteringSettings](Rendering.FilteringSettings.html) exampleFilteringSettings)
        {
            // Create the parameters that tell Unity how to override the render state
            var stateBlock0 = new [RenderStateBlock](Rendering.RenderStateBlock.html)([RenderStateMask.Depth](Rendering.RenderStateMask.Depth.html));
            stateBlock0.depthState = new [DepthState](Rendering.DepthState.html)(true, [CompareFunction.Greater](Rendering.CompareFunction.Greater.html));
            var stateBlock1 = new [RenderStateBlock](Rendering.RenderStateBlock.html)([RenderStateMask.Depth](Rendering.RenderStateMask.Depth.html));
            stateBlock1.depthState = new [DepthState](Rendering.DepthState.html)(true, [CompareFunction.Less](Rendering.CompareFunction.Less.html));
            var stateBlocks = new NativeArray<[RenderStateBlock](Rendering.RenderStateBlock.html)>(2, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            stateBlocks[0] = stateBlock0;
            stateBlocks[1] = stateBlock1; // default override  
      
            // Create the parameters that tell Unity when to override the render state
            [ShaderTagId](Rendering.ShaderTagId.html) tagName = new [ShaderTagId](Rendering.ShaderTagId.html)("ExamplePassTagName");
            bool isPassTagName = true;
            var tagValues = new NativeArray<[ShaderTagId](Rendering.ShaderTagId.html)>(2, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            tagValues[0] = new [ShaderTagId](Rendering.ShaderTagId.html)("ExamplePassTagValue");
            tagValues[1] = new [ShaderTagId](Rendering.ShaderTagId.html)(); // catch all  
      
            // Schedule a command to draw the geometry using the desired render state
            // Unity will execute all scheduled commands during the next call to [ScriptableRenderContext.Submit](Rendering.ScriptableRenderContext.Submit.html)
            scriptableRenderContext.DrawRenderers(exampleCullingResults, ref exampleDrawingSettings, ref exampleFilteringSettings, tagName, isPassTagName, tagValues, stateBlocks);  
      
            // DrawRenderers copies the array contents, so it is safe to dispose of the native arrays
            stateBlocks.Dispose();
            tagValues.Dispose();
        }
    }
    

Additional resources: [Creating a simple render loop in a custom Scriptable
Render Pipeline](../Manual/srp-creating-simple-render-loop.html)
[CullingResults](Rendering.CullingResults.html),
[DrawingSettings](Rendering.DrawingSettings.html),
[FilteringSettings](Rendering.FilteringSettings.html),
[RenderStateBlock](Rendering.RenderStateBlock.html).

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

