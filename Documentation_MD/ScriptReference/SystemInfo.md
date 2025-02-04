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

class in UnityEngine

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

Access system and hardware information.

Use this class to figure out capabilities of the underlying platform and
hardware. For example, you can check which [RenderTexture](RenderTexture.html)
formats are supported
([SupportsRenderTextureFormat](SystemInfo.SupportsRenderTextureFormat.html)),
how many CPU threads are available ([processorCount](SystemInfo-
processorCount.html)), and so on.

### Static Properties

[batteryLevel](SystemInfo-batteryLevel.html)| The current battery level (Read
Only).  
---|---  
[batteryStatus](SystemInfo-batteryStatus.html)| Returns the current status of
the device's battery (Read Only).  
[computeSubGroupSize](SystemInfo-computeSubGroupSize.html)| Size of the
compute thread group that supports efficient memory sharing on the GPU (Read
Only).  
[constantBufferOffsetAlignment](SystemInfo-
constantBufferOffsetAlignment.html)| Minimum buffer offset (in bytes) when
binding a constant buffer using Shader.SetConstantBuffer or
Material.SetConstantBuffer.  
[copyTextureSupport](SystemInfo-copyTextureSupport.html)| Support for various
Graphics.CopyTexture cases (Read Only).  
[deviceModel](SystemInfo-deviceModel.html)| The model of the device (Read
Only).  
[deviceName](SystemInfo-deviceName.html)| The user defined name of the device
(Read Only).  
[deviceType](SystemInfo-deviceType.html)| Returns the kind of device the
application is running on (Read Only).  
[deviceUniqueIdentifier](SystemInfo-deviceUniqueIdentifier.html)| A unique
device identifier. It's guaranteed to be unique for every device (Read Only).  
[foveatedRenderingCaps](SystemInfo-foveatedRenderingCaps.html)| The foveated
rendering technique supported on this platform.  
[graphicsDeviceID](SystemInfo-graphicsDeviceID.html)| The identifier code of
the graphics device (Read Only).  
[graphicsDeviceName](SystemInfo-graphicsDeviceName.html)| The name of the
graphics device (Read Only).  
[graphicsDeviceType](SystemInfo-graphicsDeviceType.html)| The graphics API
type used by the graphics device (Read Only).  
[graphicsDeviceVendor](SystemInfo-graphicsDeviceVendor.html)| The vendor of
the graphics device (Read Only).  
[graphicsDeviceVendorID](SystemInfo-graphicsDeviceVendorID.html)| The
identifier code of the graphics device vendor (Read Only).  
[graphicsDeviceVersion](SystemInfo-graphicsDeviceVersion.html)| The graphics
API type and driver version used by the graphics device (Read Only).  
[graphicsMemorySize](SystemInfo-graphicsMemorySize.html)| Amount of video
memory present (Read Only).  
[graphicsMultiThreaded](SystemInfo-graphicsMultiThreaded.html)| Is graphics
device using multi-threaded rendering (Read Only)?  
[graphicsShaderLevel](SystemInfo-graphicsShaderLevel.html)| Graphics device
shader capability level (Read Only).  
[graphicsUVStartsAtTop](SystemInfo-graphicsUVStartsAtTop.html)| Returns true
if the texture UV coordinate convention for this platform has Y starting at
the top of the image.  
[hasDynamicUniformArrayIndexingInFragmentShaders](SystemInfo-
hasDynamicUniformArrayIndexingInFragmentShaders.html)| Returns true when the
GPU has native support for indexing uniform arrays in fragment shaders without
restrictions.  
[hasHiddenSurfaceRemovalOnGPU](SystemInfo-hasHiddenSurfaceRemovalOnGPU.html)|
True if the GPU supports hidden surface removal.  
[hasMipMaxLevel](SystemInfo-hasMipMaxLevel.html)| Returns true if the GPU
supports partial mipmap chains (Read Only).  
[hdrDisplaySupportFlags](SystemInfo-hdrDisplaySupportFlags.html)| Returns a
bitwise combination of HDRDisplaySupportFlags describing the support for HDR
displays on the system.  
[maxAnisotropyLevel](SystemInfo-maxAnisotropyLevel.html)| Returns the maximum
anisotropic level for anisotropic filtering that is supported on the device.  
[maxComputeBufferInputsCompute](SystemInfo-
maxComputeBufferInputsCompute.html)| Determines how many compute buffers Unity
supports simultaneously in a compute shader for reading. (Read Only)  
[maxComputeBufferInputsDomain](SystemInfo-maxComputeBufferInputsDomain.html)|
Determines how many compute buffers Unity supports simultaneously in a domain
shader for reading. (Read Only)  
[maxComputeBufferInputsFragment](SystemInfo-
maxComputeBufferInputsFragment.html)| Determines how many compute buffers
Unity supports simultaneously in a fragment shader for reading. (Read Only)  
[maxComputeBufferInputsGeometry](SystemInfo-
maxComputeBufferInputsGeometry.html)| Determines how many compute buffers
Unity supports simultaneously in a geometry shader for reading. (Read Only)  
[maxComputeBufferInputsHull](SystemInfo-maxComputeBufferInputsHull.html)|
Determines how many compute buffers Unity supports simultaneously in a hull
shader for reading. (Read Only)  
[maxComputeBufferInputsVertex](SystemInfo-maxComputeBufferInputsVertex.html)|
Determines how many compute buffers Unity supports simultaneously in a vertex
shader for reading. (Read Only)  
[maxComputeWorkGroupSize](SystemInfo-maxComputeWorkGroupSize.html)| The
largest total number of invocations in a single local work group that can be
dispatched to a compute shader (Read Only).  
[maxComputeWorkGroupSizeX](SystemInfo-maxComputeWorkGroupSizeX.html)| The
maximum number of work groups that a compute shader can use in X dimension
(Read Only).  
[maxComputeWorkGroupSizeY](SystemInfo-maxComputeWorkGroupSizeY.html)| The
maximum number of work groups that a compute shader can use in Y dimension
(Read Only).  
[maxComputeWorkGroupSizeZ](SystemInfo-maxComputeWorkGroupSizeZ.html)| The
maximum number of work groups that a compute shader can use in Z dimension
(Read Only).  
[maxConstantBufferSize](SystemInfo-maxConstantBufferSize.html)| The maximum
size of a constant buffer binding (Read Only).  
[maxCubemapSize](SystemInfo-maxCubemapSize.html)| Maximum cubemap texture size
in pixels (Read Only).  
[maxGraphicsBufferSize](SystemInfo-maxGraphicsBufferSize.html)| The maximum
size of a graphics buffer (GraphicsBuffer, ComputeBuffer, vertex/index buffer,
etc.) in bytes (Read Only).  
[maxTexture3DSize](SystemInfo-maxTexture3DSize.html)| Maximum 3D texture size
in pixels (Read Only).  
[maxTextureArraySlices](SystemInfo-maxTextureArraySlices.html)| Maximum number
of slices in a Texture array (Read Only).  
[maxTextureSize](SystemInfo-maxTextureSize.html)| Maximum texture size in
pixels (Read Only).  
[npotSupport](SystemInfo-npotSupport.html)| What NPOT (non-power of two size)
texture support does the GPU provide? (Read Only)  
[operatingSystem](SystemInfo-operatingSystem.html)| Operating system name with
version (Read Only).  
[operatingSystemFamily](SystemInfo-operatingSystemFamily.html)| Returns the
operating system family the game is running on (Read Only).  
[processorCount](SystemInfo-processorCount.html)| Number of processors present
(Read Only).  
[processorFrequency](SystemInfo-processorFrequency.html)| Processor frequency
in MHz (Read Only).  
[processorManufacturer](SystemInfo-processorManufacturer.html)| Specifies the
manufacturer name of the processor in the user's device (Read Only).  
[processorModel](SystemInfo-processorModel.html)| Specifies the model name of
the processor in the user's device (Read Only).  
[processorType](SystemInfo-processorType.html)| Processor name (Read Only).  
[renderingThreadingMode](SystemInfo-renderingThreadingMode.html)|
Application's actual rendering threading mode (Read Only).  
[supportedRandomWriteTargetCount](SystemInfo-
supportedRandomWriteTargetCount.html)| The maximum number of random write
targets (UAV) that Unity supports simultaneously. (Read Only)  
[supportedRenderTargetCount](SystemInfo-supportedRenderTargetCount.html)| How
many simultaneous render targets (MRTs) are supported? (Read Only)  
[supports2DArrayTextures](SystemInfo-supports2DArrayTextures.html)| Are 2D
Array textures supported? (Read Only)  
[supports32bitsIndexBuffer](SystemInfo-supports32bitsIndexBuffer.html)| Are
32-bit index buffers supported? (Read Only)  
[supports3DRenderTextures](SystemInfo-supports3DRenderTextures.html)| Are 3D
(volume) RenderTextures supported? (Read Only)  
[supports3DTextures](SystemInfo-supports3DTextures.html)| Are 3D (volume)
textures supported? (Read Only)  
[supportsAccelerometer](SystemInfo-supportsAccelerometer.html)| Is an
accelerometer available on the device?  
[supportsAnisotropicFilter](SystemInfo-supportsAnisotropicFilter.html)|
Returns true when anisotropic filtering is supported on the device.  
[supportsAsyncCompute](SystemInfo-supportsAsyncCompute.html)| Returns true
when the platform supports asynchronous compute queues and false if otherwise.  
[supportsAsyncGPUReadback](SystemInfo-supportsAsyncGPUReadback.html)| Returns
true if asynchronous readback of GPU data is available for this device and
false otherwise.  
[supportsAudio](SystemInfo-supportsAudio.html)| Is there an Audio device
available for playback? (Read Only)  
[supportsCompressed3DTextures](SystemInfo-supportsCompressed3DTextures.html)|
Are compressed formats for 3D (volume) textures supported? (Read Only).  
[supportsComputeShaders](SystemInfo-supportsComputeShaders.html)| Are compute
shaders supported? (Read Only)  
[supportsConservativeRaster](SystemInfo-supportsConservativeRaster.html)| Is
conservative rasterization supported? (Read Only)  
[supportsCubemapArrayTextures](SystemInfo-supportsCubemapArrayTextures.html)|
Are Cubemap Array textures supported? (Read Only)  
[supportsDepthFetchInRenderPass](SystemInfo-
supportsDepthFetchInRenderPass.html)| Indicates whether RenderPass can use its
depth attachment as input. (Read Only)  
[supportsGeometryShaders](SystemInfo-supportsGeometryShaders.html)| Are
geometry shaders supported? (Read Only)  
[supportsGpuRecorder](SystemInfo-supportsGpuRecorder.html)| Specifies whether
the current platform supports the GPU Recorder or not. (Read Only).  
[supportsGraphicsFence](SystemInfo-supportsGraphicsFence.html)|  true if the
platform supports GraphicsFences, otherwise false.  
[supportsGyroscope](SystemInfo-supportsGyroscope.html)| Is a gyroscope
available on the device?  
[supportsHardwareQuadTopology](SystemInfo-supportsHardwareQuadTopology.html)|
Does the hardware support quad topology? (Read Only)  
[supportsIndirectArgumentsBuffer](SystemInfo-
supportsIndirectArgumentsBuffer.html)| Returns true if the graphics system
supports GPU draw calls with indirect argument buffers. (Read Only)  
[supportsIndirectDispatchRays](SystemInfo-supportsIndirectDispatchRays.html)|
Returns true if the graphics system supports indirect ray tracing dispatch.
(Read Only)  
[supportsInlineRayTracing](SystemInfo-supportsInlineRayTracing.html)| Is
inline ray tracing (ray query) supported? (Read Only)  
[supportsInstancing](SystemInfo-supportsInstancing.html)| Is GPU draw call
instancing supported? (Read Only)  
[supportsLocationService](SystemInfo-supportsLocationService.html)| Is the
device capable of reporting its location?  
[supportsMipStreaming](SystemInfo-supportsMipStreaming.html)| Is streaming of
texture mip maps supported? (Read Only)  
[supportsMotionVectors](SystemInfo-supportsMotionVectors.html)| Whether motion
vectors are supported on this platform.  
[supportsMultisampleAutoResolve](SystemInfo-
supportsMultisampleAutoResolve.html)| Returns true if multisampled textures
are resolved automatically  
[supportsMultisampled2DArrayTextures](SystemInfo-
supportsMultisampled2DArrayTextures.html)| Boolean that indicates whether
multisampled texture arrays are supported (true if supported, false if not
supported).  
[supportsMultisampledTextures](SystemInfo-supportsMultisampledTextures.html)|
Returns a value of 1 or higher if multisampled textures are supported. (Read
Only)  
[supportsMultisampleResolveDepth](SystemInfo-
supportsMultisampleResolveDepth.html)| Returns true if the platform supports
multisample resolve of depth textures.  
[supportsMultisampleResolveStencil](SystemInfo-
supportsMultisampleResolveStencil.html)| Returns true if the platform supports
multisample resolve of stencil textures. Otherwise, returns false.  
[supportsMultiview](SystemInfo-supportsMultiview.html)| Boolean that indicates
whether Multiview is supported (true if supported, false if not supported).
(Read Only)  
[supportsParallelPSOCreation](SystemInfo-supportsParallelPSOCreation.html)|
Returns true if parallel PSO creation is available for this device and false
otherwise.  
[supportsRawShadowDepthSampling](SystemInfo-
supportsRawShadowDepthSampling.html)| Is sampling raw depth from shadowmaps
supported? (Read Only)  
[supportsRayTracing](SystemInfo-supportsRayTracing.html)| Checks if any ray
tracing features are supported by the current system configuration. (Read
Only)  
[supportsRayTracingShaders](SystemInfo-supportsRayTracingShaders.html)| Checks
if ray tracing shaders are supported by the current system configuration.
(Read Only)  
[supportsRenderTargetArrayIndexFromVertexShader](SystemInfo-
supportsRenderTargetArrayIndexFromVertexShader.html)| Boolean that indicates
if SV_RenderTargetArrayIndex can be used in a vertex shader (true if it can be
used, false if not).  
[supportsSeparatedRenderTargetsBlend](SystemInfo-
supportsSeparatedRenderTargetsBlend.html)| Returns true when the platform
supports different blend modes when rendering to multiple render targets, or
false otherwise.  
[supportsSetConstantBuffer](SystemInfo-supportsSetConstantBuffer.html)| Does
the current renderer support binding constant buffers directly? (Read Only)  
[supportsShadows](SystemInfo-supportsShadows.html)| Are built-in shadows
supported? (Read Only)  
[supportsSparseTextures](SystemInfo-supportsSparseTextures.html)| Are sparse
textures supported? (Read Only)  
[supportsStoreAndResolveAction](SystemInfo-
supportsStoreAndResolveAction.html)| This property is true if the graphics API
of the target build platform takes RenderBufferStoreAction.StoreAndResolve
into account, false if otherwise.  
[supportsTessellationShaders](SystemInfo-supportsTessellationShaders.html)|
Are tessellation shaders supported? (Read Only)  
[supportsTextureWrapMirrorOnce](SystemInfo-
supportsTextureWrapMirrorOnce.html)| Returns a value of 1 or higher if the
'Mirror Once' texture wrap mode is supported. (Read Only)  
[supportsVibration](SystemInfo-supportsVibration.html)| Is the device capable
of providing the user haptic feedback by vibration?  
[systemMemorySize](SystemInfo-systemMemorySize.html)| Amount of system memory
present (Read Only).  
[unsupportedIdentifier](SystemInfo-unsupportedIdentifier.html)| Value returned
by SystemInfo string properties which are not supported on the current
platform.  
[usesLoadStoreActions](SystemInfo-usesLoadStoreActions.html)| True if the
Graphics API takes RenderBufferLoadAction and RenderBufferStoreAction into
account, false if otherwise.  
[usesReversedZBuffer](SystemInfo-usesReversedZBuffer.html)| This property is
true if the current platform uses a reversed depth buffer (where values range
from 1 at the near plane and 0 at far plane), and false if the depth buffer is
normal (0 is near, 1 is far). (Read Only)  
  
### Static Methods

[GetCompatibleFormat](SystemInfo.GetCompatibleFormat.html)| Returns a format
supported by the platform for the specified usage.  
---|---  
[GetGraphicsFormat](SystemInfo.GetGraphicsFormat.html)| Returns the platform-
specific GraphicsFormat that is associated with the DefaultFormat.  
[GetRenderTextureSupportedMSAASampleCount](SystemInfo.GetRenderTextureSupportedMSAASampleCount.html)|
Checks if the target platform supports the MSAA samples count in the
RenderTextureDescriptor argument.  
[IsFormatSupported](SystemInfo.IsFormatSupported.html)| Verifies that the
specified graphics format is supported for the specified usage.  
[SupportsBlendingOnRenderTextureFormat](SystemInfo.SupportsBlendingOnRenderTextureFormat.html)|
Is blending supported on render texture format?  
[SupportsRandomWriteOnRenderTextureFormat](SystemInfo.SupportsRandomWriteOnRenderTextureFormat.html)|
Tests if a RenderTextureFormat can be used with
RenderTexture.enableRandomWrite.  
[SupportsRenderTextureFormat](SystemInfo.SupportsRenderTextureFormat.html)| Is
render texture format supported?  
[SupportsTextureFormat](SystemInfo.SupportsTextureFormat.html)| Is texture
format supported on this device?  
[SupportsVertexAttributeFormat](SystemInfo.SupportsVertexAttributeFormat.html)|
Indicates whether the given combination of a vertex attribute format and
dimension is supported on this device.  
  
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

