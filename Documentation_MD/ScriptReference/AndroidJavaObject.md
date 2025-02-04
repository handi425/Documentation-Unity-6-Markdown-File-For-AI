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

# AndroidJavaObject

class in UnityEngine

/

Implemented
in:[UnityEngine.AndroidJNIModule](UnityEngine.AndroidJNIModule.html)

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

AndroidJavaObject is the Unity representation of a generic instance of
java.lang.Object.

It can be used as type-less interface to an instance of any Java class.
**Note** : this API can be used from custom thread, but requires that thread
to be attached to JVM first, see
[AndroidJNI.AttachCurrentThread](AndroidJNI.AttachCurrentThread.html).

### Constructors

[AndroidJavaObject](AndroidJavaObject-ctor.html)| Construct an
AndroidJavaObject based on the name of the class.  
---|---  
  
### Public Methods

[Call](AndroidJavaObject.Call.html)| Calls a Java method on an object (non-
static).  
---|---  
[CallStatic](AndroidJavaObject.CallStatic.html)| Call a static Java method on
a class.  
[CloneReference](AndroidJavaObject.CloneReference.html)| Creates a clone of
the C# object that references the same Java object.  
[Dispose](AndroidJavaObject.Dispose.html)| IDisposable callback.  
[Get](AndroidJavaObject.Get.html)| Get the value of a field in an object (non-
static).  
[GetRawClass](AndroidJavaObject.GetRawClass.html)| Retrieves the raw jclass
pointer to the Java class.Note: Using raw JNI functions requires advanced
knowledge of the Android Java Native Interface (JNI).  
[GetRawObject](AndroidJavaObject.GetRawObject.html)| Retrieves the raw jobject
pointer to the Java object.Note: Using raw JNI functions requires advanced
knowledge of the Android Java Native Interface (JNI).  
[GetStatic](AndroidJavaObject.GetStatic.html)| Get the value of a static field
in an object type.  
[Set](AndroidJavaObject.Set.html)| Set the value of a field in an object (non-
static).  
[SetStatic](AndroidJavaObject.SetStatic.html)| Set the value of a static field
in an object type.  
  
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

