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

#  [Sprite](Sprite.html).vertices

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

public Vector2[] vertices;

### Description

Returns a copy of the array containing Sprite mesh vertex positions.

    
    
    // Obtain the vertices from the script and modify the position of one of them. Use OverrideGeometry() for this.
    //Attach this script to a [Sprite](Sprite.html) [GameObject](GameObject.html)
    //To see the vertices changing, make sure you have your [Scene](SceneManagement.Scene.html) tab visible while in Play mode.
    //Press the "Draw [Debug](Debug.html)" [Button](UIElements.Button.html) in the Game tab during Play [Mode](Scripting.GarbageCollector.Mode.html) to draw the shape. [Switch](PlayerSettings.Switch.html) back to the [Scene](SceneManagement.Scene.html) tab to see the shape.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private [SpriteRenderer](SpriteRenderer.html) m_SpriteRenderer;
        private [Rect](Rect.html) buttonPos1;
        private [Rect](Rect.html) buttonPos2;  
      
        void Start()
        {
            m_SpriteRenderer = gameObject.GetComponent<[SpriteRenderer](SpriteRenderer.html)>();
            buttonPos1 = new [Rect](Rect.html)(10.0f, 10.0f, 200.0f, 30.0f);
            buttonPos2 = new [Rect](Rect.html)(10.0f, 50.0f, 200.0f, 30.0f);
        }  
      
        void OnGUI()
        {
            //Press this [Button](UIElements.Button.html) to show the [Sprite](Sprite.html) triangles (in the [Scene](SceneManagement.Scene.html) tab)
            if ([GUI.Button](GUI.Button.html)(buttonPos1, "Draw [Debug](Debug.html)"))
                DrawDebug();
            //Press this [Button](UIElements.Button.html) to edit the vertices obtained from the [Sprite](Sprite.html)
            if ([GUI.Button](GUI.Button.html)(buttonPos2, "Perform OverrideGeometry"))
                ChangeSprite();
        }  
      
        // Show the [Sprite](Sprite.html) triangles
        void DrawDebug()
        {
            [Sprite](Sprite.html) sprite = m_SpriteRenderer.sprite;  
      
            ushort[] triangles = sprite.triangles;
            [Vector2](Vector2.html)[] vertices = sprite.vertices;
            int a, b, c;  
      
            // draw the triangles using grabbed vertices
            for (int i = 0; i < triangles.Length; i = i + 3)
            {
                a = triangles[i];
                b = triangles[i + 1];
                c = triangles[i + 2];  
      
                //To see these you must view the game in the [Scene](SceneManagement.Scene.html) tab while in Play mode
                [Debug.DrawLine](Debug.DrawLine.html)(vertices[a], vertices[b], [Color.red](Color-red.html), 100.0f);
                [Debug.DrawLine](Debug.DrawLine.html)(vertices[b], vertices[c], [Color.red](Color-red.html), 100.0f);
                [Debug.DrawLine](Debug.DrawLine.html)(vertices[c], vertices[a], [Color.red](Color-red.html), 100.0f);
            }
        }  
      
        // Edit the vertices obtained from the [Sprite](Sprite.html).  Use OverrideGeometry to
        // submit the changes.
        void ChangeSprite()
        {
            //Fetch the [Sprite](Sprite.html) and vertices from the [SpriteRenderer](SpriteRenderer.html)
            [Sprite](Sprite.html) sprite = m_SpriteRenderer.sprite;
            [Vector2](Vector2.html)[] spriteVertices = sprite.vertices;  
      
            for (int i = 0; i < spriteVertices.Length; i++)
            {
                spriteVertices[i].x = [Mathf.Clamp](Mathf.Clamp.html)(
                    (sprite.vertices[i].x - sprite.bounds.center.x -
                        (sprite.textureRectOffset.x / sprite.texture.width) + sprite.bounds.extents.x) /
                    (2.0f * sprite.bounds.extents.x) * sprite.rect.width,
                    0.0f, sprite.rect.width);  
      
                spriteVertices[i].y = [Mathf.Clamp](Mathf.Clamp.html)(
                    (sprite.vertices[i].y - sprite.bounds.center.y -
                        (sprite.textureRectOffset.y / sprite.texture.height) + sprite.bounds.extents.y) /
                    (2.0f * sprite.bounds.extents.y) * sprite.rect.height,
                    0.0f, sprite.rect.height);  
      
                // Make a small change to the second vertex
                if (i == 2)
                {
                    //Make sure the vertices stay inside the [Sprite](Sprite.html) rectangle
                    if (spriteVertices[i].x < sprite.rect.size.x - 5)
                    {
                        spriteVertices[i].x = spriteVertices[i].x + 5;
                    }
                    else spriteVertices[i].x = 0;
                }
            }
            //Override the geometry with the new vertices
            sprite.OverrideGeometry(spriteVertices, sprite.triangles);
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

