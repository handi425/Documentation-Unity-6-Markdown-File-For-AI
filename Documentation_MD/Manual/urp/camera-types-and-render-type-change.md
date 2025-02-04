[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/camera-types-and-render-type-change.html)
  * [中文](/cn/current/Manual/urp/camera-types-and-render-type-change.html)
  * [日本語](/ja/current/Manual/urp/camera-types-and-render-type-change.html)
  * [한국어](/kr/current/Manual/urp/camera-types-and-render-type-change.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/camera-types-and-render-type-change.html)
  * [中文](/cn/current/Manual/urp/camera-types-and-render-type-change.html)
  * [日本語](/ja/current/Manual/urp/camera-types-and-render-type-change.html)
  * [한국어](/kr/current/Manual/urp/camera-types-and-render-type-change.html)

  * [Working in Unity](../working-in-unity.html)
  * [Cameras](../Cameras.html)
  * [Cameras in URP](../urp/urp-cameras-landing.html)
  * [Camera render types in URP](../urp/camera-types-and-render-type.html)
  * Change the render type of a camera in URP

[](../urp/camera-types-and-render-type-introduction.html)

Introduction to camera render types in URP

[](../urp/cameras-multiple.html)

Multiple cameras in URP

# Change the render type of a camera in URP

Use a **Camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera)’s **Render Type** property to make
it a Base Camera or an Overlay Camera.

To change the type of a Camera in the Unity Editor:

  1. Create or select a Camera in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

  2. In the Camera **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector), use the **Render Type** drop-
down menu to select a different type of Camera. Select either:

     * **Base** to change the Camera to a Base Camera

     * **Overlay** to change the Camera to an Overlay Camera

You can change a Camera’s type in a script, by setting the `renderType`
property of the Camera’s [Universal Additional Camera
Data](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalAdditionalCameraData.html)
component, like this:

    
    
    var cameraData = camera.GetUniversalAdditionalCameraData();
    cameraData.renderType = CameraRenderType.Base;
    

[](../urp/camera-types-and-render-type-introduction.html)

Introduction to camera render types in URP

[](../urp/cameras-multiple.html)

Multiple cameras in URP

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

