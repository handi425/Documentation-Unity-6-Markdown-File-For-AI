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

#  [Quaternion](Quaternion.html).Lerp

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

public static [Quaternion](Quaternion.html) Lerp([Quaternion](Quaternion.html)
a, [Quaternion](Quaternion.html) b, float t);

### Parameters

a | Start unit quaternion value, returned when t = 0.  
---|---  
b | End unit quaternion value, returned when t = 1.  
t | Interpolation ratio. The value is clamped to the range [0, 1].  
  
### Returns

**Quaternion** A unit quaternion interpolated between quaternions `a` and `b`.

### Description

Interpolates between `a` and `b` by `t` and normalizes the result afterwards.

This is faster than Slerp but the angular velocity will not be constant if the
rotations are far apart.

    
    
    // Interpolates rotation between the rotations
    // of from and to.
    // (Choose from and to not to be the same as
    // the object you attach this script to)  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Transform](Transform.html) from;
        [Transform](Transform.html) to;
        float speed = 0.01f;
        float timeCount = 0.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            transform.rotation = [Quaternion.Lerp](Quaternion.Lerp.html)(from.rotation, to.rotation, timeCount * speed);
            timeCount = timeCount + [Time.deltaTime](Time-deltaTime.html);
        }
    }
    

Additional resources: [Slerp](Quaternion.Slerp.html).
[LerpUnclamped](Quaternion.LerpUnclamped.html).

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

