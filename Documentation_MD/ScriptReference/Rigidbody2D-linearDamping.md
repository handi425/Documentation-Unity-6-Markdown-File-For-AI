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

#  [Rigidbody2D](Rigidbody2D.html).linearDamping

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

public float linearDamping;

### Description

The linear damping of the Rigidbody2D linear velocity.

Damping can be used to reduce the magnitude of the
[Rigidbody2D.linearVelocity](Rigidbody2D-linearVelocity.html) (linear speed)
of a [Rigidbody2D](Rigidbody2D.html) over time.  
  
Zero indicates that no damping should be used whereas higher values increase
the damping, effectively slowing down the linear motion faster. Unlike contact
friction, linear damping is always applied.  
  
**Note:** The following formula is how the linear damping is applied:
`linearVelocity *= 1.0f / ( 1.0f + simulation-time-step * linearDamping )`  
  
Additional resources:
[Rigidbody2D.angularDamping](Rigidbody2D-angularDamping.html).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Rigidbody2D](Rigidbody2D.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButton](Input.GetButton.html)("Fire1"))
                OpenParachute();  
      
            if ([Input.GetButton](Input.GetButton.html)("space"))
                CloseParachute();
        }  
      
        void OpenParachute()
        {
            // Set a large damping to simulate an open parachute.
            rb.linearDamping = 20f;
        }  
      
        void CloseParachute()
        {
            // Turn-off damping to simulate a closed parachute.
            rb.linearDamping = 0f;
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

