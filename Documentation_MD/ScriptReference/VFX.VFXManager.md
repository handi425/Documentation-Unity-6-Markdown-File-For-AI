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

# VFXManager

class in UnityEngine.VFX

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

Use this class to set a number of properties that control VisualEffect
behavior within your Unity Project.

### Static Properties

[fixedTimeStep](VFX.VFXManager-fixedTimeStep.html)| The fixed interval in
which the frame rate updates. The tick rate is in seconds.  
---|---  
[maxDeltaTime](VFX.VFXManager-maxDeltaTime.html)| The maximum allowed delta
time for an update interval. This limit affects fixedDeltaTime and deltaTime.
The tick rate is in seconds.  
  
### Static Methods

[FlushEmptyBatches](VFX.VFXManager.FlushEmptyBatches.html)| Deallocates all
empty batches used in the VFX runtime.  
---|---  
[GetBatchedEffectInfo](VFX.VFXManager.GetBatchedEffectInfo.html)| Gets
information on how a Visual Effect Asset is batched.  
[GetBatchedEffectInfos](VFX.VFXManager.GetBatchedEffectInfos.html)| Gets batch
information of all active Visual Effect Assets.  
[IsCameraBufferNeeded](VFX.VFXManager.IsCameraBufferNeeded.html)| Queries
which buffers the VFX Manager needs for the given Camera.  
[PrepareCamera](VFX.VFXManager.PrepareCamera.html)| Use this method to prepare
per-Camera VFX commands for this frame.  
[ProcessCameraCommand](VFX.VFXManager.ProcessCameraCommand.html)| Use this
method to process per-Camera VFX commands for the current frame.  
[RequestRtasAabbConstruction](VFX.VFXManager.RequestRtasAabbConstruction.html)|
Request the construction of AABB buffers by the Visual Effects for the current
frame.  
[SetCameraBuffer](VFX.VFXManager.SetCameraBuffer.html)| Use this method to set
the buffer of a given type for this Camera. This allows the VFX Manager to use
the buffer.  
[SetRayTracingEnabled](VFX.VFXManager.SetRayTracingEnabled.html)| Enables or
disables Ray Tracing for all Visual Effects.  
  
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

