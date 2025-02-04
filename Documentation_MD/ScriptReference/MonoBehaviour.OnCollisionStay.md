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

#  [MonoBehaviour](MonoBehaviour.html).OnCollisionStay(Collision)

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

other | The Collision data associated with this collision.  
---|---  
  
### Description

OnCollisionStay is called once per frame for every Collider or Rigidbody that
touches another Collider or Rigidbody.

In contrast to OnTriggerStay, OnCollisionStay is passed the
[Collision](Collision.html) class and not a [Collider](Collider.html). The
[Collision](Collision.html) class contains information about contact points,
impact velocity etc. If you don't use collisionInfo in the function, leave out
the collisionInfo parameter as this avoids unneccessary calculations.  
  
**Note:** Collision events are only sent if one of the colliders also has a
non-kinematic rigidbody attached. Collision events will be sent to disabled
MonoBehaviours, to allow enabling Behaviours in response to collisions.  
  
Collision stay events are not sent for sleeping Rigidbodies.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnCollisionStay([Collision](Collision.html) collisionInfo)
        {
            // [Debug](Debug.html)-draw all contact points and normals
            foreach ([ContactPoint](ContactPoint.html) contact in collisionInfo.contacts)
            {
                [Debug.DrawRay](Debug.DrawRay.html)(contact.point, contact.normal, [Color.white](Color-white.html));
            }
        }
    }
    

OnCollisionStay can be a co-routine, simply use the yield statement in the
function.

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

