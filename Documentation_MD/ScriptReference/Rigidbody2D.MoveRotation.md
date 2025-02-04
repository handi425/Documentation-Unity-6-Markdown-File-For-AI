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

#  [Rigidbody2D](Rigidbody2D.html).MoveRotation

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

public void MoveRotation(float angle);

### Parameters

angle | The new rotation angle for the Rigidbody object.  
---|---  
  
### Description

Rotates the Rigidbody to `angle` (given in degrees).

Rotates the Rigidbody to the specified `angle` by calculating the appropriate
angular velocity required to rotate the Rigidbody to that angle during the
next physics update. During the move,
[angularDamping](Rigidbody2D-angularDamping.html) won't affect the body. This
causes the object to rapidly move from the existing angle to the specified
`angle`.  
  
Because this feature allows a Rigidbody to be rotated rapidly to the specified
`angle`, any colliders attached to the Rigidbody will react as expected i.e.
they will produce collisions and/or triggers. This also means that if the
colliders produce a collision then it will affect the Rigidbody movement and
potentially stop it from reaching the specified `angle` during the next
physics update. If the Rigidbody is kinematic then any collisions won't affect
the Rigidbody itself and will only affect any other dynamic colliders.  
  
[Rigidbody2D](Rigidbody2D.html) components have a fixed limit on how fast they
can rotate therefore attempting to rotate large angles over short time-scales
can result in the Rigidbody not reaching the specified `angle` during the next
physics update. It is recommended that you use this for relatively small
rotational movements only.  
  
It is important to understand that the actual rotation change will only occur
during the next physics update therefore calling this method repeatedly
without waiting for the next physics update will result in the last call being
used. For this reason, it is recommended that it is called during the
FixedUpdate callback.

    
    
    // MoveRotation
    // The sprite is set a rotation speed.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture2D](Texture2D.html) tex;  
      
        private [Rigidbody2D](Rigidbody2D.html) rb2D;
        private [Sprite](Sprite.html) mySprite;
        private [SpriteRenderer](SpriteRenderer.html) sr;
        private float revSpeed = 50.0f;  
      
        void Awake()
        {
            sr = gameObject.AddComponent<[SpriteRenderer](SpriteRenderer.html)>();
            rb2D = gameObject.AddComponent<[Rigidbody2D](Rigidbody2D.html)>();
        }  
      
        void Start()
        {
            mySprite = [Sprite.Create](Sprite.Create.html)(tex, new [Rect](Rect.html)(0.0f, 0.0f, tex.width, tex.height), new [Vector2](Vector2.html)(0.5f, 0.5f), 100.0f);
            transform.localScale = new [Vector3](Vector3.html)(3.0f, 3.0f, 3.0f);
            rb2D.gravityScale = 0.0f;
            sr.sprite = mySprite;
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            rb2D.MoveRotation(rb2D.rotation + revSpeed * [Time.fixedDeltaTime](Time-fixedDeltaTime.html));
        }
    }
    

* * *

## Declaration

public void MoveRotation([Quaternion](Quaternion.html) rotation);

### Parameters

rotation | Full 3D rotation used to extract only the z-axis rotation.  
---|---  
  
### Description

An overload of MoveRotation that allows a full 3D rotation as an argument.

The z-axis rotation is extracted from the given [Quaternion](Quaternion.html)
`rotation` and used as a target angle to move the
[Rigidbody2D](Rigidbody2D.html) to. It is important to understand that the
full 3D rotation isn't used because the [Rigidbody2D](Rigidbody2D.html) only
has a single degree of rotational freedom around the z-axis.

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

