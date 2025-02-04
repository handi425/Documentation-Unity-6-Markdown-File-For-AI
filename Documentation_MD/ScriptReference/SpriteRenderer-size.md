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

#  [SpriteRenderer](SpriteRenderer.html).size

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

public [Vector2](Vector2.html) size;

### Description

Property to set or get the size to render when the
[SpriteRenderer.drawMode](SpriteRenderer-drawMode.html) is set to
[SpriteDrawMode.Sliced](SpriteDrawMode.Sliced.html) or
[SpriteDrawMode.Tiled](SpriteDrawMode.Tiled.html).

Assigning a Sprite to [SpriteRenderer.sprite](SpriteRenderer-sprite.html) when
it is null will also set the [SpriteRenderer.size](SpriteRenderer-size.html)
value to the Sprite's width and height.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Rigidbody2D](Rigidbody2D.html) rb;
        private [SpriteRenderer](SpriteRenderer.html) sprRend;  
      
        void Awake()
        {
            sprRend = gameObject.AddComponent<[SpriteRenderer](SpriteRenderer.html)>() as [SpriteRenderer](SpriteRenderer.html);
            sprRend.drawMode = [SpriteDrawMode.Sliced](SpriteDrawMode.Sliced.html);  
      
            rb = gameObject.AddComponent<[Rigidbody2D](Rigidbody2D.html)>() as [Rigidbody2D](Rigidbody2D.html);
            rb.bodyType = [RigidbodyType2D.Kinematic](RigidbodyType2D.Kinematic.html);
        }  
      
        void Start()
        {
            gameObject.GetComponent<[SpriteRenderer](SpriteRenderer.html)>().sprite = [Resources.Load](Resources.Load.html)<[Sprite](Sprite.html)>("image256x128");
            gameObject.transform.Translate(0.0f, 0.0f, 0.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the [Space](Space.html) key to increase the size of the sprite
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                sprRend.size += new [Vector2](Vector2.html)(0.05f, 0.01f);
                [Debug.Log](Debug.Log.html)("[Sprite](Sprite.html) size: " + sprRend.size.ToString("F2"));
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

