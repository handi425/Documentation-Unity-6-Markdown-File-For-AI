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
[TerrainPaintUtility](TerrainTools.TerrainPaintUtility.html).BeginPaintHoles

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
BeginPaintHoles([Terrain](Terrain.html) terrain, [Rect](Rect.html)
boundsInTerrainSpace, int extraBorderPixels = 0, bool fillOutsideTerrain =
true);

### Parameters

terrain | Reference Terrain tile.  
---|---  
boundsInTerrainSpace | The region in Terrain space to edit.  
extraBorderPixels | Number of extra border pixels required.  
fillOutsideTerrain | Whether to fill empty space outside of Terrain tiles with data from the nearest tile.  
  
### Returns

**PaintContext** PaintContext that contains the combined Terrain holes data
for the specified region.

### Description

Helper function to set up a PaintContext for modifying the Terrain holes of
one or more Terrain tiles.

BeginPaintHoles identifies all of the Terrain holes pixels that are within
`extraBorderPixels` of the bounds rectangle. The search is performed across
adjacent connected Terrain tiles. The pixels are collected into a temporary
render texture and stored in
[PaintContext.sourceRenderTexture](TerrainTools.PaintContext-
sourceRenderTexture.html).  
  
After you call this function, you can write new values into
[PaintContext.destinationRenderTexture](TerrainTools.PaintContext-
destinationRenderTexture.html) to modify the Terrain holes. Then, you may
complete the modification by calling
[TerrainPaintUtility.EndPaintHoles](TerrainTools.TerrainPaintUtility.EndPaintHoles.html)
to copy the modified data back to the Terrain tiles. Alteratively, you may
cancel the modification by calling
[TerrainPaintUtility.ReleaseContextResources](TerrainTools.TerrainPaintUtility.ReleaseContextResources.html)
to release the RenderTexture resources.  
  
Additional resources:
[TerrainPaintUtility.EndPaintHoles](TerrainTools.TerrainPaintUtility.EndPaintHoles.html)
and [PaintContext](TerrainTools.PaintContext.html).

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

