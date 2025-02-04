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

# WaitForSeconds

class in UnityEngine

/

Inherits from:[YieldInstruction](YieldInstruction.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Suspends the coroutine execution for the given amount of seconds using scaled
time.

The real time suspended is equal to the given time divided by
[Time.timeScale](Time-timeScale.html). See
[WaitForSecondsRealtime](WaitForSecondsRealtime.html) if you wish to wait
using unscaled time. [WaitForSeconds](WaitForSeconds.html) can only be used
with a `yield` statement in coroutines.  
  
There are some factors which can mean the actual amount of time waited does
not precisely match the amount of time specified:  
**1.** Start waiting at the `end` of the current frame. If you start
[WaitForSeconds](WaitForSeconds.html) with duration 't' in a long frame (for
example, one which has a long operation which blocks the main thread such as
some synchronous loading), the coroutine will return 't' seconds after the end
of the frame, not 't' seconds after it was called.  
**2.** Allow the coroutine to resume on the first frame after 't' seconds has
passed, not exactly after 't' seconds has passed.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class WaitForSecondsExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            //Start the coroutine we define below named ExampleCoroutine.
            StartCoroutine(ExampleCoroutine());
        }  
      
        IEnumerator ExampleCoroutine()
        {
            //Print the time of when the function is first called.
            [Debug.Log](Debug.Log.html)("Started [Coroutine](Coroutine.html) at timestamp : " + [Time.time](Time-time.html));  
      
            //yield on a new [YieldInstruction](YieldInstruction.html) that waits for 5 seconds.
            yield return new [WaitForSeconds](WaitForSeconds.html)(5);  
      
            //After we have waited 5 seconds print the time again.
            [Debug.Log](Debug.Log.html)("Finished [Coroutine](Coroutine.html) at timestamp : " + [Time.time](Time-time.html));
        }
    }
    

Additional resources:
[MonoBehaviour.StartCoroutine](MonoBehaviour.StartCoroutine.html),
[AsyncOperation](AsyncOperation.html),
[WaitForEndOfFrame](WaitForEndOfFrame.html),
[WaitForFixedUpdate](WaitForFixedUpdate.html),
[WaitForSecondsRealtime](WaitForSecondsRealtime.html),
[WaitUntil](WaitUntil.html), [WaitWhile](WaitWhile.html).

### Constructors

[WaitForSeconds](WaitForSeconds-ctor.html)| Suspends the coroutine execution
for the given amount of seconds using scaled time.  
---|---  
  
### Inherited Members

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

