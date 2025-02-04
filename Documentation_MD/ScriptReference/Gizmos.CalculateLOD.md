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

#  [Gizmos](Gizmos.html).CalculateLOD

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

public static float CalculateLOD([Vector3](Vector3.html) position, float
radius);

### Parameters

position | The centre of the gizmo in world space.  
---|---  
radius | The maximum extent of the gizmo.  
  
### Returns

**float** Returns a value between 0 and 1 that represents the level of detail
for the gizmo.

### Description

Determines the appropriate level of detail for a gizmo in the Scene view at a
specified position with a specified radius.

A return value of 0 indicates the gizmo is not visible. The gizmo might not be
visible because it is too small on the screen or because it is outside of the
Scene view camera frustum. The return value is quantized to eighths to reduce
the number of produced batches. This can be further controlled with the 'Fade
Gizmos' options in the [Gizmos menu](../Manual/GizmosMenu.html).

    
    
    using UnityEngine;  
      
    public class MyLODedComponent : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draw a blue sphere at the transform's position, fading out as it gets further away
        private void OnDrawGizmos()
        {
            float lod = [Gizmos.CalculateLOD](Gizmos.CalculateLOD.html)(transform.position, 1);  
      
            // Cull any gizmos that are too small or off screen
            if (lod == 0.0f)
                return;  
      
            // Fade the gizmos out so that they don't pop in and out when scrolling around the scene
            [Gizmos.color](Gizmos-color.html) = [Color.blue](Color-blue.html) * lod;
            [Gizmos.DrawSphere](Gizmos.DrawSphere.html)(transform.position, 1);
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

