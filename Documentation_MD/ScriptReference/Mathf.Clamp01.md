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

#  [Mathf](Mathf.html).Clamp01

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

public static float Clamp01(float value);

### Description

Clamps value between 0 and 1 and returns value.

If the value is negative then zero is returned. If value is greater than one
then one is returned.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Set the position of the transform to be that of the time
        // but never less than 0 or more than 1  
      
        void [Update](PlayerLoop.Update.html)()
        {
            transform.position = new [Vector3](Vector3.html)([Mathf.Clamp01](Mathf.Clamp01.html)([Time.time](Time-time.html)), 0, 0);
        }
    }
    
    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // Print a random number every second.  This number is chosen over a
    // range from startValue to endValue.  The random number is clamped
    // to between zero and one by Clamp01().  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public float startValue = -0.5f;
        public float endValue = 1.5f;  
      
        private float timeCount = 0.0f;  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            timeCount += [Time.deltaTime](Time-deltaTime.html);  
      
            if (timeCount > 1.0f)
            {
                float result = [Random.value](Random-value.html);
                result = result * (endValue - startValue);
                result = result + startValue;  
      
                float clampValue = [Mathf.Clamp01](Mathf.Clamp01.html)(result);  
      
                [Debug.Log](Debug.Log.html)("value: " + result.ToString("F3") + " result: " + clampValue.ToString("F3"));  
      
                timeCount = 0.0f;
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

