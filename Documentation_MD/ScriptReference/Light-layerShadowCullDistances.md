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

#  [Light](Light.html).layerShadowCullDistances

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

[Switch to Manual](../Manual/class-Light.html "Go to Light Component in the
Manual")

public float[] layerShadowCullDistances;

### Description

Per-light, per-layer shadow culling distances. Directional lights only.

Dynamic shadows can be cast into view from shadow casters that are very far
away from the camera. At low incident light angles, this can lead to a lot of
objects needing to cast dynamic shadows, which in turn can result in high
rendering costs during shadow maps generation.  
  
Using [Light.layerShadowCullDistances](Light-layerShadowCullDistances.html)
lets you limit, on a per-layer basis, how far from the camera shadows casters
are allowed to be before they get culled from shadow maps generation. The
feature complements [Camera.layerCullDistances](Camera-
layerCullDistances.html), but only affects shadow casting, not regular object
rendering.  
  
Just like [Camera.layerCullDistances](Camera-layerCullDistances.html),
[Light.layerShadowCullDistances](Light-layerShadowCullDistances.html) requires
that you assign a float array of exactly 32 values. A distance of 0 in a
layer's index means keep current behaviour for that layer. Assigning null
completely disables shadow distance culling, and is effectively the same as
passing an array of 32 zeros.  
  
By default, per-layer shadow culling will use a plane aligned with the camera.
You can change this to a sphere by setting [Camera.layerCullSpherical](Camera-
layerCullSpherical.html) to true. The effect of this flag is shared by both
[Camera.layerCullDistances](Camera-layerCullDistances.html) and
[Light.layerShadowCullDistances](Light-layerShadowCullDistances.html).  
  
Please be aware that when you restrict camera culling distances using
[Camera.layerCullDistances](Camera-layerCullDistances.html), this also
restricts shadow casting to those same culling distances. As a result, if you
use [Camera.layerCullDistances](Camera-layerCullDistances.html) and
[Light.layerShadowCullDistances](Light-layerShadowCullDistances.html) at the
same time *for the same layer index*, the effective shadow culling distance
for that layer will be the smallest of those two distances. For layer indices
where one of the values are zero, the other value gets used directly, and for
layer indices where both values are zero, no special culling behaviour gets
applied for that layer.  
  
Only works with [Directional](LightType.Directional.html) lights.  
  
See Also: [Camera.layerCullDistances](Camera-layerCullDistances.html),
[Camera.layerCullSpherical](Camera-layerCullSpherical.html)

    
    
    using UnityEngine;  
      
    [[RequireComponent](RequireComponent.html)(typeof([Light](Light.html)))]
    public class LayerShadowCullDistancesExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnEnable()
        {
            // Setup shadow cull distances
            var shadowCullDistances = new float[32];
            shadowCullDistances[10] = 5f;   // Let's imagine this is our 'Tiny Objects' layer
            shadowCullDistances[11] = 15f;  // Let's imagine this is our 'Small Things' layer
            shadowCullDistances[12] = 100f; // Let's imagine this is our 'Trees' layer  
      
            // Assign shadow cull distances. This will only affect layers 10, 11 and 12.
            GetComponent<[Light](Light.html)>().layerShadowCullDistances = shadowCullDistances;
        }  
      
        void OnDisable()
        {
            // Completely disable shadow cull distances
            GetComponent<[Light](Light.html)>().layerShadowCullDistances = null;
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

