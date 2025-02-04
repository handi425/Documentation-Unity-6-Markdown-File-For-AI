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

#  [Assert](Assertions.Assert.html).AreEqual

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

public static void AreEqual([Object](Object.html) expected,
[Object](Object.html) actual, string message);

## Declaration

public static void AreEqual(sbyte expected, sbyte actual, string message);

## Declaration

public static void AreEqual(byte expected, byte actual, string message);

## Declaration

public static void AreEqual(char expected, char actual, string message);

## Declaration

public static void AreEqual(short expected, short actual, string message);

## Declaration

public static void AreEqual(ushort expected, ushort actual);

## Declaration

public static void AreEqual(sbyte expected, sbyte actual);

## Declaration

public static void AreEqual(byte expected, byte actual);

## Declaration

public static void AreEqual(char expected, char actual);

## Declaration

public static void AreEqual(short expected, short actual);

## Declaration

public static void AreEqual(ushort expected, ushort actual, string message);

## Declaration

public static void AreEqual(int expected, int actual, string message);

## Declaration

public static void AreEqual(uint expected, uint actual);

## Declaration

public static void AreEqual(int expected, int actual);

## Declaration

public static void AreEqual(uint expected, uint actual, string message);

## Declaration

public static void AreEqual(long expected, long actual);

## Declaration

public static void AreEqual(long expected, long actual, string message);

## Declaration

public static void AreEqual(ulong expected, ulong actual);

## Declaration

public static void AreEqual(ulong expected, ulong actual, string message);

## Declaration

public static void AreEqual(T expected, T actual);

## Declaration

public static void AreEqual(T expected, T actual, string message);

## Declaration

public static void AreEqual(T expected, T actual, string message,
IEqualityComparer<T> comparer);

### Parameters

expected | The assumed [Assert](Assertions.Assert.html) value.  
---|---  
actual | The exact [Assert](Assertions.Assert.html) value.  
message | The string used to describe the [Assert](Assertions.Assert.html).  
comparer | Method to compare `expected` and `actual` arguments have the same value.  
  
### Description

Assert that the values are equal.

Show message when the `expected` and `actual` are not equal. If no comparer is
specified, `EqualityComparer<T>.Default` is used.

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class AssertionExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Make sure the Game Object is always tagged as "Player"
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)("Player", gameObject.tag);
        }
    }
    

Another example:

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    // [Assert.AreEqual](Assertions.Assert.AreEqual.html) and [Assert.AreNotEqual](Assertions.Assert.AreNotEqual.html) example
    //
    // Compare 32 to 32. AreNotEqual prints message.
    // Compare 32 to 33. AreEqual prints message.  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            int expectedInt = 32;
            int actualInt = 32;  
      
            // Do not show message (32 is equal to 32).
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(expectedInt, actualInt, "AreEqual: " + expectedInt + " equals " + actualInt);  
      
            // Show message (32 is equal to 32).
            [Assert.AreNotEqual](Assertions.Assert.AreNotEqual.html)(expectedInt, actualInt, "AreNotEqual: " + expectedInt + " not equal to " + actualInt);  
      
            actualInt = 33;  
      
            // Show message (32 is not equal to 33).
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(expectedInt, actualInt, "AreEqual: " + expectedInt + " equals " + actualInt);  
      
            // Do not show message (32 is not equal to 33).
            [Assert.AreNotEqual](Assertions.Assert.AreNotEqual.html)(expectedInt, actualInt, "AreNotEqual: " + expectedInt + " not equal to " + actualInt);
        }
    }
    

And another example:

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    // Assertion.Assert.AreEqual example
    //
    // Compare [Vector2Int](Vector2Int.html) [Assert](Assertions.Assert.html) using IEqualityComparer.  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Implement the EqualityComparer class.
        class EqualityComparer : IEqualityComparer<[Vector2Int](Vector2Int.html)>
        {
            // Compare two [Vector2Int](Vector2Int.html) structures.
            // These represent the expected and actual values.
            public bool Equals([Vector2Int](Vector2Int.html) v1, [Vector2Int](Vector2Int.html) v2)
            {
                if ((v1.x == v2.x) && (v1.y == v2.y))
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }  
      
            public int GetHashCode([Vector2Int](Vector2Int.html) v)
            {
                int vCode = v.x ^ v.y;
                return vCode.GetHashCode();
            }
        }  
      
        void Start()
        {
            // Creates three [Vector2Int](Vector2Int.html) structures. v1 and v3 have equal values.
            [Vector2Int](Vector2Int.html) v1 = new [Vector2Int](Vector2Int.html)(1, 2);
            [Vector2Int](Vector2Int.html) v2 = new [Vector2Int](Vector2Int.html)(2, 1);
            [Vector2Int](Vector2Int.html) v3 = new [Vector2Int](Vector2Int.html)(1, 2);  
      
            // [Display](Display.html) missing matches between the three [Vector2Int](Vector2Int.html) structures.
            EqualityComparer comparer = new EqualityComparer();  
      
            [Debug.Log](Debug.Log.html)("Comparison of v1 against v2");
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(v1, v2, "v1 does not matches v2", comparer);
            [Assert.AreNotEqual](Assertions.Assert.AreNotEqual.html)(v1, v2, "v1 matches v2", comparer);  
      
            [Debug.Log](Debug.Log.html)("Comparison of v1 against v3");
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(v1, v3, "v1 does not matches v3", comparer);
            [Assert.AreNotEqual](Assertions.Assert.AreNotEqual.html)(v1, v3, "v1 matches v3", comparer);  
      
            [Debug.Log](Debug.Log.html)("Comparison of v2 against v3");
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(v2, v3, "v2 does not matches v3", comparer);
            [Assert.AreNotEqual](Assertions.Assert.AreNotEqual.html)(v2, v3, "v2 matches v3", comparer);
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

