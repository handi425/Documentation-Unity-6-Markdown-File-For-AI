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

#  [Tilemap](Tilemaps.Tilemap.html).GetCellCenterWorld

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

public [Vector3](Vector3.html)
GetCellCenterWorld([Vector3Int](Vector3Int.html) position);

### Parameters

position | Grid cell position.  
---|---  
  
### Returns

**Vector3** Returns the center of the cell transformed into world space
coordinates.

### Description

Gets the logical center coordinate of a [Grid](Grid.html) cell in world space.
The logical center for a cell of the [Tilemap](Tilemaps.Tilemap.html) is
defined by the Tile Anchor of the Tilemap.

In a rectangular grid layout, a call to
[GridLayout.CellToWorld](GridLayout.CellToWorld.html) with
[Vector3Int](Vector3Int.html) parameter returns a [Vector3](Vector3.html)
coordinate that represents the lower left of the cell. This is mathematically
correct, but in certain cases such as when instantiating a GameObject into the
grid, you may prefer the center of the cell instead.

    
    
    // Snap the [GameObject](GameObject.html) to parent [Tilemap](Tilemaps.Tilemap.html) center of cell
    using UnityEngine;
    using UnityEngine.Tilemaps;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Tilemap](Tilemaps.Tilemap.html) tilemap = transform.parent.GetComponent<[Tilemap](Tilemaps.Tilemap.html)>();
            [Vector3Int](Vector3Int.html) cellPosition = tilemap.WorldToCell(transform.position);
            transform.position = tilemap.GetCellCenterWorld(cellPosition);
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

