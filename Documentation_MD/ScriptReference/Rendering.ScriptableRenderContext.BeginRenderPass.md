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

#
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html).BeginRenderPass

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

## Declaration

public void BeginRenderPass(int width, int height, int samples,
NativeArray<AttachmentDescriptor> attachments, int depthAttachmentIndex);

## Declaration

public void BeginRenderPass(int width, int height, int volumeDepth, int
samples, NativeArray<AttachmentDescriptor> attachments, int
depthAttachmentIndex);

### Parameters

width | The width of the render pass surfaces in pixels.  
---|---  
height | The height of the render pass surfaces in pixels.  
volumeDepth | The number of slices of the render pass surfaces. The default value is 1.  
samples | MSAA sample count; set to 1 to disable antialiasing.  
attachments | Array of color attachments to use within this render pass. The values in the array are copied immediately.  
depthAttachmentIndex | The index of the attachment to be used as the depth/stencil buffer for this render pass, or -1 to disable depth/stencil.  
  
### Description

Schedules the beginning of a new render pass. Only one render pass can be
active at any time.

A render pass provides a new way to switch rendertargets in the context of a
Scriptable Rendering Pipeline. As opposed to the SetRenderTargets function,
the render pass specifies a clear beginning and an end for the rendering,
alongside explicit load/store actions on the rendering surfaces.  
  
The render pass also allows running multiple subpasses within the same
renderpass, where the pixel shaders have a read access to the current pixel
value within the renderpass. This allows for efficient implementation of
various rendering methods on tile-based GPUs, such as deferred rendering.  
  
Render passes are natively implemented on Metal (iOS) and Vulkan, but the API
is fully functional on all rendering backends via emulation (using legacy
SetRenderTargets calls and reading the current pixel values via texel
fetches).  
  
The render pass mechanism has the following limitations:  
\- All attachments must have the same resolution and MSAA sample count  
\- The rendering results of previous subpasses are only available within the
same screen-space pixel  
coordinate via the UNITY_READ_FRAMEBUFFER_INPUT(x) macro in the shader; the
attachments cannot be bound as textures or otherwise accessed until the
renderpass has ended  
\- iOS Metal does not allow reading from the Z-Buffer, so an additional render
target is needed to work around that  
\- The maximum amount of attachments allowed per render pass is currently 8 +
depth, but note that various GPUs may have stricter limits.  
  
  
Additional resources:
[BeginSubPass](Rendering.ScriptableRenderContext.BeginSubPass.html),
[EndRenderPass](Rendering.ScriptableRenderContext.EndRenderPass.html),
[BeginScopedRenderPass](Rendering.ScriptableRenderContext.BeginScopedRenderPass.html),
[BeginScopedSubPass](Rendering.ScriptableRenderContext.BeginScopedSubPass.html).  
  
A quick example on how to use the render pass API within the Scriptable Render
Pipeline to implement deferred rendering:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using Unity.Collections;  
      
    public static class DeferredRenderer
    {
        public static void ExecuteRenderLoop([Camera](Camera.html) camera, [CullingResults](Rendering.CullingResults.html) cullResults, [ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context)
        {
            // Create the attachment descriptors. If these attachments are not specifically bound to any [RenderTexture](RenderTexture.html) using the ConfigureTarget calls,
            // these are treated as temporary surfaces that are discarded at the end of the renderpass
            var albedo = new [AttachmentDescriptor](Rendering.AttachmentDescriptor.html)([RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html));
            var specRough = new [AttachmentDescriptor](Rendering.AttachmentDescriptor.html)([RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html));
            var normal = new [AttachmentDescriptor](Rendering.AttachmentDescriptor.html)([RenderTextureFormat.ARGB2101010](RenderTextureFormat.ARGB2101010.html));
            var emission = new [AttachmentDescriptor](Rendering.AttachmentDescriptor.html)([RenderTextureFormat.ARGBHalf](RenderTextureFormat.ARGBHalf.html));
            var depth = new [AttachmentDescriptor](Rendering.AttachmentDescriptor.html)([RenderTextureFormat.Depth](RenderTextureFormat.Depth.html));  
      
            // At the beginning of the render pass, clear the emission buffer to all black, and the depth buffer to 1.0f
            emission.ConfigureClear(new [Color](Color.html)(0.0f, 0.0f, 0.0f, 0.0f), 1.0f, 0);
            depth.ConfigureClear(new [Color](Color.html)(), 1.0f, 0);  
      
            // Bind the albedo surface to the current camera target, so the final pass will render the [Scene](SceneManagement.Scene.html) to the screen backbuffer
            // The second argument specifies whether the existing contents of the surface need to be loaded as the initial values;
            // in our case we do not need that because we'll be clearing the attachment anyway. This saves a lot of memory
            // bandwidth on tiled GPUs.
            // The third argument specifies whether the rendering results need to be written out to memory at the end of
            // the renderpass. We need this as we'll be generating the final image there.
            // We could do this in the constructor already, but the camera target may change on the fly, esp. in the editor
            albedo.ConfigureTarget([BuiltinRenderTextureType.CameraTarget](Rendering.BuiltinRenderTextureType.CameraTarget.html), false, true);  
      
            // All other attachments are transient surfaces that are not stored anywhere. If the renderer allows,
            // those surfaces do not even have a memory allocated for the pixel values, saving RAM usage.  
      
            // Start the renderpass using the given scriptable rendercontext, resolution, samplecount, array of attachments that will be used within the renderpass and the depth surface
            var attachments = new NativeArray<[AttachmentDescriptor](Rendering.AttachmentDescriptor.html)>(5, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            const int depthIndex = 0, albedoIndex = 1, specRoughIndex = 2, normalIndex = 3, emissionIndex = 4;
            attachments[depthIndex] = depth;
            attachments[albedoIndex] = albedo;
            attachments[specRoughIndex] = specRough;
            attachments[normalIndex] = normal;
            attachments[emissionIndex] = emission;
            context.BeginRenderPass(camera.pixelWidth, camera.pixelHeight, 1, 1, attachments, depthIndex);
            attachments.Dispose();  
      
            // Start the first subpass, GBuffer creation: render to albedo, specRough, normal and emission, no need to read any input attachments
            var gbufferColors = new NativeArray<int>(4, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            gbufferColors[0] = albedoIndex;
            gbufferColors[1] = specRoughIndex;
            gbufferColors[2] = normalIndex;
            gbufferColors[3] = emissionIndex;
            context.BeginSubPass(gbufferColors);
            gbufferColors.Dispose();  
      
            // Render the deferred G-Buffer
            // RenderGBuffer(cullResults, camera, context);  
      
            context.EndSubPass();  
      
            // Second subpass, lighting: Render to the emission buffer, read from albedo, specRough, normal and depth.
            // The last parameter indicates whether the depth buffer can be bound as read-only.
            // Note that some renderers (notably [iOS](PlayerSettings.iOS.html) Metal) won't allow reading from the depth buffer while it's bound as Z-buffer,
            // so those renderers should write the Z into an additional FP32 render target manually in the pixel shader and read from it instead
            var lightingColors = new NativeArray<int>(1, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            lightingColors[0] = emissionIndex;
            var lightingInputs = new NativeArray<int>(4, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            lightingInputs[0] = albedoIndex;
            lightingInputs[1] = specRoughIndex;
            lightingInputs[2] = normalIndex;
            lightingInputs[3] = depthIndex;
            context.BeginSubPass(lightingColors, lightingInputs, true);
            lightingColors.Dispose();
            lightingInputs.Dispose();  
      
            // PushGlobalShadowParams(context);
            // RenderLighting(camera, cullResults, context);  
      
            context.EndSubPass();  
      
            // Third subpass, tonemapping: Render to albedo (which is bound to the camera target), read from emission.
            var tonemappingColors = new NativeArray<int>(1, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            tonemappingColors[0] = albedoIndex;
            var tonemappingInputs = new NativeArray<int>(1, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            tonemappingInputs[0] = emissionIndex;
            context.BeginSubPass(tonemappingColors, tonemappingInputs, true);
            tonemappingColors.Dispose();
            tonemappingInputs.Dispose();  
      
            // present frame buffer.
            // FinalPass(context);  
      
            context.EndSubPass();  
      
            context.EndRenderPass();
        }
    }
    

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

