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

# Display

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Provides access to a display / screen for rendering operations.

Unity supports multi-display rendering on:

  * Desktop platforms (Windows, macOS X, and Linux)
  * Android (OpenGL ES and Vulkan)
  * iOS

Some features in the Display class only work on some of the supported
platforms. See the properties and methods for more information about platform
compatibility.  
  
Use the Display class to operate on the displays themselves, and
[Camera.targetDisplay](Camera-targetDisplay.html) to set up cameras for
rendering to individual displays.  
  
Additional resources: [Camera.targetDisplay](Camera-targetDisplay.html),
[Canvas.targetDisplay](Canvas-targetDisplay.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Camera](Camera.html) extCam;
        [Camera](Camera.html) cam;  
      
        void Start()
        {
            // [GUI](GUI.html) is rendered with last camera.
            // As we want it to end up in the main screen, make sure main camera is the last one drawn.
            extCam.depth = cam.depth - 1;  
      
            cam.SetTargetBuffers(Display.main.colorBuffer, Display.main.depthBuffer);
            extCam.enabled = false;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (Display.displays.Length > 1 && !extCam.enabled)
            {
                [Display.displays](Display-displays.html)[1].SetRenderingResolution(256, 256);
                extCam.SetTargetBuffers([Display.displays](Display-displays.html)[1].colorBuffer, [Display.displays](Display-displays.html)[1].depthBuffer);
            }
            extCam.enabled = Display.displays.Length > 1;
        }
    }
    

### Static Properties

[activeEditorGameViewTarget](Display-activeEditorGameViewTarget.html)| Get the
Editors active GameView display target.  
---|---  
[displays](Display-displays.html)| The list of connected displays.  
[main](Display-main.html)| Main Display.  
  
### Properties

[active](Display-active.html)| Gets the state of the display and returns true
if the display is active and false if otherwise.  
---|---  
[colorBuffer](Display-colorBuffer.html)| Color RenderBuffer.  
[depthBuffer](Display-depthBuffer.html)| Depth RenderBuffer.  
[renderingHeight](Display-renderingHeight.html)| Vertical resolution that the
display is rendering at.  
[renderingWidth](Display-renderingWidth.html)| Horizontal resolution that the
display is rendering at in the viewport.  
[requiresBlitToBackbuffer](Display-requiresBlitToBackbuffer.html)| True when
the back buffer requires an intermediate texture to render.  
[requiresSrgbBlitToBackbuffer](Display-requiresSrgbBlitToBackbuffer.html)|
True when doing a blit to the back buffer requires manual color space
conversion.  
[systemHeight](Display-systemHeight.html)| Vertical native display resolution.  
[systemWidth](Display-systemWidth.html)| Horizontal native display resolution.  
  
### Public Methods

[Activate](Display.Activate.html)| Activates an external display. For example,
a secondary monitor connected to the system.  
---|---  
[SetParams](Display.SetParams.html)| Windows platforms only. Sets rendering
size and position on screen.  
[SetRenderingResolution](Display.SetRenderingResolution.html)| Sets rendering
resolution for the display.  
  
### Static Methods

[RelativeMouseAt](Display.RelativeMouseAt.html)| Query relative mouse
coordinates.  
---|---  
  
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

