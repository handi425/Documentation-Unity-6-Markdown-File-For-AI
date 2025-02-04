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

#  [RaycastHit2D](RaycastHit2D.html).transform

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

public [Transform](Transform.html) transform;

### Description

The [Transform](Transform.html) on the [GameObject](GameObject.html) that the
[Collider2D](Collider2D.html) is attached to.

When the [RaycastHit2D](RaycastHit2D.html) result is returned from a physics
query, the `collider` refers to the specific [Collider2D](Collider2D.html)
that was detected however `transform` refers to the
[Transform](Transform.html) on the [GameObject](GameObject.html) that the
[RaycastHit2D.collider](RaycastHit2D-collider.html) is attached to.  
  
**NOTE** : `transform` is equivalent to using
[Collider2D.transform](Collider2D-transform.html) and is provided for
convenience only. This field will be NULL if nothing was detected.  
  
Additional resources: [RaycastHit2D.collider](RaycastHit2D-collider.html).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector2](Vector2.html) direction;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Cast a ray in the specified direction.
            [RaycastHit2D](RaycastHit2D.html) hit = [Physics2D.Raycast](Physics2D.Raycast.html)(transform.position, direction);  
      
            // If something was hit then move the transform to the world origin.
            if (hit)
                hit.transform.position = [Vector3.zero](Vector3-zero.html);
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

