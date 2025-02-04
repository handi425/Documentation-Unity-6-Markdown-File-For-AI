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

#  [LightmapParameters](LightmapParameters.html).backFaceTolerance

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

[Switch to Manual](../Manual/class-LightmapParameters.html "Go to
LightmapParameters Component in the Manual")

public float backFaceTolerance;

### Description

The percentage of rays shot from a ray origin that must hit front faces to be
considered usable.

The precompute calculates visibility from ray origins to clusters, but
attempts to reject ray origins that are inside geometry. If the percentage of
rays that hit front faces is less than backFaceTolerance, the ray origin is
marked invalid and will not affect the radiosity computation.  
  
  
  
For example, if backFaceTolerance is 0.0, the ray origin is rejected only if
it sees nothing but backfaces. If 1.0, the ray origin is rejected if it has
even one ray that hits a backface.  
  
  
  
This setting can help control light leaking, but should be considered in the
context of the mesh authoring workflow. Preventing ray origin rejection by
setting a value of 0.0 will ensure Enlighten Realtime Global Illumination does
not reject ray origins due to single-sided geometry. However, if the majority
of the meshes are closed, so visible backfaces are rare, a positive value can
reduce light leaking or darkening that intersecting geometry would otherwise
cause.

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

