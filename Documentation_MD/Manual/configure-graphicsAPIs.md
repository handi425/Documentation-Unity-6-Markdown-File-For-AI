[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/configure-graphicsAPIs.html)
  * [中文](/cn/current/Manual/configure-graphicsAPIs.html)
  * [日本語](/ja/current/Manual/configure-graphicsAPIs.html)
  * [한국어](/kr/current/Manual/configure-graphicsAPIs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/configure-graphicsAPIs.html)
  * [中文](/cn/current/Manual/configure-graphicsAPIs.html)
  * [日本語](/ja/current/Manual/configure-graphicsAPIs.html)
  * [한국어](/kr/current/Manual/configure-graphicsAPIs.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * [Graphics API support](GraphicsAPIs.html)
  * Configure graphics APIs

[](GraphicsAPIs.html)

Graphics API support

[](UsingDX11GL3Features.html)

DirectX

# Configure graphics APIs

Unity uses a built-in set of graphics APIs or the graphics APIs that you
select in the Unity Editor.

To use Unity’s default graphics APIs:

  1. Open the [Player settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) (menu: **Edit** > **Project
Settings** > **Player**).

  2. Navigate to **Other Settings** > **Rendering** section and enable **Auto Graphics API for a platform (Windows/Mac/Linux)** :

![Using the default graphics
APIs](../uploads/Main/AutoGraphicsAPICheckboxes.png) Using the default
graphics APIs

When you enable **Auto Graphics API for a platform (Windows/Mac/Linux)** , the
Player build includes a set of built-in graphics APIs and uses the appropriate
one at runtime to produce a best case scenario.

## Override default graphics APIs

You can override the default graphics APIs and use an alternate graphics API
for the Editor and Player. Use the following steps:

  1. In the **Player settings** > **Other settings** > **Rendering** section, disable the **Auto Graphics API for a platform (Windows/Mac/Linux)**. 

When **Auto Graphics API for a platform (Windows/Mac/Linux)** is disabled, the
Unity Editor displays a list of supported graphics API for that platform and
uses the first API in the list. The graphics API at the top of the **Graphics
API** list is the default API. If the default API isn’t supported by a
specific platform, Unity uses the next API in the **Graphics API** list.

  2. Select the **Add** (**+**) button, then select the graphics API from the dropdown.

![Adding OpenGLCore to the Graphics APIs for Windows
list](../uploads/Main/SelectGraphicsAPIs.png).

You can reorder the graphics APIs in the list. For example, to check how your
application runs on OpenGL Core in the Editor, move **OpenGLCore** to the top
of the list and the Editor switches to use OpenGL Core rendering.

For information on how graphics rendering behaves between the platforms and
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) language semantics, refer to
[Platform-specific rendering differences](SL-PlatformDifferences.html).

## Additional resources

  * [Graphics API support](GraphicsAPIs.html)
  * [Surface Shaders with DX11 / OpenGL Core Tessellation](SL-SurfaceShaderTessellation.html)

[](GraphicsAPIs.html)

Graphics API support

[](UsingDX11GL3Features.html)

DirectX

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

