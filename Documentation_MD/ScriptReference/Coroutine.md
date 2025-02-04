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

# Coroutine

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

[MonoBehaviour.StartCoroutine](MonoBehaviour.StartCoroutine.html) returns a
Coroutine. Instances of this class are only used to reference these
coroutines, and do not hold any exposed properties or functions.

A coroutine is a function that can suspend its execution (yield) until the
given [YieldInstruction](YieldInstruction.html) finishes.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator WaitAndPrint()
        {
            // suspend execution for 5 seconds
            yield return new [WaitForSeconds](WaitForSeconds.html)(5);
            print("WaitAndPrint " + [Time.time](Time-time.html));
        }  
      
        IEnumerator Start()
        {
            print("Starting " + [Time.time](Time-time.html));  
      
            // Start function WaitAndPrint as a coroutine
            yield return StartCoroutine("WaitAndPrint");
            print("Done " + [Time.time](Time-time.html));
        }
    }
    

This example shows a normal Start:

    
    
    using UnityEngine;
    using System.Collections;  
      
    // In this example we show how to invoke a coroutine and execute
    // the function in parallel.  Start does not need IEnumerator.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private IEnumerator coroutine;  
      
        void Start()
        {
            // - After 0 seconds, prints "Starting 0.0 seconds"
            // - After 0 seconds, prints "[Coroutine](Coroutine.html) started"
            // - After 2 seconds, prints "[Coroutine](Coroutine.html) ended: 2.0 seconds"
            print("Starting " + [Time.time](Time-time.html) + " seconds");  
      
            // Start function WaitAndPrint as a coroutine.  
      
            coroutine = WaitAndPrint(2.0f);
            StartCoroutine(coroutine);  
      
            print("[Coroutine](Coroutine.html) started");
        }  
      
        private IEnumerator WaitAndPrint(float waitTime)
        {
            yield return new [WaitForSeconds](WaitForSeconds.html)(waitTime);
            print("[Coroutine](Coroutine.html) ended: " + [Time.time](Time-time.html) + " seconds");
        }
    }
    

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

