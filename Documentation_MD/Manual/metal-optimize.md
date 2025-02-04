[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/metal-optimize.html)
  * [中文](/cn/current/Manual/metal-optimize.html)
  * [日本語](/ja/current/Manual/metal-optimize.html)
  * [한국어](/kr/current/Manual/metal-optimize.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/metal-optimize.html)
  * [中文](/cn/current/Manual/metal-optimize.html)
  * [日本語](/ja/current/Manual/metal-optimize.html)
  * [한국어](/kr/current/Manual/metal-optimize.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * [Graphics API support](GraphicsAPIs.html)
  * [Metal](Metal.html)
  * Optimize Metal graphics

[](metal-debug.html)

Debug Metal graphics

[](OpenGLCoreDetails.html)

OpenGL Core

# Optimize Metal graphics

Metal supports multiple optimizations that you can use to increase the
performance of your application.

## Use memoryless render targets

Metal supports memoryless render targets which enables you to render to a
[RenderTexture](../ScriptReference/RenderTexture.html) without backing it up
in system memory. Unity only stores the contents temporarily in the on-tile
memory during rendering.

Metal supports memoryless render targets on mobile devices from iOS 10.0, tvOS
10.0, visionOS 1.0, and on desktop devices (including Apple silicon) from
macOS 11.

## Additional resources

  * [RenderTexture.memorylessMode](../ScriptReference/RenderTexture-memorylessMode.html)

[](metal-debug.html)

Debug Metal graphics

[](OpenGLCoreDetails.html)

OpenGL Core

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

