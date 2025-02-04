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

#  [PaintContext](TerrainTools.PaintContext.html).Scatter

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

public void Scatter(Func<ITerrainInfo,RenderTexture> terrainDest,
[Material](Material.html) blitMaterial, int blitPass, Action<ITerrainInfo>
beforeBlit, Action<ITerrainInfo> afterBlit);

### Parameters

terrainDest | Function returning the RenderTexture to be written for each Terrain.  
---|---  
blitMaterial | The material used to copy the data. If null, the default blit material is used.  
blitPass | The material pass used to copy the data. Its default value is 0.  
beforeBlit | An optional action to call before copying to each Terrain.  
afterBlit | An optional action to call after copying to each Terrain.  
  
### Description

Applies an edited PaintContext by copying modifications back to user-specified
RenderTextures for the source Terrain tiles.

After the edits to a PaintContext are complete, this function applies the
modified data in `destinationRenderTexture` to the data stored for each
Terrain. Scatter performs this copy to a set of RenderTextures, which is
specified by `terrainDest`.  
  
This function uses the following steps to scatter to each Terrain in the
PaintContext:  
1) Calls `terrainDest` to retrieve the target RenderTexture.  
2) Calls `beforeBlit`.  
3) Uses `blitMaterial` and `blitPass` to copy the `destinationRenderTexture`
into the target RenderTexture.  
4) Calls `afterBlit`.  
  
Additional resources: [PaintContext](TerrainTools.PaintContext.html),
[PaintContext.Gather](TerrainTools.PaintContext.Gather.html).

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

