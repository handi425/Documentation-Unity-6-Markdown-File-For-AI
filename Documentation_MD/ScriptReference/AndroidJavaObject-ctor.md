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

# AndroidJavaObject Constructor

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

public AndroidJavaObject(string className, params object[] args);

### Parameters

className | Specifies the Java class name (e.g. "`java.lang.String`" or "`java/lang/String`").  
---|---  
args | An array of parameters passed to the constructor.  
  
### Description

Construct an AndroidJavaObject based on the name of the class.

This essentially means locate the class type, allocate an object and run the
specified constructor.

* * *

## Declaration

public AndroidJavaObject(IntPtr jobject);

### Parameters

jobject | A reference to existing Java object.  
---|---  
  
### Description

Create AndroidJavaObject for existing Java object.

Does not take ownership of passed reference, you still have to delete it.

* * *

## Declaration

public AndroidJavaObject(IntPtr clazz, IntPtr constructorID, params object[]
args);

### Parameters

clazz | A pointer to Java class.  
---|---  
constructorID | A method ID for the constructor to be used.  
args | An array of parameters passed to the constructor.  
  
### Description

Create AndroidJavaObject (and it's Java counterpart) using given Java class
and constructor.

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

