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

# FrameTiming

struct in UnityEngine

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

Struct containing basic FrameTimings and accompanying relevant data.

### Properties

[cpuFrameTime](FrameTiming-cpuFrameTime.html)| This is the total CPU frame
time calculated as the time between ends of two frames, which includes all
waiting time and overheads, in ms.  
---|---  
[cpuMainThreadFrameTime](FrameTiming-cpuMainThreadFrameTime.html)| Total time
between start of the frame and when the main thread finished the job, in ms.  
[cpuMainThreadPresentWaitTime](FrameTiming-cpuMainThreadPresentWaitTime.html)|
The CPU time the last frame spent in waiting for Present on the main thread,
in ms.  
[cpuRenderThreadFrameTime](FrameTiming-cpuRenderThreadFrameTime.html)| The
frame time between start of the work on the render thread and when Present was
called, in ms.  
[cpuTimeFrameComplete](FrameTiming-cpuTimeFrameComplete.html)| This is the CPU
clock time at the point GPU finished rendering the frame and interrupted the
CPU.  
[cpuTimePresentCalled](FrameTiming-cpuTimePresentCalled.html)| This is the CPU
clock time at the point Present was called for the current frame.  
[firstSubmitTimestamp](FrameTiming-firstSubmitTimestamp.html)| This is the CPU
clock time of the time when the first job was submitted to GPU.  
[frameStartTimestamp](FrameTiming-frameStartTimestamp.html)| This is the CPU
clock time of the time when the frame was started.  
[gpuFrameTime](FrameTiming-gpuFrameTime.html)| The GPU time for a given frame,
in ms.  
[heightScale](FrameTiming-heightScale.html)| This was the height scale factor
of the Dynamic Resolution system(if used) for the given frame and the linked
frame timings.  
[syncInterval](FrameTiming-syncInterval.html)| This was the vsync mode for the
given frame and the linked frame timings.  
[widthScale](FrameTiming-widthScale.html)| This was the width scale factor of
the Dynamic Resolution system(if used) for the given frame and the linked
frame timings.  
  
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

