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

#  [Lightmapping](Lightmapping.html).Tetrahedralize

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

public static void Tetrahedralize(Vector3[] positions, out int[] outIndices,
out Vector3[] outPositions);

### Parameters

positions | An array of Light Probe positions.  
---|---  
outIndices | An array that Unity populates with updated Light Probe indices.  
outPositions | An array that Unity populates with updated Light Probe positions.  
  
### Description

Calculates tetrahderons from positions using Delaunay Tetrahedralization.

This is an Editor-only method for visualizing the tetrahedrons that Unity uses
for blending probe lighting.  
  
When you pass an array of Light Probe positions, Unity performs the same
calculations as it does when regenerating the tetrahedrons, and populates the
out parameters with the results of those calculations:  
  
`outIndices`: every four entries correspond to the vertices of a tetrahedron
`outPositions`: indexed in the same order as `outIndices`, containing the
positions of the corresponding probes  
  
Unity considers Light Probes at the same position (within some tolerance) as
duplicates, and does not include them in the tetrahedralization. When this
happens, only the first element is included. As a result, `outPositions` might
have fewer elements than `positions`.  
  
Note that this method does not cause Unity to update the tetrahedrons that it
uses for Light Probes; use this method only for visualizing the results of
such an operation.  
  
Additional resources:
[LightProbes.Tetrahedralize](LightProbes.Tetrahedralize.html),
[LightProbes.TetrahedralizeAsync](LightProbes.TetrahedralizeAsync.html),
[Light Probes and Scene loading](../Manual/light-probes-and-scene-
loading.html).

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

