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

#  [Physics](Physics.html).OverlapSphereNonAlloc

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

public static int OverlapSphereNonAlloc([Vector3](Vector3.html) position,
float radius, Collider[] results, int layerMask = AllLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

position | Center of the sphere.  
---|---  
radius | Radius of the sphere.  
results | The buffer to store the results into.  
layerMask | A [Layer mask](../Manual/Layers.html) defines which layers of colliders to include in the query.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**int** Returns the amount of colliders stored into the `results` buffer.

### Description

Computes and stores colliders touching or inside the sphere into the provided
buffer.

Does not attempt to grow the buffer if it runs out of space. The length of the
buffer is returned when the buffer is full. Like
[Physics.OverlapSphere](Physics.OverlapSphere.html), but generates no garbage.
Additional resources: [Physics.AllLayers](Physics.AllLayers.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void ExplosionDamage([Vector3](Vector3.html) center, float radius)
        {
            int maxColliders = 10;
            [Collider](Collider.html)[] hitColliders = new [Collider](Collider.html)[maxColliders];
            int numColliders = [Physics.OverlapSphereNonAlloc](Physics.OverlapSphereNonAlloc.html)(center, radius, hitColliders);
            for (int i = 0; i < numColliders; i++)
            {
                hitColliders[i].SendMessage("AddDamage");
            }
        }
    }
    

Additional resources: [Layer mask](../Manual/Layers.html) particularly
"Casting Rays Selectively" for a detailed example of Layer masking.

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

