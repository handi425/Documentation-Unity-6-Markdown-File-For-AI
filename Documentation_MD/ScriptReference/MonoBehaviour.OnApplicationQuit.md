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

#  [MonoBehaviour](MonoBehaviour.html).OnApplicationQuit()

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

Sent to all GameObjects before the application quits.

In the Editor, Unity calls this message when playmode is stopped.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnApplicationQuit()
        {
            [Debug.Log](Debug.Log.html)("[Application](Application.html) ending after " + [Time.time](Time-time.html) + " seconds");
        }
    }
    

**Note:** iOS applications are usually suspended and do not quit. For iOS
builds, enable the "`Exit on Suspend`" property in Player Settings to make the
application quit and not suspend, otherwise you might not see this call. If
you do not enable the "`Exit on Suspend`" property then you will see calls to
[OnApplicationPause](MonoBehaviour.OnApplicationPause.html) instead.  
  
On Windows Store Apps and Windows Phone 8.1 there is no application quit
event. Use the [OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html)
event when focusStatus equals `false`.  
On WebGL it is not possible to implement
[OnApplicationQuit](MonoBehaviour.OnApplicationQuit.html) because of the way
browser tabs close. For a workaround, see the Unity User Manual documentation
on [Interacting with browser scripting in WebGL](../Manual/webgl-
interactingwithbrowserscripting.html).  
  
**Warning** : If the user suspends your application on a mobile platform, the
operating system can quit the application to free up resources. In this case,
depending on the operating system, Unity might be unable to call this method.
On mobile platforms, it is best practice to not rely on this method to save
the state of your application. Instead, consider every loss of application
focus as the exit of the application and use
[MonoBehaviour.OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) to
save any data.

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

