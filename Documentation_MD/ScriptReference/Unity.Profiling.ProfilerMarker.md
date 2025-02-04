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

# ProfilerMarker

struct in Unity.Profiling

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

Performance marker used for profiling arbitrary code blocks.

Use _ProfilerMarker_ to mark up script code blocks for the Profiler.  
The information produced by markers is displayed in the [CPU
Profiler](../Manual/ProfilerCPU.html) and can be also captured with
[Recorder](Profiling.Recorder.html). During development (in Editor and
Development Players) this can help to get performance overview of different
parts of game code and identify performance issues.

    
    
    using Unity.Profiling;  
      
    public class MySystemClass
    {
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) s_PreparePerfMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)("MySystem.Prepare");
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) s_SimulatePerfMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)([ProfilerCategory.Ai](Unity.Profiling.ProfilerCategory.Ai.html), "MySystem.Simulate");  
      
        public void UpdateLogic()
        {
            s_PreparePerfMarker.Begin();
            // ...
            s_PreparePerfMarker.End();  
      
            using (s_SimulatePerfMarker.Auto())
            {
                // ...
            }
        }
    }
    

_ProfilerMarker_ represents a named profiler handle and is the most efficient
way of profiling your code. It can be used in jobified code.  
Methods [Begin](Unity.Profiling.ProfilerMarker.Begin.html) and
[End](Unity.Profiling.ProfilerMarker.End.html) are marked with
ConditionalAttribute. They are conditionally compiled away and thus have zero
overhead in non-Development (Release) builds.  
  
When Profiler collects instrumentation data, _ProfilerMarker_ helps to reduce
overhead and the amount of transferred data.
[Profiler.BeginSample](Profiling.Profiler.BeginSample.html) transfers full
string to the data stream while
[ProfilerMarker.Begin](Unity.Profiling.ProfilerMarker.Begin.html) and
[CustomSampler.Begin](Profiling.CustomSampler.Begin.html) only integer
identifier of the marker.  
  
Also [ProfilerMarker.End](Unity.Profiling.ProfilerMarker.End.html) provides a
context information to the [Recorder](Profiling.Recorder.html) making it
possible to track timings of a marked code in Players.  
  
Additional resources: [Recorder](Profiling.Recorder.html).

### Properties

[Handle](Unity.Profiling.ProfilerMarker.Handle.html)| Gets native handle of
the ProfilerMarker.  
---|---  
  
### Constructors

[ProfilerMarker](Unity.Profiling.ProfilerMarker-ctor.html)| Constructs a new
performance marker for code instrumentation.  
---|---  
  
### Public Methods

[Auto](Unity.Profiling.ProfilerMarker.Auto.html)| Creates a helper struct for
the scoped using blocks.  
---|---  
[Begin](Unity.Profiling.ProfilerMarker.Begin.html)| Begin profiling a piece of
code marked with a custom name defined by this instance of ProfilerMarker.  
[End](Unity.Profiling.ProfilerMarker.End.html)| End profiling a piece of code
marked with a custom name defined by this instance of ProfilerMarker.  
  
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

