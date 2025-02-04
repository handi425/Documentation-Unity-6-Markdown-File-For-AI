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

#  [TerrainData](TerrainData.html).SetHolesDelayLOD

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

public void SetHolesDelayLOD(int xBase, int yBase, bool[,] holes);

### Parameters

xBase | First x index of Terrain holes samples to set.  
---|---  
yBase | First y index of Terrain holes samples to set.  
holes | Array of Terrain holes samples to set (array indexed as [y,x]).  
  
### Description

Sets an array of Terrain holes samples.

Sets Terrain holes data using a two-dimensional array of Terrain holes
samples. The samples are represented as bool values: `true` for surface and
`false` for hole. The array dimensions define the area affected, which starts
at `xBase` and `yBase`. The Terrain holes array is indexed as [y,x].  
  
Unlike [TerrainData.SetHoles](TerrainData.SetHoles.html), this method does not
update LOD information for the Terrain, or any tree/vegetation objects; this
means that some tree/vegetation objects might still be present over holes, but
makes the method fast enough to be used in interactive editing scenarios.
After modifications to the Terrain are complete - for example, when the user
releases the mouse button - call
[TerrainData.SyncTexture](TerrainData.SyncTexture.html) and use
[TerrainData.HolesTextureName](TerrainData.HolesTextureName.html) as a Texture
name to update all LOD and vegetation information.

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

