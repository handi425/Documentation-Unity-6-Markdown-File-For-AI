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

#  [Mathf](Mathf.html).Max

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

public static float Max(float a, float b);

## Declaration

public static float Max(params float[] values);

### Description

Returns the largest of two or more values. When comparing negative values,
values closer to zero are considered larger.

    
    
    using UnityEngine;  
      
    public class ScriptExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // prints 2.4
            [Debug.Log](Debug.Log.html)([Mathf.Max](Mathf.Max.html)(1.2f, 2.4f));
        }
    }
    

* * *

## Declaration

public static int Max(int a, int b);

## Declaration

public static int Max(params int[] values);

### Description

Returns the largest value. When comparing negative values, values closer to
zero are considered larger.

    
    
    using UnityEngine;  
      
    public class ScriptExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // prints 2
            [Debug.Log](Debug.Log.html)([Mathf.Max](Mathf.Max.html)(1, 2));  
      
            // prints -1.2
            [Debug.Log](Debug.Log.html)([Mathf.Max](Mathf.Max.html)(-5.6f, -1.2f));
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

