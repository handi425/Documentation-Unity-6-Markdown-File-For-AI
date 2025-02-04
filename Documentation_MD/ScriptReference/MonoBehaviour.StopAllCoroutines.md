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

#  [MonoBehaviour](MonoBehaviour.html).StopAllCoroutines

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

## Declaration

public void StopAllCoroutines();

### Description

Stops all coroutines running on this behaviour.

A MonoBehaviour can execute zero or more coroutines. Created coroutines can
execute for a range of times. In the script example below two coroutines are
created and run without stopping. However,
[StopAllCoroutines](MonoBehaviour.StopAllCoroutines.html) is used to stop both
of them. This action can be made to happen on a script that runs multiple
coroutines. No arguments are needed because all coroutines on a script are
stopped.  
**Note:** [StopAllCoroutines](MonoBehaviour.StopAllCoroutines.html) operates
only on the one script it is attached to.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Create two coroutines that run at different speeds.
    // When the space key is pressed stop both of them.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        //coroutine 1
        IEnumerator DoSomething1()
        {
            while (true)
            {
                print("DoSomething1");
                yield return new [WaitForSeconds](WaitForSeconds.html)(1.0f);
            }
        }  
      
        //coroutine 2
        IEnumerator DoSomething2()
        {
            while (true)
            {
                print("DoSomething2");
                yield return new [WaitForSeconds](WaitForSeconds.html)(1.5f);
            }
        }  
      
        void Start()
        {
            StartCoroutine("DoSomething1");
            StartCoroutine("DoSomething2");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)("space"))
            {
                StopAllCoroutines();
                print("Stopped all Coroutines: " + [Time.time](Time-time.html));
            }
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

