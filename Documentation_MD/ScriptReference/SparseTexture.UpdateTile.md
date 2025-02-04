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

#  [SparseTexture](SparseTexture.html).UpdateTile

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

public void UpdateTile(int tileX, int tileY, int miplevel, Color32[] data);

### Parameters

tileX | Tile X coordinate.  
---|---  
tileY | Tile Y coordinate.  
miplevel | Mipmap level of the texture.  
data | Tile color data.  
  
### Description

Update sparse texture tile with color values.

This function makes a tile at (tileX,tileY) coordinates resident in memory,
and updates its pixels. If a tile is already resident, then only the pixels
are updated.  
  
Data passed should have enough pixels for the tile (tileWidth*tileHeight
elements). Exception can be small mipmap levels that are smaller than tile
size; then it's ok to pass enough data for the mip level size.  
  
UpdateTile only works for non-compressed color formats. If you use a sparse
texture with a compressed format, use
[UpdateTileRaw](SparseTexture.UpdateTileRaw.html) and pass raw tile data bytes
(e.g. DXT/BCn-compressed data). UpdateTileRaw can also be more efficient if
texture format is not RGBA32, as then Unity does not have to convert from
Color32 data into the underlying texture format.  
  
Additional resources: [UnloadTile](SparseTexture.UnloadTile.html),
[UpdateTileRaw](SparseTexture.UpdateTileRaw.html).

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

