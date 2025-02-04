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

#  [PaintContext](TerrainTools.PaintContext.html).CreateFromBounds

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

public static [TerrainTools.PaintContext](TerrainTools.PaintContext.html)
CreateFromBounds([Terrain](Terrain.html) terrain, [Rect](Rect.html)
boundsInTerrainSpace, int inputTextureWidth, int inputTextureHeight, int
extraBorderPixels = 0, bool sharedBoundaryTexel = true, bool
fillOutsideTerrain = true);

### Parameters

terrain | Terrain that defines terrain space for this PaintContext.  
---|---  
boundsInTerrainSpace | Terrain space bounds to edit in the target terrain texture.  
inputTextureWidth | Width of the input Terrain Texture for all connected Terrains.  
inputTextureHeight | Height of the input Terrain Texture for all connected Terrains.  
extraBorderPixels | Number of extra border pixels required. The default value is 0.  
sharedBoundaryTexel | Whether to stretch the Textures so that edge texels lie on the Terrain boundary, and are shared with connected Terrains.  
fillOutsideTerrain | Whether to fill empty space outside of the Terrain tiles with data from the nearest tile.  
  
### Description

Constructs a PaintContext that you can use to edit a texture on a Terrain, in
the region defined by boundsInTerrainSpace and extraBorderPixels.

This function calculates a pixelRect from `boundsInTerrainSpace` and
`extraBorderPixels`, and then constructs a PaintContext from the pixelRect.  
  
This function is called internally by
[TerrainPaintUtility.BeginPaintHeightmap](TerrainTools.TerrainPaintUtility.BeginPaintHeightmap.html),
[TerrainPaintUtility.BeginPaintTexture](TerrainTools.TerrainPaintUtility.BeginPaintTexture.html)
and
[TerrainPaintUtility.CollectNormals](TerrainTools.TerrainPaintUtility.CollectNormals.html).  
  
Additional resources: [PaintContext](TerrainTools.PaintContext.html).

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

