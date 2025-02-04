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

#  [Rigidbody](Rigidbody.html).isKinematic

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

[Switch to Manual](../Manual/class-Rigidbody.html "Go to Rigidbody Component
in the Manual")

public bool isKinematic;

### Description

Controls whether physics affects the rigidbody.

If isKinematic is enabled, Forces, collisions or joints will not affect the
rigidbody anymore. The rigidbody will be under full control of animation or
script control by changing transform.position. Kinematic bodies also affect
the motion of other rigidbodies through collisions or joints. Eg. can connect
a kinematic rigidbody to a normal rigidbody with a joint and the rigidbody
will be constrained with the motion of the kinematic body. Kinematic
rigidbodies are also particularly useful for making characters which are
normally driven by an animation, but on certain events can be quickly turned
into a ragdoll by setting isKinematic to false.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rigidbody](Rigidbody.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        // Let the rigidbody take control and detect collisions.
        void EnableRagdoll()
        {
            rb.isKinematic = false;
            rb.detectCollisions = true;
        }  
      
        // Let animation control the rigidbody and ignore collisions.
        void DisableRagdoll()
        {
            rb.isKinematic = true;
            rb.detectCollisions = false;
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

