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

#  [Camera](Camera.html).ScreenPointToRay

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

public [Ray](Ray.html) ScreenPointToRay([Vector3](Vector3.html) pos);

## Declaration

public [Ray](Ray.html) ScreenPointToRay([Vector3](Vector3.html) pos,
[Camera.MonoOrStereoscopicEye](Camera.MonoOrStereoscopicEye.html) eye);

### Parameters

pos | A 3D point, with the x and y coordinates containing a 2D screen space point in pixels. The lower left pixel of the screen is (0,0). The upper right pixel of the screen is (screen width in pixels - 1, screen height in pixels - 1). Unity ignores the z coordinate.  
---|---  
eye | Optional argument that can be used to specify which eye transform to use. Default is Mono.  
  
### Description

Returns a ray going from camera through a screen point.

Resulting ray is in world space, starting on the near plane of the camera and
going through position's (x,y) pixel coordinates on the screen.

    
    
    //Attach this script to your [Camera](Camera.html)
    //This draws a line in the [Scene](SceneManagement.Scene.html) view going through a point 200 pixels from the lower-left corner of the screen
    //To see this, enter Play [Mode](Scripting.GarbageCollector.Mode.html) and switch to the **Scene** tab. Zoom into your [Camera](Camera.html)'s position.
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Camera](Camera.html) cam;
        [Vector3](Vector3.html) pos = new [Vector3](Vector3.html)(200, 200, 0);  
      
    
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Ray](Ray.html) ray = cam.ScreenPointToRay(pos);
            [Debug.DrawRay](Debug.DrawRay.html)(ray.origin, ray.direction * 10, [Color.yellow](Color-yellow.html));
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

