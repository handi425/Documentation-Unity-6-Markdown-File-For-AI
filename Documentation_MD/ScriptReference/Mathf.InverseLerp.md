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

#  [Mathf](Mathf.html).InverseLerp

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

public static float InverseLerp(float a, float b, float value);

### Parameters

a | The start of the range.  
---|---  
b | The end of the range.  
value | The point within the range you want to calculate.  
  
### Returns

**float** A value between zero and one, representing where the "value"
parameter falls within the range defined by a and b.

### Description

Determines where a `value` lies between two points.

The a and b values define the start and end of a linear numeric range. The
"value" parameter you supply represents a value which might lie somewhere
within that range. This method calculates where, within the specified range,
the "value" parameter falls.  
If the "value" parameter is within the range, InverseLerp returns a value
between zero and one, proportional to the value's position within the range.
If the "value" parameter falls outside of the range, InverseLerp returns
either zero or one, depending on whether it falls before the start of the
range or after the end of the range.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float start = 20.0f;
        public float end = 40.0f;
        public float currentProgress = 22.0f;  
      
        void Start()
        {
            // the progress between start and end is stored as a 0-1 value, in 'i'
            float i = [Mathf.InverseLerp](Mathf.InverseLerp.html)(start, end, currentProgress);  
      
            // this will display "Current progress: 0.1 or 10%" in Console window
            [Debug.Log](Debug.Log.html)("Current progress: " + i + " or " + i * 100 + "%");  
      
            // the needle of an on-screen dial could then be set to a
            // rotational angle out of 360 degrees, based on the progress.
            float dialNeedleAngle = i * 360;  
      
            //// this will display "Needle angle: 36" in Console window
            [Debug.Log](Debug.Log.html)("Needle angle: " + dialNeedleAngle);
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

