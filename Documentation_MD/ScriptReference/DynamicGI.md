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

# DynamicGI

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

Allows to control the dynamic Global Illumination.

Additional resources:
[RendererExtensions.UpdateGIMaterials](RendererExtensions.UpdateGIMaterials.html),
[TerrainExtensions.UpdateGIMaterials](TerrainExtensions.UpdateGIMaterials.html).

### Static Properties

[indirectScale](DynamicGI-indirectScale.html)| Allows for scaling the
contribution coming from real-time & baked lightmaps.Note: this value can be
set in the Lighting Window UI and it is serialized, that is not the case for
other properties in this class.  
---|---  
[isConverged](DynamicGI-isConverged.html)| Is precomputed Enlighten Realtime
Global Illumination output converged?  
[materialUpdateTimeSlice](DynamicGI-materialUpdateTimeSlice.html)| The number
of milliseconds that can be spent on material updates.  
[synchronousMode](DynamicGI-synchronousMode.html)| When enabled, new dynamic
Global Illumination output is shown in each frame.  
[updateThreshold](DynamicGI-updateThreshold.html)| Determines the percentage
change in lighting intensity that triggers Unity to recalculate the real-time
lightmap.  
  
### Static Methods

[SetEmissive](DynamicGI.SetEmissive.html)| Allows to set an emissive color for
a given renderer quickly, without the need to render the emissive input for
the entire system.  
---|---  
[SetEnvironmentData](DynamicGI.SetEnvironmentData.html)| Allows overriding the
distant environment lighting for Enlighten Realtime Global Illumination,
without changing the Skybox Material.  
[UpdateEnvironment](DynamicGI.UpdateEnvironment.html)| Schedules an update of
the environment cubemap.  
[UpdateMaterials](DynamicGI.UpdateMaterials.html)| Schedules an update of the
albedo and emissive textures of a system that contains the renderer or the
terrain.  
  
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

