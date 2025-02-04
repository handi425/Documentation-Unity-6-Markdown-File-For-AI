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

# ClosestPointCommand

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

Struct used to set up a closest point command to be performed asynchronously
during a job.  
  
When you use this struct to schedule a batch of closest commands, they are
performed asynchronously and in parallel to each other. The results of the
closest points are written to the results buffer. Because the results are
written asynchronously, the results buffer cannot be accessed until the job
has been completed.  
  
The result for a command at index N in the command buffer is stored at index N
in the results buffer.

Additional resources: [Physics.ClosestPoint](Physics.ClosestPoint.html).

    
    
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine;  
      
    public class ClosestPoint : [MonoBehaviour](MonoBehaviour.html)
    {
        private void Start()
        {
            var collider = new [GameObject](GameObject.html)().AddComponent<[BoxCollider](BoxCollider.html)>();
            // Perform a single closest point using [ClosestPointCommand](ClosestPointCommand.html) and wait for it to complete
            // Set up the command and result buffers
            var results = new NativeArray<[Vector3](Vector3.html)>(1, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));  
      
            var commands = new NativeArray<[ClosestPointCommand](ClosestPointCommand.html)>(1, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));  
      
            commands[0] = new [ClosestPointCommand](ClosestPointCommand.html)([Vector3.one](Vector3-one.html) * 5, collider.GetInstanceID(), [Vector3.zero](Vector3-zero.html), [Quaternion.identity](Quaternion-identity.html), collider.transform.lossyScale);  
      
            // Schedule the batch of closest points
            [JobHandle](Unity.Jobs.JobHandle.html) handle = [ClosestPointCommand.ScheduleBatch](ClosestPointCommand.ScheduleBatch.html)(commands, results, 1, default([JobHandle](Unity.Jobs.JobHandle.html)));  
      
            // Wait for the batch processing job to complete
            handle.Complete();  
      
            // Copy the result. If the point is inside of the [Collider](Collider.html), it is returned as a result
            [Vector3](Vector3.html) closestPoint = results[0];  
      
            // Dispose of the buffers
            results.Dispose();
            commands.Dispose();
        }
    }
    

### Properties

[colliderInstanceID](ClosestPointCommand-colliderInstanceID.html)| The ID of
the Collider that you find the closest point on.  
---|---  
[point](ClosestPointCommand-point.html)| Location you want to find the closest
point to.  
[position](ClosestPointCommand-position.html)| The position of the Collider.  
[rotation](ClosestPointCommand-rotation.html)| The rotation of the Collider.  
[scale](ClosestPointCommand-scale.html)| The global scale of the Collider.  
  
### Constructors

[ClosestPointCommand](ClosestPointCommand-ctor.html)| Create a
ClosestPointCommand using Instance ID of the Collider.  
---|---  
  
### Static Methods

[ScheduleBatch](ClosestPointCommand.ScheduleBatch.html)| Schedule a batch of
closest points which are performed in a job.  
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

