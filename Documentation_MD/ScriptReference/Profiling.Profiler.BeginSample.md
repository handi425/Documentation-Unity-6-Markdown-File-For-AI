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

#  [Profiler](Profiling.Profiler.html).BeginSample

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

public static void BeginSample(string name);

## Declaration

public static void BeginSample(string name, [Object](Object.html)
targetObject);

### Parameters

name | A string to identify the sample in the Profiler window.  
---|---  
targetObject | An object that provides context to the sample,.  
  
### Description

Begin profiling a piece of code with a custom label.

The Profiler displays the sample in the Hierarchy and Timeline views. The
sample is nested under the events or functional calls that lead to the
execution of the sampled code. For example, a sample placed in Update displays
under `Update.ScriptRunBehaviourUpdate` in the Profiler Hierarchy and Timeline
views. If you supply a `targetObject`, then you can click on the sample in the
Profiler Timeline to select that object in the Editor (when profiling from the
Editor Play mode).  
  
Profiler.BeginSample is conditionally compiled away using
ConditionalAttribute. Thus it will have zero overhead, when it is deployed in
non-Development Build.

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.Profiling;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Example()
        {
            [Profiler.BeginSample](Profiling.Profiler.BeginSample.html)("MyPieceOfCode");
            // Code to measure...
            [Profiler.EndSample](Profiling.Profiler.EndSample.html)();
        }
    }
    

Additional resources: [Profiler.EndSample](Profiling.Profiler.EndSample.html),
[ProfilerCPU](../Manual/ProfilerCPU.html).

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

