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

#
[ProfilerFlowEventType](Unity.Profiling.ProfilerFlowEventType.html).ParallelNext

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

Use for the parallel flow continuation point.

All parallel flow instances are equivalent and connected to the same
[Begin](Unity.Profiling.ProfilerFlowEventType.Begin.html) or
[Next](Unity.Profiling.ProfilerFlowEventType.Next.html) events that happened
previously. An example of a flow start point is job scheduling. For instance,
[IJobParallelForExtensions.Schedule](Unity.Jobs.IJobParallelForExtensions.Schedule.html)
generates an implicit
[Begin](Unity.Profiling.ProfilerFlowEventType.Begin.html) Profiler flow event
and [IJobParallelFor.Execute](Unity.Jobs.IJobParallelFor.Execute.html)
generates an implicit
[ParallelNext](Unity.Profiling.ProfilerFlowEventType.ParallelNext.html) event.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Threading;
    using Unity.Profiling;
    using Unity.Profiling.LowLevel;
    using Unity.Profiling.LowLevel.Unsafe;  
      
    public class Example
    {
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_ScheduleParallelTasksMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)("Schedule Parallel Tasks");
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_ParallelTaskMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)("Parallel [Task](VersionControl.Task.html)");  
      
        static void EmitFlowEventAndChainThread(uint flowId)
        {
            // Mark the next k_ParallelTaskMarker as a beginning of the flow
            [ProfilerUnsafeUtility.FlowEvent](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html)(flowId, [ProfilerFlowEventType.ParallelNext](Unity.Profiling.ProfilerFlowEventType.ParallelNext.html));
            using (k_ParallelTaskMarker.Auto())
            {
                // Do work
            }
        }  
      
        static void ScheduleParallelTask()
        {
            using (k_ScheduleParallelTasksMarker.Auto())
            {
                var flowId = [ProfilerUnsafeUtility.CreateFlow](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateFlow.html)([ProfilerUnsafeUtility.CategoryScripts](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html));
                // Mark the parent k_ScheduleParallelTasksMarker as a beginning of the flow
                [ProfilerUnsafeUtility.FlowEvent](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html)(flowId, [ProfilerFlowEventType.Begin](Unity.Profiling.ProfilerFlowEventType.Begin.html));
                var thread = new Thread(() => EmitFlowEventAndChainThread(flowId));
                thread.Start();
            }
        }
    }
    

Additional resources:
[ProfilerUnsafeUtility.FlowEvent](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html).

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

