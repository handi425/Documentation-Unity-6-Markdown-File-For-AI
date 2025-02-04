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

#  [PaintContext](TerrainTools.PaintContext.html).Gather

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

public void Gather(Func<ITerrainInfo,Texture> terrainSource,
[Color](Color.html) defaultColor, [Material](Material.html) blitMaterial, int
blitPass, Action<ITerrainInfo> beforeBlit, Action<ITerrainInfo> afterBlit);

### Parameters

terrainSource | A function that returns the Texture data to collect from each Terrain.  
---|---  
defaultColor | The default color for `sourceRenderTexture`.  
blitMaterial | The material used to copy the data. If null, the default blit material is used.  
blitPass | The material pass used to copy the data.  
beforeBlit | An optional action to call before copying from each Terrain. The default is null.  
afterBlit | An optional action to call after copying from each Terrain. The default is null.  
  
### Description

Gathers user-specified Texture data into `sourceRenderTexture`.

This function collects Texture data from all Terrain tiles in the
PaintContext, and merges that data into `sourceRenderTexture`. The
`terrainSource` function specifies what data to collect from each Terrain.
Gather assumes that the Texture data, which `terrainSource` returns, is mapped
over the Terrain tile in a manner similar to the Heightmap and Alphamaps.  
  
First, the function clears `sourceRenderTexture` to `defaultColor`.  
Then, it uses the following steps to gather each Terrain in the PaintContext:  
1) Calls `terrainSource` to retrieve the Texture.  
2) Calls `beforeBlit`.  
3) Uses `blitMaterial` and `blitPass` to copy The Texture into
`sourceRenderTexture`.  
4) Calls `afterBlit`.  
  
Additional resources: [PaintContext](TerrainTools.PaintContext.html),
[PaintContext.Scatter](TerrainTools.PaintContext.Scatter.html).

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

