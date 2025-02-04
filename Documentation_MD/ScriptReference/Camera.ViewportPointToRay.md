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

#  [Camera](Camera.html).ViewportPointToRay

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

public [Ray](Ray.html) ViewportPointToRay([Vector3](Vector3.html) pos);

## Declaration

public [Ray](Ray.html) ViewportPointToRay([Vector3](Vector3.html) pos,
[Camera.MonoOrStereoscopicEye](Camera.MonoOrStereoscopicEye.html) eye);

### Parameters

eye | Optional argument that can be used to specify which eye transform to use. Default is Mono.  
---|---  
  
### Description

Returns a ray going from camera through a viewport point.

Resulting ray is in world space, starting on the near plane of the camera and
going through position's (x,y) coordinates on the viewport (position.z is
ignored).  
  
Viewport coordinates are normalized and relative to the camera. The bottom-
left of the camera is (0,0); the top-right is (1,1).

    
    
    // Prints the name of the object camera is directly looking at
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Ray](Ray.html) ray = cam.ViewportPointToRay(new [Vector3](Vector3.html)(0.5F, 0.5F, 0));
            [RaycastHit](RaycastHit.html) hit;
            if ([Physics.Raycast](Physics.Raycast.html)(ray, out hit))
                print("I'm looking at " + hit.transform.name);
            else
                print("I'm looking at nothing!");
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

