[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/universal-additional-camera-data.html)
  * [中文](/cn/current/Manual/urp/universal-additional-camera-data.html)
  * [日本語](/ja/current/Manual/urp/universal-additional-camera-data.html)
  * [한국어](/kr/current/Manual/urp/universal-additional-camera-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/universal-additional-camera-data.html)
  * [中文](/cn/current/Manual/urp/universal-additional-camera-data.html)
  * [日本語](/ja/current/Manual/urp/universal-additional-camera-data.html)
  * [한국어](/kr/current/Manual/urp/universal-additional-camera-data.html)

  * [Working in Unity](../working-in-unity.html)
  * [Cameras](../Cameras.html)
  * [Cameras in URP](../urp/urp-cameras-landing.html)
  * Access camera data with the Universal Additional Camera Data component in URP

[](../urp/stp/stp-debug-views.html)

Spatial-Temporal Post-processing Rendering Debugger reference for URP

[](../urp/camera-components-reference-landing.html)

Camera Inspector windows reference for URP

# Access camera data with the Universal Additional Camera Data component in
URP

The Universal Additional **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) Data component is a component the
Universal **Render Pipeline** A series of operations that take the contents of
a Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) uses for internal
data storage. The Universal Additional Camera Data component allows URP to
extend and override the functionality and appearance of Unity’s standard
Camera component.

In URP, a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) that has a Camera component
must also have a Universal Additional Camera Data component. If your Project
uses URP, Unity automatically adds the Universal Additional Camera Data
component when you create a Camera GameObject. You cannot remove the Universal
Additional Camera Data component from a Camera GameObject.

If you don’t use **scripts** A piece of code that allows you to create your
own Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](../creating-
scripts.html)  
See in [Glossary](../Glossary.html#Scripts) to control and customise URP, you
do not need to do anything with the Universal Additiona Camera Data component.

If you do use scripts to control and customise URP, you can access a Camera’s
Universal Additional Camera Data component in a script like this:

    
    
    UniversalAdditionalCameraData cameraData = camera.GetUniversalAdditionalCameraData();
    

**Note:** To use the `GetUniversalAdditionalCameraData()` method you must use
the `UnityEngine.Rendering.Universal` namespace. To do this, add the following
statement at the top of your script: `using UnityEngine.Rendering.Universal;`.

For more information, refer to the [UniversalAdditionalCameraData
API](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalAdditionalCameraData.html).

If you need to access the Universal Additional Camera Data component
frequently in a script, you should cache the reference to it to avoid
unnecessary CPU work.

**Note:** When a Camera uses a Preset, only a subset of properties are
supported. Unsupported properties are hidden.

[](../urp/stp/stp-debug-views.html)

Spatial-Temporal Post-processing Rendering Debugger reference for URP

[](../urp/camera-components-reference-landing.html)

Camera Inspector windows reference for URP

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

