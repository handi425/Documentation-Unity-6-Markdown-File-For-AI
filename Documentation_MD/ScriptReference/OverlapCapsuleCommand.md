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

# OverlapCapsuleCommand

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

Struct used to set up an overlap capsule command to be performed
asynchronously during a job.

When you use this struct to schedule a batch of overlap capsule commands, the
commands are performed asynchronously. The results of the overlap capsule are
written to the results buffer. Because the results are written asynchronously,
the results buffer can't be accessed until the job is complete.  
  
The results for a command at index N in the command buffer are stored at index
N * maxHits in the results buffer.  
  
If maxHits is larger than the actual number of results for the command the
result buffer will contain some invalid results which did not hit anything.
The first invalid result is identified by the collider instance ID being 0.
The second and later invalid results are not written to the overlap capsule
command so their collider instance IDs are not guaranteed to be 0. When
iterating over the results the loop should stop when the first invalid result
is found.  
  
Overlap capsule command also controls whether or not Trigger colliders
generate a hit. You should adjust maxHits and result array size accordingly to
store all hits. Use QueryParameters to control hit flags.
[QueryParameters.hitBackfaces](QueryParameters-hitBackfaces.html) and
[QueryParameters.hitMultipleFaces](QueryParameters-hitMultipleFaces.html)
flags are not supported and won’t have any impact on overlap results.  
  
Note: Only BatchQuery.ExecuteOverlapCapsuleJob is logged into the profiler.
Query count information is not logged.  
  
Additional resources: [Physics.OverlapCapsule](Physics.OverlapCapsule.html),
[ColliderHit](ColliderHit.html).

    
    
    using Unity.Collections;
    using UnityEngine;  
      
    public class CapsuleOverlap : [MonoBehaviour](MonoBehaviour.html)
    {
        //Print iname of GameObjects inside the capsule
        void BatchOverlapCapsule()
        {
            var commands = new NativeArray<[OverlapCapsuleCommand](OverlapCapsuleCommand.html)>(1, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));
            var results = new NativeArray<[ColliderHit](ColliderHit.html)>(3, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));  
      
            commands[0] = new [OverlapCapsuleCommand](OverlapCapsuleCommand.html)([Vector3.zero](Vector3-zero.html), [Vector3.one](Vector3-one.html), 10f, [QueryParameters.Default](QueryParameters.Default.html));  
      
            [OverlapCapsuleCommand.ScheduleBatch](OverlapCapsuleCommand.ScheduleBatch.html)(commands, results, 1, 3).Complete();  
      
            foreach (var hit in results)
                [Debug.Log](Debug.Log.html)(hit.collider.name);  
      
            commands.Dispose();
            results.Dispose();
        }
    }
    

### Properties

[physicsScene](OverlapCapsuleCommand-physicsScene.html)| The physics scene
this command is run in.  
---|---  
[point0](OverlapCapsuleCommand-point0.html)| The center of the sphere at the
start of the capsule.  
[point1](OverlapCapsuleCommand-point1.html)| The center of the sphere at the
end of the capsule.  
[queryParameters](OverlapCapsuleCommand-queryParameters.html)| Structure for
specifying additional parameters for a batch query such as layer mask or hit
triggers.  
[radius](OverlapCapsuleCommand-radius.html)| The radius of the capsule.  
  
### Constructors

[OverlapCapsuleCommand](OverlapCapsuleCommand-ctor.html)| Create an
OverlapCapsuleCommand.  
---|---  
  
### Static Methods

[ScheduleBatch](OverlapCapsuleCommand.ScheduleBatch.html)| Schedule a batch of
overlap capsule commands to perform in a job.  
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

