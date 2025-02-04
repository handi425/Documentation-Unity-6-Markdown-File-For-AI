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

#  [TerrainData](TerrainData.html).SetHeights

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

public void SetHeights(int xBase, int yBase, float[,] heights);

### Parameters

xBase | First x index of heightmap samples to set.  
---|---  
yBase | First y index of heightmap samples to set.  
heights | Array of heightmap samples to set (values range from 0 to 1, array indexed as [y,x]).  
  
### Description

Sets an array of heightmap samples.

Sets heightmap data using a two dimensional array of heightmap samples. The
samples are represented as float values ranging from 0 to 1. The area affected
is defined by the array dimensions and starts at xBase and yBase. The heights
array is indexed as [y,x].  
  
This method recomputes all the LOD and vegetation information for the terrain
on each call, which can be computationally expensive. In interactive editing
scenarios, it may be better to call
[TerrainData.SetHeightsDelayLOD](TerrainData.SetHeightsDelayLOD.html) instead,
followed by [TerrainData.SyncHeightmap](TerrainData.SyncHeightmap.html) when
the user completes an editing action.

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

