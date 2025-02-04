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

#  [Vector3](Vector3.html).SmoothDamp

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

## Declaration

public static [Vector3](Vector3.html) SmoothDamp([Vector3](Vector3.html)
current, [Vector3](Vector3.html) target, ref [Vector3](Vector3.html)
currentVelocity, float smoothTime, float maxSpeed = Mathf.Infinity, float
deltaTime = Time.deltaTime);

### Parameters

current | The current position.  
---|---  
target | The position we are trying to reach.  
currentVelocity | The current velocity, this value is modified by the function every time you call it.  
smoothTime | Approximately the time it will take to reach the target. A smaller value will reach the target faster.  
maxSpeed | Optionally allows you to clamp the maximum speed.  
deltaTime | The time since the last call to this function. By default Time.deltaTime.  
  
### Description

Gradually changes a vector towards a desired goal over time.

The vector is smoothed by some spring-damper like function, which will never
overshoot. The most common use is for smoothing a follow camera.

    
    
    // Smooth towards the target  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;
        public float smoothTime = 0.3F;
        private [Vector3](Vector3.html) velocity = [Vector3.zero](Vector3-zero.html);  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Define a target position above and behind the target transform
            [Vector3](Vector3.html) targetPosition = target.TransformPoint(new [Vector3](Vector3.html)(0, 5, -10));  
      
            // Smoothly move the camera towards that target position
            transform.position = [Vector3.SmoothDamp](Vector3.SmoothDamp.html)(transform.position, targetPosition, ref velocity, smoothTime);
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

