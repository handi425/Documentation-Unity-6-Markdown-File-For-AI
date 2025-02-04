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

#  [Collider2D](Collider2D.html).OnTriggerEnter2D(Collider2D)

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

### Parameters

other | The other [Collider2D](Collider2D.html) involved in this collision.  
---|---  
  
### Description

Sent when another object enters a trigger collider attached to this object (2D
physics only).

Further information about the other collider is reported in the
[Collider2D](Collider2D.html) parameter passed during the call.  
  
Trigger events will be sent to disabled [MonoBehaviour](MonoBehaviour.html)s,
to allow enabling [Behaviour](Behaviour.html)s in response to collisions.  
  
Additional resources: The [Collider2D](Collider2D.html) class and the
[OnTriggerExit2D](Collider2D.OnTriggerExit2D.html) and
[OnTriggerStay2D](Collider2D.OnTriggerStay2D.html) messages.  
  
An [OnTriggerEnter2D](Collider2D.OnTriggerEnter2D.html) example is shown. This
example has two empty [GameObject](GameObject.html)s, called `GameObject1` and
`GameObject2`. These both have script files which makes the example work. The
first script, `Example1`, creates a [Sprite](Sprite.html) and adds a
[BoxCollider2D](BoxCollider2D.html) and a [Rigidbody2D](Rigidbody2D.html).
This object falls under gravity and collides with `Example2`. `Example2` has
no visibility. (The rectangle it creates is visible in the Scene window.) Both
[GameObject](GameObject.html)s report the collision.  
  
The script below is Example1.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // Create GameObject1 that falls under gravity.  It will pass through
    // Example2 and cause a collision.  GameObject1 is moved back to
    // the start position and it will again start to fall under gravity.  
      
    public class Example1 : [MonoBehaviour](MonoBehaviour.html)
    {
        void Awake()
        {
            [SpriteRenderer](SpriteRenderer.html) sr;
            sr = gameObject.AddComponent<[SpriteRenderer](SpriteRenderer.html)>() as [SpriteRenderer](SpriteRenderer.html);
            sr.color = new [Color](Color.html)(0.9f, 0.9f, 0.1f, 1.0f);  
      
            [BoxCollider2D](BoxCollider2D.html) bc;
            bc = gameObject.AddComponent<[BoxCollider2D](BoxCollider2D.html)>() as [BoxCollider2D](BoxCollider2D.html);
            bc.size = new [Vector2](Vector2.html)(1.0f, 1.0f);  
      
            [Rigidbody2D](Rigidbody2D.html) rb;
            rb = gameObject.AddComponent<[Rigidbody2D](Rigidbody2D.html)>() as [Rigidbody2D](Rigidbody2D.html);
            rb.gravityScale = 1.0f;  
      
            // A square in the [Resources](Resources.html) folder is used.
            gameObject.GetComponent<[SpriteRenderer](SpriteRenderer.html)>().sprite = [Resources.Load](Resources.Load.html)<[Sprite](Sprite.html)>("square");  
      
            // GameObject1 starts 3 units in the Up direction.
            gameObject.transform.position = new [Vector3](Vector3.html)(0.0f, 3.0f, 0.0f);
            gameObject.transform.localScale = new [Vector3](Vector3.html)(0.5f, 0.5f, 1.0f);
        }  
      
        private float timer = 0.0f;
        private bool restart = false;  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            if (restart == true)
            {
                timer = timer + [Time.deltaTime](Time-deltaTime.html);
                if (timer > 0.25f)
                {
                    gameObject.transform.position = new [Vector3](Vector3.html)(0.0f, 3.0f, 0.0f);
                    gameObject.GetComponent<[Rigidbody2D](Rigidbody2D.html)>().velocity = new [Vector2](Vector2.html)(0.0f, 0.0f);
                    restart = false;
                }
            }
        }  
      
        // called when this [GameObject](GameObject.html) collides with GameObject2.
        void OnTriggerEnter2D([Collider2D](Collider2D.html) col)
        {
            [Debug.Log](Debug.Log.html)("GameObject1 collided with " + col.name);
            restart = true;
            timer = 0.0f;
        }
    }
    

This is `Example2` which is the collide script for the second
[GameObject](GameObject.html):

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // Create a rectangle that the other [GameObject](GameObject.html) will collide with.
    // Note that this [GameObject](GameObject.html) has no visibility.
    // (View in the [Scene](SceneManagement.Scene.html) view to see this [GameObject](GameObject.html).)  
      
    public class Example2 : [MonoBehaviour](MonoBehaviour.html)
    {
        void Awake()
        {
            [BoxCollider2D](BoxCollider2D.html) bc;
            bc = gameObject.AddComponent<[BoxCollider2D](BoxCollider2D.html)>() as [BoxCollider2D](BoxCollider2D.html);
            bc.size = new [Vector2](Vector2.html)(3.0f, 1.0f);
            bc.isTrigger = true;  
      
            gameObject.transform.localScale = new [Vector3](Vector3.html)(3.0f, 1.0f, 1.0f);
            gameObject.transform.position = new [Vector3](Vector3.html)(0.0f, -2.0f, 0.0f);
        }  
      
        void OnTriggerEnter2D([Collider2D](Collider2D.html) col)
        {
            [Debug.Log](Debug.Log.html)("GameObject2 collided with " + col.name);
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

