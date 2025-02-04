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

#  [Tilemap](Tilemaps.Tilemap.html).SetTilesBlock

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

public void SetTilesBlock([BoundsInt](BoundsInt.html) position, TileBase[]
tileArray);

### Parameters

position | Bounds to be filled.  
---|---  
tileArray | An array of [Tile](Tilemaps.Tile.html)s to be placed.  
  
### Description

Fills bounds with array of [Tile](Tilemaps.Tile.html)s.

This is meant for a more performant way to set Tiles as a batch, when compared
to calling SetTile for every single Tile. The bounds size must match the array
size. For example bounds of 1x2x3 needs an array length of 6.

    
    
    // Fill area on [Tilemap](Tilemaps.Tilemap.html) with checkerboard pattern of tileA and tileB
    using UnityEngine;
    using UnityEngine.Tilemaps;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [TileBase](Tilemaps.TileBase.html) tileA;
        public [TileBase](Tilemaps.TileBase.html) tileB;
        public [BoundsInt](BoundsInt.html) area;  
      
        void Start()
        {
            [TileBase](Tilemaps.TileBase.html)[] tileArray = new [TileBase](Tilemaps.TileBase.html)[area.size.x * area.size.y * area.size.z];
            for (int index = 0; index < tileArray.Length; index++)
            {
                tileArray[index] = index % 2 == 0 ? tileA : tileB;
            }
            [Tilemap](Tilemaps.Tilemap.html) tilemap = GetComponent<[Tilemap](Tilemaps.Tilemap.html)>();
            tilemap.SetTilesBlock(area, tileArray);
        }
    }
    

Refer to [Scriptable Tiles](../Manual/Tilemap-ScriptableTiles-TileBase.html)
and [Tilemap](../Manual/class-Tilemap.html) for more information.

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

