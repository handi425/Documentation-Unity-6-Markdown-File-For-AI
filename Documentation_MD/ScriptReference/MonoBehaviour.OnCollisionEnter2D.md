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

#  [MonoBehaviour](MonoBehaviour.html).OnCollisionEnter2D(Collision2D)

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Parameters

other | The Collision2D data associated with this collision.  
---|---  
  
### Description

Sent when an incoming collider makes contact with this object's collider (2D
physics only).

Further information about the collision is reported in the Collision2D
parameter passed during the call. If you don't need this information then you
can declare [OnCollisionEnter2D](MonoBehaviour.OnCollisionEnter2D.html)
without the parameter.  
  
**Note:** Collision events will be sent to disabled MonoBehaviours, to allow
enabling Behaviours in response to collisions.  
  
Additional resources: [Collision2D](Collision2D.html) class,
[OnCollisionExit2D](MonoBehaviour.OnCollisionExit2D.html),
[OnCollisionStay2D](MonoBehaviour.OnCollisionStay2D.html).  
  
The folllowing two script examples create an
[OnCollisionEnter2D](MonoBehaviour.OnCollisionEnter2D.html) demo. Example1
generates a (white) `box` sprite called `GameObject1`. This sprite collides
with the Example2 `GameObject2` which is the `floor` sprite. The `box` sprite
can be moved using the up, down, left and right keys. For example, once the
`box` has fallen to the `floor` it can be pushed upwards with the up key. Once
the up key is released the `box` will fall back to the `floor`. Each time the
`box` hits the `floor` an
[OnCollisionEnter2D](MonoBehaviour.OnCollisionEnter2D.html) call will be made.
`GameObject1` simply provides a string in the console to indicate the
collision has happened.

    
    
    using UnityEngine;  
      
    // Create a box sprite which falls and hits a floor sprite.  The box can be moved/animated
    // with the up, left, right, and down keys.  Moving the box sprite upwards and letting it
    // fall will increase the number of calls from OnCollisionEnter2D.  
      
    public class Example1 : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture2D](Texture2D.html) tex;  
      
        void Awake()
        {
            [SpriteRenderer](SpriteRenderer.html) sr = gameObject.AddComponent<[SpriteRenderer](SpriteRenderer.html)>() as [SpriteRenderer](SpriteRenderer.html);
            transform.position = new [Vector3](Vector3.html)(0.0f, 2.5f, 0.0f);  
      
            [Sprite](Sprite.html) sp = [Sprite.Create](Sprite.Create.html)(tex, new [Rect](Rect.html)(0.0f, 0.0f, tex.width, tex.height), new [Vector2](Vector2.html)(0.5f, 0.5f), 100.0f);
            sr.sprite = sp;  
      
            gameObject.AddComponent<[BoxCollider2D](BoxCollider2D.html)>();  
      
            [Rigidbody2D](Rigidbody2D.html) rb = gameObject.AddComponent<[Rigidbody2D](Rigidbody2D.html)>();
            rb.bodyType = [RigidbodyType2D.Dynamic](RigidbodyType2D.Dynamic.html);
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            float moveHorizontal = [Input.GetAxis](Input.GetAxis.html)("Horizontal");
            float moveVertical = [Input.GetAxis](Input.GetAxis.html)("Vertical");  
      
            gameObject.transform.Translate(moveHorizontal * 0.05f, moveVertical * 0.25f, 0.0f);
        }  
      
        // called when the cube hits the floor
        void OnCollisionEnter2D([Collision2D](Collision2D.html) col)
        {
            [Debug.Log](Debug.Log.html)("OnCollisionEnter2D");
        }
    }
    

Example2. This creates the floor.

    
    
    using UnityEngine;  
      
    public class Example2 : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture2D](Texture2D.html) tex;  
      
        void Awake()
        {
            [SpriteRenderer](SpriteRenderer.html) sr = gameObject.AddComponent<[SpriteRenderer](SpriteRenderer.html)>() as [SpriteRenderer](SpriteRenderer.html);
            transform.position = new [Vector3](Vector3.html)(0.0f, -2.0f, 0.0f);  
      
            [Sprite](Sprite.html) sp = [Sprite.Create](Sprite.Create.html)(tex, new [Rect](Rect.html)(0.0f, 0.0f, tex.width, tex.height), new [Vector2](Vector2.html)(0.5f, 0.5f), 100.0f);
            sr.sprite = sp;  
      
            gameObject.AddComponent<[BoxCollider2D](BoxCollider2D.html)>();
        }
    }
    

The two objects are stored as GameObjects each with one of the scripts. These
GameObjects start with just the script example that it needs. Example1 is
applied to GameObject1 and Example2 to GameObject2.

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

