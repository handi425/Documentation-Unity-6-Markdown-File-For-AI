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

# WaitUntil

class in UnityEngine

/

Inherits from:[CustomYieldInstruction](CustomYieldInstruction.html)

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

Suspends the coroutine execution until the supplied delegate evaluates to
`true`.

WaitUntil can only be used with a `yield` statement in coroutines.  
  
Supplied delegate will be executed each frame after script
[MonoBehaviour.Update](MonoBehaviour.Update.html) and before
[MonoBehaviour.LateUpdate](MonoBehaviour.LateUpdate.html). When the delegate
finally evaluates to `true`, the coroutine will proceed with its execution.  
  
Additional resources: [AsyncOperation](AsyncOperation.html),
[WaitForEndOfFrame](WaitForEndOfFrame.html),
[WaitForFixedUpdate](WaitForFixedUpdate.html),
[WaitForSeconds](WaitForSeconds.html),
[WaitForSecondsRealtime](WaitForSecondsRealtime.html),
[WaitWhile](WaitWhile.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class WaitUntilExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public int frame;  
      
        void Start()
        {
            StartCoroutine(Example());
        }  
      
        IEnumerator Example()
        {
            [Debug.Log](Debug.Log.html)("Waiting for princess to be rescued...");
            yield return new [WaitUntil](WaitUntil.html)(() => frame >= 10);
            [Debug.Log](Debug.Log.html)("Princess was rescued!");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (frame <= 10)
            {
                [Debug.Log](Debug.Log.html)("Frame: " + frame);
                frame++;
            }
        }
    }
    

### Constructors

[WaitUntil](WaitUntil-ctor.html)| Initializes a yield instruction with a given
delegate to be evaluated.  
---|---  
  
### Inherited Members

### Properties

[keepWaiting](CustomYieldInstruction-keepWaiting.html)| Indicates if coroutine
should be kept suspended.  
---|---  
  
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

