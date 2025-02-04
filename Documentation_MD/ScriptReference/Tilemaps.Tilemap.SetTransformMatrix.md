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

#  [Tilemap](Tilemaps.Tilemap.html).SetTransformMatrix

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

public void SetTransformMatrix([Vector3Int](Vector3Int.html) position,
[Matrix4x4](Matrix4x4.html) transform);

### Parameters

position | Position of the Tile on the [Tilemap](Tilemaps.Tilemap.html).  
---|---  
transform | The transform matrix.  
  
### Description

Sets the transform matrix of a [Tile](Tilemaps.Tile.html) given the XYZ
coordinates of a cell in the [Tilemap](Tilemaps.Tilemap.html).

Note that if the Tile has set
[TileFlags.LockTransform](Tilemaps.TileFlags.LockTransform.html), then this
matrix has no effect.

    
    
    // [Rotate](UIElements.Rotate.html) the tile in (0,0,0) 90 degrees
    using UnityEngine;
    using UnityEngine.Tilemaps;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Tilemap](Tilemaps.Tilemap.html) tilemap = GetComponent<[Tilemap](Tilemaps.Tilemap.html)>();
            [Matrix4x4](Matrix4x4.html) matrix = [Matrix4x4.TRS](Matrix4x4.TRS.html)([Vector3.zero](Vector3-zero.html), [Quaternion.Euler](Quaternion.Euler.html)(0f, 0f, 90f), [Vector3.one](Vector3-one.html));
            tilemap.SetTransformMatrix(new [Vector3Int](Vector3Int.html)(0, 0, 0), matrix);
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

