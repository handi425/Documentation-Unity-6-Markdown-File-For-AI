[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/job-system-parallel-for-jobs.html)
  * [中文](/cn/current/Manual/job-system-parallel-for-jobs.html)
  * [日本語](/ja/current/Manual/job-system-parallel-for-jobs.html)
  * [한국어](/kr/current/Manual/job-system-parallel-for-jobs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/job-system-parallel-for-jobs.html)
  * [中文](/cn/current/Manual/job-system-parallel-for-jobs.html)
  * [日本語](/ja/current/Manual/job-system-parallel-for-jobs.html)
  * [한국어](/kr/current/Manual/job-system-parallel-for-jobs.html)

  * [Scripting](scripting.html)
  * [Code optimization](scripting-optimization.html)
  * [Job system](job-system.html)
  * Parallel jobs

[](job-system-job-dependencies.html)

Job dependencies

[](debugging-and-diagnostics.html)

Debugging and diagnostics

# Parallel jobs

When you [schedule a job](job-system-creating-jobs.html#schedule-a-job) there
can only be one job doing one task. However, there will be times where you
need to perform the same operation on a lot of objects. To do this, use a
ParallelFor job type, which inherits from
[`IJobParallelFor`](../ScriptReference/Unity.Jobs.IJobParallelFor.html).

A ParallelFor job uses a
[`NativeArray`](../ScriptReference/Unity.Collections.NativeArray_1.html) of
data to act on as its data source. ParallelFor jobs run across multiple CPU
cores. There’s one job per core, with each handling a subset of the workload.

`IJobParallelFor` behaves like [`IJob`](job-system-jobs.html), but instead of
a single [`Execute`](../ScriptReference/Unity.Jobs.IJob.Execute.html) method,
it invokes the `Execute` method once per item in the data source. There’s also
an integer parameter index in the `Execute` method, which you can use to
access and operate on a single element of the data source within the job
implementation.

The following is an example of a ParallelFor job definition:

    
    
    struct IncrementByDeltaTimeJob: IJobParallelFor
    {
        public NativeArray<float> values;
        public float deltaTime;
    
        public void Execute (int index)
        {
            float temp = values[index];
            temp += deltaTime;
            values[index] = temp;
        }
    }
    

## Schedule a ParallelFor job

To schedule a `ParallelFor` job, you must specify the length of the
`NativeArray` data source that you want to split. The job system doesn’t know
which `NativeArray` you want to use as the data source if there are several in
the struct. The length also tells the job system how many `Execute` methods to
expect.

In Unity’s native code, the scheduling of `ParallelFor` jobs is more
complicated. When Unity schedules a `ParallelFor` job, the job system divides
the work into batches to distribute between cores. Each batch contains a
subset of `Execute` methods. The job system then schedules one job in Unity’s
native job system per CPU core and passes that native job to the batches to
complete.

![A ParallelFor job dividing batches across
cores](../uploads/Main/jobsystem_parallelfor_job_batches.svg) A ParallelFor
job dividing batches across cores

When a native job completes its batches before others, it [steals](job-system-
overview.html#work-stealing) remaining batches from the other native jobs. It
only steals half of a native job’s remaining batches at a time, to ensure
[cache locality](https://en.wikipedia.org/wiki/Locality_of_reference).

To optimize the process, you need to specify a batch count. The batch count
controls how many jobs you get, and how fine-grained the redistribution of
work between threads is. Having a low batch count, such as 1, gives you an
even distribution of work between threads. However, it comes with some
overhead, so sometimes it’s better to increase the batch count. Starting at 1
and increasing the batch count until there are negligible performance gains is
a good strategy.

The following is an example of scheduling a ParallelFor job

Job code:

    
    
    // Job adding two floating point values together
    public struct MyParallelJob : IJobParallelFor
    {
        [ReadOnly]
        public NativeArray<float> a;
        [ReadOnly]
        public NativeArray<float> b;
        public NativeArray<float> result;
    
        public void Execute(int i)
        {
            result[i] = a[i] + b[i];
        }
    }
    

Main thread code:

    
    
    NativeArray<float> a = new NativeArray<float>(2, Allocator.TempJob);
    
    NativeArray<float> b = new NativeArray<float>(2, Allocator.TempJob);
    
    NativeArray<float> result = new NativeArray<float>(2, Allocator.TempJob);
    
    a[0] = 1.1;
    b[0] = 2.2;
    a[1] = 3.3;
    b[1] = 4.4;
    
    MyParallelJob jobData = new MyParallelJob();
    jobData.a = a;
    jobData.b = b;
    jobData.result = result;
    
    // Schedule the job with one Execute per index in the results array and only 1 item per processing batch
    JobHandle handle = jobData.Schedule(result.Length, 1);
    
    // Wait for the job to complete
    handle.Complete();
    
    // Free the memory allocated by the arrays
    a.Dispose();
    b.Dispose();
    result.Dispose();
    

## ParallelForTransform jobs

A `ParallelForTransform` job is another type of `ParallelFor` job designed
specifically for operating on [Transforms](class-Transform.html). It’s useful
for working on Transform operations from jobs efficiently.

## Additional resources

  * [ParallelForTransform API reference](../ScriptReference/Jobs.IJobParallelForTransform.html).
  * [Create and run a job](job-system-creating-jobs.html)

[](job-system-job-dependencies.html)

Job dependencies

[](debugging-and-diagnostics.html)

Debugging and diagnostics

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

