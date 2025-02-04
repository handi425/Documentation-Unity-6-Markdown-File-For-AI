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
[PaintContext](TerrainTools.PaintContext.html).GetClippedPixelRectInTerrainPixels

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

public [RectInt](RectInt.html) GetClippedPixelRectInTerrainPixels(int
terrainIndex);

### Parameters

terrainIndex | Index of the Terrain.  
---|---  
  
### Returns

**RectInt** Returns the clipped pixel rectangle.

### Description

Retrieves the clipped pixel rectangle for a Terrain.

When painting across a border, the PaintContext can refer to several Terrain
tiles. GetClippedPixelRectInTerrainPixels returns the
[PaintContext.pixelRect](TerrainTools.PaintContext-pixelRect.html) clipped to
the specified Terrain, in the pixel coordinates of the target texture on that
Terrain. terrainIndex must be between 0 and
[PaintContext.terrainCount](TerrainTools.PaintContext-terrainCount.html) \- 1.
Additional resources:
[PaintContext.GetTerrain](TerrainTools.PaintContext.GetTerrain.html),
[PaintContext.targetTextureWidth](TerrainTools.PaintContext-
targetTextureWidth.html), and
[PaintContext.targetTextureHeight](TerrainTools.PaintContext-
targetTextureHeight.html).

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

