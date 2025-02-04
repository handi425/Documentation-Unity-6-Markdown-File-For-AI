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

# PaintContext Constructor

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

public PaintContext([Terrain](Terrain.html) terrain, [RectInt](RectInt.html)
pixelRect, int targetTextureWidth, int targetTextureHeight, bool
sharedBoundaryTexel = true, bool fillOutsideTerrain = true);

### Parameters

terrain | Terrain that defines terrain space for this PaintContext.  
---|---  
pixelRect | Pixel rectangle to edit in the target terrain texture.  
targetTextureWidth | Width of the target terrain texture (per Terrain).  
targetTextureHeight | Height of the target terrain texture (per Terrain).  
sharedBoundaryTexel | Whether to stretch the Textures so that edge texels lie on the Terrain boundary, and are shared with connected Terrains.  
fillOutsideTerrain | Whether to fill empty space outside of the Terrain tiles with data from the nearest tile.  
  
### Description

Creates a new PaintContext, to edit a target texture on a Terrain, in a region
defined by pixelRect.

This constructor finds all Terrain tiles that touch the pixelRect, searching
across adjacent connected Terrain tiles. It also calculates the relevant
regions on each Terrain, as well as the transforms between them.  
  
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

