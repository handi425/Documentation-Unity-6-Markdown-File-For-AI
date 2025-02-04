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

#  [Profiler](Profiling.Profiler.html).EndThreadProfiling

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

public static void EndThreadProfiling();

### Description

Frees the internal resources used by the Profiler for the thread.

Profiler allocates memory to store information about the thread. To free that
memory use _EndThreadProfiling_. Once called, Profiler stops collecting any
data on the thread.  
  
**Note:** Calling this method on an internal Unity thread (such as main
thread, render thread or job system threads) has no effect.

    
    
    using UnityEngine;
    using UnityEngine.Profiling;
    using System.Threading;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [CustomSampler](Profiling.CustomSampler.html) sampler;
        void Start()
        {
            sampler = [CustomSampler.Create](Profiling.CustomSampler.Create.html)("MyCustomSampler");
            var thread = new Thread(MyThreadFunc) { IsBackground = true };
            thread.Start();
        }  
      
        void MyThreadFunc()
        {
            [Profiler.BeginThreadProfiling](Profiling.Profiler.BeginThreadProfiling.html)("My threads", "My thread 1");
            // Now samples will show up in the profiler timeline view
            for (int i = 0; i < 10; i++)
            {
                sampler.Begin();
                // ...
                sampler.End();
            }  
      
            // Unregister the thread before exit
            [Profiler.EndThreadProfiling](Profiling.Profiler.EndThreadProfiling.html)();
        }
    }
    

Additional resources:
[Profiler.BeginThreadProfiling](Profiling.Profiler.BeginThreadProfiling.html),
[CustomSampler](Profiling.CustomSampler.html).

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

