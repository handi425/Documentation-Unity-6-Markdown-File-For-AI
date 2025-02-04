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

# AndroidJavaProxy

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

This class can be used to implement any java interface. Any java vm method
invocation matching the interface on the proxy object will automatically be
passed to the c# implementation.

**Note** : this API can be used from custom thread, but requires that thread
to be attached to JVM first, see
[AndroidJNI.AttachCurrentThread](AndroidJNI.AttachCurrentThread.html).

    
    
    // Opens an android date picker dialog and grabs the result using a callback.
    using UnityEngine;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private static DateTime selectedDate = DateTime.Now;  
      
        class DateCallback : [AndroidJavaProxy](AndroidJavaProxy.html)
        {
            public DateCallback() : base("android.app.DatePickerDialog$OnDateSetListener") {}
            void onDateSet([AndroidJavaObject](AndroidJavaObject.html) view, int year, int monthOfYear, int dayOfMonth)
            {
                selectedDate = new DateTime(year, monthOfYear + 1, dayOfMonth);
                // If you have no longer any uses for the object, it must be disposed to prevent a leak
                view.Dispose();
            }
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(15, 15, 450, 75), string.Format("{0:yyyy-MM-dd}", selectedDate)))
            {
                var activity = new [AndroidJavaClass](AndroidJavaClass.html)("com.unity3d.player.UnityPlayer").GetStatic<[AndroidJavaObject](AndroidJavaObject.html)>("currentActivity");
                activity.Call("runOnUiThread", new [AndroidJavaRunnable](AndroidJavaRunnable.html)(() =>
                {
                    new [AndroidJavaObject](AndroidJavaObject.html)("android.app.DatePickerDialog", activity, new DateCallback(), selectedDate.Year, selectedDate.Month - 1, selectedDate.Day).Call("show");
                }));
            }
        }
    }
    

### Properties

[javaInterface](AndroidJavaProxy-javaInterface.html)| Java interface
implemented by the proxy.  
---|---  
  
### Constructors

[AndroidJavaProxy](AndroidJavaProxy-ctor.html)|  
---|---  
  
### Public Methods

[equals](AndroidJavaProxy-equals.html)| The equivalent of the java.lang.Object
equals() method.  
---|---  
[hashCode](AndroidJavaProxy-hashCode.html)| The equivalent of the
java.lang.Object hashCode() method.  
[Invoke](AndroidJavaProxy.Invoke.html)| Called by the java vm whenever a
method is invoked on the java proxy interface. You can override this to run
special code on method invocation, or you can leave the implementation as is,
and leave the default behavior which is to look for c# methods matching the
signature of the java method.  
[toString](AndroidJavaProxy-toString.html)| The equivalent of the
java.lang.Object toString() method.  
  
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

