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

#  [Collider2D](Collider2D.html).attachedRigidbody

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

public [Rigidbody2D](Rigidbody2D.html) attachedRigidbody;

### Description

The [Rigidbody2D](Rigidbody2D.html) attached to the
[Collider2D](Collider2D.html).

[Collider2D](Collider2D.html) are automatically attached to a
[Rigidbody2D](Rigidbody2D.html) on the same [GameObject](GameObject.html) as
the [Collider2D](Collider2D.html) or if none is present then on a
[Rigidbody2D](Rigidbody2D.html) on the nearest parent
[GameObject](GameObject.html). The property will be null if no
[Rigidbody2D](Rigidbody2D.html) is attached. In this case, the
[Collider2D](Collider2D.html) is attached to a hidden body known as the ground
body that lives at the world origin as is set to be
[RigidbodyType2D.Static](RigidbodyType2D.Static.html). No reference to this
hidden body is available however.  
  
Additional resources: [Rigidbody2D](Rigidbody2D.html),
[RigidbodyType2D](RigidbodyType2D.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector2](Vector2.html) force = [Vector2.up](Vector2-up.html);  
      
        void Start()
        {
            // Apply a force to the rigidbody attached to the collider.
            GetComponent<[Collider2D](Collider2D.html)>().attachedRigidbody.AddForce(force);
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

