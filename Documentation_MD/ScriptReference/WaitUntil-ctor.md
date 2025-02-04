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

# WaitUntil Constructor

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

public WaitUntil(Func<bool> predicate);

### Parameters

predicate | Supplied delegate will be evaluated each frame after [MonoBehaviour.Update](MonoBehaviour.Update.html) and before [MonoBehaviour.LateUpdate](MonoBehaviour.LateUpdate.html) until delegate returns `true`.  
---|---  
  
### Description

Initializes a yield instruction with a given delegate to be evaluated.

* * *

## Declaration

public WaitUntil(Func<bool> predicate, TimeSpan timeout,
[Unity.Android.Gradle.Manifest.Action](Unity.Android.Gradle.Manifest.Action.html)
onTimeout, [WaitTimeoutMode](WaitTimeoutMode.html) timeoutMode);

### Parameters

predicate | Supplied delegate will be evaluated each frame after [MonoBehaviour.Update](MonoBehaviour.Update.html) and before [MonoBehaviour.LateUpdate](MonoBehaviour.LateUpdate.html) until delegate returns `true`.  
---|---  
timeout | Maximum time to wait after creation of the instance for the predicate to return `true`.  
onTimeout | The action to perform when the `timeout` is reached. Only performed if the predicate fails to return `true` before the maximum time specified.  
timeoutMode | Mode in which to measure time to determine `timeout`. Real time by default. Can be set to in-game time, which is scaled according to the value of [Time.timeScale](Time-timeScale.html).  
  
### Description

Initializes a yield instruction with a given delegate to be evaluated.

    
    
    using UnityEngine;
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;  
      
    public class WaitUntilExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public bool buttonPressed;  
      
        void Start()
        {
            StartCoroutine(Example());
        }  
      
        IEnumerator Example()
        {
            [Debug.Log](Debug.Log.html)("Waiting for button to be pressed...");
            yield return new [WaitUntil](WaitUntil.html)(() => buttonPressed, TimeSpan.FromSeconds(3), () => [Debug.Log](Debug.Log.html)("button was not pressed in time!"));
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

