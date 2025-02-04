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

#  [Tilemap](Tilemaps.Tilemap.html).GetTilesRangeNonAlloc

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

public int GetTilesRangeNonAlloc([Vector3Int](Vector3Int.html) startPosition,
[Vector3Int](Vector3Int.html) endPosition, Vector3Int[] positions, TileBase[]
tiles);

### Parameters

startPosition | The starting position of the range to retrieve Tiles from.  
---|---  
endPosition | The ending position of the range to retrieve Tiles from.  
positions | The positions of Tiles within the given range.  
tiles | The Tiles within the given range.  
  
### Returns

**int** Returns the number of positions and Tiles retrieved.

### Description

Retrieves an array of Tiles within the given range, inclusive of the Cells at
both the starting position and the ending positions. This method begins at the
given starting position and iterates through all available Z Positions, then
iterates through the X and Y positions until it reaches the ending position.

This method begins at the given starting position, and is inclusive of the
Cell at this starting position. It retrieves all Tiles at a given Cell,
including Tiles at all Z Positions at that Cell position. After retrieving all
Tiles available at the current Cell, the method continues iterating onto the
next Cell along the same row until it reaches the rightmost bounds of the
Tilemap. After reaching the end of the Tilemap along the initial row of Cells,
the method then iterates along the next row of Cells above the initial row,
starting from the leftmost edge of the Tilemap. The method continues iterating
in this pattern until it reaches the Cell at the ending position of the given
range.  
  
If the starting position's value is higher than the ending position's value,
then the method begins with the Cell at the starting position but iterates in
the opposite direction of the usual method, ending when it reaches the Cell at
the ending position.  
  
If the size of the arrays passed in as parameters are less than the number of
Tiles within the range, the arrays will not be resized and the results will be
limited.

    
    
    // Retrieves all tiles with a range on the tilemap and prints out the positions and tiles to console
    using UnityEngine;
    using UnityEngine.Tilemaps;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Tilemap](Tilemaps.Tilemap.html) tilemap = GetComponent<[Tilemap](Tilemaps.Tilemap.html)>();
            SetTiles(tilemap);  
      
            [Vector3Int](Vector3Int.html)[] positions = new [Vector3Int](Vector3Int.html)[16];
            [TileBase](Tilemaps.TileBase.html)[] tiles = new [TileBase](Tilemaps.TileBase.html)[16];
            var count = tilemap.GetTilesRangeNonAlloc(new [Vector3Int](Vector3Int.html)(0, 0, 0), new [Vector3Int](Vector3Int.html)(5, 1, 0), positions, tiles);
            for (int index = 0; index < count; index++)
            {
                print(positions[index]);
                print(tiles[index]);
            }
        }  
      
        // Sets Tiles in a 10 by 10 block
        void SetTiles([Tilemap](Tilemaps.Tilemap.html) tilemap)
        {
            [Tile](Tilemaps.Tile.html) tile = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<[Tile](Tilemaps.Tile.html)>();
            [TileBase](Tilemaps.TileBase.html)[] tiles = new [TileBase](Tilemaps.TileBase.html)[10 * 10];
            for (int index = 0; index < tiles.Length; index++)
            {
                tiles[index] = tile;
            }
            tilemap.SetTilesBlock(new [BoundsInt](BoundsInt.html)(0, 0, 0, 10, 10, 1), tiles);
        }
    }
    

In the example above, GetTilesRangeNonAlloc with a starting position (0, 0, 0)
and an ending position (5, 1, 0) will return an array of sixteen Tiles: ten
Tiles from (0, 0, 0) to (10, 0, 0), as well as the six Tiles from (0, 1, 0) to
(5, 1, 0).  
  
If the starting and ending positions were swapped, then GetTilesRangeNonAlloc
with starting position (5, 1, 0) and ending position (0, 0, 0) will return an
array of sixteen Tiles: six Tiles from (5, 1, 0) to (0, 1, 0), as well as the
ten Tiles from (10, 0, 0) to (0, 0, 0).

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

