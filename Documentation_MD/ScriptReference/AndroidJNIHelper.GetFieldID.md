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

#  [AndroidJNIHelper](AndroidJNIHelper.html).GetFieldID

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

public static IntPtr GetFieldID(IntPtr javaClass, string fieldName);

## Declaration

public static IntPtr GetFieldID(IntPtr javaClass, string fieldName, string
signature);

## Declaration

public static IntPtr GetFieldID(IntPtr javaClass, string fieldName, string
signature, bool isStatic = false);

### Parameters

javaClass | Raw JNI Java class object (obtained by calling AndroidJNI.FindClass).  
---|---  
fieldName | Name of the field as declared in Java.  
signature | Field signature (e.g. obtained by calling AndroidJNIHelper.GetSignature).  
isStatic | Set to `true` for static fields; `false` for instance (nonstatic) fields.  
  
### Description

Scans a particular Java class for a field matching a name and a signature.

The signature comparison is done to allow sub-/base-classes of a class types.
If no signature is provided the first field with the correct name will be
returned.  
  
Additional resources:
[AndroidJNIHelper.GetSignature](AndroidJNIHelper.GetSignature.html),
[AndroidJNIHelper.GetConstructorID](AndroidJNIHelper.GetConstructorID.html),
[AndroidJNIHelper.GetMethodID](AndroidJNIHelper.GetMethodID.html).

* * *

## Declaration

public static IntPtr GetFieldID(IntPtr jclass, string fieldName, bool
isStatic);

### Parameters

javaClass | Raw JNI Java class object (obtained by calling AndroidJNI.FindClass).  
---|---  
fieldName | Name of the field as declared in Java.  
isStatic | Set to `true` for static fields; `false` for instance (nonstatic) fields.  
  
### Description

Get a JNI field ID based on type detection. Generic parameter represents the
field type.

Scans a particular Java class for a field matching a signature of the field
type. The signature comparison is done to allow for sub-/base-classes of the
class types.

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

