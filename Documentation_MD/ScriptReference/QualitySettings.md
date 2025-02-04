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

# QualitySettings

class in UnityEngine

/

Inherits from:[Object](Object.html)

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

[Switch to Manual](../Manual/class-QualitySettings.html "Go to QualitySettings
Component in the Manual")

### Description

This represents the script interface for [Quality Settings](../Manual/class-
QualitySettings.html).

Use the `QualitySettings` class to change the current quality level at
runtime. You can check the details of quality settings in your project's
[Quality Settings](../Manual/class-QualitySettings.html).

### Static Properties

[activeColorSpace](QualitySettings-activeColorSpace.html)| Active color space
(Read Only).  
---|---  
[anisotropicFiltering](QualitySettings-anisotropicFiltering.html)| Global
anisotropic filtering mode.  
[antiAliasing](QualitySettings-antiAliasing.html)| Choose the level of Multi-
Sample Anti-aliasing (MSAA) that the GPU performs.  
[asyncUploadBufferSize](QualitySettings-asyncUploadBufferSize.html)|
Asynchronous texture and mesh data upload provides timesliced async texture
and mesh data upload on the render thread with tight control over memory and
timeslicing. There are no allocations except for the ones which driver has to
do. To read data and upload texture and mesh data, Unity re-uses a ringbuffer
whose size can be controlled.Use asyncUploadBufferSize to set the buffer size
for asynchronous texture and mesh data uploads. The minimum value is 2
megabytes and the maximum value is 2047 megabytes. The buffer resizes
automatically to fit the largest texture currently loading. To avoid a buffer
resize (which can use extra system resources) set this value to the size of
the largest texture in the Scene. If you have issues with excessive memory
usage, you may need to reduce the value of this buffer or disable
asyncUploadPersistentBuffer. Memory fragmentation can occur if you choose the
latter option.  
[asyncUploadPersistentBuffer](QualitySettings-
asyncUploadPersistentBuffer.html)| This flag controls if the async upload
pipeline's ring buffer remains allocated when there are no active loading
operations. Set this to true, to make the ring buffer allocation persist after
all upload operations have completed. If you have issues with excessive memory
usage, you can set this to false. This means you reduce the runtime memory
footprint, but memory fragmentation can occur. The default value is true.  
[asyncUploadTimeSlice](QualitySettings-asyncUploadTimeSlice.html)| Async
texture upload provides timesliced async texture upload on the render thread
with tight control over memory and timeslicing. There are no allocations
except for the ones which driver has to do. To read data and upload texture
data a ringbuffer whose size can be controlled is re-used.Use
asyncUploadTimeSlice to set the time-slice in milliseconds for asynchronous
texture uploads per frame. Minimum value is 1 and maximum is 33.  
[billboardsFaceCameraPosition](QualitySettings-
billboardsFaceCameraPosition.html)| If enabled, billboards will face towards
camera position rather than camera orientation.  
[count](QualitySettings-count.html)| The number of Quality Levels.  
[desiredColorSpace](QualitySettings-desiredColorSpace.html)| Desired color
space (Read Only).  
[enableLODCrossFade](QualitySettings-enableLODCrossFade.html)| Enables or
disables LOD Cross Fade.  
[globalTextureMipmapLimit](QualitySettings-globalTextureMipmapLimit.html)|
Indicates how many of the highest-resolution mips of each texture Unity does
not upload at the given quality level. To set more specific mipmap limits, you
can flag textures to ignore mipmap limits or assign them to mipmap limit
groups.  
[lodBias](QualitySettings-lodBias.html)| Global multiplier for the LOD's
switching distance.  
[maximumLODLevel](QualitySettings-maximumLODLevel.html)| A maximum LOD level.
All LOD groups.  
[maxQueuedFrames](QualitySettings-maxQueuedFrames.html)| Maximum number of
frames queued up by graphics driver.  
[names](QualitySettings-names.html)| The indexed list of available Quality
Settings.  
[particleRaycastBudget](QualitySettings-particleRaycastBudget.html)| Budget
for how many ray casts can be performed per frame for approximate collision
testing.  
[pixelLightCount](QualitySettings-pixelLightCount.html)| The maximum number of
pixel lights that should affect any object.  
[realtimeGICPUUsage](QualitySettings-realtimeGICPUUsage.html)| How much CPU
usage to assign to the final lighting calculations at runtime.  
[realtimeReflectionProbes](QualitySettings-realtimeReflectionProbes.html)|
Enables or disables real-time reflection probes.  
[renderPipeline](QualitySettings-renderPipeline.html)| The RenderPipelineAsset
that defines the override render pipeline for the current quality level.  
[resolutionScalingFixedDPIFactor](QualitySettings-
resolutionScalingFixedDPIFactor.html)| In resolution scaling mode, this factor
is used to multiply with the target Fixed DPI specified to get the actual
Fixed DPI to use for this quality setting.  
[shadowCascade2Split](QualitySettings-shadowCascade2Split.html)| The
normalized cascade distribution for a 2 cascade setup. The value defines the
position of the cascade with respect to Zero.  
[shadowCascade4Split](QualitySettings-shadowCascade4Split.html)| The
normalized cascade start position for a 4 cascade setup. Each member of the
vector defines the normalized position of the coresponding cascade with
respect to Zero.  
[shadowCascades](QualitySettings-shadowCascades.html)| Number of cascades to
use for directional light shadows.  
[shadowDistance](QualitySettings-shadowDistance.html)| Shadow drawing
distance.  
[shadowmaskMode](QualitySettings-shadowmaskMode.html)| The rendering mode of
Shadowmask.  
[shadowNearPlaneOffset](QualitySettings-shadowNearPlaneOffset.html)| Offset
shadow frustum near plane.  
[shadowProjection](QualitySettings-shadowProjection.html)| Directional light
shadow projection.  
[shadowResolution](QualitySettings-shadowResolution.html)| The default
resolution of the shadow maps.  
[shadows](QualitySettings-shadows.html)| Real-time Shadows type to be used.  
[skinWeights](QualitySettings-skinWeights.html)| The maximum number of bones
per vertex that are taken into account during skinning, for all meshes in the
project.  
[softParticles](QualitySettings-softParticles.html)| Should soft blending be
used for particles?  
[softVegetation](QualitySettings-softVegetation.html)| Use a two-pass shader
for the vegetation in the terrain engine.  
[streamingMipmapsActive](QualitySettings-streamingMipmapsActive.html)| Enable
automatic streaming of texture mipmap levels based on their distance from all
active cameras.  
[streamingMipmapsAddAllCameras](QualitySettings-
streamingMipmapsAddAllCameras.html)| Process all enabled Cameras for texture
streaming (rather than just those with StreamingController components).  
[streamingMipmapsMaxFileIORequests](QualitySettings-
streamingMipmapsMaxFileIORequests.html)| The maximum number of active texture
file IO requests from the texture streaming system.  
[streamingMipmapsMaxLevelReduction](QualitySettings-
streamingMipmapsMaxLevelReduction.html)| The maximum number of mipmap levels
to discard for each texture.  
[streamingMipmapsMemoryBudget](QualitySettings-
streamingMipmapsMemoryBudget.html)| The total amount of memory (in megabytes)
to be used by streaming and non-streaming textures.  
[streamingMipmapsRenderersPerFrame](QualitySettings-
streamingMipmapsRenderersPerFrame.html)| The number of renderer instances that
are processed each frame when calculating which texture mipmap levels should
be streamed.  
[terrainBasemapDistance](QualitySettings-terrainBasemapDistance.html)| Value
set to Terrain.basemapDistance if TerrainQualityOverrides.BasemapDistance is
set in terrainQualityOverrides.  
[terrainBillboardStart](QualitySettings-terrainBillboardStart.html)| Value set
to Terrain.treeBillboardDistance if TerrainQualityOverrides.BillboardStart is
set in terrainQualityOverrides.  
[terrainDetailDensityScale](QualitySettings-terrainDetailDensityScale.html)|
Value set to Terrain.detailObjectDensity if
TerrainQualityOverrides.DetailDensity is set in terrainQualityOverrides.  
[terrainDetailDistance](QualitySettings-terrainDetailDistance.html)| Value set
to Terrain.detailObjectDistance if TerrainQualityOverrides.DetailDistance is
set in terrainQualityOverrides.  
[terrainFadeLength](QualitySettings-terrainFadeLength.html)| Value set to
Terrain.treeCrossFadeLength if TerrainQualityOverrides.FadeLength is set in
terrainQualityOverrides.  
[terrainMaxTrees](QualitySettings-terrainMaxTrees.html)| Value set to
Terrain.treeMaximumFullLODCount if TerrainQualityOverrides.MaxTrees is set in
terrainQualityOverrides.  
[terrainPixelError](QualitySettings-terrainPixelError.html)| Value set to
Terrain.heightmapPixelError if TerrainQualityOverrides.PixelError is set in
terrainQualityOverrides.  
[terrainQualityOverrides](QualitySettings-terrainQualityOverrides.html)|
Controls which fields should have their values overriden in active Terrains.  
[terrainTreeDistance](QualitySettings-terrainTreeDistance.html)| Value set to
Terrain.treeDistance if TerrainQualityOverrides.TreeDistance is set in
terrainQualityOverrides.  
[useLegacyDetailDistribution](QualitySettings-
useLegacyDetailDistribution.html)| Use the legacy pre-2022.2 algorithm for
distributing details on terrain.  
[vSyncCount](QualitySettings-vSyncCount.html)| Represents the number of
vertical syncs that should pass between each frame.  
  
### Static Methods

[DecreaseLevel](QualitySettings.DecreaseLevel.html)| Decrease the current
quality level.  
---|---  
[ForEach](QualitySettings.ForEach.html)| Executes the given Action for each
tier on the QualitySettings.  
[GetActiveQualityLevelsForPlatform](QualitySettings.GetActiveQualityLevelsForPlatform.html)|
[Editor Only] Obtains an array with the Quality Level indexes that are
selected for the given platform.  
[GetActiveQualityLevelsForPlatformCount](QualitySettings.GetActiveQualityLevelsForPlatformCount.html)|
[Editor Only] Obtains the number of Quality Levels that are selected for a
given platform.  
[GetAllRenderPipelineAssetsForPlatform](QualitySettings.GetAllRenderPipelineAssetsForPlatform.html)|
[Editor Only] Fills the given list with all the Render Pipeline Assets on any
Quality Level for the given platform. Without filtering by Render Pipeline
Asset type or null.  
[GetQualityLevel](QualitySettings.GetQualityLevel.html)| Returns the current
graphics quality level.  
[GetQualitySettings](QualitySettings.GetQualitySettings.html)| Provides a
reference to the QualitySettings object.  
[GetRenderPipelineAssetAt](QualitySettings.GetRenderPipelineAssetAt.html)|
Provides a reference to the RenderPipelineAsset that defines the override
render pipeline for a given quality level.  
[GetRenderPipelineAssetsForPlatform](QualitySettings.GetRenderPipelineAssetsForPlatform.html)|
[Editor Only] Obtains a set with the non null Render Pipeline Assets selected
on all the Quality Levels for the given platform.  
[GetTextureMipmapLimitSettings](QualitySettings.GetTextureMipmapLimitSettings.html)|
Retrieves a copy of the TextureMipmapLimitSettings from a texture mipmap limit
group.  
[IncreaseLevel](QualitySettings.IncreaseLevel.html)| Increase the current
quality level.  
[IsPlatformIncluded](QualitySettings.IsPlatformIncluded.html)| [Editor Only]
Returns if the given platform is included by the Quality Level.  
[SetLODSettings](QualitySettings.SetLODSettings.html)| Sets the lodBias and
maximumLODLevel at the same time.  
[SetQualityLevel](QualitySettings.SetQualityLevel.html)| Sets a new graphics
quality level.  
[SetTextureMipmapLimitSettings](QualitySettings.SetTextureMipmapLimitSettings.html)|
Applies new TextureMipmapLimitSettings to the indicated texture mipmap limit
group.  
[TryExcludePlatformAt](QualitySettings.TryExcludePlatformAt.html)| [Editor
Only] Excludes a platform for the given Quality Level.  
[TryIncludePlatformAt](QualitySettings.TryIncludePlatformAt.html)| [Editor
Only] Includes a platform to be supported by the Quality Level.  
  
### Events

[activeQualityLevelChanged](QualitySettings-activeQualityLevelChanged.html)|
Delegate that you can use to invoke custom code when Unity changes the current
Quality Level.  
---|---  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

