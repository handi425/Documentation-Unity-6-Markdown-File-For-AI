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

# Assert

class in UnityEngine.Assertions

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

The Assert class contains assertion methods for setting invariants in the
code.

All method calls will be conditionally included only in a development build,
unless specified explicitly. See
[BuildOptions.ForceEnableAssertions](BuildOptions.ForceEnableAssertions.html).
The inclusion of an assertion is controlled by the `UNITY_ASSERTIONS` define.  
  
Assert throws exceptions whenever an assertion fails.  
  
If a debugger is attached to the project
(System.Diagnostics.Debugger.IsAttached is true),
[AssertionException](Assertions.AssertionException.html) is thrown to pause
the execution and invoke the debugger.

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class AssertionExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public int health;
        public [GameObject](GameObject.html) go;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // You expect the health never to be equal to zero
            [Assert.AreNotEqual](Assertions.Assert.AreNotEqual.html)(0, health);  
      
            // The referenced [GameObject](GameObject.html) should be always (in every frame) be active
            [Assert.IsTrue](Assertions.Assert.IsTrue.html)(go.activeInHierarchy);
        }
    }
    

### Static Methods

[AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)| Assert
the values are approximately equal.  
---|---  
[AreEqual](Assertions.Assert.AreEqual.html)| Assert that the values are equal.  
[AreNotApproximatelyEqual](Assertions.Assert.AreNotApproximatelyEqual.html)|
Asserts that the values are approximately not equal.  
[AreNotEqual](Assertions.Assert.AreNotEqual.html)| Assert that the values are
not equal.  
[IsFalse](Assertions.Assert.IsFalse.html)| Return true when the condition is
false. Otherwise return false.  
[IsNotNull](Assertions.Assert.IsNotNull.html)| Assert that the value is not
null.  
[IsNull](Assertions.Assert.IsNull.html)| Assert the value is null.  
[IsTrue](Assertions.Assert.IsTrue.html)| Asserts that the condition is true.  
  
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

