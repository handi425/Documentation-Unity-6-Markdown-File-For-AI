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

#  [Mathf](Mathf.html).SmoothDamp

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

public static float SmoothDamp(float current, float target, ref float
currentVelocity, float smoothTime, float maxSpeed = Mathf.Infinity, float
deltaTime = Time.deltaTime);

### Parameters

current | The current value.  
---|---  
target | The target value.  
currentVelocity | Use this parameter to specify the initial velocity to move the current value towards the target value. This method updates the currentVelocity based on this movement and smooth-damping.  
smoothTime | The approximate time it takes for the current value to reach the target value. The lower the smoothTime, the faster the current value reaches the target value. The minimum smoothTime is 0.0001. If a lower value is specified, it is clamped to the minimum value.  
maxSpeed | Use this optional parameter to specify a maximum speed. By default, the maximum speed is set to infinity.  
deltaTime | The time since this method was last called. By default, this is set to `Time.deltaTime`.  
  
### Returns

**float** The current value after moving one step towards the target value.

### Description

Gradually moves the current value towards a target value, over a specified
time and at a specified velocity.

This method smoothes the current value towards a target value with a spring-
damper like algorithm. This algorithm is based on Game Programming Gems 4,
Chapter 1.10.  
  
**Note:** This method attempts to avoid overshooting the target value. When
deltaTime is 0.0f, this yields NaN for the currentVelocity. If you call back
with a currentVelocity of NaN, this method returns a NaN.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Smooth towards the height of the target  
      
        public [Transform](Transform.html) target;
        float smoothTime = 0.3f;
        float yVelocity = 0.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            float newPosition = [Mathf.SmoothDamp](Mathf.SmoothDamp.html)(transform.position.y, target.position.y, ref yVelocity, smoothTime);
            transform.position = new [Vector3](Vector3.html)(transform.position.x, newPosition, transform.position.z);
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

