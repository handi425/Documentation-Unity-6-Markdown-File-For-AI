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

# VisibleReflectionProbe

struct in UnityEngine.Rendering

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

Holds data of a visible reflection reflectionProbe.

After
[ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html) is
done, [CullingResults.visibleReflectionProbes](Rendering.CullingResults-
visibleReflectionProbes.html) will contain an array of reflection
reflectionProbes that are visible. The visible reflection reflectionProbe
structure contains packed information for most commonly used
[ReflectionProbe](ReflectionProbe.html) variables, and a
VisibleReflectionProbe.probe reference to the component itself.  
  
Additional resources:
[CullingResults.visibleReflectionProbes](Rendering.CullingResults-
visibleReflectionProbes.html), [ReflectionProbe](ReflectionProbe.html).

### Properties

[blendDistance](Rendering.VisibleReflectionProbe-blendDistance.html)| Probe
blending distance.  
---|---  
[bounds](Rendering.VisibleReflectionProbe-bounds.html)| The probe's world
space axis-aligned bounding box in which the probe can contribute to
reflections.  
[center](Rendering.VisibleReflectionProbe-center.html)| The center of the
probe's bounding box in which the probe can contribute to reflections. The
center is relative to the position of the probe.  
[hdrData](Rendering.VisibleReflectionProbe-hdrData.html)| Shader data for
probe HDR texture decoding.  
[importance](Rendering.VisibleReflectionProbe-importance.html)| Probe
importance.  
[isBoxProjection](Rendering.VisibleReflectionProbe-isBoxProjection.html)|
Should probe use box projection.  
[localToWorldMatrix](Rendering.VisibleReflectionProbe-
localToWorldMatrix.html)| Probe transformation matrix.  
[reflectionProbe](Rendering.VisibleReflectionProbe-reflectionProbe.html)|
Accessor to ReflectionProbe component.  
[texture](Rendering.VisibleReflectionProbe-texture.html)| Probe texture.  
  
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

