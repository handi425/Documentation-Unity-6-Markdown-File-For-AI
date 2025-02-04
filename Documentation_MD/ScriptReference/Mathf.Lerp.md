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

#  [Mathf](Mathf.html).Lerp

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

public static float Lerp(float a, float b, float t);

### Parameters

a | The start value.  
---|---  
b | The end value.  
t | The interpolation value between the two floats.  
  
### Returns

**float** The interpolated float result between the two float values.

### Description

Linearly interpolates between `a` and `b` by `t`.

The parameter `t` is clamped to the range [0, 1].  
  
When `t` = 0 returns `a`.  
When `t` = 1 return `b`.  
When `t` = 0.5 returns the midpoint of `a` and `b`.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // animate the game object from -1 to +1 and back
        public float minimum = -1.0F;
        public float maximum =  1.0F;  
      
        // starting value for the Lerp
        static float t = 0.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // animate the position of the game object...
            transform.position = new [Vector3](Vector3.html)([Mathf.Lerp](Mathf.Lerp.html)(minimum, maximum, t), 0, 0);  
      
            // .. and increase the t interpolater
            t += 0.5f * [Time.deltaTime](Time-deltaTime.html);  
      
            // now check if the interpolator has reached 1.0
            // and swap maximum and minimum so game object moves
            // in the opposite direction.
            if (t > 1.0f)
            {
                float temp = maximum;
                maximum = minimum;
                minimum = temp;
                t = 0.0f;
            }
        }
    }
    

Additional resources: [LerpUnclamped](Mathf.LerpUnclamped.html),
[LerpAngle](Mathf.LerpAngle.html), [InverseLerp](Mathf.InverseLerp.html).

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

