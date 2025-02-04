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

#  [Profiler](Profiling.Profiler.html).enableAllocationCallstacks

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

public static bool enableAllocationCallstacks;

### Description

Enables the recording of callstacks for managed allocations.

When enabled, the Unity player saves callstack for each managed allocation
sample which is known as _GC.Alloc_. You can see the callstacks in the
Timeline View or in the Object Details pane of the Hierarchy View when
selecting the _GC.Alloc_ sample.  
  
You must also set [Profiler.enabled](Profiling.Profiler-enabled.html) to
`true` in order to start the capture.

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.Profiling;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Profiler.logFile](Profiling.Profiler-logFile.html) = "mylog"; //Also supports passing "myLog.raw"
            [Profiler.enableBinaryLog](Profiling.Profiler-enableBinaryLog.html) = true;
            [Profiler.enableAllocationCallstacks](Profiling.Profiler-enableAllocationCallstacks.html) = true;
            [Profiler.enabled](Profiling.Profiler-enabled.html) = true;  
      
            // Optional, if more memory is needed for the buffer
            [Profiler.maxUsedMemory](Profiling.Profiler-maxUsedMemory.html) = 256 * 1024 * 1024;
        }
    }
    

**Note:** Callstacks capture adds noticable performance overhead to the
profiling for every managed allocation.

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

