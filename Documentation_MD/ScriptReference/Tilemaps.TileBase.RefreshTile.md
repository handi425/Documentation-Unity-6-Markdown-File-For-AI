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

#  [TileBase](Tilemaps.TileBase.html).RefreshTile

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

public void RefreshTile([Vector3Int](Vector3Int.html) position,
[Tilemaps.ITilemap](Tilemaps.ITilemap.html) tilemap);

### Parameters

position | Position of the Tile on the [Tilemap](Tilemaps.Tilemap.html).  
---|---  
tilemap | The [Tilemap](Tilemaps.Tilemap.html) the tile is present on.  
  
### Description

This method is called when the tile is refreshed.

Implement this and call
[Tilemap.RefreshTile](Tilemaps.Tilemap.RefreshTile.html) on all affected
[tiles](../Manual/Tilemap-ScriptableTiles-TileBase.html) on the
[Tilemap](Tilemaps.Tilemap.html) including the tile at the given position to
refresh them. This is also useful if the placement of a tile affects the
properties of neighboring tiles.

    
    
    using UnityEngine;
    using UnityEngine.Tilemaps;  
      
    // [Tile](Tilemaps.Tile.html) that displays a [Sprite](Sprite.html) when it is alone and a different [Sprite](Sprite.html) when it is orthogonally adjacent to the same NeighourTile
    [CreateAssetMenu]
    public class NeighbourTile : [TileBase](Tilemaps.TileBase.html)
    {
        public [Sprite](Sprite.html) spriteA;
        public [Sprite](Sprite.html) spriteB;  
      
        public override void RefreshTile([Vector3Int](Vector3Int.html) position, [ITilemap](Tilemaps.ITilemap.html) tilemap)
        {
            for (int yd = -1; yd <= 1; yd++)
            {
                [Vector3Int](Vector3Int.html) location = new [Vector3Int](Vector3Int.html)(position.x, position.y + yd, position.z);
                if (IsNeighbour(location, tilemap))
                    tilemap.RefreshTile(location);
            }
            for (int xd = -1; xd <= 1; xd++)
            {
                [Vector3Int](Vector3Int.html) location = new [Vector3Int](Vector3Int.html)(position.x + xd, position.y, position.z);
                if (IsNeighbour(location, tilemap))
                    tilemap.RefreshTile(location);
            }
        }  
      
        public override void GetTileData([Vector3Int](Vector3Int.html) position, [ITilemap](Tilemaps.ITilemap.html) tilemap, ref [TileData](Tilemaps.TileData.html) tileData)
        {
            tileData.sprite = spriteA;
            for (int yd = -1; yd <= 1; yd += 2)
            {
                [Vector3Int](Vector3Int.html) location = new [Vector3Int](Vector3Int.html)(position.x, position.y + yd, position.z);
                if (IsNeighbour(location, tilemap))
                    tileData.sprite = spriteB;
            }
            for (int xd = -1; xd <= 1; xd += 2)
            {
                [Vector3Int](Vector3Int.html) location = new [Vector3Int](Vector3Int.html)(position.x + xd, position.y, position.z);
                if (IsNeighbour(location, tilemap))
                    tileData.sprite = spriteB;
            }
        }  
      
        private bool IsNeighbour([Vector3Int](Vector3Int.html) position, [ITilemap](Tilemaps.ITilemap.html) tilemap)
        {
            [TileBase](Tilemaps.TileBase.html) tile = tilemap.GetTile(position);
            return (tile != null && tile == this);
        }
    }
    

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

