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

#  [SpriteRenderer](SpriteRenderer.html).sprite

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

public [Sprite](Sprite.html) sprite;

### Description

The Sprite to render.

The [SpriteRenderer](SpriteRenderer.html) component will render the assigned
Sprite.sprite sprite. The rendered sprite can be changed by specifying a
different sprite in the [sprite](SpriteRenderer-sprite.html) variable.

    
    
    // Example that loads sprites from a texture in the [Resources](Resources.html) folder
    // and allows them to be chosen by the selection button.  
      
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private string spriteNames = "part_explosion";
        private [Rect](Rect.html) buttonPos;
        private int spriteVersion = 0;
        private [SpriteRenderer](SpriteRenderer.html) spriteR;
        private [Sprite](Sprite.html)[] sprites;  
      
        void Start()
        {
            buttonPos = new [Rect](Rect.html)(10.0f, 10.0f, 150.0f, 50.0f);
            spriteR = gameObject.GetComponent<[SpriteRenderer](SpriteRenderer.html)>();
            sprites = [Resources.LoadAll](Resources.LoadAll.html)<[Sprite](Sprite.html)>(spriteNames);
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(buttonPos, "Choose next sprite"))
            {
                spriteVersion += 1;
                if (spriteVersion > 3)
                    spriteVersion = 0;
                spriteR.sprite = sprites[spriteVersion];
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

