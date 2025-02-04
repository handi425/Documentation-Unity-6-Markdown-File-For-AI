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

#  [ProfilerFlowEventType](Unity.Profiling.ProfilerFlowEventType.html).Begin

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

Use for the flow start point.

The _Begin_ flow event type marks up the profiler sample as a flow start
point. The new flow identifier is generated for the _Begin_ event. Use it to
track all profiler samples which belong to the same flow.
[Next](Unity.Profiling.ProfilerFlowEventType.Next.html) denotes the next point
of the flow and [End](Unity.Profiling.ProfilerFlowEventType.End.html) denotes
the flow termination. Flow identifier starts from 1 and is incremented by 1
for each new _Begin_.  
  
An example of a flow start point is job scheduling. For instance,
[IJobExtensions.Schedule](Unity.Jobs.IJobExtensions.Schedule.html) generates
an implicit [Begin](Unity.Profiling.ProfilerFlowEventType.Begin.html) Profiler
flow event and [IJob.Execute](Unity.Jobs.IJob.Execute.html) generates an
implicit [Next](Unity.Profiling.ProfilerFlowEventType.Next.html) event.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Threading;
    using Unity.Profiling;
    using Unity.Profiling.LowLevel;
    using Unity.Profiling.LowLevel.Unsafe;  
      
    public class Example
    {
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_ScheduleTasksMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)("Schedule [Task](VersionControl.Task.html)");
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_TaskMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)("[Task](VersionControl.Task.html)");  
      
        static void EmitFlowEventAndChainThread(uint flowId)
        {
            // Mark the next k_TaskMarker as a beginning of the flow
            [ProfilerUnsafeUtility.FlowEvent](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html)(flowId, [ProfilerFlowEventType.Next](Unity.Profiling.ProfilerFlowEventType.Next.html));
            using (k_TaskMarker.Auto())
            {
                // Do work
            }
        }  
      
        static void ScheduleTask()
        {
            using (k_ScheduleTasksMarker.Auto())
            {
                var flowId = [ProfilerUnsafeUtility.CreateFlow](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateFlow.html)([ProfilerUnsafeUtility.CategoryScripts](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html));
                // Mark the parent k_ScheduleTasksMarker as a beginning of the flow
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

