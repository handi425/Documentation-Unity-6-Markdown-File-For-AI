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

# VisibleLight

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

Holds data of a visible light.

After
[ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html) is
done, [CullingResults.visibleLights](Rendering.CullingResults-
visibleLights.html) will contain an array of lights that are visible. The
visible light structure contains packed information for most commonly used
[Light](Light.html) variables, and a
[VisibleLight.light](Rendering.VisibleLight-light.html) reference to the Light
component itself.  
  
Additional resources: [CullingResults.visibleLights](Rendering.CullingResults-
visibleLights.html), [Light](Light.html).

### Properties

[finalColor](Rendering.VisibleLight-finalColor.html)| Light color multiplied
by intensity.  
---|---  
[forcedVisible](Rendering.VisibleLight-forcedVisible.html)| Has the light been
forced to be visibile.  
[intersectsFarPlane](Rendering.VisibleLight-intersectsFarPlane.html)| Light
intersects far clipping plane.  
[intersectsNearPlane](Rendering.VisibleLight-intersectsNearPlane.html)| Light
intersects near clipping plane.  
[light](Rendering.VisibleLight-light.html)| Accessor to Light component.  
[lightType](Rendering.VisibleLight-lightType.html)| Light type.  
[localToWorldMatrix](Rendering.VisibleLight-localToWorldMatrix.html)| Light
transformation matrix.  
[range](Rendering.VisibleLight-range.html)| Light range.  
[screenRect](Rendering.VisibleLight-screenRect.html)| Light's influence
rectangle on screen.  
[spotAngle](Rendering.VisibleLight-spotAngle.html)| Spot light angle.  
  
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

