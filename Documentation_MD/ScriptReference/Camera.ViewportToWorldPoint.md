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

#  [Camera](Camera.html).ViewportToWorldPoint

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

## Declaration

public [Vector3](Vector3.html) ViewportToWorldPoint([Vector3](Vector3.html)
position);

### Parameters

position | The 3d vector in Viewport space.  
---|---  
  
### Returns

**Vector3** The 3d vector in World space.

### Description

Transforms `position` from viewport space into world space.

Viewport space is normalized and relative to the camera. The bottom-left of
the viewport is (0,0); the top-right is (1,1). The z position is in world
units from the camera.  
  
Note that [ViewportToWorldPoint](Camera.ViewportToWorldPoint.html) transforms
an x-y screen position into a x-y-z position in 3D space.  
  
Provide the function with a vector where the x-y components of the vector are
the screen coordinates and the z component is the distance of the resulting
plane from the camera.

    
    
    // Draw a yellow sphere at top-right corner of the near plane
    // for the selected camera in the [Scene](SceneManagement.Scene.html) view.
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnDrawGizmosSelected()
        {
            [Camera](Camera.html) camera = GetComponent<[Camera](Camera.html)>();
            [Vector3](Vector3.html) p = camera.ViewportToWorldPoint(new [Vector3](Vector3.html)(1, 1, camera.nearClipPlane));
            [Gizmos.color](Gizmos-color.html) = [Color.yellow](Color-yellow.html);
            [Gizmos.DrawSphere](Gizmos.DrawSphere.html)(p, 0.1F);
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

