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

#  [MonoBehaviour](MonoBehaviour.html).StartCoroutine

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

public [Coroutine](Coroutine.html) StartCoroutine(IEnumerator routine);

### Description

Starts a Coroutine.

The execution of a coroutine can be paused at any point using the yield
statement. When a yield statement is used, the coroutine pauses execution and
automatically resumes at the next frame. See the [
Coroutines](../Manual/Coroutines.html) documentation for more details.  
  
Coroutines are excellent when modeling behavior over several frames. The
StartCoroutine method returns upon the first yield return, however you can
yield the result, which waits until the coroutine has finished execution.
There is no guarantee coroutines end in the same order they started, even if
they finish in the same frame.  
  
Yielding of any type, including null, results in the execution coming back on
a later frame, unless the coroutine is stopped or has completed.  
  
Note: You can stop a coroutine using MonoBehaviour.StopCoroutine and
MonoBehaviour.StopAllCoroutines. Coroutines are also stopped when the
MonoBehaviour is destroyed or if the GameObject the MonoBehaviour is attached
to is disabled. Coroutines are not stopped when a MonoBehaviour is disabled.  
  
See also: [Coroutine](Coroutine.html),
[YieldInstruction](YieldInstruction.html)  
  
An example of [StartCoroutine](MonoBehaviour.StartCoroutine.html):

    
    
    using UnityEngine;
    using System.Collections;  
      
    
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // In this example we show how to invoke a coroutine and
        // continue executing the function in parallel.  
      
        private IEnumerator coroutine;  
      
        void Start()
        {
            // - After 0 seconds, prints "Starting 0.0"
            // - After 0 seconds, prints "Before WaitAndPrint Finishes 0.0"
            // - After 2 seconds, prints "WaitAndPrint 2.0"
            print("Starting " + [Time.time](Time-time.html));  
      
            // Start function WaitAndPrint as a coroutine.  
      
            coroutine = WaitAndPrint(2.0f);
            StartCoroutine(coroutine);  
      
            print("Before WaitAndPrint Finishes " + [Time.time](Time-time.html));
        }  
      
        // every 2 seconds perform the print()
        private IEnumerator WaitAndPrint(float waitTime)
        {
            while (true)
            {
                yield return new [WaitForSeconds](WaitForSeconds.html)(waitTime);
                print("WaitAndPrint " + [Time.time](Time-time.html));
            }
        }
    }
    

Another example:

    
    
    // In this example we show how to invoke a coroutine and wait until it
    // is completed  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator Start()
        {
            // - After 0 seconds, prints "Starting 0.0"
            // - After 2 seconds, prints "WaitAndPrint 2.0"
            // - After 2 seconds, prints "Done 2.0"
            print("Starting " + [Time.time](Time-time.html));  
      
            // Start function WaitAndPrint as a coroutine. And wait until it is completed.
            // the same as yield return WaitAndPrint(2.0f);
            yield return StartCoroutine(WaitAndPrint(2.0f));
            print("Done " + [Time.time](Time-time.html));
        }  
      
        // suspend execution for waitTime seconds
        IEnumerator WaitAndPrint(float waitTime)
        {
            yield return new [WaitForSeconds](WaitForSeconds.html)(waitTime);
            print("WaitAndPrint " + [Time.time](Time-time.html));
        }
    }
    

* * *

## Declaration

public [Coroutine](Coroutine.html) StartCoroutine(string methodName, object
value = null);

### Description

Starts a coroutine named `methodName`.

In most cases you want to use the StartCoroutine variation above. However
StartCoroutine using a string method name lets you use
[StopCoroutine](MonoBehaviour.StopCoroutine.html) with a specific method name.
The downside is that the string version has a higher runtime overhead to start
the coroutine and you can pass only one parameter.

    
    
    // In this example we show how to invoke a coroutine using a string name and stop it.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator Start()
        {
            StartCoroutine("DoSomething", 2.0f);
            yield return new [WaitForSeconds](WaitForSeconds.html)(1);
            StopCoroutine("DoSomething");
        }  
      
        IEnumerator DoSomething(float someParameter)
        {
            while (true)
            {
                print("DoSomething Loop");  
      
                // Yield execution of this coroutine and return to the main loop until next frame
                yield return null;
            }
        }
    }
    

A created coroutine can start another coroutine. These two coroutines can
operate together in many ways. This includes both coroutines running in
parallel. Alternatively one coroutine can stop the other while it continues
itself. The example below shows one coroutine pausing as it starts another
one. When the second coroutine finishes it restarts the first one.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(coroutineA());
        }  
      
        IEnumerator coroutineA()
        {
            // wait for 1 second
            [Debug.Log](Debug.Log.html)("coroutineA created");
            yield return new [WaitForSeconds](WaitForSeconds.html)(1.0f);
            yield return StartCoroutine(coroutineB());
            [Debug.Log](Debug.Log.html)("coroutineA running again");
        }  
      
        IEnumerator coroutineB()
        {
            [Debug.Log](Debug.Log.html)("coroutineB created");
            yield return new [WaitForSeconds](WaitForSeconds.html)(2.5f);
            [Debug.Log](Debug.Log.html)("coroutineB enables coroutineA to run");
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

