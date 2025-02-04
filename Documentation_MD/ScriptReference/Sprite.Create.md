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

#  [Sprite](Sprite.html).Create

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

public static [Sprite](Sprite.html) Create([Texture2D](Texture2D.html)
texture, [Rect](Rect.html) rect, [Vector2](Vector2.html) pivot, float
pixelsPerUnit, uint extrude);

## Declaration

public static [Sprite](Sprite.html) Create([Texture2D](Texture2D.html)
texture, [Rect](Rect.html) rect, [Vector2](Vector2.html) pivot, float
pixelsPerUnit, uint extrude, [SpriteMeshType](SpriteMeshType.html) meshType);

## Declaration

public static [Sprite](Sprite.html) Create([Texture2D](Texture2D.html)
texture, [Rect](Rect.html) rect, [Vector2](Vector2.html) pivot, float
pixelsPerUnit, uint extrude, [SpriteMeshType](SpriteMeshType.html) meshType,
[Vector4](Vector4.html) border, bool generateFallbackPhysicsShape);

## Declaration

public static [Sprite](Sprite.html) Create([Texture2D](Texture2D.html)
texture, [Rect](Rect.html) rect, [Vector2](Vector2.html) pivot, float
pixelsPerUnit, uint extrude, [SpriteMeshType](SpriteMeshType.html) meshType,
[Vector4](Vector4.html) border);

## Declaration

public static [Sprite](Sprite.html) Create([Texture2D](Texture2D.html)
texture, [Rect](Rect.html) rect, [Vector2](Vector2.html) pivot);

## Declaration

public static [Sprite](Sprite.html) Create([Texture2D](Texture2D.html)
texture, [Rect](Rect.html) rect, [Vector2](Vector2.html) pivot, float
pixelsPerUnit);

## Declaration

public static [Sprite](Sprite.html) Create([Texture2D](Texture2D.html)
texture, [Rect](Rect.html) rect, [Vector2](Vector2.html) pivot, float
pixelsPerUnit, uint extrude, [SpriteMeshType](SpriteMeshType.html) meshType,
[Vector4](Vector4.html) border, bool generateFallbackPhysicsShape,
SecondarySpriteTexture[] secondaryTextures);

### Parameters

texture | The Texture to obtain the Sprite graphic from.   
---|---  
rect | The rectangular section of the Texture to use for the Sprite.   
pivot | The Sprite's pivot point relative to its graphic rectangle.   
pixelsPerUnit | The number of pixels in the Sprite that correspond to one unit in world space.   
extrude | The amount by which the Sprite mesh should be expanded outwards.   
meshType | The type of mesh that is generated for the Sprite.   
border | The border sizes of the Sprite (X=left, Y=bottom, Z=right, W=top).   
generateFallbackPhysicsShape | Whether to generate a default physics shape for the Sprite.  
secondaryTextures | The Secondary Texture properties to be used by the created Sprite.   
  
### Description

Create a new Sprite object.

[Sprite.Create](Sprite.Create.html) creates a new [Sprite](Sprite.html) which
can be used in game applications. A Texture needs to be loaded and assigned to
[Sprite.Create](Sprite.Create.html) in order to control how the new
[Sprite](Sprite.html) will look. In the script example below a new Sprite is
displayed when the button is pressed. The new Sprite is created in Start.  
  
The second argument `rect` defines the sub-texture used. The `rect` argument
is defined in pixels of the Texture. A Rect(50.0f, 10.0f, 200.0f, 140.0f)
would create a left to right range from 50.0f to 50.0f + 200.0f = 250.0f. The
bottom to top range would be 10.0f to 10.0f + 140.0f = 150.0f. The third
argument `pivot` determines what becomes the center of the
[Sprite](Sprite.html). This is a `Vector2` relative to the `rect` where
Vector2(0.0f, 0.0f) is the bottom left and Vector2(1.0f, 1.0f) is the top
right. The [pixelsPerUnit](Sprite-pixelsPerUnit.html) value controls the size
of the Sprite. Reducing this below 100 pixels per world increases the size of
the Sprite. The `extrude` value defines the number of pixels which surround
the `Sprite`. This is useful if the [Sprite](Sprite.html) is included in an
atlas. `meshType` selects whether `FullRect` or `Tight` is used. Finally
`border` determines the slicing of the Sprite and is usually used to define
Sprite tiling behaviour. The values are in pixel units.  
  
Additional resources: [SpriteRenderer](SpriteRenderer.html) class.

    
    
    // Create a [Sprite](Sprite.html) at startup.
    // Assign a [Texture](Texture.html) to the [Sprite](Sprite.html) when the button is pressed.  
      
    using UnityEngine;  
      
    public class SpriteCreate : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture2D](Texture2D.html) tex;
        private [Sprite](Sprite.html) mySprite;
        private [SpriteRenderer](SpriteRenderer.html) sr;  
      
        void Awake()
        {
            sr = gameObject.AddComponent<[SpriteRenderer](SpriteRenderer.html)>() as [SpriteRenderer](SpriteRenderer.html);
            sr.color = new [Color](Color.html)(0.9f, 0.9f, 0.9f, 1.0f);  
      
            transform.position = new [Vector3](Vector3.html)(1.5f, 1.5f, 0.0f);
        }  
      
        void Start()
        {
            mySprite = [Sprite.Create](Sprite.Create.html)(tex, new [Rect](Rect.html)(0.0f, 0.0f, tex.width, tex.height), new [Vector2](Vector2.html)(0.5f, 0.5f), 100.0f);
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 100, 30), "Add sprite"))
            {
                sr.sprite = mySprite;
            }
        }
    }
    

The following code example shows how to create a Sprite at startup with
Secondary Texture properties.

    
    
    using UnityEngine;  
      
    // Create a [Sprite](Sprite.html) at startup with Secondary Textures properties  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var texture = new [Texture2D](Texture2D.html)(64, 64);
            var secondaryTexture1 = new [Texture2D](Texture2D.html)(64, 64);
            var secondaryTexture2 = new [Texture2D](Texture2D.html)(64, 64);
            var secondaryTexture3 = new [Texture2D](Texture2D.html)(64, 64);
            var secondarySpriteTexture = new[]
            {
                new [SecondarySpriteTexture](SecondarySpriteTexture.html)()
                {
                    name = "_SecondaryTexture1",
                    texture = secondaryTexture1
                },
                new [SecondarySpriteTexture](SecondarySpriteTexture.html)()
                {
                    name = "_SecondaryTexture2",
                    texture = secondaryTexture2
                },
                new [SecondarySpriteTexture](SecondarySpriteTexture.html)()
                {
                    name = "_SecondaryTexture3",
                    texture = secondaryTexture3
                }
            };  
      
            var sprite = [Sprite.Create](Sprite.Create.html)(texture, new [Rect](Rect.html)(0, 0, texture.width, texture.height), [Vector2.zero](Vector2-zero.html), 100, 0, [SpriteMeshType.FullRect](SpriteMeshType.FullRect.html), [Vector4.zero](Vector4-zero.html), false, secondarySpriteTexture);
            int spriteSecondaryTextureCount = sprite.GetSecondaryTextureCount();
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

