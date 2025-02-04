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

#  [AndroidJNIHelper](AndroidJNIHelper.html).Unbox

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

public static void Unbox(IntPtr obj, out sbyte value);

## Declaration

public static void Unbox(IntPtr obj, out short value);

## Declaration

public static void Unbox(IntPtr obj, out int value);

## Declaration

public static void Unbox(IntPtr obj, out long value);

## Declaration

public static void Unbox(IntPtr obj, out float value);

## Declaration

public static void Unbox(IntPtr obj, out double value);

## Declaration

public static void Unbox(IntPtr obj, out char value);

## Declaration

public static void Unbox(IntPtr obj, out bool value);

### Parameters

obj | A Java object that is a counterpart of a primitive type of the value parameter.  
---|---  
value | Destination for the primitive value of obj.  
  
### Description

Converts Java object of a boxed type to its primitive counterpart.

Each primitive type in Java has a counterpart class, for example
java.lang.Integer class is a counterpart for primitive type int. Note, that
this methods is designed Java object to be of the correct type depending of
the value you want to get. Fix example, if value is short, then obj is
expected to be of type java.lang.Short, though in practice any descendant of
java.lang.Number should work for any numeric destination, possibly with
rounding or loss.

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

