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

#  [RaycastHit](RaycastHit.html).colliderInstanceID

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

public int colliderInstanceID;

### Description

Instance ID of the [Collider](Collider.html) that was hit.

Provides a reference to the collider that was hit in a way that is accessible
from jobs. For more information on creating jobs see [Create
Jobs](../Manual/JobSystemCreatingJobs.html).

    
    
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine;  
      
    public class BatchExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public struct CollisionJob : [IJob](Unity.Jobs.IJob.html)
        {
            public int colliderID;
            public NativeArray<[RaycastHit](RaycastHit.html)> results;  
      
            public void Execute()
            {
                // This is where we check what we collided with and do any appropriate actions
                // If you tried accessing [RaycastHit.collider](RaycastHit-collider.html) you would get an error
                if (colliderID == results[0].colliderInstanceID)
                    [Debug.Log](Debug.Log.html)("Detected the a hit with the requested collider");
            }
        }
        void Start()
        {
            // We create the raycast command buffer and an array to store the RaycastHits
            NativeArray<[RaycastCommand](RaycastCommand.html)> commands = new NativeArray<[RaycastCommand](RaycastCommand.html)>(1, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));
            NativeArray<[RaycastHit](RaycastHit.html)> results = new NativeArray<[RaycastHit](RaycastHit.html)>(1, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));  
      
            var boxCollider = new [GameObject](GameObject.html)().AddComponent<[BoxCollider](BoxCollider.html)>();  
      
            // Create a new command for the buffer, pointing at the collider we created
            commands[0] = new [RaycastCommand](RaycastCommand.html)([Vector3.up](Vector3-up.html) * 2, [Vector3.down](Vector3-down.html));  
      
            // Schedule the commands in the buffer and store results in the 'results' array
            var batchHandle = [RaycastCommand.ScheduleBatch](RaycastCommand.ScheduleBatch.html)(commands, results, 1, 1);  
      
            // This job is for doing something on the other thread when the collider of interest was hit
            var job = new CollisionJob();
            job.colliderID = boxCollider.GetInstanceID();
            job.results = results;  
      
            //Schedule the job to start after batchHandle has finished
            var jobHandle = job.Schedule(batchHandle);
            jobHandle.Complete();  
      
            commands.Dispose();
            results.Dispose();
        }
    }
    

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

