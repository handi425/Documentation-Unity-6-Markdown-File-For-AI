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

#  [Collider](Collider.html).isTrigger

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

public bool isTrigger;

### Description

Specify if this collider is configured as a trigger.

A trigger doesn't register a collision with an incoming
[Rigidbody](Rigidbody.html). Instead, it sends
[OnTriggerEnter](Collider.OnTriggerEnter.html),
[OnTriggerExit](Collider.OnTriggerExit.html) and
[OnTriggerStay](Collider.OnTriggerStay.html) message when a rigidbody enters
or exits the trigger volume.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Collider](Collider.html) m_ObjectCollider;  
      
        void Start()
        {
            //Fetch the [GameObject](GameObject.html)'s [Collider](Collider.html) (make sure they have a [Collider](Collider.html) component)
            m_ObjectCollider = GetComponent<[Collider](Collider.html)>();
            //Here the [GameObject](GameObject.html)'s [Collider](Collider.html) is not a trigger
            m_ObjectCollider.isTrigger = false;
            //Output whether the [Collider](Collider.html) is a trigger type [Collider](Collider.html) or not
            [Debug.Log](Debug.Log.html)("Trigger On : " + m_ObjectCollider.isTrigger);
        }  
      
        void OnMouseDown()
        {
            //[GameObject](GameObject.html)'s [Collider](Collider.html) is now a trigger [Collider](Collider.html) when the [GameObject](GameObject.html) is clicked. It now acts as a trigger
            m_ObjectCollider.isTrigger = true;
            //Output to console the [GameObject](GameObject.html)’s trigger state
            [Debug.Log](Debug.Log.html)("Trigger On : " + m_ObjectCollider.isTrigger);
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

