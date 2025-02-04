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
[ProfilerUnsafeUtility](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html).FlowEvent

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

public static void FlowEvent(uint flowId,
[Unity.Profiling.ProfilerFlowEventType](Unity.Profiling.ProfilerFlowEventType.html)
flowEventType);

### Parameters

flowId | Profiler flow identifier.  
---|---  
flowEventType | Flow event type.  
  
### Description

Add flow event to a Profiler sample.

Use Profiler flow events to highlight the dependencies between task execution
on different threads.  
  
Flow event works in conjunction with
[ProfilerMarker](Unity.Profiling.ProfilerMarker.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Threading;
    using Unity.Profiling;
    using Unity.Profiling.LowLevel;
    using Unity.Profiling.LowLevel.Unsafe;  
      
    public class Example
    {
        public const int k_NumberOfTasks = 4;  
      
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_ScheduleParallelTasksMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)("Schedule Parallel Tasks");
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_ParallelTaskMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)("Parallel [Task](VersionControl.Task.html)");
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_TaskSyncMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)("Sync [Task](VersionControl.Task.html)");  
      
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
            uint flowId;
            var threads = new Thread[k_NumberOfTasks];
            using (k_ScheduleParallelTasksMarker.Auto())
            {
                flowId = [ProfilerUnsafeUtility.CreateFlow](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateFlow.html)([ProfilerUnsafeUtility.CategoryScripts](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html));
                // Mark the parent k_ScheduleParallelTasksMarker as a beginning of the flow
                [ProfilerUnsafeUtility.FlowEvent](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html)(flowId, [ProfilerFlowEventType.Begin](Unity.Profiling.ProfilerFlowEventType.Begin.html));
                for (var i = 0; i < k_NumberOfTasks; ++i)
                {
                    var thread = new Thread(() => EmitFlowEventAndChainThread(flowId));
                    thread.Start();
                    threads[i] = thread;
                }
            }  
      
            using (k_TaskSyncMarker.Auto())
            {
                // Mark the parent k_TaskSyncMarker as a beginning of the flow
                [ProfilerUnsafeUtility.FlowEvent](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html)(flowId, [ProfilerFlowEventType.End](Unity.Profiling.ProfilerFlowEventType.End.html));
                for (var i = 0; i < k_NumberOfTasks; ++i)
                    threads[i].Join();
            }
        }
    }
    

You must use `FlowEvent` together with a
[ProfilerMarker](Unity.Profiling.ProfilerMarker.html).  
  
To mark the sample as a beginning or end of a flow, use `FlowEvent` with
[ProfilerFlowEventType.Begin](Unity.Profiling.ProfilerFlowEventType.Begin.html)
and
[ProfilerFlowEventType.End](Unity.Profiling.ProfilerFlowEventType.End.html)
events within a scope that is instrumented with
[ProfilerMarker.Begin](Unity.Profiling.ProfilerMarker.Begin.html) and
[ProfilerMarker.End](Unity.Profiling.ProfilerMarker.End.html), or within the
`using` scope of
[ProfilerMarker.Auto](Unity.Profiling.ProfilerMarker.Auto.html).  
  
  
To mark the sample as a flow continuation point, use `FlowEvent` with
[ProfilerFlowEventType.Next](Unity.Profiling.ProfilerFlowEventType.Next.html)
and
[ProfilerFlowEventType.ParallelNext](Unity.Profiling.ProfilerFlowEventType.ParallelNext.html)
before a call to
[ProfilerMarker.Begin](Unity.Profiling.ProfilerMarker.Begin.html) or
[ProfilerMarker.Auto](Unity.Profiling.ProfilerMarker.Auto.html).  
  
**Note:** Unity Job System automatically marks up job scheduling, execution
and wait points.  
  
Additional resources:
[CreateFlow](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateFlow.html),
[CPU Usage Profiler module](../Manual/ProfilerCPU.html).

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

