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

#  [RaycastHit2D](RaycastHit2D.html).bool

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

### Parameters

hit | The RaycastHit2D to being checked for valid results.  
---|---  
  
### Description

Implicit operator used to return a `true` or `false` result indicating if the
result is valid or not.

When using any physics query that returns a RaycastHit2D, you should always
first check to see if it contains a valid result which indicates a hit
(intersection) was detected. You can do this by checking if the RaycastHit2D
is `true` or `false`.  
  
**NOTE:** A valid result is indicated by the field
[RaycastHit2D.Collider](RaycastHit2D.Collider.html) referring to a valid
[Collider2D](Collider2D.html) i.e. not being NULL. This operator is therefore
equivalent to checking if that field is NULL ( `false` ) or not NULL ( `true`
).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector2](Vector2.html) direction;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Cast a ray in the direction specified in the inspector.
            [RaycastHit2D](RaycastHit2D.html) hit = [Physics2D.Raycast](Physics2D.Raycast.html)(transform.position, direction);  
      
            // If something was hit, draw a line from the start position to the point we intersected.
            if (hit)
                [Debug.DrawLine](Debug.DrawLine.html)(transform.position, hit.point, [Color.yellow](Color-yellow.html));
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

