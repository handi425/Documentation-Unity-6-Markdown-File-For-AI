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

# IJobFor

interface in Unity.Jobs

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

An interface that represents a job that performs the same independent
operation for each element of a native container or for a fixed number of
iterations.

This job type has the following options to schedule work:

  * [IJobForExtensions.Run](Unity.Jobs.IJobForExtensions.Run.html) runs the job on the main thread and finishes immediately.
  * [IJobForExtensions.Schedule](Unity.Jobs.IJobForExtensions.Schedule.html) schedules the job to run on a worker thread or the main thread, but indicates that the work should happen in a single thread. This option allows for work to be done off the main thread, but the work is performed sequentially.
  * [IJobForExtensions.ScheduleParallel](Unity.Jobs.IJobForExtensions.ScheduleParallel.html) schedules the job to run on multiple worker threads concurrently. This scheduling option can give the best performance, but conflicts might happen when accessing the same data from multiple worker threads simultaneously.
  * `Execute(int index)` is executed once for each index from 0 to the provided length.

`Run` and `Schedule` guarantees that the the job's `Execute(int index)` method
is invoked sequentially. `ScheduleParallel` doesn't invoke the job's `Execute`
method sequentially because it's called from multiple worker threads in
parallel to each other.  
  
Each iteration must be independent from other iterations and the safety system
enforces this rule for you. The indices have no guaranteed order and are
executed on multiple cores in parallel.  
  
Unity automatically splits the work into chunks of no less than the provided
`batchSize`, and schedules an appropriate number of jobs based on the number
of worker threads, the length of the array and the batch size. You should
choose the batch size based on the amount of work performed in the job. A
simple job, for example adding a couple of Vector3 to each other should have a
batch size of 32 to 128. However, if the work performed is very expensive then
it's best practice to use a small batch size, for example, a batch size of 1.
IJobFor performs work stealing using atomic operations. Batch sizes can be
small but they are not for free.  
  
You can use the returned `JobHandle` to check that the job has completed, or
pass it to other jobs as a dependency. When you pass a `JobHandle` as a
dependency, it ensures that the jobs are executed one after another on the
worker threads.  
  
Additional resources: [IJobForExtensions](Unity.Jobs.IJobForExtensions.html)

    
    
    using UnityEngine;
    using Unity.Collections;
    using Unity.Jobs;  
      
    class ApplyVelocityParallelForSample : [MonoBehaviour](MonoBehaviour.html)
    {
        struct VelocityJob : [IJobFor](Unity.Jobs.IJobFor.html)
        {
            // Jobs declare all data that will be accessed in the job
            // By declaring it as read only, multiple jobs are allowed to access the data in parallel
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public NativeArray<[Vector3](Vector3.html)> velocity;  
      
            // By default containers are assumed to be read & write
            public NativeArray<[Vector3](Vector3.html)> position;  
      
            // Delta time must be copied to the job since jobs generally don't have concept of a frame.
            // The main thread waits for the job same frame or next frame, but the job should do work deterministically
            // independent on when the job happens to run on the worker threads.
            public float deltaTime;  
      
            // The code actually running on the job
            public void Execute(int i)
            {
                // Move the positions based on delta time and velocity
                position[i] = position[i] + velocity[i] * deltaTime;
            }
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            var position = new NativeArray<[Vector3](Vector3.html)>(500, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            var velocity = new NativeArray<[Vector3](Vector3.html)>(500, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            for (var i = 0; i < velocity.Length; i++)
                velocity[i] = new [Vector3](Vector3.html)(0, 10, 0);  
      
            // Initialize the job data
            var job = new VelocityJob()
            {
                deltaTime = [Time.deltaTime](Time-deltaTime.html),
                position = position,
                velocity = velocity
            };  
      
            // Schedule job to run immediately on main thread. First parameter is how many for-each iterations to perform.
            job.Run(position.Length);  
      
            // Schedule job to run at a later point on a single worker thread.
            // First parameter is how many for-each iterations to perform.
            // The second parameter is a [JobHandle](Unity.Jobs.JobHandle.html) to use for this job's dependencies.
            //   [Dependencies](Unity.Android.Gradle.Dependencies.html) are used to ensure that a job executes on worker threads after the dependency has completed execution.
            //   In this case we don't need our job to depend on anything so we can use a default one.
            [JobHandle](Unity.Jobs.JobHandle.html) scheduleJobDependency = new [JobHandle](Unity.Jobs.JobHandle.html)();
            [JobHandle](Unity.Jobs.JobHandle.html) scheduleJobHandle = job.Schedule(position.Length, scheduleJobDependency);  
      
            // Schedule job to run on parallel worker threads.
            // First parameter is how many for-each iterations to perform.
            // The second parameter is the batch size,
            //   essentially the no-overhead innerloop that just invokes Execute(i) in a loop.
            //   When there is a lot of work in each iteration then a value of 1 can be sensible.
            //   When there is very little work values of 32 or 64 can make sense.
            // The third parameter is a [JobHandle](Unity.Jobs.JobHandle.html) to use for this job's dependencies.
            //   [Dependencies](Unity.Android.Gradle.Dependencies.html) are used to ensure that a job executes on worker threads after the dependency has completed execution.
            [JobHandle](Unity.Jobs.JobHandle.html) scheduleParallelJobHandle = job.ScheduleParallel(position.Length, 64, scheduleJobHandle);  
      
            // Ensure the job has completed.
            // It is not recommended to Complete a job immediately,
            // since that reduces the chance of having other jobs run in parallel with this one.
            // You optimally want to schedule a job early in a frame and then wait for it later in the frame.
            scheduleParallelJobHandle.Complete();  
      
            [Debug.Log](Debug.Log.html)(job.position[0]);  
      
            // Native arrays must be disposed manually.
            position.Dispose();
            velocity.Dispose();
        }
    }
    

### Public Methods

[Execute](Unity.Jobs.IJobFor.Execute.html)| Performs work against a specific
iteration index.  
---|---  
  
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

