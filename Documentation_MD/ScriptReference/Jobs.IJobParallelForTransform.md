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

# IJobParallelForTransform

interface in UnityEngine.Jobs

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

An interface that allows you to perform the same independent operation for
each position, rotation and scale of all the transforms passed into a job.

    
    
    using UnityEngine;
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine.Jobs;  
      
    class ApplyVelocitySample : [MonoBehaviour](MonoBehaviour.html)
    {
        public struct VelocityJob : [IJobParallelForTransform](Jobs.IJobParallelForTransform.html)
        {
            // Jobs declare all data that will be accessed in the job
            // By declaring it as read only, multiple jobs are allowed to access the data in parallel
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public NativeArray<[Vector3](Vector3.html)> velocity;  
      
            // Delta time must be copied to the job since jobs generally don't have a concept of a frame.
            // The main thread waits for the job same frame or next frame, but the job should do work deterministically
            // independent on when the job happens to run on the worker threads.
            public float deltaTime;  
      
            // The code actually running on the job
            public void Execute(int index, [TransformAccess](Jobs.TransformAccess.html) transform)
            {
                // Move the transforms based on delta time and velocity
                var pos = transform.position;
                pos += velocity[index] * deltaTime;
                transform.position = pos;
            }
        }  
      
        // Assign transforms in the inspector to be acted on by the job
        [[SerializeField](SerializeField.html)] public [Transform](Transform.html)[] m_Transforms;
        [TransformAccessArray](Jobs.TransformAccessArray.html) m_AccessArray;  
      
        void Awake()
        {
            // Store the transforms inside a [TransformAccessArray](Jobs.TransformAccessArray.html) instance,
            // so that the transforms can be accessed inside a job.
            m_AccessArray = new [TransformAccessArray](Jobs.TransformAccessArray.html)(m_Transforms);
        }  
      
        void OnDestroy()
        {
            // TransformAccessArrays must be disposed manually.
            m_AccessArray.Dispose();
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            var velocity = new NativeArray<[Vector3](Vector3.html)>(m_Transforms.Length, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            for (var i = 0; i < velocity.Length; ++i)
                velocity[i] = new [Vector3](Vector3.html)(0f, 10f, 0f);  
      
            // Initialize the job data
            var job = new VelocityJob()
            {
                deltaTime = [Time.deltaTime](Time-deltaTime.html),
                velocity = velocity
            };  
      
            // Schedule a parallel-for-transform job.
            // The method takes a [TransformAccessArray](Jobs.TransformAccessArray.html) which contains the Transforms that will be acted on in the job.
            [JobHandle](Unity.Jobs.JobHandle.html) jobHandle = job.Schedule(m_AccessArray);  
      
            // Ensure the job has completed.
            // It is not recommended to Complete a job immediately,
            // since that reduces the chance of having other jobs run in parallel with this one.
            // You optimally want to schedule a job early in a frame and then wait for it later in the frame.
            jobHandle.Complete();  
      
            [Debug.Log](Debug.Log.html)(m_Transforms[0].position);  
      
            // Native arrays must be disposed manually.
            velocity.Dispose();
        }
    }
    

### Public Methods

[Execute](Jobs.IJobParallelForTransform.Execute.html)| Performs work against a
specific iteration index and transform.  
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

