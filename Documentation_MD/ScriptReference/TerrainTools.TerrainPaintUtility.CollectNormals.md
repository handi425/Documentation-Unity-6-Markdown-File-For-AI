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

#  [TerrainPaintUtility](TerrainTools.TerrainPaintUtility.html).CollectNormals

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
CollectNormals([Terrain](Terrain.html) terrain, [Rect](Rect.html)
boundsInTerrainSpace, int extraBorderPixels = 0, bool fillOutsideTerrain =
true);

### Parameters

terrain | Reference Terrain tile.  
---|---  
boundsInTerrainSpace | The region in terrain space from which to collect normals.  
extraBorderPixels | Number of extra border pixels required.  
fillOutsideTerrain | Whether to fill empty space outside of Terrain tiles with data from the nearest tile.  
  
### Returns

**PaintContext** PaintContext containing the combined normalmap data for the
specified region.

### Description

Helper function to set up a PaintContext that collects mesh normal data from
one or more Terrain tiles.

CollectNormals identifies all of the normalmap pixels that are within
`extraBorderPixels` of the bounds rectangle. The search is performed across
adjacent connected Terrain tiles. The pixels are collected into a temporary
render texture and stored in
[PaintContext.sourceRenderTexture](TerrainTools.PaintContext-
sourceRenderTexture.html).  
  
Important: there is no corresponding function to write modified normalmap data
back to the Terrain tiles, because the normalmap is not stored; it is
calculated from the heightmap.  
  
Once you are done using the sourceRenderTexture, you must call
[TerrainPaintUtility.ReleaseContextResources](TerrainTools.TerrainPaintUtility.ReleaseContextResources.html)
to release the RenderTexture resources.  
  
Additional resources:
[PaintContext.GatherNormals](TerrainTools.PaintContext.GatherNormals.html) and
[PaintContext](TerrainTools.PaintContext.html).

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

