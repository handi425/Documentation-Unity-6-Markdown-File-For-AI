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

# SystemInfo

class in UnityEngine.Device

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Access platform-specific system and hardware information.

This class has the same functionality as [SystemInfo](SystemInfo.html) and
also mimics platform-specific behavior in the Unity Editor. Use it together
with the Device Simulator to test platform-specific behaviors inside the
Editor. Outside of the Editor, this class behaves exactly like the
[SystemInfo](SystemInfo.html) class. Unity strips all simulation capabilities
during the build process. Use the original [SystemInfo](SystemInfo.html) class
if you work directly with the Unity Editor (for example, to create a custom
Editor tool) and you don't need to use any simulated values.

### Static Properties

[batteryLevel](Device.SystemInfo-batteryLevel.html)| This has the same
functionality as SystemInfo.batteryLevel and also mimics platform-specific
behavior in the Unity Editor.  
---|---  
[batteryStatus](Device.SystemInfo-batteryStatus.html)| This has the same
functionality as SystemInfo.batteryStatus and also mimics platform-specific
behavior in the Unity Editor.  
[computeSubGroupSize](Device.SystemInfo-computeSubGroupSize.html)| This has
the same functionality as SystemInfo.computeSubGroupSize and also mimics
platform-specific behavior in the Unity Editor.  
[constantBufferOffsetAlignment](Device.SystemInfo-
constantBufferOffsetAlignment.html)| This has the same functionality as
SystemInfo.constantBufferOffsetAlignment and also mimics platform-specific
behavior in the Unity Editor.  
[copyTextureSupport](Device.SystemInfo-copyTextureSupport.html)| This has the
same functionality as SystemInfo.copyTextureSupport and also mimics platform-
specific behavior in the Unity Editor.  
[deviceModel](Device.SystemInfo-deviceModel.html)| This has the same
functionality as SystemInfo.deviceModel and also mimics platform-specific
behavior in the Unity Editor.  
[deviceName](Device.SystemInfo-deviceName.html)| This has the same
functionality as SystemInfo.deviceName and also mimics platform-specific
behavior in the Unity Editor.  
[deviceType](Device.SystemInfo-deviceType.html)| This has the same
functionality as SystemInfo.deviceType and also mimics platform-specific
behavior in the Unity Editor.  
[deviceUniqueIdentifier](Device.SystemInfo-deviceUniqueIdentifier.html)| This
has the same functionality as SystemInfo.deviceUniqueIdentifier and also
mimics platform-specific behavior in the Unity Editor.  
[foveatedRenderingCaps](Device.SystemInfo-foveatedRenderingCaps.html)| This
has the same functionality as SystemInfo.foveatedRenderingCaps and also mimics
platform-specific behavior in the Unity Editor.  
[graphicsDeviceID](Device.SystemInfo-graphicsDeviceID.html)| This has the same
functionality as SystemInfo.graphicsDeviceID and also mimics platform-specific
behavior in the Unity Editor.  
[graphicsDeviceName](Device.SystemInfo-graphicsDeviceName.html)| This has the
same functionality as SystemInfo.graphicsDeviceName and also mimics platform-
specific behavior in the Unity Editor.  
[graphicsDeviceType](Device.SystemInfo-graphicsDeviceType.html)| This has the
same functionality as SystemInfo.graphicsDeviceType and also mimics platform-
specific behavior in the Unity Editor.  
[graphicsDeviceVendor](Device.SystemInfo-graphicsDeviceVendor.html)| This has
the same functionality as SystemInfo.graphicsDeviceVendor and also mimics
platform-specific behavior in the Unity Editor.  
[graphicsDeviceVendorID](Device.SystemInfo-graphicsDeviceVendorID.html)| This
has the same functionality as SystemInfo.graphicsDeviceVendorID and also
mimics platform-specific behavior in the Unity Editor.  
[graphicsDeviceVersion](Device.SystemInfo-graphicsDeviceVersion.html)| This
has the same functionality as SystemInfo.graphicsDeviceVersion and also mimics
platform-specific behavior in the Unity Editor.  
[graphicsMemorySize](Device.SystemInfo-graphicsMemorySize.html)| This has the
same functionality as SystemInfo.graphicsMemorySize and also mimics platform-
specific behavior in the Unity Editor.  
[graphicsMultiThreaded](Device.SystemInfo-graphicsMultiThreaded.html)| This
has the same functionality as SystemInfo.graphicsMultiThreaded and also mimics
platform-specific behavior in the Unity Editor.  
[graphicsShaderLevel](Device.SystemInfo-graphicsShaderLevel.html)| This has
the same functionality as SystemInfo.graphicsShaderLevel and also mimics
platform-specific behavior in the Unity Editor.  
[graphicsUVStartsAtTop](Device.SystemInfo-graphicsUVStartsAtTop.html)| This
has the same functionality as SystemInfo.graphicsUVStartsAtTop and also mimics
platform-specific behavior in the Unity Editor.  
[hasDynamicUniformArrayIndexingInFragmentShaders](Device.SystemInfo-
hasDynamicUniformArrayIndexingInFragmentShaders.html)| This has the same
functionality as SystemInfo.hasDynamicUniformArrayIndexingInFragmentShaders
and also mimics platform-specific behavior in the Unity Editor.  
[hasHiddenSurfaceRemovalOnGPU](Device.SystemInfo-
hasHiddenSurfaceRemovalOnGPU.html)| This has the same functionality as
SystemInfo.hasHiddenSurfaceRemovalOnGPU and also mimics platform-specific
behavior in the Unity Editor.  
[hasMipMaxLevel](Device.SystemInfo-hasMipMaxLevel.html)| This has the same
functionality as SystemInfo.hasMipMaxLevel and also mimics platform-specific
behavior in the Unity Editor.  
[hdrDisplaySupportFlags](Device.SystemInfo-hdrDisplaySupportFlags.html)| This
has the same functionality as SystemInfo.hdrDisplaySupportFlags and also
mimics platform-specific behavior in the Unity Editor.  
[maxAnisotropyLevel](Device.SystemInfo-maxAnisotropyLevel.html)| This has the
same functionality as SystemInfo.maxAnisotropyLevel and also mimics platform-
specific behavior in the Unity Editor.  
[maxComputeBufferInputsCompute](Device.SystemInfo-
maxComputeBufferInputsCompute.html)| This has the same functionality as
SystemInfo.maxComputeBufferInputsCompute and also mimics platform-specific
behavior in the Unity Editor.  
[maxComputeBufferInputsDomain](Device.SystemInfo-
maxComputeBufferInputsDomain.html)| This has the same functionality as
SystemInfo.maxComputeBufferInputsDomain and also mimics platform-specific
behavior in the Unity Editor.  
[maxComputeBufferInputsFragment](Device.SystemInfo-
maxComputeBufferInputsFragment.html)| This has the same functionality as
SystemInfo.maxComputeBufferInputsFragment and also mimics platform-specific
behavior in the Unity Editor.  
[maxComputeBufferInputsGeometry](Device.SystemInfo-
maxComputeBufferInputsGeometry.html)| This has the same functionality as
SystemInfo.maxComputeBufferInputsGeometry and also mimics platform-specific
behavior in the Unity Editor.  
[maxComputeBufferInputsHull](Device.SystemInfo-
maxComputeBufferInputsHull.html)| This has the same functionality as
SystemInfo.maxComputeBufferInputsHull and also mimics platform-specific
behavior in the Unity Editor.  
[maxComputeBufferInputsVertex](Device.SystemInfo-
maxComputeBufferInputsVertex.html)| This has the same functionality as
SystemInfo.maxComputeBufferInputsVertex and also mimics platform-specific
behavior in the Unity Editor.  
[maxComputeWorkGroupSize](Device.SystemInfo-maxComputeWorkGroupSize.html)|
This has the same functionality as SystemInfo.maxComputeWorkGroupSize and also
mimics platform-specific behavior in the Unity Editor.  
[maxComputeWorkGroupSizeX](Device.SystemInfo-maxComputeWorkGroupSizeX.html)|
This has the same functionality as SystemInfo.maxComputeWorkGroupSizeX and
also mimics platform-specific behavior in the Unity Editor.  
[maxComputeWorkGroupSizeY](Device.SystemInfo-maxComputeWorkGroupSizeY.html)|
This has the same functionality as SystemInfo.maxComputeWorkGroupSizeY and
also mimics platform-specific behavior in the Unity Editor.  
[maxComputeWorkGroupSizeZ](Device.SystemInfo-maxComputeWorkGroupSizeZ.html)|
This has the same functionality as SystemInfo.maxComputeWorkGroupSizeZ and
also mimics platform-specific behavior in the Unity Editor.  
[maxConstantBufferSize](Device.SystemInfo-maxConstantBufferSize.html)| This
property mimics platform-specific behavior caused by
SystemInfo.maxConstantBufferSize. Use this property for platform-specific
testing in the Unity Editor.  
[maxCubemapSize](Device.SystemInfo-maxCubemapSize.html)| This has the same
functionality as SystemInfo.maxCubemapSize and also mimics platform-specific
behavior in the Unity Editor.  
[maxGraphicsBufferSize](Device.SystemInfo-maxGraphicsBufferSize.html)| The
maximum size of a graphics buffer (GraphicsBuffer, ComputeBuffer, vertex/index
buffer, etc.) in bytes (Read Only).  
[maxTexture3DSize](Device.SystemInfo-maxTexture3DSize.html)| This has the same
functionality as SystemInfo.maxTexture3DSize and also mimics platform-specific
behavior in the Unity Editor.  
[maxTextureArraySlices](Device.SystemInfo-maxTextureArraySlices.html)| This
has the same functionality as SystemInfo.maxTextureArraySlices and also mimics
platform-specific behavior in the Unity Editor.  
[maxTextureSize](Device.SystemInfo-maxTextureSize.html)| This has the same
functionality as SystemInfo.maxTextureSize and also mimics platform-specific
behavior in the Unity Editor.  
[npotSupport](Device.SystemInfo-npotSupport.html)| This has the same
functionality as SystemInfo.npotSupport and also mimics platform-specific
behavior in the Unity Editor.  
[operatingSystem](Device.SystemInfo-operatingSystem.html)| This has the same
functionality as SystemInfo.operatingSystem and also mimics platform-specific
behavior in the Unity Editor.  
[operatingSystemFamily](Device.SystemInfo-operatingSystemFamily.html)| This
has the same functionality as SystemInfo.operatingSystemFamily and also mimics
platform-specific behavior in the Unity Editor.  
[processorCount](Device.SystemInfo-processorCount.html)| This has the same
functionality as SystemInfo.processorCount and also mimics platform-specific
behavior in the Unity Editor.  
[processorFrequency](Device.SystemInfo-processorFrequency.html)| This has the
same functionality as SystemInfo.processorFrequency and also mimics platform-
specific behavior in the Unity Editor.  
[processorManufacturer](Device.SystemInfo-processorManufacturer.html)| This
has the same functionality as SystemInfo.processorManufacturer and also mimics
platform-specific behavior in the Unity Editor.  
[processorModel](Device.SystemInfo-processorModel.html)| This has the same
functionality as SystemInfo.processorModel and also mimics platform-specific
behavior in the Unity Editor.  
[processorType](Device.SystemInfo-processorType.html)| This has the same
functionality as SystemInfo.processorType and also mimics platform-specific
behavior in the Unity Editor.  
[renderingThreadingMode](Device.SystemInfo-renderingThreadingMode.html)| This
has the same functionality as SystemInfo.renderingThreadingMode and also
mimics platform-specific behavior in the Unity Editor.  
[supportedRandomWriteTargetCount](Device.SystemInfo-
supportedRandomWriteTargetCount.html)| This has the same functionality as
SystemInfo.supportedRandomWriteTargetCount and also mimics platform-specific
behavior in the Unity Editor.  
[supportedRenderTargetCount](Device.SystemInfo-
supportedRenderTargetCount.html)| This has the same functionality as
SystemInfo.supportedRenderTargetCount and also mimics platform-specific
behavior in the Unity Editor.  
[supports2DArrayTextures](Device.SystemInfo-supports2DArrayTextures.html)|
This has the same functionality as SystemInfo.supports2DArrayTextures and also
mimics platform-specific behavior in the Unity Editor.  
[supports32bitsIndexBuffer](Device.SystemInfo-supports32bitsIndexBuffer.html)|
This has the same functionality as SystemInfo.supports32bitsIndexBuffer and
also mimics platform-specific behavior in the Unity Editor.  
[supports3DRenderTextures](Device.SystemInfo-supports3DRenderTextures.html)|
This has the same functionality as SystemInfo.supports3DRenderTextures and
also mimics platform-specific behavior in the Unity Editor.  
[supports3DTextures](Device.SystemInfo-supports3DTextures.html)| This has the
same functionality as SystemInfo.supports3DTextures and also mimics platform-
specific behavior in the Unity Editor.  
[supportsAccelerometer](Device.SystemInfo-supportsAccelerometer.html)| This
has the same functionality as SystemInfo.supportsAccelerometer and also mimics
platform-specific behavior in the Unity Editor.  
[supportsAnisotropicFilter](Device.SystemInfo-supportsAnisotropicFilter.html)|
This has the same functionality as SystemInfo.supportsAnisotropicFilter and
also mimics platform-specific behavior in the Unity Editor.  
[supportsAsyncCompute](Device.SystemInfo-supportsAsyncCompute.html)| This has
the same functionality as SystemInfo.supportsAsyncCompute and also mimics
platform-specific behavior in the Unity Editor.  
[supportsAsyncGPUReadback](Device.SystemInfo-supportsAsyncGPUReadback.html)|
This has the same functionality as SystemInfo.supportsAsyncGPUReadback and
also mimics platform-specific behavior in the Unity Editor.  
[supportsAudio](Device.SystemInfo-supportsAudio.html)| This has the same
functionality as SystemInfo.supportsAudio and also mimics platform-specific
behavior in the Unity Editor.  
[supportsCompressed3DTextures](Device.SystemInfo-
supportsCompressed3DTextures.html)| This has the same functionality as
SystemInfo.supportsCompressed3DTextures and also mimics platform-specific
behavior in the Unity Editor.  
[supportsComputeShaders](Device.SystemInfo-supportsComputeShaders.html)| This
has the same functionality as SystemInfo.supportsComputeShaders and also
mimics platform-specific behavior in the Unity Editor.  
[supportsConservativeRaster](Device.SystemInfo-
supportsConservativeRaster.html)| This has the same functionality as
SystemInfo.supportsConservativeRaster and also mimics platform-specific
behavior in the Unity Editor.  
[supportsCubemapArrayTextures](Device.SystemInfo-
supportsCubemapArrayTextures.html)| This has the same functionality as
SystemInfo.supportsCubemapArrayTextures and also mimics platform-specific
behavior in the Unity Editor.  
[supportsDepthFetchInRenderPass](Device.SystemInfo-
supportsDepthFetchInRenderPass.html)| Indicates whether RenderPass can use its
depth attachment as input. (Read Only)  
[supportsGeometryShaders](Device.SystemInfo-supportsGeometryShaders.html)|
This has the same functionality as SystemInfo.supportsGeometryShaders and also
mimics platform-specific behavior in the Unity Editor.  
[supportsGpuRecorder](Device.SystemInfo-supportsGpuRecorder.html)| This has
the same functionality as SystemInfo.supportsGpuRecorder and also mimics
platform-specific behavior in the Unity Editor.  
[supportsGraphicsFence](Device.SystemInfo-supportsGraphicsFence.html)| This
has the same functionality as SystemInfo.supportsGraphicsFence and also mimics
platform-specific behavior in the Unity Editor.  
[supportsGyroscope](Device.SystemInfo-supportsGyroscope.html)| This has the
same functionality as SystemInfo.supportsGyroscope and also mimics platform-
specific behavior in the Unity Editor.  
[supportsHardwareQuadTopology](Device.SystemInfo-
supportsHardwareQuadTopology.html)| This has the same functionality as
SystemInfo.supportsHardwareQuadTopology and also mimics platform-specific
behavior in the Unity Editor.  
[supportsIndirectArgumentsBuffer](Device.SystemInfo-
supportsIndirectArgumentsBuffer.html)| This property has the same
functionality as SystemInfo.supportsIndirectArgumentsBuffer and also mimics
platform-specific behavior in the Unity Editor.  
[supportsIndirectDispatchRays](Device.SystemInfo-
supportsIndirectDispatchRays.html)| This property has the same functionality
as SystemInfo.supportsIndirectDispatchRays and also mimics platform-specific
behavior in the Unity Editor.  
[supportsInlineRayTracing](Device.SystemInfo-supportsInlineRayTracing.html)|
This property has the same functionality as
SystemInfo.supportsInlineRayTracing and also mimics platform-specific behavior
in the Unity Editor.  
[supportsInstancing](Device.SystemInfo-supportsInstancing.html)| This has the
same functionality as SystemInfo.supportsInstancing and also mimics platform-
specific behavior in the Unity Editor.  
[supportsLocationService](Device.SystemInfo-supportsLocationService.html)|
This has the same functionality as SystemInfo.supportsLocationService and also
mimics platform-specific behavior in the Unity Editor.  
[supportsMipStreaming](Device.SystemInfo-supportsMipStreaming.html)| This has
the same functionality as SystemInfo.supportsMipStreaming and also mimics
platform-specific behavior in the Unity Editor.  
[supportsMotionVectors](Device.SystemInfo-supportsMotionVectors.html)| This
has the same functionality as SystemInfo.supportsMotionVectors and also mimics
platform-specific behavior in the Unity Editor.  
[supportsMultisampleAutoResolve](Device.SystemInfo-
supportsMultisampleAutoResolve.html)| This has the same functionality as
SystemInfo.supportsMultisampleAutoResolve and also mimics platform-specific
behavior in the Unity Editor.  
[supportsMultisampled2DArrayTextures](Device.SystemInfo-
supportsMultisampled2DArrayTextures.html)| This has the same functionality as
SystemInfo.supportsMultisampled2DArrayTextures and also mimics platform-
specific behavior in the Unity Editor.  
[supportsMultisampledTextures](Device.SystemInfo-
supportsMultisampledTextures.html)| This has the same functionality as
SystemInfo.supportsMultisampledTextures and also mimics platform-specific
behavior in the Unity Editor.  
[supportsMultisampleResolveDepth](Device.SystemInfo-
supportsMultisampleResolveDepth.html)| This property has the same
functionality as SystemInfo.supportsMultisampleResolveDepth and also mimics
platform-specific behavior in the Unity Editor.  
[supportsMultisampleResolveStencil](Device.SystemInfo-
supportsMultisampleResolveStencil.html)| This property has the same
functionality as SystemInfo.supportsMultisampleResolveStencil and also mimics
platform-specific behavior in the Unity Editor.  
[supportsMultiview](Device.SystemInfo-supportsMultiview.html)| This has the
same functionality as SystemInfo.supportsMultiview and also mimics platform-
specific behavior in the Unity Editor.  
[supportsParallelPSOCreation](Device.SystemInfo-
supportsParallelPSOCreation.html)| This has the same functionality as
SystemInfo.supportsParallelPSOCreation and also mimics platform-specific
behavior in the Unity Editor.  
[supportsRawShadowDepthSampling](Device.SystemInfo-
supportsRawShadowDepthSampling.html)| This has the same functionality as
SystemInfo.supportsRawShadowDepthSampling and also mimics platform-specific
behavior in the Unity Editor.  
[supportsRayTracing](Device.SystemInfo-supportsRayTracing.html)| This has the
same functionality as SystemInfo.supportsRayTracing and also mimics platform-
specific behavior in the Unity Editor.  
[supportsRayTracingShaders](Device.SystemInfo-supportsRayTracingShaders.html)|
This has the same functionality as SystemInfo.supportsRayTracingShaders and
also mimics platform-specific behavior in the Unity Editor.  
[supportsRenderTargetArrayIndexFromVertexShader](Device.SystemInfo-
supportsRenderTargetArrayIndexFromVertexShader.html)| This has the same
functionality as SystemInfo.supportsRenderTargetArrayIndexFromVertexShader and
also mimics platform-specific behavior in the Unity Editor.  
[supportsSeparatedRenderTargetsBlend](Device.SystemInfo-
supportsSeparatedRenderTargetsBlend.html)| This has the same functionality as
SystemInfo.supportsSeparatedRenderTargetsBlend and also mimics platform-
specific behavior in the Unity Editor.  
[supportsSetConstantBuffer](Device.SystemInfo-supportsSetConstantBuffer.html)|
This has the same functionality as SystemInfo.supportsSetConstantBuffer and
also mimics platform-specific behavior in the Unity Editor.  
[supportsShadows](Device.SystemInfo-supportsShadows.html)| This has the same
functionality as SystemInfo.supportsShadows and also mimics platform-specific
behavior in the Unity Editor.  
[supportsSparseTextures](Device.SystemInfo-supportsSparseTextures.html)| This
has the same functionality as SystemInfo.supportsSparseTextures and also
mimics platform-specific behavior in the Unity Editor.  
[supportsStoreAndResolveAction](Device.SystemInfo-
supportsStoreAndResolveAction.html)| This property has the same functionality
as SystemInfo.supportsStoreAndResolveAction and also shows platform-specific
behavior in the Unity Editor.  
[supportsTessellationShaders](Device.SystemInfo-
supportsTessellationShaders.html)| This has the same functionality as
SystemInfo.supportsTessellationShaders and also mimics platform-specific
behavior in the Unity Editor.  
[supportsTextureWrapMirrorOnce](Device.SystemInfo-
supportsTextureWrapMirrorOnce.html)| This has the same functionality as
SystemInfo.supportsTextureWrapMirrorOnce and also mimics platform-specific
behavior in the Unity Editor.  
[supportsVibration](Device.SystemInfo-supportsVibration.html)| This has the
same functionality as SystemInfo.supportsVibration and also mimics platform-
specific behavior in the Unity Editor.  
[systemMemorySize](Device.SystemInfo-systemMemorySize.html)| This has the same
functionality as SystemInfo.systemMemorySize and also mimics platform-specific
behavior in the Unity Editor.  
[unsupportedIdentifier](Device.SystemInfo-unsupportedIdentifier.html)| This
has the same functionality as SystemInfo.unsupportedIdentifier.  
[usesLoadStoreActions](Device.SystemInfo-usesLoadStoreActions.html)| This has
the same functionality as SystemInfo.usesLoadStoreActions and also mimics
platform-specific behavior in the Unity Editor.  
[usesReversedZBuffer](Device.SystemInfo-usesReversedZBuffer.html)| This has
the same functionality as SystemInfo.usesReversedZBuffer and also mimics
platform-specific behavior in the Unity Editor.  
  
### Static Methods

[GetCompatibleFormat](Device.SystemInfo.GetCompatibleFormat.html)| This has
the same functionality as SystemInfo.GetCompatibleFormat and also mimics
platform-specific behavior in the Unity Editor.  
---|---  
[GetGraphicsFormat](Device.SystemInfo.GetGraphicsFormat.html)| This has the
same functionality as SystemInfo.GetGraphicsFormat and also mimics platform-
specific behavior in the Unity Editor.  
[GetRenderTextureSupportedMSAASampleCount](Device.SystemInfo.GetRenderTextureSupportedMSAASampleCount.html)|
This has the same functionality as
SystemInfo.GetRenderTextureSupportedMSAASampleCount and also mimics platform-
specific behavior in the Unity Editor.  
[IsFormatSupported](Device.SystemInfo.IsFormatSupported.html)| This has the
same functionality as SystemInfo.IsFormatSupported and also mimics platform-
specific behavior in the Unity Editor.  
[SupportsBlendingOnRenderTextureFormat](Device.SystemInfo.SupportsBlendingOnRenderTextureFormat.html)|
This has the same functionality as
SystemInfo.SupportsBlendingOnRenderTextureFormat and also mimics platform-
specific behavior in the Unity Editor.  
[SupportsRandomWriteOnRenderTextureFormat](Device.SystemInfo.SupportsRandomWriteOnRenderTextureFormat.html)|
This has the same functionality as
SystemInfo.SupportsRandomWriteOnRenderTextureFormat. At the moment, the Device
Simulator doesn't support simulation of this method.  
[SupportsRenderTextureFormat](Device.SystemInfo.SupportsRenderTextureFormat.html)|
This has the same functionality as SystemInfo.SupportsRenderTextureFormat and
also mimics platform-specific behavior in the Unity Editor.  
[SupportsTextureFormat](Device.SystemInfo.SupportsTextureFormat.html)| This
has the same functionality as SystemInfo.SupportsTextureFormat and also mimics
platform-specific behavior in the Unity Editor.  
[SupportsVertexAttributeFormat](Device.SystemInfo.SupportsVertexAttributeFormat.html)|
This has the same functionality as SystemInfo.SupportsVertexAttributeFormat
and also mimics platform-specific behavior in the Unity Editor.  
  
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

