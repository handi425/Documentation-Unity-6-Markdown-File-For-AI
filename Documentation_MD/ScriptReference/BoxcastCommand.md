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

# BoxcastCommand

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

Use this struct to set up a box cast command to be performed asynchronously
during a job.

When you use this struct to schedule a batch of box casts, the box casts will
are performed asynchronously and in parallel. The results of each box cast is
written to the results buffer. Since the results are written asynchronously,
you cannot accesss the results buffer until the job is completed.  
  
The results for a command at index N in the command buffer are stored at index
N * maxHits in the results buffer.  
  
Boxcast command also allows you to control whether or not Trigger colliders
and back-face triangles generate a hit. Use
[QueryParameters](QueryParameters.html) to control hit flags.  
  
Note: Only BatchQuery.ExecuteBoxcastJob is logged into the profiler. Query
count information is not logged.  
  
Additional resources: Physics.Boxcast.

    
    
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine;  
      
    public class BoxcastCommandExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Perform a single boxcast using [BoxcastCommand](BoxcastCommand.html) and wait for it to complete
            // Set up the command and result buffers
            var results = new NativeArray<[RaycastHit](RaycastHit.html)>(2, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));
            var commands = new NativeArray<[BoxcastCommand](BoxcastCommand.html)>(1, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));  
      
            // Set the data of the first command
            [Vector3](Vector3.html) center = [Vector3.zero](Vector3-zero.html);
            [Vector2](Vector2.html) halfExtents = [Vector3.one](Vector3-one.html) * 0.5f;
            [Quaternion](Quaternion.html) orientation = [Quaternion.identity](Quaternion-identity.html);
            [Vector3](Vector3.html) direction = [Vector3.forward](Vector3-forward.html);  
      
            commands[0] = new [BoxcastCommand](BoxcastCommand.html)(center, halfExtents, orientation, direction, [QueryParameters.Default](QueryParameters.Default.html));  
      
            // Schedule the batch of boxcasts
            var handle = [BoxcastCommand.ScheduleBatch](BoxcastCommand.ScheduleBatch.html)(commands, results, 1, 2, default([JobHandle](Unity.Jobs.JobHandle.html)));  
      
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

[center](BoxcastCommand-center.html)| The center of the box.  
---|---  
[direction](BoxcastCommand-direction.html)| The direction in which to sweep
the box.  
[distance](BoxcastCommand-distance.html)| The maximum distance of the sweep.  
[halfExtents](BoxcastCommand-halfExtents.html)| The half size of the box in
each dimension.  
[orientation](BoxcastCommand-orientation.html)| The rotation of the box.  
[physicsScene](BoxcastCommand-physicsScene.html)| The physics scene this
command is run in.  
[queryParameters](BoxcastCommand-queryParameters.html)| Structure for
specifying additional parameters for a batch query such as layer mask, hit
triggers and hit backfaces.  
  
### Constructors

[BoxcastCommand](BoxcastCommand-ctor.html)| Creates a BoxcastCommand.  
---|---  
  
### Static Methods

[ScheduleBatch](BoxcastCommand.ScheduleBatch.html)| Schedules a batch of
boxcasts to be performed in a job.  
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

