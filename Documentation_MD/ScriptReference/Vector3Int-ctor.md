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

# Vector3Int Constructor

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

public Vector3Int(int x, int y, int z);

### Parameters

x | The X component of the Vector3Int.  
---|---  
y | The Y component of the Vector3Int.  
z | The Z component of the Vector3Int.  
  
### Description

Initializes and returns an instance of a new Vector3Int with x, y, z
components.

    
    
    // Attach this script to a [GameObject](GameObject.html).
    // Attach a [Tilemap](Tilemaps.Tilemap.html) component to the [GameObject](GameObject.html) (Click **Add Component** button in the Inspector window and go to **2D** <**Tilemap**)
    // This script sets a [Tile](WSA.Tile.html) at a [Vector3Int](Vector3Int.html) position
    using UnityEngine;
    using UnityEngine.Tilemaps;  
      
    public class Vector3IntCtorExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [Vector3Int](Vector3Int.html) m_Position;
        [Tilemap](Tilemaps.Tilemap.html) m_Tilemap;
        [Tile](WSA.Tile.html) m_Tile;  
      
        void Start()
        {
            // [Position](UIElements.Position.html) to set the [Tile](WSA.Tile.html) at
            m_Position = new [Vector3Int](Vector3Int.html)(1, 5, -2);
            // Fetch the [Tilemap](Tilemaps.Tilemap.html) you attach to the [GameObject](GameObject.html)
            m_Tilemap = GetComponent<[Tilemap](Tilemaps.Tilemap.html)>();
            // Create a [Tile](WSA.Tile.html)
            m_Tile = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<[Tile](WSA.Tile.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Sets a [Tile](WSA.Tile.html) at the position if a [Tile](WSA.Tile.html) does not exist at the position on the [Tilemap](Tilemaps.Tilemap.html)
            if (!m_Tilemap.HasTile(m_Position))
                m_Tilemap.SetTile(m_Position, m_Tile);
        }
    }
    

* * *

## Declaration

public Vector3Int(int x, int y);

### Parameters

x | The X component of the Vector3Int.  
---|---  
y | The Y component of the Vector3Int.  
  
### Description

Initializes and returns an instance of a new Vector3Int with x and y
components and sets `z` to zero.

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

