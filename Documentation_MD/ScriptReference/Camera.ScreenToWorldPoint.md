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

#  [Camera](Camera.html).ScreenToWorldPoint

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

public [Vector3](Vector3.html) ScreenToWorldPoint([Vector3](Vector3.html)
position);

## Declaration

public [Vector3](Vector3.html) ScreenToWorldPoint([Vector3](Vector3.html)
position, [Camera.MonoOrStereoscopicEye](Camera.MonoOrStereoscopicEye.html)
eye);

### Parameters

position | A 2D screen space point in pixels, plus a z coordinate for the distance from the camera in world units. The lower left pixel of the screen is (0,0). The upper right pixel of the screen is (screen width in pixels - 1, screen height in pixels - 1).  
---|---  
eye | By default, [Camera.MonoOrStereoscopicEye.Mono](Camera.MonoOrStereoscopicEye.Mono.html). Can be set to [Camera.MonoOrStereoscopicEye.Left](Camera.MonoOrStereoscopicEye.Left.html) or [Camera.MonoOrStereoscopicEye.Right](Camera.MonoOrStereoscopicEye.Right.html) for use in stereoscopic rendering (e.g., for VR).  
  
### Returns

**Vector3** The world space point created by converting the screen space point
at the provided distance z from the camera plane.

### Description

Transforms a point from screen space into world space, where world space is
defined as the coordinate system at the very top of your game's hierarchy.

World space coordinates can still be calculated even when provided as an off-
screen coordinate, for example for instantiating an off-screen object near a
specific corner of the screen.  
  
To make sure the world space point is part of the camera's view volume, the z
coordinate you provide must be between the camera's `nearClipPlane` and
`farClipPlane`.

    
    
    // Convert the 2D position of the mouse into a
    // 3D position.  [Display](Display.html) these on the game window.  
      
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = [Camera.main](Camera-main.html);
        }  
      
        void OnGUI()
        {
            [Vector3](Vector3.html) point = new [Vector3](Vector3.html)();
            [Event](Event.html)   currentEvent = [Event.current](Event-current.html);
            [Vector2](Vector2.html) mousePos = new [Vector2](Vector2.html)();  
      
            // Get the mouse position from [Event](Event.html).
            // Note that the y position from [Event](Event.html) is inverted.
            mousePos.x = currentEvent.mousePosition.x;
            mousePos.y = cam.pixelHeight - currentEvent.mousePosition.y;  
      
            point = cam.ScreenToWorldPoint(new [Vector3](Vector3.html)(mousePos.x, mousePos.y, cam.nearClipPlane));  
      
            [GUILayout.BeginArea](GUILayout.BeginArea.html)(new [Rect](Rect.html)(20, 20, 250, 120));
            [GUILayout.Label](GUILayout.Label.html)("[Screen](Screen.html) pixels: " + cam.pixelWidth + ":" + cam.pixelHeight);
            [GUILayout.Label](GUILayout.Label.html)("Mouse position: " + mousePos);
            [GUILayout.Label](GUILayout.Label.html)("World position: " + point.ToString("F3"));
            [GUILayout.EndArea](GUILayout.EndArea.html)();
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

