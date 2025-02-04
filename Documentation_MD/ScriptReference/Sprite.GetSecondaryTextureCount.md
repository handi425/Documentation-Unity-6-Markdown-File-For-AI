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

#  [Sprite](Sprite.html).GetSecondaryTextureCount

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

public int GetSecondaryTextureCount();

### Returns

**int** Returns the number of Secondary Textures that the Sprite is using.

### Description

Gets the number of Secondary Textures that the Sprite is using.

    
    
    using UnityEngine;  
      
    // Create a [Sprite](Sprite.html) with Secondary [Texture](Texture.html) properties and retrieves the total number of
    // Secondary [Texture](Texture.html) properties the [Sprite](Sprite.html) has.  
      
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
            // This will print 3 since there are 3 Secondary [Texture](Texture.html) properties in the [Sprite](Sprite.html).
            print(spriteSecondaryTextureCount);
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

