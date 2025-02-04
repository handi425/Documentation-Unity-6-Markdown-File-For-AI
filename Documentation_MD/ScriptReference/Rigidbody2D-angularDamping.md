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

#  [Rigidbody2D](Rigidbody2D.html).angularDamping

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

public float angularDamping;

### Description

The angular damping of the Rigidbody2D angular velocity.

Damping can be used to reduce the
[Rigidbody2D.angularVelocity](Rigidbody2D-angularVelocity.html) (angular
speed) of a [Rigidbody2D](Rigidbody2D.html) over time.  
  
Zero indicates that no damping should be used whereas higher values increase
the damping, effectively slowing down the rotational movement faster. Unlike
contact friction, angular damping is always applied.  
  
**Note:** The following formula is how the angular damping is applied
`angularVelocity *= 1.0f / ( 1.0f + simulation-time-step * angularDamping )`  
  
Additional resources:
[Rigidbody2D.linearDamping](Rigidbody2D-linearDamping.html).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Rigidbody2D](Rigidbody2D.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();  
      
            // Start the object spining fast.
            rb.angularVelocity = 45f;  
      
            // Turn-off the angular damping.
            rb.angularDamping = 0f;
        }  
      
     
        void [Update](PlayerLoop.Update.html)()
        {
            // Set a large angular damping to slow down the spin fast.
            if ([Input.GetKeyDown](Input.GetKeyDown.html)("space"))
                rb.angularDamping = 0.8f;
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

