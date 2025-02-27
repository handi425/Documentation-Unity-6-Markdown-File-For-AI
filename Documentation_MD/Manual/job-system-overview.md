[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/job-system-overview.html)
  * [中文](/cn/current/Manual/job-system-overview.html)
  * [日本語](/ja/current/Manual/job-system-overview.html)
  * [한국어](/kr/current/Manual/job-system-overview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/job-system-overview.html)
  * [中文](/cn/current/Manual/job-system-overview.html)
  * [日本語](/ja/current/Manual/job-system-overview.html)
  * [한국어](/kr/current/Manual/job-system-overview.html)

  * [Scripting](scripting.html)
  * [Code optimization](scripting-optimization.html)
  * [Job system](job-system.html)
  * Job system overview

[](job-system.html)

Job system

[](job-system-jobs.html)

Jobs overview

# Job system overview

Unity’s job system lets you create multithreaded code so that your application
can use all available CPU cores to execute your code. This provides improved
performance because your application uses the capacity of all the CPU cores
it’s running on more efficiently, rather than running all code on one CPU
core.

You can use the job system by itself, but for improved performance, you should
also use the [Burst
compiler](https://docs.unity3d.com/Packages/com.unity.burst@latest/), which is
specifically designed to compile jobs for Unity’s job system. The Burst
compiler has improved code generation, which results in increased performance
and a reduction of battery consumption on mobile devices.

You can also use the job system with Unity’s [Entity Component
System](https://docs.unity3d.com/Packages/com.unity.entities@latest/) to
create high performance data-oriented code.

## Multithreading

Unity uses its own native job system to process its own native code over
multiple **worker threads** , which are dependent on the number of CPU cores
available on the device your application runs on. Usually Unity executes your
code on one thread which runs by default at the start of the program, called
the **main thread**. However, when you use the job system, Unity executes your
code over the worker threads, which is called **multithreading.**

Multithreading takes advantage of a CPU’s capability to process a lot of
threads at the same time across multiple cores. Instead of tasks or
instructions executing one after another, they run simultaneously. The worker
threads run in parallel to one another, and synchronize their results with the
main thread once completed.

The job system ensures that there are only enough threads to match the
capacity of the CPU cores, which means that you can schedule as many tasks as
you need without specifically needing to know how many CPU cores are
available. This differs from other job systems that rely on techniques such as
[thread pooling](https://en.wikipedia.org/wiki/Thread_pool), where it’s easier
to inefficiently create more threads than CPU cores.

## Work stealing

The job system uses work stealing as part of its scheduling strategy to even
out the amount of tasks shared across worker threads. Worker threads might
process tasks faster than others, so once a worker thread has finished
processing all of its tasks, it looks at the other worker threads’ queues and
then processes tasks assigned to another worker thread.

## Safety system

To make it easier to write multithreaded code, the job system has a safety
system that detects all potential race conditions and protects you from the
bugs they can cause. A race condition happens when the output of one operation
depends on the timing of another process outside of its control.

For example, if the job system sends a reference to data from your code in the
main thread to a job, it can’t verify whether the main thread is reading the
data at the same time the job is writing to it. This scenario creates a race
condition.

To solve this problem, the job system sends each job a copy of the data it
needs to operate on rather than a reference to the data in the main thread.
This copy isolates the data, which eliminates the race condition.

The way that the job system copies data means that a job can only access
[blittable data types](https://en.wikipedia.org/wiki/Blittable_types). These
types don’t need conversion when passed between managed and native code.

The job system uses
[memcpy](http://www.cplusplus.com/reference/cstring/memcpy/) to copy blittable
types and transfer the data between the managed and native parts of Unity. It
uses memcpy to put data into native memory when scheduling jobs and gives the
managed side access to that copy when executing jobs. For more information,
see [Scheduling jobs](job-system-creating-jobs.html#schedule-a-job).

## Collections package

In addition to the job system provided in the core Unity engine, the
Collections package extends many of the [job types](job-system-jobs.html) and
[native containers](job-system-native-container.html). For more information,
see the [Collections
documentation](https://docs.unity3d.com/Packages/com.unity.collections@latest).

## Additional resources

  * [Jobs overview](job-system-jobs.html)

[](job-system.html)

Job system

[](job-system-jobs.html)

Jobs overview

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

