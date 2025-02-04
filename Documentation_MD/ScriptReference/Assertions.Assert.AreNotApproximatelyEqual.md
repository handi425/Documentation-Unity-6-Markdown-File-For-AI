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

#  [Assert](Assertions.Assert.html).AreNotApproximatelyEqual

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

public static void AreNotApproximatelyEqual(float expected, float actual);

## Declaration

public static void AreNotApproximatelyEqual(float expected, float actual,
string message);

## Declaration

public static void AreNotApproximatelyEqual(float expected, float actual,
float tolerance);

## Declaration

public static void AreNotApproximatelyEqual(float expected, float actual,
float tolerance, string message);

### Parameters

tolerance | Tolerance of approximation.  
---|---  
expected | The assumed [Assert](Assertions.Assert.html) value.  
actual | The exact [Assert](Assertions.Assert.html) value.  
message | The string used to describe the [Assert](Assertions.Assert.html).  
  
### Description

Asserts that the values are approximately not equal.

An absolute error check is used for approximate equality check (|a-b| <
tolerance). Default tolerance is 0.00001f.

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class AssertionExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) rb;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Make sure the rigidbody never stops.
            // AreNotApproximatelyEqual should be used for comparing floating point variables.
            // Unless specified, default error tolerance will be used.
            [Assert.AreNotApproximatelyEqual](Assertions.Assert.AreNotApproximatelyEqual.html)(0.0f, rb.velocity.magnitude);
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

