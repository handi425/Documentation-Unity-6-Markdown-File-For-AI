[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/create-custom-renderer-feature.html)
  * [中文](/cn/current/Manual/urp/renderer-features/create-custom-renderer-feature.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/create-custom-renderer-feature.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/create-custom-renderer-feature.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/create-custom-renderer-feature.html)
  * [中文](/cn/current/Manual/urp/renderer-features/create-custom-renderer-feature.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/create-custom-renderer-feature.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/create-custom-renderer-feature.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](../../urp/inject-a-render-pass.html)
  * [Injecting a render pass via a Scriptable Renderer Feature in URP](../../urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
  * Example of a complete Scriptable Renderer Feature in URP

[](../../urp/renderer-features/scriptable-renderer-features/apply-scriptable-
feature-to-specific-camera.html)

Apply a Scriptable Renderer Feature to a specific camera type in URP

[](../../urp/renderer-features/scriptable-renderer-features/scriptable-
renderer-feature-reference.html)

Scriptable Renderer Feature API reference for URP

# Example of a complete Scriptable Renderer Feature in URP

This section describes how to create a complete [Scriptable Renderer
Feature](./scriptable-renderer-features/intro-to-scriptable-renderer-
features.html) for a URP Renderer.

This walkthrough contains the following sections:

  * Overview of this example implementation
  * Create example Scene and GameObjects
  * Create a scriptable Renderer Feature and add it to the Universal Renderer
    * Add the Renderer Feature to the the Universal Renderer asset
  * Create the scriptable Render Pass
  * Implement the settings for the custom render pass
  * Implement the render passes
  * Enqueue the render pass in the custom renderer feature
  * Implement the volume component
  * All complete code for the scripts in this example
    * Custom Renderer Feature code
    * Custom render pass code
    * Volume Component code
  * The custom shader for the blur effect

##  Overview of this example implementation

The example workflow on this page implements a custom Renderer Feature that
uses [custom Render Passes](./intro-to-scriptable-render-passes.html) to add a
blur effect to the **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) output.

The implementation consists of the following parts:

  * A `ScriptableRendererFeature` instance that enqueues a `ScriptableRenderPass` instance every frame.

  * A `ScriptableRenderPass` instance that performs the following steps:

    * Creates a temporary **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](../../class-RenderTexture.html)  
See in [Glossary](../../Glossary.html#RenderTexture) using the
`RenderTextureDescriptor` API.

    * Applies two passes of the custom shader to the camera output using the `TextureHandle` and the [AddBlitPass](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.RenderGraphModule.Util.RenderGraphUtils.html#UnityEngine_Rendering_RenderGraphModule_Util_RenderGraphUtils_AddBlitPass_UnityEngine_Rendering_RenderGraphModule_RenderGraph_UnityEngine_Rendering_RenderGraphModule_Util_RenderGraphUtils_BlitMaterialParameters_System_String_) API.

##  Create example Scene and GameObjects

To set your project up for this example workflow:

  1. Create a new **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene).

  2. Create two GameObjects: a Cube **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) called `Cube`, and a Sphere
GameObject called `Sphere`.

  3. Create two Materials with a shader that lets you specify the base color (for example, the `Universal Render Pipeline/Lit` shader). Call the Materials `Blue` and `Red`, and set the base colors of the Materials to blue and red respectively.

  4. Assign the `Red` Material to the cube and the `Blue` Material to the sphere.

  5. Position the camera so that it has the cube and the sphere in its view.

  6. In the URP Asset, set the property **Quality** > **Anti Aliasing (MSAA)** to **Disabled**. The purpose of this step is to simplify the example implementation.

The sample scene should look like the following image:

![Sample scene](../../../uploads/urp/customizing-urp/custom-renderer-
feature/sample-scene.png) Sample scene

##  Create a scriptable Renderer Feature and add it to the Universal Renderer

  1. Create a new C# script and name it `BlurRendererFeature.cs`.

  2. In the script, remove the code that Unity inserted in the `BlurRendererFeature` class.

  3. Add the following `using` directive:
    
        using UnityEngine.Rendering.Universal;
    

  4. Create the `BlurRendererFeature` class that inherits from the **ScriptableRendererFeature** class.
    
        public class BlurRendererFeature : ScriptableRendererFeature    
    

  5. In the `BlurRendererFeature` class, implement the following methods:

     * `Create`: Unity calls this method on the following events:

       * When the Renderer Feature loads the first time.

       * When you enable or disable the Renderer Feature.

       * When you change a property in the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../UsingTheInspector.html)  
See in [Glossary](../../Glossary.html#Inspector) of the Renderer Feature.

     * `AddRenderPasses`: Unity calls this method every frame, once for each camera. This method lets you inject `ScriptableRenderPass` instances into the scriptable Renderer.

Now you have the custom `BlurRendererFeature` Renderer Feature with its main
methods.

Below is the complete code for this step.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Rendering.Universal;
    
    public class BlurRendererFeature : ScriptableRendererFeature
    {
        public override void Create()
        {
    
        }
    
        public override void AddRenderPasses(ScriptableRenderer renderer,
            ref RenderingData renderingData)
        {
    
        }
    }
    

###  Add the Renderer Feature to the the Universal Renderer asset

Add the Renderer Feature you created to the the Universal Renderer asset. For
information on how to do this, refer to the page [How to add a Renderer
Feature to a Renderer](../urp-renderer-feature.html).

##  Create the scriptable Render Pass

This section demonstrates how to create a scriptable Render Pass and enqueue
its instance into the scriptable Renderer.

  1. Create a new C# script and name it `BlurRenderPass.cs`.

  2. In the script, remove the code that Unity inserted in the `BlurRenderPass` class. Add the following `using` directive:
    
        using UnityEngine.Rendering;
    using UnityEngine.Rendering.RenderGraphModule;
    using UnityEngine.Rendering.RenderGraphModule.Util;
    using UnityEngine.Rendering.Universal;
    

  3. Create the `BlurRenderPass` class that inherits from the **ScriptableRenderPass** class.
    
        public class BlurRenderPass : ScriptableRenderPass
    

  4. Add the `RecordRenderGraph` method to the class. This method adds and configures render passes in the render graph. This process includes declaring render pass inputs and outputs, but does not include adding commands to command buffers. Unity calls this method every frame, once for each camera.
    
        public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameData)
    { }
    

Below is the complete code for the `BlurRenderPass.cs` file from this section.

    
    
    using UnityEngine.Rendering;
    using UnityEngine.Rendering.RenderGraphModule;
    using UnityEngine.Rendering.RenderGraphModule.Util;
    using UnityEngine.Rendering.Universal;
    
    public class BlurRenderPass : ScriptableRenderPass
    {
        public override void RecordRenderGraph(RenderGraph renderGraph,
        ContextContainer frameData)
        {
            
        }
    }
    

## Implement the settings for the custom render pass

This section demonstrates how to implement the settings for the custom blur
render pass.

  1. The Renderer Feature in this example uses the shaderA program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) that performs the blur
horizontally in one pass, and vertically in another pass. To let users control
the blur value for each pass, add the following `BlurSettings` class to the
`BlurRendererFeature.cs` script.

    
        [Serializable]
    public class BlurSettings
    {
        [Range(0,0.4f)] public float horizontalBlur;
        [Range(0,0.4f)] public float verticalBlur;
    }
    

  2. In the `BlurRendererFeature` class, declare the following fields:
    
        [SerializeField] private BlurSettings settings;
    [SerializeField] private Shader shader;
    private Material material;
    private BlurRenderPass blurRenderPass;
    

  3. In the `BlurRenderPass` class, add the fields for the settings, the Material, and the constructor that uses those fields.
    
        private BlurSettings defaultSettings;
    private Material material;
    
    public BlurRenderPass(Material material, BlurSettings defaultSettings)
    {
        this.material = material;
        this.defaultSettings = defaultSettings;
    }
    

  4. In the `BlurRenderPass` class, add the `RenderTextureDescriptor` field and initialize it in the constructor. The `RenderTextureDescriptor` class lets you specify the properties of a render texture, such as the width, height, and format.
    
        using UnityEngine;
    
    private RenderTextureDescriptor blurTextureDescriptor;
    
    public BlurRenderPass(Material material, BlurSettings defaultSettings)
    {
        this.material = material;
        this.defaultSettings = defaultSettings;
    
        blurTextureDescriptor = new RenderTextureDescriptor(Screen.width, Screen.height,
        RenderTextureFormat.Default, 0);
    }
    

  5. In the `RecordRenderGraph` method, create the variable for storing the `UniversalResourceData` instance from the `frameData` parameter. `UniversalResourceData` contains all the texture references used by URP, including the active color and depth textures of the camera.
    
        UniversalResourceData resourceData = frameData.Get<UniversalResourceData>();
    

  6. Declare the variables for interacting with the shader properties.
    
        private static readonly int horizontalBlurId = Shader.PropertyToID("_HorizontalBlur");
    private static readonly int verticalBlurId = Shader.PropertyToID("_VerticalBlur");
    private const string k_BlurTextureName = "_BlurTexture";
    private const string k_VerticalPassName = "VerticalBlurRenderPass";
    private const string k_HorizontalPassName = "HorizontalBlurRenderPass";
    

  7. In the `RecordRenderGraph` method, declare the `TextureHandle` fields to store the references to the input and the output textures. `CreateRenderGraphTexture` is a helper method that calls the `RenderGraph.CreateTexture` method.
    
        TextureHandle srcCamColor = resourceData.activeColorTexture;
    TextureHandle dst = UniversalRenderer.CreateRenderGraphTexture(renderGraph, blurTextureDescriptor, k_BlurTextureName, false);
    

  8. In the `BlurRenderPass` class, implement the `UpdateBlurSettings` method that updates the shader values.
    
        private void UpdateBlurSettings()
    {
        if (material == null) return;
    
        // Use the Volume settings or the default settings if no Volume is set.
        var volumeComponent =
            VolumeManager.instance.stack.GetComponent<CustomVolumeComponent>();
        float horizontalBlur = volumeComponent.horizontalBlur.overrideState ?
            volumeComponent.horizontalBlur.value : defaultSettings.horizontalBlur;
        float verticalBlur = volumeComponent.verticalBlur.overrideState ?
            volumeComponent.verticalBlur.value : defaultSettings.verticalBlur;
        material.SetFloat(horizontalBlurId, horizontalBlur);
        material.SetFloat(verticalBlurId, verticalBlur);
    }
    

  9. In the `RecordRenderGraph` method, add the variable for storing the `UniversalCameraData` data, and set the `RenderTextureDescriptor` values using that data.
    
        UniversalCameraData cameraData = frameData.Get<UniversalCameraData>();
    
    // The following line ensures that the render pass doesn't blit
    // from the back buffer.
    if (resourceData.isActiveTargetBackBuffer)
        return;
    
    // Set the blur texture size to be the same as the camera target size.
    blurTextureDescriptor.width = cameraData.cameraTargetDescriptor.width;
    blurTextureDescriptor.height = cameraData.cameraTargetDescriptor.height;
    blurTextureDescriptor.depthBufferBits = 0;
    

  10. In the `RecordRenderGraph` method, add the function to continuously update the blur settings in the material.
    
        // Update the blur settings in the material
    UpdateBlurSettings();
    
    // This check is to avoid an error from the material preview in the scene
    if (!srcCamColor.IsValid() || !dst.IsValid())
        return;
    

## Implement the render passes

In the `RecordRenderGraph` method, using the `AddBlitPass` method, add the
vertical and the horizontal blur render passes.

    
    
    // The AddBlitPass method adds a vertical blur render graph pass that blits from the source texture (camera color in this case) to the destination texture using the first shader pass (the shader pass is defined in the last parameter).
    RenderGraphUtils.BlitMaterialParameters paraVertical = new(srcCamColor, dst, material, 0);
    renderGraph.AddBlitPass(paraVertical, k_VerticalPassName);
    
    // The AddBlitPass method adds a horizontal blur render graph pass that blits from the texture written by the vertical blur pass to the camera color texture. The method uses the second shader pass.
    RenderGraphUtils.BlitMaterialParameters paraHorizontal = new(dst, srcCamColor, material, 1);
    renderGraph.AddBlitPass(paraHorizontal, k_HorizontalPassName);
    

The complete code for this part is in section Custom render pass code.

## Enqueue the render pass in the custom renderer feature

In this section, you instantiate the render pass in the `Create` method of the
`BlurRendererFeature` class, and enqueue it in the `AddRenderPasses` method.

  1. In the `Create` method of the `BlurRendererFeature` class, instantiate the `BlurRenderPass` class.

In the method, use the `renderPassEvent` field to specify when to execute the
render pass.

    
        public override void Create()
    {
        if (shader == null)
        {
            return;
        }
        material = new Material(shader);
        blurRenderPass = new BlurRenderPass(material, settings);
    
        blurRenderPass.renderPassEvent = RenderPassEvent.AfterRenderingSkybox;
    }
    

  2. In the `AddRenderPasses` method of the `BlurRendererFeature` class, enqueue the render pass with the `EnqueuePass` method.
    
        public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        if (blurRenderPass == null)
        { 
            return;
        }                
        if (renderingData.cameraData.cameraType == CameraType.Game)
        {
            renderer.EnqueuePass(blurRenderPass);
        }
    }
    

  3. Implement the `Dispose` method that destroys the material instance that the Renderer Feature creates.
    
        protected override void Dispose(bool disposing)
    {
        if (Application.isPlaying)
        {
            Destroy(material);
        }
        else
        {
            DestroyImmediate(material);
        }
    }
    

For the complete Renderer Feature code, refer to section Custom Renderer
Feature code.

The Scriptable Renderer Feature is now complete. The following image shows the
effect of the feature in the Game view and the example settings.

![The effect of the Scriptable Renderer Feature in the Game
view](../../../uploads/urp/customizing-urp/custom-renderer-feature/final-
effect.png)  
_The effect of the Scriptable Renderer Feature in the Game view._

##  Implement the volume component

This section shows how to implement a volume component that lets you control
the input values for the custom renderer feature.

  1. Create a new C# script and name it `CustomVolumeComponent.cs`.

  2. Inherit the `CustomVolumeComponent` class from the `VolumeComponent` class, add the `[Serializable]` attribute to the class. Add the `using UnityEngine.Rendering;` directive.
    
        using System;
    using UnityEngine.Rendering;
    
    [Serializable]
    public class CustomVolumeComponent : VolumeComponent
    {
    
    }
    

  3. Add the fields to control the blur settings defined in the custom renderer feature.
    
        [Serializable]
    public class CustomVolumeComponent : VolumeComponent
    {
        public ClampedFloatParameter horizontalBlur =
            new ClampedFloatParameter(0.05f, 0, 0.5f);
        public ClampedFloatParameter verticalBlur =
            new ClampedFloatParameter(0.05f, 0, 0.5f);
    }
    

  4. In the `BlurRenderPass` script, change the `UpdateBlurSettings` method so that it uses the settings defined in a Volume or the default settings if no Volume is set.
    
        private void UpdateBlurSettings()
    {
        if (material == null) return;
    
        // Use the Volume settings or the default settings if no Volume is set.
        var volumeComponent =
            VolumeManager.instance.stack.GetComponent<CustomVolumeComponent>();
        float horizontalBlur = volumeComponent.horizontalBlur.overrideState ?
            volumeComponent.horizontalBlur.value : defaultSettings.horizontalBlur;
        float verticalBlur = volumeComponent.verticalBlur.overrideState ?
            volumeComponent.verticalBlur.value : defaultSettings.verticalBlur;
        material.SetFloat(horizontalBlurId, horizontalBlur);
        material.SetFloat(verticalBlurId, verticalBlur);
    }
    

  5. In the Unity scene, create a [local Box Volume](../Volumes.html). If a [Volume Profile](../Volume-Profile.html) is missing, create a new one by clicking **New** next to the **Profile** property. Add the `Custom Volume Component` [override](../VolumeOverrides.html) to the Volume.

![Box Volume properties](../../../uploads/urp/customizing-urp/custom-renderer-
feature/local-volume.png) Box Volume properties

  6. Enable the settings in the `Custom Volume Component` override and set the values for this Volume. Move the Volume so that the camera is inside it. The settings from the Volume override the default settings from the custom renderer feature. 

## All complete code for the scripts in this example

This section contains the complete code for all the **scripts** A piece of
code that allows you to create your own Components, trigger game events,
modify Component properties over time and respond to user input in any way you
like. [More info](../../creating-scripts.html)  
See in [Glossary](../../Glossary.html#Scripts) in this example.

###  Custom Renderer Feature code

Below is the complete code for the custom Renderer Feature script.

    
    
    using System;
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.Rendering.Universal;
    
    public class BlurRendererFeature : ScriptableRendererFeature
    {
        [SerializeField] private BlurSettings settings;
        [SerializeField] private Shader shader;
        private Material material;
        private BlurRenderPass blurRenderPass;
    
        public override void Create()
        {
            if (shader == null)
            {
                return;
            }
            material = new Material(shader);
            blurRenderPass = new BlurRenderPass(material, settings);
            
            blurRenderPass.renderPassEvent = RenderPassEvent.BeforeRenderingPostProcessing;
        }
    
        public override void AddRenderPasses(ScriptableRenderer renderer,
            ref RenderingData renderingData)
        {
            if (blurRenderPass == null)
            { 
                return;
            }    
            if (renderingData.cameraData.cameraType == CameraType.Game)
            {
                renderer.EnqueuePass(blurRenderPass);
            }
        }
    
        protected override void Dispose(bool disposing)
        {
            if (Application.isPlaying)
            {
                Destroy(material);
            }
            else
            {
                DestroyImmediate(material);
            }
        }
    }
    
    [Serializable]
    public class BlurSettings
    {
        [Range(0, 0.4f)] public float horizontalBlur;
        [Range(0, 0.4f)] public float verticalBlur;
    }
    

###  Custom render pass code

Below is the complete code for the custom Render Pass script.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using UnityEngine.Rendering.RenderGraphModule;
    using UnityEngine.Rendering.RenderGraphModule.Util;
    using UnityEngine.Rendering.Universal;
    
    public class BlurRenderPass : ScriptableRenderPass
    {
        private static readonly int horizontalBlurId = Shader.PropertyToID("_HorizontalBlur");
        private static readonly int verticalBlurId = Shader.PropertyToID("_VerticalBlur");
        private const string k_BlurTextureName = "_BlurTexture";
        private const string k_VerticalPassName = "VerticalBlurRenderPass";
        private const string k_HorizontalPassName = "HorizontalBlurRenderPass";
    
        private BlurSettings defaultSettings;
        private Material material;
    
        private RenderTextureDescriptor blurTextureDescriptor;
    
        public BlurRenderPass(Material material, BlurSettings defaultSettings)
        {
            this.material = material;
            this.defaultSettings = defaultSettings;
    
            blurTextureDescriptor = new RenderTextureDescriptor(Screen.width, Screen.height,
                RenderTextureFormat.Default, 0);
        }
    
        private void UpdateBlurSettings()
        {
            if (material == null) return;
    
            // Use the Volume settings or the default settings if no Volume is set.
            var volumeComponent =
                VolumeManager.instance.stack.GetComponent<CustomVolumeComponent>();
            float horizontalBlur = volumeComponent.horizontalBlur.overrideState ?
                volumeComponent.horizontalBlur.value : defaultSettings.horizontalBlur;
            float verticalBlur = volumeComponent.verticalBlur.overrideState ?
                volumeComponent.verticalBlur.value : defaultSettings.verticalBlur;
            material.SetFloat(horizontalBlurId, horizontalBlur);
            material.SetFloat(verticalBlurId, verticalBlur);
        }
    
        public override void RecordRenderGraph(RenderGraph renderGraph,
        ContextContainer frameData)
        {
            UniversalResourceData resourceData = frameData.Get<UniversalResourceData>();
    
            UniversalCameraData cameraData = frameData.Get<UniversalCameraData>();
    
            // The following line ensures that the render pass doesn't blit
            // from the back buffer.
            if (resourceData.isActiveTargetBackBuffer)
                return;
    
            // Set the blur texture size to be the same as the camera target size.
            blurTextureDescriptor.width = cameraData.cameraTargetDescriptor.width;
            blurTextureDescriptor.height = cameraData.cameraTargetDescriptor.height;
            blurTextureDescriptor.depthBufferBits = 0;
    
            TextureHandle srcCamColor = resourceData.activeColorTexture;
            TextureHandle dst = UniversalRenderer.CreateRenderGraphTexture(renderGraph,
                blurTextureDescriptor, k_BlurTextureName, false);
    
            // Update the blur settings in the material
            UpdateBlurSettings();
    
            // This check is to avoid an error from the material preview in the scene
            if (!srcCamColor.IsValid() || !dst.IsValid())
                return;
            
            // The AddBlitPass method adds a vertical blur render graph pass that blits from the source texture (camera color in this case) to the destination texture using the first shader pass (the shader pass is defined in the last parameter).
            RenderGraphUtils.BlitMaterialParameters paraVertical = new(srcCamColor, dst, material, 0);
            renderGraph.AddBlitPass(paraVertical, k_VerticalPassName);
            
            // The AddBlitPass method adds a horizontal blur render graph pass that blits from the texture written by the vertical blur pass to the camera color texture. The method uses the second shader pass.
            RenderGraphUtils.BlitMaterialParameters paraHorizontal = new(dst, srcCamColor, material, 1);
            renderGraph.AddBlitPass(paraHorizontal, k_HorizontalPassName);
        }
    }
    

###  Volume Component code

Below is the complete code for the Volume Component script.

    
    
    using System;
    using UnityEngine.Rendering;
    
    [Serializable]
    public class CustomVolumeComponent : VolumeComponent
    {
        public ClampedFloatParameter horizontalBlur =
            new ClampedFloatParameter(0.05f, 0, 0.5f);
        public ClampedFloatParameter verticalBlur =
            new ClampedFloatParameter(0.05f, 0, 0.5f);
    }
    

##  The custom shader for the blur effect

This section contains the code for the custom shader that implements the blur
effect.

    
    
    Shader "CustomEffects/Blur"
    {
        HLSLINCLUDE
        
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
            // The Blit.hlsl file provides the vertex shader (Vert),
            // the input structure (Attributes), and the output structure (Varyings)
            #include "Packages/com.unity.render-pipelines.core/Runtime/Utilities/Blit.hlsl"
    
            float _VerticalBlur;
            float _HorizontalBlur;
        
            float4 BlurVertical (Varyings input) : SV_Target
            {
                const float BLUR_SAMPLES = 64;
                const float BLUR_SAMPLES_RANGE = BLUR_SAMPLES / 2;
                
                float3 color = 0;
                float blurPixels = _VerticalBlur * _ScreenParams.y;
                
                for(float i = -BLUR_SAMPLES_RANGE; i <= BLUR_SAMPLES_RANGE; i++)
                {
                    float2 sampleOffset = float2 (0, (blurPixels / _BlitTexture_TexelSize.w) * (i / BLUR_SAMPLES_RANGE));
                    color += SAMPLE_TEXTURE2D(_BlitTexture, sampler_LinearClamp, input.texcoord + sampleOffset).rgb;
                }
                
                return float4(color.rgb / (BLUR_SAMPLES + 1), 1);
            }
    
            float4 BlurHorizontal (Varyings input) : SV_Target
            {
                const float BLUR_SAMPLES = 64;
                const float BLUR_SAMPLES_RANGE = BLUR_SAMPLES / 2;
                
                UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(input);
                float3 color = 0;
                float blurPixels = _HorizontalBlur * _ScreenParams.x;
                for(float i = -BLUR_SAMPLES_RANGE; i <= BLUR_SAMPLES_RANGE; i++)
                {
                    float2 sampleOffset =
                        float2 ((blurPixels / _BlitTexture_TexelSize.z) * (i / BLUR_SAMPLES_RANGE), 0);
                    color += SAMPLE_TEXTURE2D(_BlitTexture, sampler_LinearClamp, input.texcoord + sampleOffset).rgb;
                }
                return float4(color / (BLUR_SAMPLES + 1), 1);
            }
        
        ENDHLSL
        
        SubShader
        {
            Tags { "RenderType"="Opaque" "RenderPipeline" = "UniversalPipeline"}
            LOD 100
            ZWrite Off Cull Off
            Pass
            {
                Name "BlurPassVertical"
    
                HLSLPROGRAM
                
                #pragma vertex Vert
                #pragma fragment BlurVertical
                
                ENDHLSL
            }
            
            Pass
            {
                Name "BlurPassHorizontal"
    
                HLSLPROGRAM
                
                #pragma vertex Vert
                #pragma fragment BlurHorizontal
                
                ENDHLSL
            }
        }
    }
    

## Additional resources

  * The **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](../../Glossary.html#blit) examples in the [URP RenderGraph
Samples](../package-sample-urp-package-samples.html)

  * [Custom render pass workflow in URP](custom-rendering-pass-workflow-in-urp.html)
  * [Textures in the Render Graph system in URP](../working-with-textures.html)

[](../../urp/renderer-features/scriptable-renderer-features/apply-scriptable-
feature-to-specific-camera.html)

Apply a Scriptable Renderer Feature to a specific camera type in URP

[](../../urp/renderer-features/scriptable-renderer-features/scriptable-
renderer-feature-reference.html)

Scriptable Renderer Feature API reference for URP

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

