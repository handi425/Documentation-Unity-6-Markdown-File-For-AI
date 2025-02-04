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

#  [Sprite](Sprite.html).OverrideGeometry

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

public void OverrideGeometry(Vector2[] vertices, ushort[] triangles);

### Parameters

vertices | Array of vertex positions in Sprite Rect space.  
---|---  
triangles | Array of sprite mesh triangle indices.  
  
### Description

Sets up new Sprite geometry.

Vertex positions are in [Sprite.rect](Sprite-rect.html) space meaning from
[Rect.zero](Rect-zero.html) to [Rect.size](Rect-size.html). Pivot offset and
transformation to unit space is done automatically.  
  
The size of the triangle array must always be a multiple of 3. The vertices
connected to the triangle can be shared by simply indexing into the same
vertex.  
  
Sprite UVs are calculated automatically by mapping the provided geometry onto
the Sprite's Texture.  
  
The Sprite's mesh type will be changed to
[SpriteMeshType.Tight](SpriteMeshType.Tight.html) when the API is called.  
  
Additional resources: [Sprite.rect](Sprite-rect.html).  
  
The script example below shows an example on how the API can be used.

    
    
    // [Switch](PlayerSettings.Switch.html) a [Sprite](Sprite.html)'s geometry between a triangle and a quad.
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [SpriteRenderer](SpriteRenderer.html) m_SpriteRenderer;
        private [Rect](Rect.html) m_ButtonPos;
        void Start()
        {
            m_SpriteRenderer = gameObject.AddComponent<[SpriteRenderer](SpriteRenderer.html)>();
            // Create a blank [Texture](Texture.html) and [Sprite](Sprite.html) to override later on.
            var texture2D = new [Texture2D](Texture2D.html)(64, 64);
            m_SpriteRenderer.sprite = [Sprite.Create](Sprite.Create.html)(texture2D, new [Rect](Rect.html)(0, 0, texture2D.width, texture2D.height), [Vector2.zero](Vector2-zero.html), 64);  
      
            m_ButtonPos = new [Rect](Rect.html)(10.0f, 10.0f, 200.0f, 30.0f);
        }  
      
        // Use OverrideGeometry to switch the [Sprite](Sprite.html)'s mesh to a triangle or quad
        void ChangeSprite()
        {
            [Sprite](Sprite.html) o = m_SpriteRenderer.sprite;
            if (o.triangles.Length != 3)
            {
                var sv = new[]
                {
                    new [Vector2](Vector2.html)(0, 0),
                    new [Vector2](Vector2.html)(o.textureRect.width, 0),
                    new [Vector2](Vector2.html)(o.textureRect.width * 0.5f, o.textureRect.height),
                };
                var indices = new ushort[] { 0, 1, 2 };
                o.OverrideGeometry(sv, indices);
            }
            else
            {
                var sv = new[]
                {
                    new [Vector2](Vector2.html)(0, 0),
                    new [Vector2](Vector2.html)(o.textureRect.width, 0),
                    new [Vector2](Vector2.html)(o.textureRect.width, o.textureRect.height),
                    new [Vector2](Vector2.html)(0, o.textureRect.height),
                };
                var indices = new ushort[] { 0, 1, 2, 2, 3, 0 };
                o.OverrideGeometry(sv, indices);
            }
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(m_ButtonPos, "Perform OverrideGeometry"))
                ChangeSprite();
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

