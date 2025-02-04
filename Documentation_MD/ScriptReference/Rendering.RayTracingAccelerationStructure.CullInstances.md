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
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).CullInstances

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

public
[Rendering.RayTracingInstanceCullingResults](Rendering.RayTracingInstanceCullingResults.html)
CullInstances(ref
[Rendering.RayTracingInstanceCullingConfig](Rendering.RayTracingInstanceCullingConfig.html)
cullingConfig);

### Parameters

cullingConfig | Parameters for culling and filtering ray tracing instances.  
---|---  
  
### Returns

**RayTracingInstanceCullingResults** Culling results.

### Description

Populates the RayTracingAccelerationStructure with ray tracing instances that
Unity associates with Renderers in the Scene by using filtering and culling
parameters.

The previous content of the acceleration structure can optionally be cleared
by using
[RayTracingAccelerationStructure.ClearInstances](Rendering.RayTracingAccelerationStructure.ClearInstances.html).
After calling this function, additional ray tracing instances can be added to
the acceleration structure using
[RayTracingAccelerationStructure.AddInstance](Rendering.RayTracingAccelerationStructure.AddInstance.html)
functions.  
  
If
[RayTracingInstanceCullingConfig.instanceTests](Rendering.RayTracingInstanceCullingConfig-
instanceTests.html) array is empty then this function doesn't have any effect.  
  
To build an acceleration structure on the GPU, call
[RayTracingAccelerationStructure.Build](Rendering.RayTracingAccelerationStructure.Build.html)
or
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html).  
  
Additional resources: [RayTracingShader](Rendering.RayTracingShader.html).

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    // This script can be attached to a [Camera](Camera.html).
    public class CullInstancesExample : [MonoBehaviour](MonoBehaviour.html)
    {
        // A [RayTracingShader](Rendering.RayTracingShader.html) is defined in a .raytrace file.
        public [RayTracingShader](Rendering.RayTracingShader.html) rayTracingShader = null;  
      
        public bool enableRayTracedReflections = true;
        public bool enableRayTracedShadows = true;  
      
        private int cameraWidth = 0;
        private int cameraHeight = 0;  
      
        private [RenderTexture](RenderTexture.html) rayTracingOutput = null;
        private [RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html) rayTracingAccelStruct = null;  
      
        void Start()
        {
            if ([SystemInfo.supportsRayTracingShaders](SystemInfo-supportsRayTracingShaders.html) == false)
            {
                [Debug.Log](Debug.Log.html)("The system doesn't support [Ray](Ray.html) Tracing.");
                return;
            }  
      
            RayTracingAccelerationStructure.Settings accelStructSetting = new RayTracingAccelerationStructure.Settings([RayTracingAccelerationStructure.ManagementMode.Manual](Rendering.RayTracingAccelerationStructure.ManagementMode.Manual.html), [RayTracingAccelerationStructure.RayTracingModeMask.Everything](Rendering.RayTracingAccelerationStructure.RayTracingModeMask.Everything.html), -1);
            rayTracingAccelStruct = new [RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)(accelStructSetting);
        }  
      
        void OnDisable()
        {
            if (rayTracingAccelStruct != null)
            {
                rayTracingAccelStruct.Release();
                rayTracingAccelStruct = null;
            }  
      
            if (rayTracingOutput)
            {
                rayTracingOutput.Release();
                rayTracingOutput = null;
            }  
      
            cameraWidth = 0;
            cameraHeight = 0;
        }  
      
        void OnRenderImage([RenderTexture](RenderTexture.html) src, [RenderTexture](RenderTexture.html) dest)
        {
            if ([SystemInfo.supportsRayTracingShaders](SystemInfo-supportsRayTracingShaders.html) == false || rayTracingShader == null)
                return;  
      
            if (cameraWidth != Camera.main.pixelWidth || cameraHeight != Camera.main.pixelHeight)
            {
                if (rayTracingOutput)
                    rayTracingOutput.Release();  
      
                rayTracingOutput = new [RenderTexture](RenderTexture.html)(Camera.main.pixelWidth, Camera.main.pixelHeight, 0, [RenderTextureFormat.ARGBHalf](RenderTextureFormat.ARGBHalf.html));
                rayTracingOutput.enableRandomWrite = true;
                rayTracingOutput.Create();  
      
                cameraWidth = Camera.main.pixelWidth;
                cameraHeight = Camera.main.pixelHeight;
            }  
      
            [RayTracingInstanceCullingConfig](Rendering.RayTracingInstanceCullingConfig.html) cullingConfig = new [RayTracingInstanceCullingConfig](Rendering.RayTracingInstanceCullingConfig.html)();  
      
            cullingConfig.flags = [RayTracingInstanceCullingFlags.EnableLODCulling](Rendering.RayTracingInstanceCullingFlags.EnableLODCulling.html) | [RayTracingInstanceCullingFlags.EnableSphereCulling](Rendering.RayTracingInstanceCullingFlags.EnableSphereCulling.html) | [RayTracingInstanceCullingFlags.EnableSolidAngleCulling](Rendering.RayTracingInstanceCullingFlags.EnableSolidAngleCulling.html);  
      
            // Configure [LOD](LOD.html) culling.
            cullingConfig.lodParameters.fieldOfView = Camera.main.fieldOfView;
            cullingConfig.lodParameters.cameraPosition = Camera.main.transform.position;
            cullingConfig.lodParameters.cameraPixelHeight = Camera.main.pixelHeight;
            cullingConfig.lodParameters.orthoSize = 0;
            cullingConfig.lodParameters.isOrthographic = false;  
      
            // Configure sphere culling. Accept only objects for which the enclosing AABBs are inside (or intersect) a sphere with a radius of 100 units around the camera.
            cullingConfig.sphereCenter = Camera.main.transform.position;
            cullingConfig.sphereRadius = 100.0f;  
      
            // Configure solid-angle culling. Accept only objects for which the projected solid angle with the apex in cullingConfig.lodParameters.cameraPosition is larger than 5 degrees.
            cullingConfig.minSolidAngle = 5.0f;  
      
            // Disable anyhit shaders for opaque geometries for best ray tracing performance.
            cullingConfig.subMeshFlagsConfig.opaqueMaterials = [RayTracingSubMeshFlags.Enabled](Rendering.RayTracingSubMeshFlags.Enabled.html) | [RayTracingSubMeshFlags.ClosestHitOnly](Rendering.RayTracingSubMeshFlags.ClosestHitOnly.html);  
      
            // Disable transparent geometries.
            cullingConfig.subMeshFlagsConfig.transparentMaterials = [RayTracingSubMeshFlags.Disabled](Rendering.RayTracingSubMeshFlags.Disabled.html);  
      
            // Enable anyhit shaders for alpha-tested / cutout geometries.
            cullingConfig.subMeshFlagsConfig.alphaTestedMaterials = [RayTracingSubMeshFlags.Enabled](Rendering.RayTracingSubMeshFlags.Enabled.html);  
      
            // Configure which triangles are double sided. For best ray tracing performance, triangle culling should be disabled.
            cullingConfig.triangleCullingConfig.checkDoubleSidedGIMaterial = true;
            cullingConfig.triangleCullingConfig.frontTriangleCounterClockwise = false;
            cullingConfig.triangleCullingConfig.optionalDoubleSidedShaderKeywords = new string[1];
            cullingConfig.triangleCullingConfig.optionalDoubleSidedShaderKeywords[0] = "_DOUBLESIDED_ON";
            cullingConfig.triangleCullingConfig.forceDoubleSided = false;  
      
            // Configure [Material](Material.html) types. Render queue intervals can also be used here.
            cullingConfig.alphaTestedMaterialConfig.optionalShaderKeywords = new string[1];
            cullingConfig.alphaTestedMaterialConfig.optionalShaderKeywords[0] = "_ALPHATEST_ON";  
      
            cullingConfig.transparentMaterialConfig.optionalShaderKeywords = new string[1];
            cullingConfig.transparentMaterialConfig.optionalShaderKeywords[0] = "_SURFACE_TYPE_TRANSPARENT";  
      
            // Configure a [Material](Material.html) test. Allow only Shaders that have a mandatory [Shader](Shader.html) Tag.
            cullingConfig.materialTest.requiredShaderTags = new [RayTracingInstanceCullingShaderTagConfig](Rendering.RayTracingInstanceCullingShaderTagConfig.html)[1];
            cullingConfig.materialTest.requiredShaderTags[0].tagId = new [ShaderTagId](Rendering.ShaderTagId.html)("[RenderPipeline](Rendering.RenderPipeline.html)");
            cullingConfig.materialTest.requiredShaderTags[0].tagValueId = new [ShaderTagId](Rendering.ShaderTagId.html)("MyAwesomeRP");  
      
            List<[RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html)> instanceTests = new List<[RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html)>();  
      
            // Configure instance tests. There can be one instance test for each ray tracing effect for example.
            // The purpose of instance tests is to use different settings (layer, material types) per ray tracing effect.
            // Use InstanceInclusionMask argument of TraceRay HLSL function to mask different instance types.  
      
            if (enableRayTracedReflections)
            {
                [RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html) instanceTest = new [RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html)();
                instanceTest.allowTransparentMaterials = false;
                instanceTest.allowOpaqueMaterials = true;
                instanceTest.allowAlphaTestedMaterials = true;
                instanceTest.layerMask = -1;
                instanceTest.shadowCastingModeMask = (1 << (int)[ShadowCastingMode.Off](Rendering.ShadowCastingMode.Off.html)) | (1 << (int)[ShadowCastingMode.On](Rendering.ShadowCastingMode.On.html)) | (1 << (int)[ShadowCastingMode.TwoSided](Rendering.ShadowCastingMode.TwoSided.html));
                instanceTest.instanceMask = 1 << 0;  
      
                instanceTests.Add(instanceTest);
            }  
      
            if (enableRayTracedShadows)
            {
                [RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html) instanceTest = new [RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html)();
                instanceTest.allowTransparentMaterials = false;
                instanceTest.allowOpaqueMaterials = true;
                instanceTest.allowAlphaTestedMaterials = true;
                instanceTest.layerMask = -1;
                instanceTest.shadowCastingModeMask = (1 << (int)[ShadowCastingMode.On](Rendering.ShadowCastingMode.On.html)) | (1 << (int)[ShadowCastingMode.TwoSided](Rendering.ShadowCastingMode.TwoSided.html));
                instanceTest.instanceMask = 1 << 1;  
      
                instanceTests.Add(instanceTest);
            }  
      
            cullingConfig.instanceTests = instanceTests.ToArray();  
      
            rayTracingAccelStruct.ClearInstances();
            rayTracingAccelStruct.CullInstances(ref cullingConfig);  
      
            // Additional ray tracing instances can be added manually using [RayTracingAccelerationStructure.AddInstance](Rendering.RayTracingAccelerationStructure.AddInstance.html) function.
            // rayTracingAccelStruct.AddInstance(...);  
      
            rayTracingAccelStruct.Build(Camera.main.transform.position);  
      
            // Use [Shader](Shader.html) [Pass](ShaderData.Pass.html) "Test" in surface (material) shaders.
            rayTracingShader.SetShaderPass("Test");  
      
            rayTracingShader.SetAccelerationStructure("g_AccelStruct", rayTracingAccelStruct);
            rayTracingShader.SetTexture("g_Output", rayTracingOutput);  
      
            rayTracingShader.Dispatch("MainRayGenShader", rayTracingOutput.width, rayTracingOutput.height, 1);  
      
            [Graphics.Blit](Graphics.Blit.html)(rayTracingOutput, dest);
        }
    }
    

This is an example of how to create, populate and build an acceleration
structure. The content of the acceleration structure is specified by
configuring culling and filtering parameters that are passed to the
CullInstances function.

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

