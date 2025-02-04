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

#  [Physics](Physics.html).RaycastAll

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

public static RaycastHit[] RaycastAll([Ray](Ray.html) ray, float maxDistance =
Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

ray | The starting point and direction of the ray.  
---|---  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**RaycastHit[]** An array of RaycastHit objects. Note that the order of the
results is undefined.

### Description

Casts a ray through the Scene and returns all hits. Note that order of the
results is undefined.

Additional resources: [Raycast](Physics.Raycast.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            [RaycastHit](RaycastHit.html)[] hits;
            hits = [Physics.RaycastAll](Physics.RaycastAll.html)(transform.position, transform.forward, 100.0F);  
      
            for (int i = 0; i < hits.Length; i++)
            {
                [RaycastHit](RaycastHit.html) hit = hits[i];
                [Renderer](Renderer.html) rend = hit.transform.GetComponent<[Renderer](Renderer.html)>();  
      
                if (rend)
                {
                    // Change the material of all hit colliders
                    // to use a transparent shader.
                    rend.material.shader = [Shader.Find](Shader.Find.html)("Transparent/Diffuse");
                    [Color](Color.html) tempColor = rend.material.color;
                    tempColor.a = 0.3F;
                    rend.material.color = tempColor;
                }
            }
        }
    }
    

**Notes:** Raycasts will not detect colliders for which the raycast origin is
inside the collider.

* * *

## Declaration

public static RaycastHit[] RaycastAll([Vector3](Vector3.html) origin,
[Vector3](Vector3.html) direction, float maxDistance = Mathf.Infinity, int
layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The starting point of the ray in world coordinates.  
---|---  
direction | The direction of the ray.  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
layermask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Description

Additional resources: [Raycast](Physics.Raycast.html).

See example above.

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

