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

#  [Sprite](Sprite.html).texture

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

public [Texture2D](Texture2D.html) texture;

### Description

Get the reference to the used Texture. If packed this will point to the atlas,
if not packed will point to the source Sprite.

This only returns the Texture the Sprite is currently using. You cannot change
the Texture using this.

    
    
    //Attach this script to a [Sprite](Sprite.html) [GameObject](GameObject.html). Make sure it has a [SpriteRenderer](SpriteRenderer.html) component (should have by default)
    //Next, attach a second [Sprite](Sprite.html) in the Inspector window of your first [Sprite](Sprite.html) [GameObject](GameObject.html)  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [SpriteRenderer](SpriteRenderer.html) m_SpriteRenderer;
        public [Sprite](Sprite.html) m_Sprite;  
      
        void Start()
        {
            //Fetch the [SpriteRenderer](SpriteRenderer.html) of the [Sprite](Sprite.html)
            m_SpriteRenderer = GetComponent<[SpriteRenderer](SpriteRenderer.html)>();
            //Output the current [Texture](Texture.html) of the [Sprite](Sprite.html) (this returns the source [Sprite](Sprite.html) if the [Texture](Texture.html) isn't packed)
            [Debug.Log](Debug.Log.html)("[Texture](Texture.html) 1 : " + m_SpriteRenderer.sprite.texture);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press [Space](Space.html) key to change the [Sprite](Sprite.html) to the [Sprite](Sprite.html) you attach in the Inspector
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //Change the [Sprite](Sprite.html)
                m_SpriteRenderer.sprite = m_Sprite;
                //Output the [Texture](Texture.html) of the new [Sprite](Sprite.html) (this returns the source [Sprite](Sprite.html) if the [Texture](Texture.html) isn't packed)
                [Debug.Log](Debug.Log.html)("[Texture](Texture.html) 2 : " + m_SpriteRenderer.sprite.texture);
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

