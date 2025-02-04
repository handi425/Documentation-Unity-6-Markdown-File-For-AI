[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/multidisplay.html)
  * [中文](/cn/current/Manual/multidisplay.html)
  * [日本語](/ja/current/Manual/multidisplay.html)
  * [한국어](/kr/current/Manual/multidisplay.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/multidisplay.html)
  * [中文](/cn/current/Manual/multidisplay.html)
  * [日本語](/ja/current/Manual/multidisplay.html)
  * [한국어](/kr/current/Manual/multidisplay.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Using multiple cameras](MultipleCameras-landing.html)
  * Display camera views on multiple monitors

[](multiple-cameras-birp.html)

Set the order of multiple cameras

[](resolution-scale.html)

Changing resolution scale

# Display camera views on multiple monitors

You can use multi-display to display up to eight different Camera views of
your application on up to eight different monitors at the same time. You can
use this for setups such as PC games, arcade game machines, or public display
installations.

Unity supports multi-display on:

  * Desktop platforms (Windows, macOS X, and Linux)
  * Android (OpenGL ES and Vulkan)
  * iOS

Some features work only on some platforms. See the
[Display](../ScriptReference/Display.html),
[Screen](../ScriptReference/Screen.html) and
[FullScreenMode](../ScriptReference/FullScreenMode.html) APIs for more
information about compatibility.

## Activating multi-display support

Unity’s default display mode is one monitor only. When you run your
application, you need use `Display.Activate()` to explicitly activate
additional displays. Once you activate a display, you can’t deactivate it.

The best time to activate additional displays is when your application creates
a new **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). A good way to do this is to attach a
script component to the default Camera. Make sure you call
`Display.Activate()` only once during startup. As a best practice, you might
find it helpful to create a small initial Scene to test your script.

### Example script

    
    
    using UnityEngine;
    using System.Collections;
    
    public class ActivateAllDisplays : MonoBehaviour
    {
        void Start ()
        {
            Debug.Log ("displays connected: " + Display.displays.Length);
                // Display.displays[0] is the primary, default display and is always ON, so start at index 1.
                // Check if additional displays are available and activate each.
        
            for (int i = 1; i < Display.displays.Length; i++)
                {
                    Display.displays[i].Activate();
                }
        }
        
        void Update()
        {
    
        }
    }
    
    

## Previewing multiple displays in your Project

To preview different Camera views, follow these steps:

  1. In the Camera’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), select a **Target Display** for
that Camera.

![Camera Inspector with Target Display
option](../uploads/Main/InspectorCamera35.png) Camera Inspector with Target
Display option

  1. Make sure you’re in the Game view.

  2. From the **Display** menu in the top-left corner, select the _Display_ to Preview.

![Display preview in the top left corner of the Game
View](../uploads/Main/TargetDisplay.png) Display preview in the top left
corner of the Game View

## API support

Unity supports the following **UnityEngine.Display** API methods:

**Method** | **Description**  
---|---  
`public void Activate()` | Activates a specific display on the current monitor’s width and height. This call must be made once on starting a new Scene. It can be called from a user script attached to a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) or dummy **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in a new Scene.  
`public void Activate(int width, int height, int refreshRate)` | Windows only. Activates a specific display of custom width and height. On Linux and macOS X, secondary displays always use the display’s current resolution, if available.  
  
[](multiple-cameras-birp.html)

Set the order of multiple cameras

[](resolution-scale.html)

Changing resolution scale

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

