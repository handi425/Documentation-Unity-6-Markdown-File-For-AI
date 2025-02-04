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

# AndroidJavaRunnable

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

public delegate void AndroidJavaRunnable();

### Description

AndroidJavaRunnable is the Unity representation of a java.lang.Runnable
object.

Note that this is a delegate. As such, a new java.lang.reflect.Proxy object is
created every time it is passed as an argument to Java. This means that
passing a variable of AndroidJavaRunnable type to Java multiple times results
in a new Java object each time with different hash code values. It also means
that calling `equals()` on the Java object created as a representation of an
AndroidJavaRunnable variable always returns false, even when compared to
itself.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // [Pass](ShaderData.Pass.html) execution context over to the Java UI thread.
        void Start()
        {
            [AndroidJavaClass](AndroidJavaClass.html) unityPlayer = new [AndroidJavaClass](AndroidJavaClass.html)("com.unity3d.player.UnityPlayer");
            [AndroidJavaObject](AndroidJavaObject.html) activity = unityPlayer.GetStatic<[AndroidJavaObject](AndroidJavaObject.html)>("currentActivity");
            activity.Call("runOnUiThread", new [AndroidJavaRunnable](AndroidJavaRunnable.html)(runOnUiThread));
        }  
      
        void runOnUiThread()
        {
            [Debug.Log](Debug.Log.html)("I'm running on the Java UI thread!");
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

