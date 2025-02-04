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

#  [Sprite](Sprite.html).GetSecondaryTextures

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

public int GetSecondaryTextures(SecondarySpriteTexture[] secondaryTexture);

### Parameters

secondaryTexture | The array of [SecondarySpriteTexture](SecondarySpriteTexture.html) to contain the Secondary Textures properties used by the Sprite.  
---|---  
  
### Returns

**int** Returns the number of Secondary Textures properties retrieved.

### Description

Retrieves an array of [SecondarySpriteTexture](SecondarySpriteTexture.html)
used by the Sprite.

If the size of the arrays passed in as parameters are less than the number of
[SecondarySpriteTexture](SecondarySpriteTexture.html) used by the sprite, the
arrays will not be resized and the results will be limited.  
  
If the size of the arrays passed in as parameters are bigger than the number
of [SecondarySpriteTexture](SecondarySpriteTexture.html) used by the sprite,
the number of elements used in the array will be indicated by the return value
of the method.

    
    
    using UnityEngine;  
      
    // Create a [Sprite](Sprite.html) with Secondary [Texture](Texture.html) properties and retrieves the
    // Secondary [Texture](Texture.html) properties with various input parameter array length.  
      
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
            var secondarySpriteTextureResult = new [SecondarySpriteTexture](SecondarySpriteTexture.html)[2];
            var resultCount = sprite.GetSecondaryTextures(secondarySpriteTextureResult);
            // There are 3 Secondary Textures, but the array is only size of 2, so the entire array is used
            print(resultCount);
            for (var i = 0; i < resultCount; ++i)
            {
                // This will print
                //_SecondaryTexture1
                //_SecondaryTexture2
                print(secondarySpriteTextureResult[i].name);
            }  
      
            secondarySpriteTextureResult = new [SecondarySpriteTexture](SecondarySpriteTexture.html)[4];
            resultCount = sprite.GetSecondaryTextures(secondarySpriteTextureResult);
            // There are 3 Secondary Textures, but the array is only size of 4, so only 3 will be used
            print(resultCount);
            for (var i = 0; i < resultCount; ++i)
            {
                // This will print
                //_SecondaryTexture1
                //_SecondaryTexture2
                //_SecondaryTexture3
                print(secondarySpriteTextureResult[i].name);
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

