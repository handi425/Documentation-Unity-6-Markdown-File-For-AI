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

#
[AndroidApplication](Android.AndroidApplication.html).InvokeOnUnityMainThread

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

public static void
InvokeOnUnityMainThread([Unity.Android.Gradle.Manifest.Action](Unity.Android.Gradle.Manifest.Action.html)
action);

### Description

Invokes delegate on Android application's main thread.

This is useful if you receive a Java callback on the UI thread, but want to
process result on Unity's main thread.  
  
Additional resources:
[Threads](https://developer.android.com/guide/components/processes-and-
threads#Threads)

    
    
    using System.Threading;
    using UnityEngine;
    using UnityEngine.Android;  
      
    public class JavaThreads : [MonoBehaviour](MonoBehaviour.html)
    {
        public class MyButtonListener : [AndroidJavaProxy](AndroidJavaProxy.html)
        {
            public MyButtonListener()
                : base("android.view.View$OnClickListener")
            {
            }  
      
            public void onClick([AndroidJavaObject](AndroidJavaObject.html) view)
            {
                [Debug.Log](Debug.Log.html)($"onClick called on UI thread ${Thread.CurrentThread.ManagedThreadId}");  
      
                [AndroidApplication.InvokeOnUnityMainThread](Android.AndroidApplication.InvokeOnUnityMainThread.html)(() =>
                {
                    [Debug.Log](Debug.Log.html)($"Delegating to main thread ${Thread.CurrentThread.ManagedThreadId}");
                });  
      
                view.Dispose();
            }
        }
        public void Start()
        {
            [AndroidApplication.InvokeOnUIThread](Android.AndroidApplication.InvokeOnUIThread.html)(() =>
            {
                // [Button](UIElements.Button.html) can only be added on UI thread
                using var button = new [AndroidJavaObject](AndroidJavaObject.html)("android.widget.Button", [AndroidApplication.currentActivity](Android.AndroidApplication-currentActivity.html));
                button.Call("setText", "Hello World");
                using var layoutParams = new [AndroidJavaObject](AndroidJavaObject.html)("android.widget.LinearLayout$LayoutParams", 500, 100);
                button.Call("setLayoutParams", layoutParams);
                button.Call("setOnClickListener", new MyButtonListener());  
      
                [AndroidApplication.unityPlayer](Android.AndroidApplication-unityPlayer.html)
                    .Call<[AndroidJavaObject](AndroidJavaObject.html)>("getFrameLayout")
                    .Call("addView", button);
            });
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

