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

# CullingOptions

enumeration

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

Flags used by
[ScriptableCullingParameters.cullingOptions](Rendering.ScriptableCullingParameters-
cullingOptions.html) to configure a culling operation.

Unity sets some of the [CullingOptions](Rendering.CullingOptions.html) flags
with default values, and others depending on the properties of the
[Camera](Camera.html) from which you obtained the
[ScriptableCullingParameters](Rendering.ScriptableCullingParameters.html)
struct. You can override these values before performing the culling operation.  
  
Additional resources:
[ScriptableCullingParameters.cullingOptions](Rendering.ScriptableCullingParameters-
cullingOptions.html),
[ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html),
[Camera](Camera.html).

### Properties

[None](Rendering.CullingOptions.None.html)| Unset all CullingOptions flags.  
---|---  
[ForceEvenIfCameraIsNotActive](Rendering.CullingOptions.ForceEvenIfCameraIsNotActive.html)|
When this flag is set, Unity performs the culling operation even if the Camera
is not active.  
[OcclusionCull](Rendering.CullingOptions.OcclusionCull.html)| When this flag
is set, Unity performs occlusion culling as part of the culling operation.  
[NeedsLighting](Rendering.CullingOptions.NeedsLighting.html)| When this flag
is set, Unity culls Lights as part of the culling operation.  
[NeedsReflectionProbes](Rendering.CullingOptions.NeedsReflectionProbes.html)|
When this flag is set, Unity culls Reflection Probes as part of the culling
operation.  
[Stereo](Rendering.CullingOptions.Stereo.html)| When this flag is set, Unity
culls both eyes together for stereo rendering.  
[DisablePerObjectCulling](Rendering.CullingOptions.DisablePerObjectCulling.html)|
When this flag is set, Unity does not perform per-object culling.  
[ShadowCasters](Rendering.CullingOptions.ShadowCasters.html)| When this flag
is set, Unity culls shadow casters as part of the culling operation.  
  
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

