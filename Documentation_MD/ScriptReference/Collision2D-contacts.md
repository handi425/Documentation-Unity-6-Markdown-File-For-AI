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

#  [Collision2D](Collision2D.html).contacts

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

public ContactPoint2D[] contacts;

### Description

The specific points of contact with the incoming Collider2D. You should avoid
using this as it produces memory garbage. Use
[GetContact](Collision2D.GetContact.html) or
[GetContacts](Collision2D.GetContacts.html) instead.

Additional resources: [Collider2D](Collider2D.html) class.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) explosion;  
      
        void OnCollisionEnter2D([Collision2D](Collision2D.html) coll)
        {
            // If a missile hits this object
            if (coll.transform.tag == "Missile")
            {
                [Debug.Log](Debug.Log.html)("HIT!");  
      
                // Spawn an explosion at each point of contact
                foreach ([ContactPoint2D](ContactPoint2D.html) missileHit in coll.contacts)
                {
                    [Vector2](Vector2.html) hitPoint = missileHit.point;
                    Instantiate(explosion, new [Vector3](Vector3.html)(hitPoint.x, hitPoint.y, 0), [Quaternion.identity](Quaternion-identity.html));
                }
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

