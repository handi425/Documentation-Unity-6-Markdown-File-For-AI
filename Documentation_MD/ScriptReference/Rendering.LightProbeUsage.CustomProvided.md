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

#  [LightProbeUsage](Rendering.LightProbeUsage.html).CustomProvided

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

The light probe shader uniform values are extracted from the material property
block set on the renderer.

Property `unity_SHAr`, `unity_SHAg`, `unity_SHAb`, `unity_SHBr`, `unity_SHBg`,
`unity_SHBb` and `unity_SHC` will be set to zero if they are not part of the
MaterialPropertyBlock.  
Property `unity_ProbesOcclusion` will be calculated as in normal lighting if
it is not part of the MaterialPropertyBlock.  
  
Note that using the light probe values baked at a different place may lead to
incorrect rendering, especially when local lights (i.e. point lights and spot
lights) are used. This mode is more useful when drawing instanced objects with
[Graphics.DrawMeshInstanced](Graphics.DrawMeshInstanced.html), where the light
probe data is pre-calculated and provided as arrays.  
  
Additional resources: [MaterialPropertyBlock](MaterialPropertyBlock.html),
[MaterialPropertyBlock.CopySHCoefficientArraysFrom](MaterialPropertyBlock.CopySHCoefficientArraysFrom.html),
[MaterialPropertyBlock.CopyProbeOcclusionArrayFrom](MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html).

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

