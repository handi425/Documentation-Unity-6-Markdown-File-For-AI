[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/job-system-job-dependencies.html)
  * [中文](/cn/current/Manual/job-system-job-dependencies.html)
  * [日本語](/ja/current/Manual/job-system-job-dependencies.html)
  * [한국어](/kr/current/Manual/job-system-job-dependencies.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/job-system-job-dependencies.html)
  * [中文](/cn/current/Manual/job-system-job-dependencies.html)
  * [日本語](/ja/current/Manual/job-system-job-dependencies.html)
  * [한국어](/kr/current/Manual/job-system-job-dependencies.html)

  * [Scripting](scripting.html)
  * [Code optimization](scripting-optimization.html)
  * [Job system](job-system.html)
  * Job dependencies

[](job-system-creating-jobs.html)

Create and run a job

[](job-system-parallel-for-jobs.html)

Parallel jobs

# Job dependencies

Often, one job depends on the results of another job. For example, Job A might
write to a `NativeArray` that job B uses as input. You must tell the job
system about such a dependency when you schedule a dependent job. The job
system won’t run the dependent job until the job it depends upon is finished.
One job can depend on more than one job.

You can also have a chain of jobs in which each job depends on the previous
one. However, dependencies delay job execution because you must wait for any
dependencies of a job to complete before it can run. Completing a dependent
job must first complete any job it depends on, and any jobs those jobs depend
on.

When you call the
[`Schedule`](../ScriptReference/Unity.Jobs.IJobExtensions.Schedule.html)
method of a job it returns a
[`JobHandle`](../ScriptReference/Unity.Jobs.JobHandle.html). You can use a
`JobHandle` as a dependency for other jobs. If a job depends on the results of
another job, you can pass the first job’s `JobHandle` as a parameter to the
second job’s `Schedule` method, like so:

    
    
    JobHandle firstJobHandle = firstJob.Schedule();
    secondJob.Schedule(firstJobHandle);
    

## Combining dependencies

If a job has a lot of dependencies, you can use the method
[`JobHandle.CombineDependencies`](../ScriptReference/Unity.Jobs.JobHandle.CombineDependencies.html)
to merge them. `CombineDependencies` allows you to pass dependencies onto the
`Schedule` method.

    
    
    NativeArray<JobHandle> handles = new NativeArray<JobHandle>(numJobs, Allocator.TempJob);
    
    // Populate `handles` with `JobHandles` from multiple scheduled jobs...
    
    JobHandle jh = JobHandle.CombineDependencies(handles);
    

## An example of multiple jobs and dependencies

The following is an example of multiple jobs that have multiple dependencies.
It’s best practice to put the job code (`MyJob` and `AddOneJob`) in a separate
file to the `Update` and `LateUpdate` code, but for the purposes of clarity,
this example is one file:

    
    
    using UnityEngine;
    using Unity.Collections;
    using Unity.Jobs;
    
    public class MyDependentJob : MonoBehaviour
    {
        // Create a native array of a single float to store the result. This example waits for the job to complete.
        NativeArray<float> result;
        // Create a JobHandle to access the results
        JobHandle secondHandle;
    
        // Set up the first job
        public struct MyJob : IJob
        {
            public float a;
            public float b;
            public NativeArray<float> result;
    
            public void Execute()
            {
                result[0] = a + b;
            }
        }
    
        // Set up the second job, which adds one to a value
        public struct AddOneJob : IJob
        {
            public NativeArray<float> result;
    
            public void Execute()
            {
                result[0] = result[0] + 1;
            }
        }
    
        // Update is called once per frame
        void Update()
        {
            // Set up the job data for the first job
            result = new NativeArray<float>(1, Allocator.TempJob);
    
            MyJob jobData = new MyJob
            {
                a = 10,
                b = 10,
                result = result
            };
    
            // Schedule the first job
            JobHandle firstHandle = jobData.Schedule();
    
            // Setup the data for the second job
            AddOneJob incJobData = new AddOneJob
            {
                result = result
            };
    
            // Schedule the second job
            secondHandle = incJobData.Schedule(firstHandle);
        }
    
        private void LateUpdate()
        {
            // Sometime later in the frame, wait for the job to complete before accessing the results.
            secondHandle.Complete();
    
            // All copies of the NativeArray point to the same memory, you can access the result in "your" copy of the NativeArray
            // float aPlusBPlusOne = result[0];
    
            // Free the memory allocated by the result array
            result.Dispose();
        }
    
    }
    
    

## Additional resources

  * [Parallel jobs](job-system-parallel-for-jobs.html)

[](job-system-creating-jobs.html)

Create and run a job

[](job-system-parallel-for-jobs.html)

Parallel jobs

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

