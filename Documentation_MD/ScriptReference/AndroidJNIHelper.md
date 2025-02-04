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

# AndroidJNIHelper

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

Helper interface for JNI interaction; signature creation and method lookups.  
  
**Note:** Using _raw_ JNI functions requires advanced knowledge of the Android
Java Native Interface (JNI). _Please take note._

### Static Properties

[debug](AndroidJNIHelper-debug.html)| Set debug to true to log calls through
the AndroidJNIHelper.  
---|---  
  
### Static Methods

[Box](AndroidJNIHelper.Box.html)| Convert primitive to it's object
counterpart.  
---|---  
[ConvertFromJNIArray](AndroidJNIHelper.ConvertFromJNIArray.html)| Creates a
managed array from a Java array.  
[ConvertToJNIArray](AndroidJNIHelper.ConvertToJNIArray.html)| Creates a Java
array from a managed array.  
[CreateJavaProxy](AndroidJNIHelper.CreateJavaProxy.html)| Creates a java proxy
object which connects to the supplied proxy implementation.  
[CreateJavaRunnable](AndroidJNIHelper.CreateJavaRunnable.html)| Creates a
UnityJavaRunnable object (implements java.lang.Runnable).  
[CreateJNIArgArray](AndroidJNIHelper.CreateJNIArgArray.html)| Creates the
parameter array to be used as argument list when invoking Java code through
CallMethod() in AndroidJNI.  
[DeleteJNIArgArray](AndroidJNIHelper.DeleteJNIArgArray.html)| Deletes any
local jni references previously allocated by CreateJNIArgArray().  
[GetConstructorID](AndroidJNIHelper.GetConstructorID.html)| Scans a particular
Java class for a constructor method matching a signature.  
[GetFieldID](AndroidJNIHelper.GetFieldID.html)| Scans a particular Java class
for a field matching a name and a signature.  
[GetMethodID](AndroidJNIHelper.GetMethodID.html)| Scans a particular Java
class for a method matching a name and a signature.  
[GetSignature](AndroidJNIHelper.GetSignature.html)| Creates the JNI signature
string for particular object type.  
[Unbox](AndroidJNIHelper.Unbox.html)| Converts Java object of a boxed type to
its primitive counterpart.  
  
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

