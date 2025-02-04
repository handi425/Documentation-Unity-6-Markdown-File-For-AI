[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/job-system-jobs.html)
  * [中文](/cn/current/Manual/job-system-jobs.html)
  * [日本語](/ja/current/Manual/job-system-jobs.html)
  * [한국어](/kr/current/Manual/job-system-jobs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/job-system-jobs.html)
  * [中文](/cn/current/Manual/job-system-jobs.html)
  * [日本語](/ja/current/Manual/job-system-jobs.html)
  * [한국어](/kr/current/Manual/job-system-jobs.html)

  * [Scripting](scripting.html)
  * [Code optimization](scripting-optimization.html)
  * [Job system](job-system.html)
  * Jobs overview

[](job-system-overview.html)

Job system overview

[](job-system-native-container.html)

Thread safe types

# Jobs overview

A job is a small unit of work that does one specific task. A job receives
parameters and operates on data, similar to how a method call behaves. Jobs
can be self-contained, or they can depend on other jobs to complete before
they can run. In Unity, a job refers to any struct that implements [the `IJob`
interface.](../ScriptReference/Unity.Jobs.IJob.html)

Only the main thread can schedule and complete jobs. It can’t access the
content of any running jobs, and two jobs can’t access the contents of a job
at the same time. To ensure efficient running of jobs, you can make them
dependent on each other. Unity’s job system allows you to create complex
dependency chains to ensure that your jobs complete in the correct order.

## Job types

  * [IJob](../ScriptReference/Unity.Jobs.IJob.html): Runs a single task on a job thread.
  * [IJobParallelFor](../ScriptReference/Unity.Jobs.IJobParallelFor.html): Runs a task in parallel. Each worker thread that runs in parallel has an exclusive index to access shared data between worker threads safely.
  * [IJobParallelForTransform](../ScriptReference/Jobs.IJobParallelForTransform.html): Runs a task in parallel. Each worker thread running in parallel has an exclusive Transform from the transform hierarchy to operate on.
  * [IJobFor](../ScriptReference/Unity.Jobs.IJobFor.html): The same as `IJobParallelFor`, but allows you to schedule the job so that it doesn’t run in parallel.

## Additional resources

  * [Create a job](job-system-creating-jobs.html)
  * [Job dependencies](job-system-job-dependencies.html)
  * [Parallel jobs](job-system-parallel-for-jobs.html)

[](job-system-overview.html)

Job system overview

[](job-system-native-container.html)

Thread safe types

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

