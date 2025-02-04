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

**Experimental** : this API is experimental and might be changed or removed in
the future.

#
[GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html).WarmUp

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

## Declaration

public [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
WarmUp([Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) dependency);

### Parameters

dependency | Job to wait for.  
---|---  
  
### Returns

**JobHandle** Handle to prewarming job.

### Description

Prewarms all shader variants in this collection using associated graphics
states.

This will result in the GPU representation of the stored shader variants being
created.  
  
The JobHandle returned by this method can be used to control if the creation
of GPU representations occurs synchronously or asynchronously.  
  
The example below will perform the warm up asynchronously.

    
    
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;
    using Unity.Jobs;  
      
    public class WarmUpExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html) graphicsStateCollection;  
      
        void Start()
        {
            [JobHandle](Unity.Jobs.JobHandle.html) handle = graphicsStateCollection.WarmUp();
        }
    }

Below is an example of how to wait on the completion of the job handle in
order to perform operations synchronously.

    
    
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;
    using Unity.Jobs;  
      
    public class WarmUpSynchronousExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html) graphicsStateCollection;  
      
        void Start()
        {
            [JobHandle](Unity.Jobs.JobHandle.html) handle = graphicsStateCollection.WarmUp();
            handle.Complete();
        }
    }

Prewarming can also be linked to other jobs using the input dependency and
returned JobHandle.

    
    
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;
    using Unity.Jobs;  
      
    public class WarmUpSynchronousExample : [MonoBehaviour](MonoBehaviour.html)
    {
        struct PostWarmUpJob : [IJob](Unity.Jobs.IJob.html)
        {
            public void Execute()
            {
                [Debug.Log](Debug.Log.html)("WarmUp is complete");
            }
        }  
      
        public [GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html) graphicsStateCollection;
        public [JobHandle](Unity.Jobs.JobHandle.html) inputJobHandle;  
      
        void Start()
        {
            [JobHandle](Unity.Jobs.JobHandle.html) handle = graphicsStateCollection.WarmUp(inputJobHandle);  
      
            var job = new PostWarmUpJob();
            job.Schedule(handle);
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

