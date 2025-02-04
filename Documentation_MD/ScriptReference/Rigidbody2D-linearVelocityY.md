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

#  [Rigidbody2D](Rigidbody2D.html).linearVelocityY

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

public float linearVelocityY;

### Description

The Y component of the linear velocity of the Rigidbody2D in world-units per
second.

The linear velocity is specified as a [Vector2](Vector2.html) with components
in the X and Y directions (there is no Z direction in 2D physics).  
  
This property lets you read or write the Y component of the
[Rigidbody2D.linearVelocity](Rigidbody2D-linearVelocity.html) separately
without affecting the X component of the
[Rigidbody2D.linearVelocity](Rigidbody2D-linearVelocity.html). This can be
convenient when dealing with only X or Y directions in isolation.  
  
Additional resources:
[Rigidbody2D.linearVelocity](Rigidbody2D-linearVelocity.html) and
[Rigidbody2D.linearVelocityX](Rigidbody2D-linearVelocityX.html).

    
    
    using UnityEngine;  
      
    // Ensure that the maximum vertical speed moving up isn't larger than the configurable value.
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public float MaximumVerticalSpeed = 2f;  
      
        private [Rigidbody2D](Rigidbody2D.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            // Clamp the vertical speed.
            if (rb.linearVelocityY > MaximumVerticalSpeed)
            {
                rb.linearVelocityY = MaximumVerticalSpeed;
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

