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

# RaycastCommand

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

Struct used to set up a raycast command to be performed asynchronously during
a job.

When you use this struct to schedule a batch of raycasts, they will be
performed asynchronously and in parallel to each other. The results of the
raycasts are written to the results buffer. Since the results are written
asynchronously the results buffer cannot be accessed until the job has been
completed.  
  
The results for a command at index N in the command buffer are stored at index
N * maxHits in the results buffer.  
  
If maxHits is larger than the actual number of results for the command the
result buffer will contain some invalid results which did not hit anything.
The first invalid result is identified by the collider being null. The second
and later invalid results are not written to by the raycast command so their
colliders are not guaranteed to be null. When iterating over the results the
loop should stop when the first invalid result is found.  
  
Raycast command also controls whether or not Trigger colliders and back-face
triangles generate a hit. If hitMultipleFaces is set to true, Raycast command
returns multiple hits per Mesh. You should adjust maxHits and result array
size accordingly to store all hits. For solid objects (Sphere, Capsule, Box,
Convex), this returns a maximum of one result. Use
[QueryParameters](QueryParameters.html) to control hit flags.  
  
Note: Only BatchQuery.ExecuteRaycastJob is logged into the profiler. Query
count information is not logged.  
  
Additional resources: [Physics.Raycast](Physics.Raycast.html),
[Physics.RaycastAll](Physics.RaycastAll.html).

    
    
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine;  
      
    public class RaycastExample : [MonoBehaviour](MonoBehaviour.html)
    {
        private void Start()
        {
            // Perform a single raycast using [RaycastCommand](RaycastCommand.html) and wait for it to complete
            // Setup the command and result buffers
            var results = new NativeArray<[RaycastHit](RaycastHit.html)>(2, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));  
      
            var commands = new NativeArray<[RaycastCommand](RaycastCommand.html)>(1, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));  
      
            // Set the data of the first command
            [Vector3](Vector3.html) origin = [Vector3.forward](Vector3-forward.html) * -10;  
      
            [Vector3](Vector3.html) direction = [Vector3.forward](Vector3-forward.html);  
      
            commands[0] = new [RaycastCommand](RaycastCommand.html)(origin, direction, [QueryParameters.Default](QueryParameters.Default.html));  
      
            // Schedule the batch of raycasts.
            [JobHandle](Unity.Jobs.JobHandle.html) handle = [RaycastCommand.ScheduleBatch](RaycastCommand.ScheduleBatch.html)(commands, results, 1, 2, default([JobHandle](Unity.Jobs.JobHandle.html)));  
      
            // Wait for the batch processing job to complete
            handle.Complete();  
      
            // Copy the result. If batchedHit.collider is null there was no hit
            foreach (var hit in results)
            {
                if (hit.collider != null)
                {
                    // If hit.collider is not null means there was a hit
                }
            }  
      
            // Dispose the buffers
            results.Dispose();
            commands.Dispose();
        }
    }
    

### Properties

[direction](RaycastCommand-direction.html)| The direction of the ray.  
---|---  
[distance](RaycastCommand-distance.html)| The maximum distance the ray should
check for collisions.  
[from](RaycastCommand-from.html)| The starting point of the ray in world
coordinates.  
[physicsScene](RaycastCommand-physicsScene.html)| The physics scene this
command is run in.  
[queryParameters](RaycastCommand-queryParameters.html)| Structure for
specifying additional parameters for a batch query such as layer mask, hit
multiple mesh faces, hit triggers and hit backfaces.  
  
### Constructors

[RaycastCommand](RaycastCommand-ctor.html)| Create a RaycastCommand.  
---|---  
  
### Static Methods

[ScheduleBatch](RaycastCommand.ScheduleBatch.html)| Schedule a batch of
raycasts to perform in a job.  
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

