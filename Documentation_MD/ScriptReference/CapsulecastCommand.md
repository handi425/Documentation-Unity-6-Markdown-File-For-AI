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

# CapsulecastCommand

struct in UnityEngine

/

Implemented in:[UnityEngine.PhysicsModule](UnityEngine.PhysicsModule.html)

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

Use this struct to set up a capsule cast command that is performed
asynchronously during a job.

When you use this struct to schedule a batch of capsule casts, the capsule
casts are performed asynchronously and in parallel. The results of each
capsule cast is written to the results buffer. Since the results are written
asynchronously, you cannot access the results buffer until the job is
completed.  
  
The results for a command at index N in the command buffer are stored at index
N * maxHits in the results buffer.  
  
Capsulecast command also allows you to control whether or not Trigger
colliders and back-face triangles generate a hit. Use
[QueryParameters](QueryParameters.html) to control hit flags.  
  
Note: Only BatchQuery.ExecuteCapsulecastJob is logged into the profiler. Query
count information is not logged.  
  
Additional resources: Physics.Capsulecast.

    
    
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine;  
      
    public class CapsulecastExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Perform a single capsule cast using [CapsulecastCommand](CapsulecastCommand.html) and wait for it to complete
            // Set up the command and result buffers
            var results = new NativeArray<[RaycastHit](RaycastHit.html)>(2, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));
            var commands = new NativeArray<[CapsulecastCommand](CapsulecastCommand.html)>(1, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));  
      
            // Set the data of the first command
            [Vector3](Vector3.html) point1 = [Vector3.up](Vector3-up.html) * -0.5f;
            [Vector3](Vector3.html) point2 = [Vector3.up](Vector3-up.html) * 0.5f;
            [Vector3](Vector3.html) direction = [Vector3.forward](Vector3-forward.html);
            float radius = 0.5f;  
      
            commands[0] = new [CapsulecastCommand](CapsulecastCommand.html)(point1, point2, radius, direction, [QueryParameters.Default](QueryParameters.Default.html));  
      
            // Schedule the batch of capsulecasts
            var handle = [CapsulecastCommand.ScheduleBatch](CapsulecastCommand.ScheduleBatch.html)(commands, results, 1, 2, default([JobHandle](Unity.Jobs.JobHandle.html)));  
      
            // Wait for the batch processing job to complete
            handle.Complete();  
      
            // If batchedHit.collider is not null there was a hit
            foreach (var hit in results)
            {
                if (hit.collider != null)
                {
                    // Do something with results
                }
            }  
      
            // Dispose the buffers
            results.Dispose();
            commands.Dispose();
        }
    }
    

### Properties

[direction](CapsulecastCommand-direction.html)| The direction of the capsule
cast.  
---|---  
[distance](CapsulecastCommand-distance.html)| The maximum distance the capsule
cast checks for collision.  
[physicsScene](CapsulecastCommand-physicsScene.html)| The physics scene this
command is run in.  
[point1](CapsulecastCommand-point1.html)| The center of the sphere at the
start of the capsule.  
[point2](CapsulecastCommand-point2.html)| The center of the sphere at the end
of the capsule.  
[queryParameters](CapsulecastCommand-queryParameters.html)| Structure for
specifying additional parameters for a batch query such as layer mask, hit
triggers and hit backfaces.  
[radius](CapsulecastCommand-radius.html)| The radius of the capsule.  
  
### Constructors

[CapsulecastCommand](CapsulecastCommand-ctor.html)| Creates a
CapsulecastCommand.  
---|---  
  
### Static Methods

[ScheduleBatch](CapsulecastCommand.ScheduleBatch.html)| Schedules a batch of
capsule casts to perform in a job.  
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

