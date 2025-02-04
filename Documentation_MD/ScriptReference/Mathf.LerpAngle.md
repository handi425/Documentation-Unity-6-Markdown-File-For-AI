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

#  [Mathf](Mathf.html).LerpAngle

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

[Switch to Manual](../Manual/class-Mathf.html "Go to Mathf Component in the
Manual")

## Declaration

public static float LerpAngle(float a, float b, float t);

### Parameters

a | The start angle. A float expressed in degrees.  
---|---  
b | The end angle. A float expressed in degrees.  
t | The interpolation value between the start and end angles. This value is clamped to the range [0, 1].  
  
### Returns

**float** Returns the interpolated float result between angle `a` and angle
`b`, based on the interpolation value `t`.

### Description

Same as [Lerp](Mathf.Lerp.html) but makes sure the values interpolate
correctly when they wrap around 360 degrees.

This method returns the shortest path between the specified angles. This
method wraps around values that are outside the range [-180, 180]. For
example, LerpAngle(1.0f, 190.0f, 1.0f) returns -170.0f. To find the longest
path use [Lerp](Mathf.Lerp.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        float minAngle = 0.0f;
        float maxAngle = 90.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            float angle = [Mathf.LerpAngle](Mathf.LerpAngle.html)(minAngle, maxAngle, [Time.time](Time-time.html));
            transform.eulerAngles = new [Vector3](Vector3.html)(0, angle, 0);
        }
    }
    

Additional resources: [Lerp](Mathf.Lerp.html).

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

