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

#  [TileBase](Tilemaps.TileBase.html).GetTileAnimationData

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

public bool GetTileAnimationData([Vector3Int](Vector3Int.html) position,
[Tilemaps.ITilemap](Tilemaps.ITilemap.html) tilemap, ref
[Tilemaps.TileAnimationData](Tilemaps.TileAnimationData.html)
tileAnimationData);

### Parameters

position | Position of the Tile on the [Tilemap](Tilemaps.Tilemap.html).  
---|---  
tilemap | The [Tilemap](Tilemaps.Tilemap.html) the tile is present on.  
tileAnimationData | Data to run an animation on the tile.  
  
### Returns

**bool** Whether the call was successful.

### Description

Retrieves any tile animation data from the scripted tile.

Implement this and fill in the
[TileAnimationData](Tilemaps.TileAnimationData.html) to have the
[Tilemap](Tilemaps.Tilemap.html) run an animation for the tile.

    
    
    using UnityEngine;
    using UnityEngine.Tilemaps;  
      
    // [Tile](Tilemaps.Tile.html) that plays an animated loops of sprites
    [CreateAssetMenu]
    public class AnimatedTile : [TileBase](Tilemaps.TileBase.html)
    {
        public [Sprite](Sprite.html)[] m_AnimatedSprites;
        public float m_AnimationSpeed = 1f;
        public float m_AnimationStartTime;  
      
        public override void GetTileData([Vector3Int](Vector3Int.html) location, [ITilemap](Tilemaps.ITilemap.html) tileMap, ref [TileData](Tilemaps.TileData.html) tileData)
        {
            if (m_AnimatedSprites != null && m_AnimatedSprites.Length > 0)
            {
                tileData.sprite = m_AnimatedSprites[m_AnimatedSprites.Length - 1];
            }
        }  
      
        public override bool GetTileAnimationData([Vector3Int](Vector3Int.html) location, [ITilemap](Tilemaps.ITilemap.html) tileMap, ref [TileAnimationData](Tilemaps.TileAnimationData.html) tileAnimationData)
        {
            if (m_AnimatedSprites != null && m_AnimatedSprites.Length > 0)
            {
                tileAnimationData.animatedSprites = m_AnimatedSprites;
                tileAnimationData.animationSpeed = m_AnimationSpeed;
                tileAnimationData.animationStartTime = m_AnimationStartTime;
                return true;
            }
            return false;
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

