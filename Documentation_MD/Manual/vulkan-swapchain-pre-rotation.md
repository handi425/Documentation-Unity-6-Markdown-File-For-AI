[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/vulkan-swapchain-pre-rotation.html)
  * [中文](/cn/current/Manual/vulkan-swapchain-pre-rotation.html)
  * [日本語](/ja/current/Manual/vulkan-swapchain-pre-rotation.html)
  * [한국어](/kr/current/Manual/vulkan-swapchain-pre-rotation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/vulkan-swapchain-pre-rotation.html)
  * [中文](/cn/current/Manual/vulkan-swapchain-pre-rotation.html)
  * [日本語](/ja/current/Manual/vulkan-swapchain-pre-rotation.html)
  * [한국어](/kr/current/Manual/vulkan-swapchain-pre-rotation.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Graphics for Android](android-graphics.html)
  * Framebuffer orientation

[](Android-SinglePassStereoRendering.html)

Single-pass stereo rendering for Android

[](allow-deny-vulkan-usage.html)

Allow or deny Vulkan API usage

# Framebuffer orientation

If your application’s framebuffer orientation doesn’t match the device’s
native display orientation (portrait, for most devices), Android rotates the
application’s framebuffer to match the device’s display every frame. Depending
on the device’s hardware capabilities, this additional rotation can negatively
affect performance. If your application uses the [Vulkan Graphics API](class-
PlayerSettingsAndroid.html#auto-graphics-api) and the device supports Vulkan,
Unity can apply this rotation during rendering which reduces the performance
impact of the rotation. This is called[ pre-rotation](https://android-
developers.googleblog.com/2020/02/handling-device-orientation-
efficiently.html).

## Using pre-rotation in Unity

To make Unity apply pre-rotation, you can use C# **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) or the Unity editor:

  * Through C# scripts: Set [PlayerSettings.vulkanEnablePreTransform](../ScriptReference/PlayerSettings-vulkanEnablePreTransform.html) to `true`.

  * Through the Unity Editor:

  *     1. Select **Edit** > **Project Settings**.
  * In the Project settings window, select the **Player** tab, then open [Android Player Settings](class-PlayerSettingsAndroid.html):  
![](../uploads/Main/android-player-settings-tab.png)

  * In the **Other Setting** s section, enable **Apply display rotation during rendering**.

## How Unity applies pre-rotation

Unity applies pre-rotation when it renders directly to the device’s
backbuffer, not when it renders to a [Render Texture](class-
RenderTexture.html)A special type of Texture that is created and updated at
runtime. To use them, first create a new Render Texture and designate one of
your Cameras to render into it. Then you can use the Render Texture in a
Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture). To apply the rotation, Unity
modifies the projection matrix which affects the `UNITY_MATRIX_MVP` and
`UNITY_MATRIX_P` [Built-in shader variables](SL-UnityShaderVariables.html).
This means that Unity applies the rotation in the vertex **shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

Using pre-rotation doesn’t affect the behavior of Unity’s C# API. For example,
you can still use `Screen.width` to access the width of the screen. The same
applies to **viewports** The user’s visible area of an app on their screen.  
See in [Glossary](Glossary.html#Viewport) and [scissor
rects](../ScriptReference/Rendering.CommandBuffer.EnableScissorRect.html).
Unity adjusts these as needed, and also handles readback operations from the
backbuffer such as Grab Pass, ReadPixels, or Screenshot.

Unity provides utility macros to handle special cases in shaders (for more
information, see the Limitations section below).

The macro UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION is only defined if all of
the following conditions are true (otherwise, it’s undefined):

  * `preTransform` is enabled in the Player Settings
  * the platform is set to Android
  * the graphics API is set to Vulkan

UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is a constant that is set to the
current `preTransform` rotation. Its value is one of the following:

  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_0`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_90`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_180`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_270`

If UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION is undefined, or when rendering
to a Render Texture, the value of UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is
UNITY_DISPLAY_ORIENTATION_0.

UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is translated into a Vulkan
specialization constant, which makes it efficient to use in if or switch
statements.

## Limitations

In the following cases, it’s likely that enabling preTransform requires
additional modifications to your Unity Project before you can use it:

  * Shaders that don’t use Unity’s projection matrix
  * Shaders that depend on the current **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) position in the fragment shader
(`SV_Position`)

  * Shaders that use screen space derivatives (ddx, ddy)
  * Native rendering plugins that use the Vulkan swapchain image might need to be modified
  * Use of backbuffer with Unity RenderPass API in an MRT setup together with other Render Textures

These cases only apply when rendering directly to the backbuffer.

## Additional resources

  * [Vulkan Design Guidelines](https://developer.android.com/ndk/guides/graphics/design-notes?hl=sk&authuser=3) on the Android developer website.
  * [Vulkan Mobile Best Practice - Appropriate Use of Surface Rotation](https://community.arm.com/developer/tools-software/graphics/b/blog/posts/appropriate-use-of-surface-rotation) on the arm community website.

[](Android-SinglePassStereoRendering.html)

Single-pass stereo rendering for Android

[](allow-deny-vulkan-usage.html)

Allow or deny Vulkan API usage

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

