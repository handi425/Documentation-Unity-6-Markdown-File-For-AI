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

#  [Physics](Physics.html).RaycastNonAlloc

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

public static int RaycastNonAlloc([Ray](Ray.html) ray, RaycastHit[] results,
float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

ray | The starting point and direction of the ray.  
---|---  
results | The buffer to store the hits into.  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**int** The amount of hits stored into the `results` buffer.

### Description

Cast a ray through the Scene and store the hits into the buffer.

Like [Physics.RaycastAll](Physics.RaycastAll.html), but generates no garbage.  
  
The raycast query ends when there are no more hits and/or the results buffer
is full. The order of the results is undefined. When a full buffer is returned
it is not guaranteed that the results are the closest hits and the length of
the buffer is returned. If a null buffer is passed in, no results are returned
and no errors or exceptions are thrown.

* * *

## Declaration

public static int RaycastNonAlloc([Vector3](Vector3.html) origin,
[Vector3](Vector3.html) direction, RaycastHit[] results, float maxDistance =
Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The starting point and direction of the ray.  
---|---  
results | The buffer to store the hits into.  
direction | The direction of the ray.  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a ray.  
  
### Returns

**int** The amount of hits stored into the `results` buffer.

### Description

Cast a ray through the Scene and store the hits into the buffer.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // The size of the array determines how many raycasts will occur
        [RaycastHit](RaycastHit.html)[] m_Results = new [RaycastHit](RaycastHit.html)[5];  
      
        // See [Order of Execution for Event Functions](../Manual/ExecutionOrder.html) for information on [FixedUpdate](PlayerLoop.FixedUpdate.html)() and [Update](PlayerLoop.Update.html)() related to physics queries
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            // Set the layer mask to all layers
            var layerMask = ~0;  
      
            int hits = [Physics.RaycastNonAlloc](Physics.RaycastNonAlloc.html)(transform.position, transform.forward, m_Results, [Mathf.Infinity](Mathf.Infinity.html), layerMask);
            for (int i = 0; i < hits; i++)
            {
                [Debug.Log](Debug.Log.html)("Hit " + m_Results[i].collider.gameObject.name);
            }
            if (hits == 0)
            {
                [Debug.Log](Debug.Log.html)("Did not hit");
            }
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

