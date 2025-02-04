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

#
[MaterialPropertyBlock](MaterialPropertyBlock.html).CopySHCoefficientArraysFrom

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

## Declaration

public void CopySHCoefficientArraysFrom(List<SphericalHarmonicsL2>
lightProbes);

## Declaration

public void CopySHCoefficientArraysFrom(SphericalHarmonicsL2[] lightProbes);

### Parameters

lightProbes | The array of SH values to copy from.  
---|---  
  
### Description

This function converts and copies the entire source array into 7 Vector4
property arrays named `unity_SHAr`, `unity_SHAg`, `unity_SHAb`, `unity_SHBr`,
`unity_SHBg`, `unity_SHBb` and `unity_SHC` for use with instanced [light
probe](../Manual/LightProbes.html) rendering.

If the array properties don't exist on the MaterialPropertyBlock, they will be
created with the length of the source array.  
Call
[LightProbes.CalculateInterpolatedLightAndOcclusionProbes](LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html)
to calculate SH values at the given world space positions.  
ArgumentNullException is thrown if `lightProbes` is `null`.  
Note that all MaterialPropertyBlock arrays can only have a maximum of 1023
elements. Warnings are printed and the excess array elements are ignored if
the source array exceeds the range.  
  
Additional resources:
[CopyProbeOcclusionArrayFrom](MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html),
[Graphics.RenderMeshInstanced](Graphics.RenderMeshInstanced.html),
[CommandBuffer.DrawMeshInstanced](Rendering.CommandBuffer.DrawMeshInstanced.html).

* * *

## Declaration

public void CopySHCoefficientArraysFrom(SphericalHarmonicsL2[] lightProbes,
int sourceStart, int destStart, int count);

## Declaration

public void CopySHCoefficientArraysFrom(List<SphericalHarmonicsL2>
lightProbes, int sourceStart, int destStart, int count);

### Parameters

lightProbes | The array of SH values to copy from.  
---|---  
sourceStart | The index of the first element in the source array to copy from.  
destStart | The index of the first element in the destination MaterialPropertyBlock array to copy to.  
count | The number of elements to copy.  
  
### Description

This function converts and copies the source array into 7 Vector4 property
arrays named `unity_SHAr`, `unity_SHAg`, `unity_SHAb`, `unity_SHBr`,
`unity_SHBg`, `unity_SHBb` and `unity_SHC` with the specified source and
destination range for use with instanced [light
probe](../Manual/LightProbes.html) rendering.

If the array properties don't exist on the MaterialPropertyBlock, they will be
created with the length of the spcified range.  
Call
[LightProbes.CalculateInterpolatedLightAndOcclusionProbes](LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html)
to calculate SH values at the given world space positions.  
ArgumentNullException is thrown if `occlusionProbes` is `null`.  
ArgumentOutOfRangeException is thrown if the source or destination range is
invalid.  
Note that all MaterialPropertyBlock arrays can only have a maximum of 1023
elements. Warnings are printed and the excess array elements are ignored if
the source array exceeds the range.  
  
Additional resources:
[CopyProbeOcclusionArrayFrom](MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html),
[Graphics.RenderMeshInstanced](Graphics.RenderMeshInstanced.html),
[CommandBuffer.DrawMeshInstanced](Rendering.CommandBuffer.DrawMeshInstanced.html).

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

