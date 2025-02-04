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

#  [BatchCullingContext](Rendering.BatchCullingContext.html).viewID

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

public
[Rendering.BatchPackedCullingViewID](Rendering.BatchPackedCullingViewID.html)
viewID;

### Description

The ID of the object from which the culling is invoked. Usage example: store
culling-related data for each object.

    
    
    // Example of per-view data, indexed by view ID  
      
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;  
      
    public class CullingExample : [MonoBehaviour](MonoBehaviour.html)
    {
        private [BatchRendererGroup](Rendering.BatchRendererGroup.html) batchRendererGroup;
        private Dictionary<[BatchPackedCullingViewID](Rendering.BatchPackedCullingViewID.html), MyViewData> myPerViewData = new Dictionary<[BatchPackedCullingViewID](Rendering.BatchPackedCullingViewID.html), MyViewData>();  
      
        void Start()
        {
            batchRendererGroup = new [BatchRendererGroup](Rendering.BatchRendererGroup.html)(this.OnPerformCulling, IntPtr.Zero);
        }  
      
        public [JobHandle](Unity.Jobs.JobHandle.html) [OnPerformCulling](Rendering.BatchRendererGroup.OnPerformCulling.html)(
            [BatchRendererGroup](Rendering.BatchRendererGroup.html) rendererGroup,
            [BatchCullingContext](Rendering.BatchCullingContext.html) cullingContext,
            [BatchCullingOutput](Rendering.BatchCullingOutput.html) cullingOutput,
            IntPtr userContext)
        {
            if (!myPerViewData.ContainsKey(cullingContext.viewID))
            {
                // If the data doesn't exist for the current view, create it.
                myPerViewData[cullingContext.viewID] = new MyViewData();
            }
            MyViewData currentViewData = myPerViewData[cullingContext.viewID];  
      
            // Do stuff with the current view's data.  
      
            /* You can also get the instance ID of the current view's gameObject
               (for example, [Camera](Camera.html), [Light](Light.html), etc.) as follows: */
            int instanceID = cullingContext.viewID.GetInstanceID();  
      
            /* The slice index depends on the view type.
               For example, for Cameras, the slice index is always zero.
               For cascaded shadow maps, it equals the index of the cascade. */
            int sliceIndex = cullingContext.viewID.GetSliceIndex();
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

