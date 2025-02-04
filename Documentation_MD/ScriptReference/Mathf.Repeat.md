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

#  [Mathf](Mathf.html).Repeat

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

public static float Repeat(float t, float length);

### Description

Loops the value t, so that it is never larger than length and never smaller
than 0.

This is similar to the modulo operator but it works with floating point
numbers. For example, using 3.0 for `t` and 2.5 for `length`, the result would
be 0.5. With `t` = 5 and `length` = 2.5, the result would be 0.0. Note,
however, that the behaviour is not defined for negative numbers as it is for
the modulo operator.  
  
In the example below, the value of time is restricted between 0.0 and just
under 3.0. When the value of time is 3, the x position will go back to 0, and
go back to 3 as time increases, in a continuous loop.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Set the x position to loop between 0 and 3
            transform.position = new [Vector3](Vector3.html)([Mathf.Repeat](Mathf.Repeat.html)([Time.time](Time-time.html), 3), transform.position.y, transform.position.z);
        }
    }
    

The example below shows different possible outputs.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // prints 4
            [Debug.Log](Debug.Log.html)([Mathf.Repeat](Mathf.Repeat.html)(-1f, 5f));  
      
            // prints 0
            [Debug.Log](Debug.Log.html)([Mathf.Repeat](Mathf.Repeat.html)(0f, 5f));  
      
            // prints 1
            [Debug.Log](Debug.Log.html)([Mathf.Repeat](Mathf.Repeat.html)(1f, 5f));  
      
            // prints 0
            [Debug.Log](Debug.Log.html)([Mathf.Repeat](Mathf.Repeat.html)(5f, 5f));  
      
            // prints 2
            [Debug.Log](Debug.Log.html)([Mathf.Repeat](Mathf.Repeat.html)(12f, 5f));  
      
            // prints 1
            [Debug.Log](Debug.Log.html)([Mathf.Repeat](Mathf.Repeat.html)(16f, 5f));  
      
            // prints 4
            [Debug.Log](Debug.Log.html)([Mathf.Repeat](Mathf.Repeat.html)(19f, 5f));
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

