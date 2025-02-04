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

# Lightmapping

class in UnityEditor

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

Allows to control the lightmapping job.

Before starting the job the bake settings can be set via
[LightingSettings](LightingSettings.html).  
  
Additional resources: [LightingSettings](LightingSettings.html).

### Static Properties

[bakedGI](Lightmapping-bakedGI.html)| This property is now obsolete. Use
LightingSettings.bakedGI.  
---|---  
[bakeOnSceneLoad](Lightmapping-bakeOnSceneLoad.html)| Determines whether
lighting data should be generated when loading a scene, for scenes that have
not already been baked.  
[buildProgress](Lightmapping-buildProgress.html)| Returns the current
lightmapping build progress or 0 if Lightmapping.isRunning is false.  
[isRunning](Lightmapping-isRunning.html)| Returns true when the bake job is
running, false otherwise (Read Only).  
[lightingDataAsset](Lightmapping-lightingDataAsset.html)| The lighting data
asset used by the active Scene.  
[lightingSettings](Lightmapping-lightingSettings.html)| The LightingSettings
that will be used for the current Scene. Will throw an exception if it is
null.  
[lightingSettingsDefaults](Lightmapping-lightingSettingsDefaults.html)|
Default LightingSettings that Unity uses for Scenes where lightingSettings is
not assigned. (Read only)  
[realtimeGI](Lightmapping-realtimeGI.html)| This property is now obsolete. Use
LightingSettings.realtimeGI.  
  
### Static Methods

[Bake](Lightmapping.Bake.html)| Starts a synchronous bake job.  
---|---  
[BakeAsync](Lightmapping.BakeAsync.html)| Starts an asynchronous bake job.  
[BakeMultipleScenes](Lightmapping.BakeMultipleScenes.html)| Bakes an array of
Scenes.  
[BakeReflectionProbe](Lightmapping.BakeReflectionProbe.html)| Starts a
synchronous bake job for the probe.  
[Cancel](Lightmapping.Cancel.html)| Cancels the currently running asynchronous
bake job.  
[Clear](Lightmapping.Clear.html)| Deletes all runtime data for the currently
loaded Scenes.  
[ClearDiskCache](Lightmapping.ClearDiskCache.html)| Clears the cache used by
lightmaps, reflection probes and default reflection.  
[ClearLightingDataAsset](Lightmapping.ClearLightingDataAsset.html)| For the
currently loaded Scenes, this method deletes the Lighting Data Asset and any
linked lightmaps and Reflection Probe assets.  
[GetAdditionalBakeDelegate](Lightmapping.GetAdditionalBakeDelegate.html)| Get
the currently set additional bake delegate.  
[GetLightingSettingsForScene](Lightmapping.GetLightingSettingsForScene.html)|
Gets the LightingSettings object of a Scene object.  
[GetTerrainGIChunks](Lightmapping.GetTerrainGIChunks.html)| Get how many
chunks the terrain is divided into for GI baking.  
[ResetAdditionalBakeDelegate](Lightmapping.ResetAdditionalBakeDelegate.html)|
Resets the additional bake delegate to Unity's default.  
[SetAdditionalBakeDelegate](Lightmapping.SetAdditionalBakeDelegate.html)| Set
a delegate that bakes additional data. This delegates must set its done
parameter to true once baking is finished to unlock the baking pipeline. Must
be reset by calling ResetDelegate again.  
[SetLightingSettingsForScene](Lightmapping.SetLightingSettingsForScene.html)|
Applies the settings specified in the LightingSettings object to the Scene
object.  
[SetLightingSettingsForScenes](Lightmapping.SetLightingSettingsForScenes.html)|
Applies the settings specified in the LightingSettings object to an array of
Scene objects.  
[Tetrahedralize](Lightmapping.Tetrahedralize.html)| Calculates tetrahderons
from positions using Delaunay Tetrahedralization.  
[TryGetLightingSettings](Lightmapping.TryGetLightingSettings.html)| Fetches
the Lighting Settings for the current Scene. Will return false if it is null.  
  
### Events

[bakeCancelled](Lightmapping-bakeCancelled.html)| Event which is called when
bake job is cancelled.  
---|---  
[bakeCompleted](Lightmapping-bakeCompleted.html)| Event which is called when
bake job is completed. Only called when LightingSettings.autoGenerate is set
to false.  
[bakeStarted](Lightmapping-bakeStarted.html)| Event which is called when a
bake is started. Only called when LightingSettings.autoGenerate is set to
false.  
[lightingDataAssetCleared](Lightmapping-lightingDataAssetCleared.html)| Event
which is called when a LightingData asset is removed from the project.  
[lightingDataCleared](Lightmapping-lightingDataCleared.html)| Event which is
called when baked Global Illumination data is cleared from the scene and from
renderers.  
[lightingDataUpdated](Lightmapping-lightingDataUpdated.html)| Event which is
called when any lighting data is updated as part of the GI backing process.  
[started](Lightmapping-started.html)| Delegate which is called when bake job
is started.  
  
### Delegates

[AdditionalBakeDelegate](Lightmapping.AdditionalBakeDelegate.html)| Delegate
called at the last stage of the baking pipeline.  
---|---  
[OnCompletedFunction](Lightmapping.OnCompletedFunction.html)| Delegate used by
Lightmapping.completed callback.  
[OnStartedFunction](Lightmapping.OnStartedFunction.html)| Delegate used by
Lightmapping.started callback.  
  
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

