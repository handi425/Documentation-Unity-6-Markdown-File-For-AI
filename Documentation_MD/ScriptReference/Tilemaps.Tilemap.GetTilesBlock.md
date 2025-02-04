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

#  [Tilemap](Tilemaps.Tilemap.html).GetTilesBlock

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

public TileBase[] GetTilesBlock([BoundsInt](BoundsInt.html) bounds);

### Parameters

bounds | The bounds to retrieve from.  
---|---  
  
### Returns

**TileBase[]** The array of [Tile](Tilemaps.Tile.html)s at the given bounds.

### Description

Retrieves an array of Tiles with the given bounds.

This is meant for more a performant way to get Tiles as a batch, when compared
to calling GetTile for every single position. The bounds size must match the
array size. For example bounds of 1x2x3 needs an array length of 6.

    
    
    // Retrieves all Tiles from an area on the [Tilemap](Tilemaps.Tilemap.html) and prints out the Tiles to console
    using UnityEngine;
    using UnityEngine.Tilemaps;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [BoundsInt](BoundsInt.html) area;  
      
        void Start()
        {
            [Tilemap](Tilemaps.Tilemap.html) tilemap = GetComponent<[Tilemap](Tilemaps.Tilemap.html)>();
            [TileBase](Tilemaps.TileBase.html)[] tileArray = tilemap.GetTilesBlock(area);
            for (int index = 0; index < tileArray.Length; index++)
            {
                print(tileArray[index]);
            }
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

