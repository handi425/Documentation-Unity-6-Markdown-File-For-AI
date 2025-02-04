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

#  [Quaternion](Quaternion.html).RotateTowards

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

[Switch to Manual](../Manual/class-Quaternion.html "Go to Quaternion Component
in the Manual")

## Declaration

public static [Quaternion](Quaternion.html)
RotateTowards([Quaternion](Quaternion.html) from,
[Quaternion](Quaternion.html) to, float maxDegreesDelta);

### Parameters

from | The unit quaternion to be aligned with `to`.  
---|---  
to | The target unit quaternion.  
maxDegreesDelta | The maximum angle in degrees allowed for this rotation.  
  
### Returns

**Quaternion** A unit quaternion rotated towards `to` by an angular step of
`maxDegreesDelta`.

### Description

Rotates a rotation `from` towards `to`.

The `from` quaternion is rotated towards `to` by an angular step of
`maxDegreesDelta`. The rotation will not overshoot the `to` quaternion.
Negative values of `maxDegreesDelta` moves away from `to` until the rotation
is exactly the opposite direction.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // The object whose rotation we want to match.
        public [Transform](Transform.html) target;  
      
        // Angular speed in degrees per sec.
        public float speed = 1.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // The step size is equal to speed times frame time.
            var step = speed * [Time.deltaTime](Time-deltaTime.html);  
      
            // [Rotate](UIElements.Rotate.html) our transform a step closer to the target's.
            transform.rotation = [Quaternion.RotateTowards](Quaternion.RotateTowards.html)(transform.rotation, target.rotation, step);
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

